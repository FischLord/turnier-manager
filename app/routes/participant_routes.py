from flask import render_template
from . import participants

@participants.route('/participants')
def participant_list():
    return render_template('participants/participant_list.html')

@participants.route('/participants/<int:participant_id>')
def participant_detail(participant_id):
    return render_template('participants/participant_detail.html')
