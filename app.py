from flask import Flask, jsonify, request, render_template
from getJWT import getJWT
from flask_cors import CORS, cross_origin
# from connectedApps import signIntoConnectedApps, getConnectAppsList
import json
app = Flask(__name__)
cors = CORS(app)


# app = Flask(__name__)
# CORS(app)
# app.config["DEBUG"] = True


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/GetJWT')
def GetJWT():
    getToken = getJWT()
    return getToken

# @app.route('/Firstpage')
# def Firstpage():
#     return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    # app.debug = True

