from flask import Flask, request, jsonify
import providers.kit as steering

app = Flask(__name__)

@app.route('/steering', methods=["POST"])
def steer():
    steering_command = request.json

    if(steering_command['direction'] == 'left'):
        steering.left()
    else:
        steering.right()