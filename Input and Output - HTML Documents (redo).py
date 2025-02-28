from flask import Flask, render_template, request
import os.path
from os import path

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])

def main():
    if request.method == "GET":
        return render_template("Input.html")
    else:
        info()
        return render_template("Output.html")

@app.route("/info",methods=["POST"])
def info():
    global useremail, userpasswd;
    print("I am in GetInfo");
    useremail = request.form.get("txtuseremail")
    userpasswd = request.form.get("txtpassword")

    FileConnectivity()
    return render_template("Output.html",username=useremail,password=userpasswd)

def FileConnectivity():
    StoredInfo = "Saveinfo.doc"
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    fileexist = bool(path.exists(StoredInfo));

    if(fileexist == True):
        adminfile = open(StoredInfo,"r");
    else:
        adminfile = open(StoredInfo,"x");
        adminfile = open(StoredInfo,"w");
        Saveinfo.write("Username: " + useremail + "Password: " + userpasswd)

    adminfile.close();


if __name__=="__main__":
    app.run()
