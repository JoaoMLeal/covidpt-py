from covidptpy.core import *
from covidptpy.models.entry import Entry

DATE_1 = "01-01-2021"
DATE_2 = "01-06-2021"

DATE_3 = "02-06-2021"
DATE_4 = "05-06-2021"
COUNTY = "ABRANTES"

e = get_entry(DATE_2)
print(e)
es = get_entry_from_until(DATE_1, DATE_2)
print(es[1].confirmados)
cs1 = get_entry_counties(DATE_3, DATE_4)



