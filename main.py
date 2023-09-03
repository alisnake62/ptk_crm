from typing import Any
import os

from flask import Flask, jsonify, Request, request

from util.crm import CRMUtil
from util.token import TokenUtil

crm_util = CRMUtil()
token_util = TokenUtil()

app = Flask(__name__)

dev_env = os.getenv("FLASK_DEBUG", "0")
dev_env = True if dev_env == "1" else False

def wrap_result(request: Request, result: Any) -> str:

    response = {
        "url": request.base_url,
        "result": result
    }
    return jsonify(response)

@app.route("/v1/customers")
def get_customers():

    try:
        token = request.authorization.token
        token_is_valid = token_util.check_token(token=token)

        if not token_is_valid: raise Exception()
    except:
        return "incorrect API token", 403

    customers = crm_util.get_customers()

    return wrap_result(request=request, result=customers)

if __name__ == "__main__":
    app.run(debug=dev_env, host = "0.0.0.0", ssl_context='adhoc')