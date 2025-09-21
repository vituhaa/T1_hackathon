from flask import Flask, jsonify, request
from flask_cors import CORS
from DataBase.positions import get_pos_by_id, get_all_positions
from DataBase.position_mathces import get_all_matches
from DataBase.employees import get_employee
from DataBase.skills_to_employees import get_all_skills_employee
from DataBase.skills import get_skill
from DataBase.skills_required import get_skills_required_for_position
from Analytics.similarity_count import count_match_score

app = Flask(__name__)
# CORS(app)  # разрешаем запросы с фронта
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})


@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Привет от Flask!"})

@app.route("/api/position_card/<int:position_id>", methods=["GET"])
def getPositionInfo(position_id):
    count_match_score(position_id)
    result = get_pos_by_id(position_id)
    employees_id = get_all_matches(position_id)
    employees = []
    for row in employees_id:
        id = row['employee_id']
        employee = get_employee(id)
        full_name = f"{employee['last_name']} {employee['first_name']} {employee.get('fath_name', '') or ''}".strip()
        employee['name'] = full_name
        skills = []
        skills_raw = get_all_skills_employee(id)
        for skill in skills_raw:
            skill_id = skill['skill_id']
            name = get_skill(skill_id)['name']
            skills.append({'name':name,'level':skill['skill_level']})
        employee['skills'] = skills
        employees.append(employee)
    result['employees'] = employees
    return jsonify(result)

@app.route("/api/positions", methods=["GET"])
def list_positions():
    positions = get_all_positions(True) 
    positions.extend(get_all_positions(False))
    for pos in positions:
        skill_ids = get_skills_required_for_position(pos['id'])
        skills = []
        for id in skill_ids:
            name = get_skill(id)['name']
            skills.append({'id':id,'name':name})
        pos['skills'] = skills
    
    return jsonify(positions)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
