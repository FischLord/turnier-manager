from flask import render_template
from . import results

@results.route('/results')
def result_list():
    return render_template('results/result_list.html')

@results.route('/results/<int:result_id>')
def result_detail(result_id):
    return render_template('results/result_detail.html')
