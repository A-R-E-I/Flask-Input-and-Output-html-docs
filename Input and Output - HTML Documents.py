from flask import Flask, render_template, request
import os.path
from os import path

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])

def main():
    if request.method == "GET":
        return render_template("Input.html")
    else:
        GetInfo()
        return render_template("Output.html")

def GetInfo():
    global useremail, userpasswd;
    print("I am in GetInfo");
    useremail = request.form.get("txtuseremail")
    userpasswd = request.form.get("txtpassword")

    FileConnectivity()
    return render_template("Output.html",username=useremail,password=userpasswd)

def FileConnectivity():
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    fileexist = bool(path.exists(StoredInfo.docx));

    if(fileexist == True):
        adminfile = open(StoredInfo.docx,"r");
    else:
        adminfile = open(StoredInfo.docx,"x");
        adminfile = open(StoredInfo.docx,"a");
        file.write("Username: " + useremail + "Password: " + userpasswd)

    adminfile.close();


if __name__=="__main__":
    app.run()
