from flask import Flask, request, jsonify

app = Flask(__name__)
students = {}
next_id = 1


@app.route('/')
def home():
    return "Student API Running"

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(list(students.values()))

@app.route('/students', methods=['POST'])
def add_student():
    global next_id
    data = request.get_json()
    student = {'id': next_id, 'name': data['name'], 'roll': data['roll']}
    students[next_id] = student
    next_id += 1
    return jsonify(student), 201

@app.route('/students/<int:sid>', methods=['DELETE'])
def delete_student(sid):
    students.pop(sid, None)
    return jsonify({'msg': 'Deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)