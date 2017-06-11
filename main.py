from flask import Flask, jsonify, request, session, url_for, render_template, redirect
import time, os
import cgibin.index as apievent

app = Flask(__name__)



###########################################################################
#  WEB PAGE                                                              #
###########################################################################
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/nav_facebook")
def nav_facebook():
    return render_template('nav_facebook.html')


###########################################################################
#  API EVENT                                                              #
###########################################################################
@app.route("/api/facebook",methods=['GET', 'POST'])
def api_facebook():
    print("in")
    fid = request.form['id']
    token = request.form['token']
    limit = request.form['limit']

    package = {"fid":fid,"token":token,"limit":limit}
    print("inin")
    rootpath = str(os.path.dirname(__file__))
    event = apievent.main(rootpath)
    result = event.api_facebook(package)
    print("ok")
    #必須為JSON格式
    return result



if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True,host='0.0.0.0')

