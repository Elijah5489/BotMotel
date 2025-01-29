from datetime import datetime, timedelta

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
