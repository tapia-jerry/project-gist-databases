from .models import Gist
from datetime import datetime

def search_gists(db_connection, github_id=None, created_at=None):
    query = None
    if github_id:
        query = db_connection.execute('SELECT * FROM gists where github_id = ?', [github_id])
    elif created_at:
        query = db_connection.execute('SELECT * FROM gists where datetime(created_at) = datetime(?)', [created_at])
    else:
        query = db_connection.execute('SELECT * FROM gists')

    result = []
    for gist in query.fetchall():
        result.append(Gist(gist))
    return result