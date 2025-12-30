from app.db import get_session

# Keep aliases here so tests can override easily
get_db = get_session
