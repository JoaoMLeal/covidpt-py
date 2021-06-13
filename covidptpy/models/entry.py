class Entry:

    def __init__(self, json_data):
        _id = next(iter(json_data['data']))
        all_data = {k: v[_id] for k, v in json_data.items()}
        all_data['id'] = _id
        all_data['dados_json'] = json_data
        self.__dict__ = all_data

    def __str__(self):
        return str(self.dados_json)
