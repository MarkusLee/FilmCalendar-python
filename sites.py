from html_parser import *

name2url = {
    'Lab111': 'https://www.lab111.nl/programma/listview/',
    'Kriterion': "https://www.kriterion.nl",
    'DeUitkijk': 'https://www.uitkijk.nl',
    # Add more name-url mappings as needed
}

name2parser = {
    'Lab111': parse_lab111,
    'Kriterion': parse_kriterion,
    'DeUitkijk': parse_deuitkijk,
    # Add more name-parser mappings as needed
}

name2location = {
    'Lab111': 'LAB111\nArie Biemondstraat 111, 1054 PD Amsterdam, Netherland',
    'Kriterion': 'Kriterion\nRoetersstraat 170, 1018 WE Amsterdam, Netherland',
    'DeUitkijk': 'De Uitkijk\nPrinsengracht 452, 1017 KE Amsterdam, Netherlands',
    # Add more name-location mappings as needed 
}

name2color = {
    'Lab111': '#ffb4d1',
    'Kriterion': '#999999',
    'DeUitkijk': '#e04625',
    # Add more name-color mappings as needed
}