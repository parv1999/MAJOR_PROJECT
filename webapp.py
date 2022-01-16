from email import message
import requests

import json

from flask_restful import Api

from flask import Flask , request , redirect , url_for , render_template ,jsonify

app = Flask(__name__)

api = Api(app)

@app.route('/',methods=["GET","POST"])
def HomePage():

    if request.method=="POST":

        Message = request.form.get("sendMessage")
         
        return render_template("welcome.html")

    return render_template('welcome.html')

if __name__=="__main__" :
     app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
     app.run(debug=True)   
