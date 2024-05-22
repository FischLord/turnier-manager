from flask import render_template
from . import events

@events.route('/events')
def event_list():
    return render_template('events/event_list.html')

@events.route('/events/<int:event_id>')
def event_detail(event_id):
    return render_template('events/event_detail.html')
