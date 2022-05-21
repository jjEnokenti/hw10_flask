from flask import Flask

# Импорт функций для обработки данных
from utils import get_candidate_by_id, get_all_candidates, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def all_candidates():
    """
    Выводит всех кандидатов
    :return candidates:
    """

    #
    candidates = get_all_candidates()

    return f"<pre>{candidates}</pre>"


@app.route("/candidates/<int:uid>/")
def get_candidate_id(uid):
    """
    Выводит всю информацию кандидата по id
    """

    #
    candidate = get_candidate_by_id(uid)

    if candidate:
        return candidate

    return "<pre>Такого кандидата нет</pre>"


@app.route("/skills/<skill>/")
def get_candidate_skill(skill):
    """
    Выводит список кандидатов по выбранному навыку
    :param skill:
    :return candidates:
    """

    #
    candidates = get_candidates_by_skill(skill)

    if candidates:
        return f"<pre>{candidates}</pre>"

    return f'Кандидатов с навыком "{skill}" нет'


if __name__ == '__main__':
    app.run()
