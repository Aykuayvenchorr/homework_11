from config import DATA_PATH
import json


def load_candidates_from_json(path=DATA_PATH):
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_candidate(candidate_id):
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate
    return 'Нет такого кандидата'


def get_candidates_by_name(candidate_name):
    candidates = load_candidates_from_json()
    list_candidates = []
    for candidate in candidates:
        if candidate_name in candidate['name'].split():
            list_candidates.append(candidate)
    return list_candidates


def get_candidates_by_skill(skill_name):
    skilled_candidates = []
    skill_name_lower = skill_name.lower()
    candidates = load_candidates_from_json()

    for candidate in candidates:
        skills = candidate['skills'].lower().strip().split(', ')
        if skill_name_lower in skills:
            skilled_candidates.append(candidate)
    return skilled_candidates


