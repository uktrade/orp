import bleach  # type: ignore[import]


def sanitize_input(search):
    """
    Sanitize user input using a library like bleach.
    """
    return bleach.clean(search.strip(), strip=True)
