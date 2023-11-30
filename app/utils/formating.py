class FormatHandler:
    
    def format_string(self, email: str) -> str:
        return email.strip().replace(" ", "").replace("\n","").replace("\r","").lower()