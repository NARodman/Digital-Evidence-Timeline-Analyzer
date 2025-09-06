from flask import Flask, jsonify

app = Flask(__name__)

#test route

@app.route('/test', methods=['GET'])
def hello():
    return jsonify({"message": "Backend is alive!"})


if __name__ == "__main__": 
    app.run(debug=True, port=5000)
