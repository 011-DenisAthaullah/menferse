
def validate_menfess(message):
    if not isinstance(message, str):
        return False

    cleaned_message = message.strip()

    if len(cleaned_message) < 1:
        return False

    if len(cleaned_message) > 500:
        return False

    return True
