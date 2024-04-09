import os
from datetime import datetime
from icalendar import Calendar, Event
from util import getUID, getDefaultEnd


class Cal:
    def __init__(self, ftname="FilmAgenda", output_path="./output"):
        self.output_path = output_path
        self.ftname = ftname
        file_path = os.path.join(self.output_path, self.ftname + ".ics")
        if not os.path.exists(file_path):
            with open("template.ics", "rb") as g:
                self.cal = Calendar.from_ical(g.read())
                self.cal["X-WR-CALNAME"] = ftname
        else:
            with open(file_path, "rb") as g:
                self.cal = Calendar.from_ical(g.read())


    def display(self):
        print(self.cal.to_ical().decode("utf-8").replace("\r\n", "\n").strip())
        return self
    
    def eventExists(self, new_event):
        for component in self.cal.walk():
            if component.name == "VEVENT":
                if (component.get('summary') == new_event.get('summary') and
                    component.get('dtstart').dt == new_event.get('dtstart').dt and
                    component.get('location') == new_event.get('location')):
                    return True
        return False

    def addEvent(self, summary, dtstart, dtend, uid, location, descripion=None):
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
        if not self.eventExists(event):
            self.cal.add_component(event)

    def write(self):
        target_file = os.path.join(self.output_path, self.ftname + ".ics")
        with open(target_file, "wb") as f:
            f.write(self.cal.to_ical())


if __name__ == "__main__":
    Cal().display().write()
