from flask import Flask, render_template, request, jsonify

# for deploying the prediction API independently WITH STANDALOBE-FRONTEND
from flask_cors import CORS

from chat import get_response

app = Flask(__name__)

# use this to deploy the prediction API independently
CORS(app)

# USE THE FOLLOWING COMMENTED CODE FOR DEPLOYMENT within the ninja2 template
# @app.get("/")
# def index_get():
#     return render_template("base.html")


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid or not
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
