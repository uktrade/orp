import re


def sanitize_input(search):
    """
    Sanitize the input to remove potential threats like SQL injection
    characters.
    This function removes or escapes characters that are commonly used
    in SQL injection attacks.
    """
    # Define a regular expression pattern to match unwanted characters or
    # patterns
    # This removes SQL keywords, single quotes, double quotes, semicolons,
    # and escape sequences
    sanitized_search = re.sub(
        r"(--|\b(SELECT|INSERT|DELETE|UPDATE|DROP|ALTER|EXEC|UNION"
        r"|CREATE)\b|'|\"|;)",
        "",
        search,
        flags=re.IGNORECASE,
    )
    return sanitized_search.strip()


def parse_search_terms(search):
    # Sanitize input before processing
    search = sanitize_input(search)

    # Initialize lists to hold terms
    search_terms_and = []
    search_terms_or = []

    # Check if input only contains "AND", "OR", "+", or whitespace
    if re.fullmatch(r"(AND|OR|\+|\s)+", search):
        return search_terms_and, search_terms_or

    # Split the search string into tokens based on spaces and keywords
    tokens = re.split(r"(\s+|\bAND\b|\bOR\b|\+)", search)

    # Temporary variables for managing terms within quotes
    current_and_term = []
    current_or_term = []

    # Flag to determine if we are inside quotes
    in_quotes = False
    current_connector = None  # Track AND/OR status outside of quotes

    for token in tokens:
        token = token.strip()

        if not token:
            continue

        # Check if token is the start/end of a quoted phrase
        if token.startswith('"') and token.endswith('"'):
            # Complete quoted term in one token
            quoted_term = token.strip('"')
            if current_connector == "AND" or current_connector is None:
                search_terms_and.append(quoted_term)
            elif current_connector == "OR":
                search_terms_or.append(quoted_term)
            continue
        elif token.startswith('"'):
            in_quotes = True
            current_and_term = []
            current_or_term = []
            current_and_term.append(token.strip('"'))
            continue
        elif token.endswith('"'):
            if in_quotes:
                if current_connector == "AND" or current_connector is None:
                    current_and_term.append(token.strip('"'))
                    search_terms_and.append(" ".join(current_and_term))
                elif current_connector == "OR":
                    current_or_term.append(token.strip('"'))
                    search_terms_or.append(" ".join(current_or_term))
                in_quotes = False
            continue

        # Handle token within quotes
        if in_quotes:
            if current_connector == "AND" or current_connector is None:
                current_and_term.append(token)
            elif current_connector == "OR":
                current_or_term.append(token)
            continue

        # Treat both + and AND as equivalent for "AND" logic
        if token.upper() == "AND" or token == "+":  # nosec BXXX
            current_connector = "AND"
        elif token.upper() == "OR":
            current_connector = "OR"
        else:
            # Handle individual terms outside quotes
            if current_connector == "AND" or current_connector is None:
                search_terms_and.append(token)
            elif current_connector == "OR":
                search_terms_or.append(token)

    return search_terms_and, search_terms_or
