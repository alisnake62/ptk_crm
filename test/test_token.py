from util.token import TokenUtil

class TestDatetime:

    def test_check_token(self):

        token_util = TokenUtil()
        token_util.token_file_path = "test/token_test.json"

        token = "1111111111111111111111111111111111111111111111111111111111111111"
        token_is_valid = token_util.check_token(token=token)

        assert token_is_valid