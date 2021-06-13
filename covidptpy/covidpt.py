from covidptpy.core import *
from covidptpy.utils import print_error


DATE_1 = "01-01-2021"
DATE_2 = "01-06-2021"
COUNTY = "ABRANTES"

print(get_county_list())
print(get_entry_from_until(DATE_1, DATE_2).json())
print(get_entry(DATE_2).json())
#print(get_entry_counties(DATE_1, DATE_2))
#print(get_entry_county(DATE_1, DATE_2, COUNTY))
#print(get_full_dataset().json())
#print(get_full_dataset_counties().json())
print(get_last_update().json())
print(get_last_update_counties().json())
print(get_last_update_specific_county(COUNTY).json())
print(get_status())


