from datetime import datetime

def time_formatted():
    return datetime.now().strftime('%d-%m-%G %H:%M')
