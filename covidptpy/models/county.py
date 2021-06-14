class County:
    def __init__(self, json_data):
        all_data = json_data
        all_data['dados_json'] = json_data
        self.__dict__ = all_data

    def __str__(self):
        return str(self.dados_json)

class CountySet:
    def __init__(self, json_data):
        all_data = [County(data) for data in json_data]
        self.county_list = all_data
        self.dados_json = json_data

    def __str__(self):
        return str(self.dados_json)

    def __iter__(self):
        return iter(self.county_list)