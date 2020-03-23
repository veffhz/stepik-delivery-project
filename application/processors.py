from datetime import datetime

from application import app


@app.context_processor
def inject_now():
    """
    Current date for footer
    """
    return {'now': datetime.now()}
