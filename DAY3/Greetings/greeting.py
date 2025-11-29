import datetime as dt
def say_hello(name):
    current_hour=dt.datetime.now().hour

    if current_hour<12:
        greeting="GOOD MORNING"
    elif 12<=current_hour<17:
        greeting="GOOD AFTERNOON"
    else:
        greeting="GOOD EVENING"

    print(f"{greeting},{name}!")