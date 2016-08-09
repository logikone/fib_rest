from flask import Flask
from flask_restful import Api
from sequence import FibSequenceResource

errors = {
        "NegativeNumberError": {
            "message": "Must pass a positive number.",
            "status": 400,
            }
        }

app = Flask(__name__)

api = Api(
        app,
        errors = errors
        )

api.add_resource(
        FibSequenceResource,
        "/fib/<string:number>"
        )

if __name__ == "__main__":
    app.run(
            host="0.0.0.0",
            debug=False
            )
