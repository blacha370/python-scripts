import json
import os


class AppRunner:
    def __init__(self):
        os.makedirs(os.environ['USERPROFILE'] + '\\app_runner_data', exist_ok=True)
        self.path = os.environ['USERPROFILE'] + '\\app_runner_data\\app_data.json'
        self.data = {'programs_list': list(), 'pages_list': set()}
        self.getUserConfig()

    def getUserConfig(self):
        try:
            with open(self.path, 'r', encoding='UTF-8') as file:
                json_data = file.read()
                try:
                    data = json.loads(json_data)
                    self.data['programs_list'] = data['programs_list']
                    self.data['pages_list'] = set(data['pages_list'])
                    return
                except json.JSONDecodeError:
                    return
        except FileNotFoundError:
            return

    def remove(self, resource_to_delete, path: str):
        structure = self.data[resource_to_delete]
        if type(structure) == list:
            for program in self.data[resource_to_delete]:
                if program['path'] == path:
                    self.data[resource_to_delete].remove(program)
                    return
        elif type(structure) == set:
            self.data[resource_to_delete].discard(path)
            return

    def add(self, resource_to_add, path):
        structure = self.data[resource_to_add]
        if type(structure) == list:
            is_in = False
            for program in self.data['programs_list']:
                if program['path'] == path:
                    is_in = True
                    program['positions'].append([0, 0, 300, 300])
            if not is_in:
                self.data['programs_list'].append({'path': path, 'positions': [[0, 0, 300, 300]]})
        elif type(structure) == set:
            if path in self.data['pages_list']:
                return
            else:
                if 'https://' in path:
                    self.data['pages_list'].add(path)
                elif 'https://' not in path:
                    self.data['pages_list'].add('https://' + path)

    def changePosition(self, path, position, index):
        for program in self.data['programs_list']:
            if program['path'] == path:
                program['positions'][index] = position

    def saveData(self):
        data = ({
            'pages_list': list(self.data['pages_list']),
            'programs_list': self.data['programs_list']
        })
        data_json = json.dumps(data)
        with open(self.path, 'w') as file:
            file.write(data_json)
