from covidptpy.utils import transpose_json


class Entry:

    def __init__(self, json_data, needs_transpose=True):
        if needs_transpose:
            new_data = transpose_json(json_data)
        else:
            new_data = json_data

        self.__dict__ = new_data
        _id = next(iter(new_data.keys()))
        self.__dict__ = new_data[_id]
        self.id = _id
        self.dados_originais = json_data
        self.dados_trans = new_data

    def __str__(self):
        return str(self.dados_trans)


class EntrySet:

    def __init__(self, json_data):
        new_data = transpose_json(json_data)

        self.entry_list = [Entry(dict([(k, v)]), needs_transpose=False) for k, v in new_data.items()]
        self.dados_originais = json_data
        self.dados_trans = new_data

    def __str__(self):
        return str(self.dados_trans)

    def __iter__(self):
        return iter(self.entry_list)

    def __getitem__(self, item):
        return self.entry_list[item]