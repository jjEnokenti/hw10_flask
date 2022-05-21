# Импорт load из json, для получения данных из json файла
from json import load


def get_data():
    """
    Формирует список словарей с информацией по кандидатам из json файла
    :return data:
    """

    # Загрузка данных из json файла
    with open('candidates.json', encoding='utf-8') as inf:
        data = load(inf)

    return data


def get_all_candidates():
    """
    Формирует список кандидатов
    :return names:
    """

    # Згрузка данных кандидатов из json файла
    candidates = get_data()

    candidates_list = ''

    # Цикл для формирования строки с дпнными всех кандидатов
    for candidate in candidates:
        candidates_list += f"{candidate['id']} {candidate['name']}\n" \
                           f"{candidate['position']}\n" \
                           f"{candidate['skills']}\n\n"

    return candidates_list


def get_candidate_by_id(user_id):
    """
    Формирует подробную информацию кандидата по id
    :param user_id:
    :return candidate_by_id:
    """

    data = get_data()

    candidate_by_id = ''

    # Цикл для формирования строки с данными кандидата выбранному по id
    for candidate in data:
        if candidate['id'] == user_id:
            candidate_by_id += f"<img src={candidate['picture']}>\n" \
                               f"<pre>{candidate['name']}\n" \
                               f"{candidate['position']}\n" \
                               f"{candidate['skills']}</pre>"

    return candidate_by_id


def get_candidates_by_skill(skill):
    """
    Формирует строку из кандидатов подходящих по выбранному навыку
    :param skill:
    :return candidates:
    """

    data = get_data()

    candidates = ''

    # Цикл для формирования строки с данными о кандидатах по выбранному навыку
    for candidate in data:
        # Поиск навыка независимо от регистра и разбивание строки с навыками на спиоск
        # для исключения ошибочных вхождений
        if skill.lower() in candidate['skills'].lower().split(', '):
            candidates += f"{candidate['name']} -\n" \
                          f"{candidate['position']}\n" \
                          f"{candidate['skills']}\n"

    return candidates
