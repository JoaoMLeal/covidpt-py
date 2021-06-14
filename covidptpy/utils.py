from datetime import date, timedelta


def today():
    """Returns today's date in the dd-mm-yyyy format"""
    today_ = date.today()
    return today_.strftime("%d-%m-%Y")


def yesterday():
    """Returns yesterday's date in the dd-mm-yyyy format"""
    yesterday_ = date.today() - timedelta(days=1)
    return yesterday_.strftime("%d-%m-%Y")


def transpose_json(json_data):
    """Returns the a transposed version of the given json data
    {k1->{id1:x1, id2:x2}, k2->{id1:y1, id2: y2}}  ==>  {id1->{k1:x1, k2:y1}, id2->{k1:x2, k2:y2}}
    """
    new_data = dict()
    count = 0
    for outer_key, outer_dict in json_data.items():
        count += 1
        for inner_key, inner_value in outer_dict.items():
            if count == 1:
                new_data[inner_key] = dict()
            new_data[inner_key][outer_key] = inner_value
    return new_data
