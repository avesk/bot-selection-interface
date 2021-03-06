
from flask import Flask, render_template, Response, request
import requests 
import json

bot_subnet = '10.0.0'
bot_net_interval = (100, 110)
bot_endpoint = 'is_active'
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html", title="HOME PAGE")

@app.route("/live_bots", methods=['GET', 'POST'])
def live_bots():
    active_bots = []
    for i in range(*bot_net_interval):
        bot_host_name = "http://" + bot_subnet + "." + str(i)
        bot_url = bot_host_name + "/" + bot_endpoint
        print(bot_url)
        try:
            res = requests.get(url=bot_url, verify=False, timeout=1).json()
            print(res)
            if res['is_active']:
                active_bots.append(bot_host_name)
        except Exception as e:
            print(e)
            print(bot_url + " unavailable")
            continue
    return Response(json.dumps(active_bots),  mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)