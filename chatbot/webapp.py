from flask_restful import Api

from flask import Flask , request , redirect , url_for , render_template ,jsonify

app = Flask(__name__)

api = Api(app)

@app.route('/')
def HomePage():

    return render_template("welcome.html")


if __name__=="__main__" :
     app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
     app.run(debug=True)   

