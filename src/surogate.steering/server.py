from flask import Flask, request, jsonify
import providers.kit as steering

app = Flask(__name__)

@app.route('/steering', methods=["POST"])
def steer():
    request_data = request.json
    print(request_data)
    steering_command = jsonify(request_data)
    print(steering_command)

    if(steering_command.direction == 'left'):
        steering.left()
    else:
        steering.right()