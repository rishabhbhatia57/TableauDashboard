from flask import Flask, jsonify, request, render_template
from getJWT import getJWT
from flask_cors import CORS, cross_origin
# from connectedApps import signIntoConnectedApps, getConnectAppsList
import json
app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def index():
    return "<h3>Python Flask API is running...</h3>"

@app.route('/GetJWT')
def GetJWT():
    getToken = getJWT()
    return getToken

@app.route('/index')
def Index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

