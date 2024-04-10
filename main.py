from cal import Cal
from data import Data
from sites import name2location

if __name__ == "__main__":

    d = Data()
    d.fetch(sites=['Kriterion', 'Lab111', 'DeUitkijk'])
    print(d.data)
    for name in d.data.keys():
        c = Cal(ftname=name)
        for e in d.data[name]:
            c.addEvent(
                summary=e["film_name"],
                dtstart=e["start_datetime"],
                dtend=e.get("end_datetime", None),
                uid=e["uid"],
                location=name2location[name],
                descripion=e["description"],
            )

        c.write()
