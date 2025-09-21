from DataBase.skills_required import get_skills_required_for_position
from DataBase.skills_to_employees import get_all_skills_employee
from DataBase.employees import get_all_employees
from DataBase.position_mathces import *

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

level_weights = {
    "beginner": 1,
    "intermediate": 2,
    "advanced": 3,
    "expert": 4
} #для учета уровня знаний в весе 

def count_match_score(position_id):
    ids_req = get_skills_required_for_position(position_id)
    ids_req_count = len(ids_req)
    all_employees = get_all_employees()

    for employee_id in all_employees:
        if not get_match_score(position_id,employee_id):
            match_count = 0
            result = get_all_skills_employee(employee_id)
            if result:
                for row in result:
                    if row['skill_id'] in ids_req:  match_count+=level_weights.get(row['skill_level'],1)
                score = round(match_count/(ids_req_count*max(level_weights.values()))*100,2)
                create_match(position_id,employee_id,score)



