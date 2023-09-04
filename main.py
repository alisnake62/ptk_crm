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

    args = request.args
    sorted_by = args.get("sorted_by")

    if sorted_by not in ["product_volume", "revenue_volume", None]:
        return "bad sorted_by argument", 400

    customers = crm_util.get_customers(sorted_by=sorted_by)

    return wrap_result(request=request, result=customers)

@app.route("/v1/customer/<customer_id>")
def get_customer(customer_id):

    try:
        token = request.authorization.token
        token_is_valid = token_util.check_token(token=token)

        if not token_is_valid: raise Exception()
    except:
        return "incorrect API token", 403

    customer = crm_util.get_customer(customer_id=customer_id)

    if customer is None:
        return "product not found", 404

    return wrap_result(request=request, result=customer)

if __name__ == "__main__":
    app.run(debug=dev_env, host = "0.0.0.0", ssl_context='adhoc')