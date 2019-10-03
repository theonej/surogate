from flask import Flask, request, jsonify
import providers.kit as steering

app = Flask(__name__)

@app.route('/steering', methods=["POST"])
def steer():
    steering_command = jsonify(request.json)
    print(steering_command)

    if(steering_command.direction == 'left'):
        steering.left()
    else:
        steering.right()