from datetime import datetime, timedelta


def getUID(name, film_name, start_datetime) -> str:
    return str(name) + "-" +str(film_name) + "-" + str(start_datetime)


def getDefaultEnd(dt: datetime, minutes=120) -> datetime:
    # add 2 hours
    dtend = dt + timedelta(minutes=minutes)
    return dtend
    
