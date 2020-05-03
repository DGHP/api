from app import app
from app.models import games, users, get_from_database

@app.shell_context_processor
def make_shell_context():
    return {'games': games, 'users': users, 'get_from_database': get_from_database}