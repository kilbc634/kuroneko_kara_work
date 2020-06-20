from flask import Flask, render_template, jsonify, request
import json

MY_NAME = 'Tsukumo'
app = Flask(MY_NAME)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/what_your_name', methods=["GET"])
def get_myName():
    myName = 'My name is {}.'.format(MY_NAME)
    return myName, 200

@app.route('/poedata', methods=["GET"])
def get_poedata():
    jsonStr = str()
    with open('poedata.json', 'r') as f:
        jsonStr = f.read()
    print('[Info] I have a json file as....')
    print(jsonStr)

    print('[Info] I want change this json data to dict type')
    jsonDict = json.loads(jsonStr)
    print('[Info] Done. Like this:')
    print(jsonDict)

    print('[Info] This request should response json data!')
    return jsonify(jsonDict), 200
    
@app.route('/poedata', methods=["POST"])
def post_poedata():
    jsonStr = str()
    with open('poedata.json', 'r') as f:
        jsonStr = f.read()
    print('[Info] I have a json file as....')
    print(jsonStr)

    print('[Info] Have a request want to modify my poedata')
    requestData = request.json
    print(requestData)

    print('[Info] Start modify my poedata.....')
    jsonDict = json.loads(jsonStr)
    for key, value in requestData.items():
        if key in jsonDict:
            jsonDict[key] = value

    print('[Info] Rewrite to origin file....')
    writeStr = json.dumps(jsonDict)
    with open('poedata.json', 'w') as f:
        f.write(writeStr)

    print('[Info] Modify complated! And I will response data after modify')
    return jsonify(jsonDict), 200
    

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80, debug=True)
