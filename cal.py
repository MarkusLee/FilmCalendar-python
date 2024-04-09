import os
from datetime import datetime
from icalendar import Calendar, Event
from util import getUID, getDefaultEnd


class Cal:
    def __init__(self, ftname="FilmAgenda"):
        self.ftname = ftname
        g = open("template.ics", "rb")
        self.cal = Calendar.from_ical(g.read())
        # change the calendar name
        self.cal["X-WR-CALNAME"] = ftname

    def display(self):
        print(self.cal.to_ical().decode("utf-8").replace("\r\n", "\n").strip())
        return self

    def setEvent(self, summary, dtstart, dtend, uid, location, descripion=None):
        event = Event()
        event.add("dtstamp", datetime.today().date(), parameters={"VALUE": "DATE"})
        event.add("uid", uid)
        event.add("summary", summary)
        event.add("dtstart", dtstart, parameters={"VALUE": "DATE"})
        if dtend is not None:
            event.add("dtend", dtend, parameters={"VALUE": "DATE"})
        else:
            # event.add('dtend', getDefaultEnd(dtstart), parameters={'VALUE': 'DATE'})
            event.add("dtend", dtstart, parameters={"VALUE": "DATE"})
        event.add("location", location)
        # event.add('class', 'PUBLIC')
        event.add("TRANSP", "OPAQUE")
        if descripion is not None:
            event.add("description", descripion)
        # event.add("X-APPLE-UNIVERSAL-ID", "42902458-1dd4-5105-04d0-2dccc0194c5f")
        self.cal.add_component(event)

    def write(self, output_path="./output"):
        target_file = os.path.join(output_path, self.ftname + ".ics")
        f = open(target_file, "wb")
        f.write(self.cal.to_ical())
        f.close()
        return self


if __name__ == "__main__":
    Cal().display().write()
