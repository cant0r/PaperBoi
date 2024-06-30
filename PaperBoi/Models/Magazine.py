class Magazine:
    def __init__(self, source_uri: str, title: str, base64_data: str) -> None:
        self.source_uri = source_uri
        self.title = title
        self.base64_data = base64_data

    def __str__(self) -> str:
        return f"""Source Uri: {self.source_uri}
Title: {self.title}
Base64 representation: {self.base64_data[:80]}...
        """
