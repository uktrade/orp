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
        r"|CREATE)\b|'|;)",
        "",
        search,
        flags=re.IGNORECASE,
    )
    return sanitized_search.strip()
