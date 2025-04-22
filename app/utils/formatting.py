def format_string(email: str) -> str:
    return email.strip() \
                .replace(" ", "") \
                .replace("\n","") \
                .replace("\r","") \
                .lower()