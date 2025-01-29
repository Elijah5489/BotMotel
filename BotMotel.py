from datetime import datetime, timedelta
from flask import Flask, session, request, render_template, jsonify
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ensure you set a secret key for session management

visitors = {}

def track_visit(session_id):
    if session_id not in visitors:
        visitors[session_id] = {
            'start_time': datetime.now(),
            'end_time': None,
            'is_bot': False
        }

def record_end_time(session_id):
    if session_id in visitors:
        visitors[session_id]['end_time'] = datetime.now()

def generate_report():
    total_time = timedelta()
    total_visitors = len(visitors)
    total_bots = sum(1 for v in visitors.values() if v['is_bot'])
    total_humans = total_visitors - total_bots

    for visitor in visitors.values():
        if visitor['end_time']:
            total_time += visitor['end_time'] - visitor['start_time']
        else:
            total_time += datetime.now() - visitor['start_time']

    return (f"Total visitors: {total_visitors}, Total bots: {total_bots}, "
            f"Total humans: {total_humans}, Total time: {total_time}")

def mark_bot(session_id):
    if session_id in visitors:
        visitors[session_id]['is_bot'] = True

def perform_search(query):
    real_results = [
        {"title": "Legit Result 1", "link": "#"},
        {"title": "Legit Result 2", "link": "#"},
    ]
    fake_results = [{"title": f"Fake Result {i}", "link": "#"} for i in range(3, 6)]
    return real_results + fake_results

@app.route('/')
def index():
    session_id = session.get('session_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        session['session_id'] = session_id
    track_visit(session_id)
    return render_template('index.html')

@app.route('/end_visit')
def end_visit():
    session_id = session.get('session_id')
    if session_id:
        record_end_time(session_id)
    return 'Visit ended.'

@app.route('/report')
def report():
    report = generate_report()
    return report

@app.route('/mark_bot/<session_id>')
def mark_bot_route(session_id):
    mark_bot(session_id)
    return f'Session {session_id} marked as bot.'

@app.route('/search')
def search():
    query = request.args.get('query')
    print(f"Search query: {query}")  # Log the search query
    results = perform_search(query)
    print(f"Search results: {results}")  # Log the search results
    return render_template('search_results.html', results=results)

@app.route('/result/<int:result_id>')
def view_result(result_id):
    return f"Viewing result {result_id}"

@app.route('/bot_detected')
def bot_detected():
    return render_template('bot_detected.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
