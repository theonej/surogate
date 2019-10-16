from flask import Flask, request, jsonify
import providers.kit as steering

app = Flask(__name__)

@app.route('/steering', methods=["POST"])
def steer():
    steering_command = request.json

    angle = 0
    index = 0
    if(steering_command['servo_index'] != None):
        index = int(steering_command['servo_index'])
        print("Setting servo index")
    if(steering_command['direction'] == 'left'):
        angle = steering.left(index)
    else:
        angle = steering.right(index)
    
    return jsonify(angle)

@app.route('/steering', methods=["POST"])
def set_angle():
    angle_command = request.json

    angle = 0
    index = 0
    if(angle_command['servo_index'] != None):
        index = int(angle_command['servo_index'])
    if(angle_command['angle'] != None):
        angle = int(angle_command['angle'])
        
    steering.set_angle(angle, index)
