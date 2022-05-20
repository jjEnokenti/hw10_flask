from flask import Flask

# Импорт функций для обработки данных
from utils import get_candidate_by_id, get_all_candidates, get_candidates_by_skill

app = Flask(__name__)


@app.route('/')
def index():
    """
    Выводит имена кандидатов
    :return candidates:
    """
    candidates = get_all_candidates()

    return f"<pre>{candidates}</pre>"


@app.route("/candidates/<int:uid>/")
def get_candidate_id(uid):
    """
    Выводит всю информацию кандидата по id
    """
    candidate = get_candidate_by_id(uid)

    return f"<img src={candidate['picture']}>\n" \
           f"<pre>{candidate['name']} -\n" \
           f"{candidate['position']}\n" \
           f"{candidate['skills']}<pre>"


@app.route("/skills/<skill>/")
def get_candidate_skill(skill):
    """
    Выводит список кандидатов по выбранному навыку
    :param skill:
    :return candidates:
    """
    candidates = get_candidates_by_skill(skill)

    return f"<pre>{candidates}</pre>"


if __name__ == '__main__':
    app.run()
