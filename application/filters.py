from application import app


@app.template_filter('date_format')
def date_format(date):
    """
    Format date to "Month day"
    """
    if date is None:
        return ''
    return f'{date:%B %d}'
