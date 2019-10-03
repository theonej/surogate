from flask import Flask, request, jsonify
import providers.kit as steering

app = Flask(__name__)

@app.route('/steering', methods=["POST"])
def steer():
    steering_command = request.json

    angle = 0
    if(steering_command['direction'] == 'left'):
        angle = steering.left()
    else:
        angle = steering.right()
    
    return jsonify(angle)
