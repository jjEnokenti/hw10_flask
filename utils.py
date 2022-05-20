# Импорт load из json, для получения данных из json файла
from json import load


def get_data():
    """
    Формирует список словарей с информацией по кандидатам из json файла
    :return data:
    """
    with open('candidates.json', encoding='utf-8') as inf:
        data = load(inf)

    return data


def get_all_candidates():
    """
    Формирует список имен кандидатов
    :return names:
    """
    data = get_data()
    candidates = [candidate['name'] for candidate in data]
    names = '\n'.join(candidates)

    return names


def get_candidate_by_id(user_id):
    """
    Формирует подробную информацию кандидата по id
    :param user_id:
    :return candidate_by_id:
    """
    data = get_data()
    candidate_by_id = {
        'name': None,
        'position': None,
        'skills': None,
        'picture': None
    }

    for candidate in data:
        if candidate['id'] == user_id:
            candidate_by_id['name'] = candidate['name']
            candidate_by_id['position'] = candidate['position']
            candidate_by_id['skills'] = candidate['skills']
            candidate_by_id['picture'] = candidate['picture']

    return candidate_by_id


def get_candidates_by_skill(skill):
    """
    Формирует строку из кандидатов подходящих по выбранному навыку
    :param skill:
    :return candidates:
    """
    data = get_data()
    candidates = []

    for candidate in data:
        if skill.lower() in candidate['skills'].lower():

            candidates.append(f"{candidate['name']} -\n"
                              f"{candidate['position']}\n"
                              f"{candidate['skills']}")

    candidates = '\n\n'.join(candidates)

    return candidates
