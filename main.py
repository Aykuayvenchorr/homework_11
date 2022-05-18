import utils
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def page_all_candidates():
    candidates = utils.load_candidates_from_json()
    return render_template('list.html', items=candidates)


@app.route('/candidate/<int:pk>')
def page_by_pk(pk):
    candidate = utils.get_candidate(pk)
    return render_template('single.html', item=candidate)


@app.route('/search/<candidate_name>')
def page_by_search_name(candidate_name):
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', items=candidates, len_can=len(candidates))


@app.route('/skill/<skill_name>')
def page_by_skills(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', items=candidates, skill=skill_name, len_can=len(candidates))


app.run(debug=True)
