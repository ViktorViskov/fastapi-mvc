class FormatHandler:
    
    def format_email(self, email: str) -> str:
        return email.strip().replace(" ", "").replace("\n","").replace("\r","").lower()