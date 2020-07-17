
from flask import Flask, render_template, Response, request
import requests 
import json

bot_subnet = '10.0.0'
bot_net_interval = (100, 255)
bot_endpoint = '/is_active'
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html", title="HOME PAGE")

@app.route("/live_bots", methods=['GET', 'POST'])
def live_bots():
    active_bots = []
    for i in range(*bot_net_interval):
        bot_url = f"http://{bot_subnet}.{i}/{bot_endpoint}"
        print(bot_url)
        r = requests.get(url = bot_url) 
        data = r.json()
        if 'yes' in data:
            active_bots += [bot_url]
    return Response(json.dumps(active_bots),  mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)