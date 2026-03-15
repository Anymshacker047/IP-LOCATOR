from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_ip_data(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    return response.json()

@app.route("/", methods=["GET","POST"])
def home():

    data = None

    if request.method == "POST":
        ip = request.form.get("ip")
        data = get_ip_data(ip)

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)