from datetime import datetime

def get_current_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S") 


get_current_time()


