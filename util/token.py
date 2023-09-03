import json

class TokenUtil:

    token_file_path = "token.json"

    def check_token(self, token: str) -> dict:

        with open(file=self.token_file_path, mode="r") as token_file:
            token_json = json.loads(token_file.read())

        if token_json['token'] == token:
            return True

        return False