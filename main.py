
from flask import Flask, render_template, Response, request
import json

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html", title="HOME PAGE")

@app.route("/live_bots", methods=['GET', 'POST'])
def live_bots():
    return Response(json.dumps(['127.0.0.1', '127.0.0.1', '127.0.0.1']),  mimetype='application/json')
    # return Response(['127.0.0.1', '127.0.0.1', '127.0.0.1'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)