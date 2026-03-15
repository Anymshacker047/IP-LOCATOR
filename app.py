from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    result = ""

    if request.method == "POST":
        ip = request.form.get("ip")

        output = subprocess.getoutput(f"python main.py {ip}")
        result = output

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()
