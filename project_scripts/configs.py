import configparser


class ProjectConfigs:
    _configs = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def configs(cls):
        if cls._configs is None:
            cls._configs = _read_configs()
        return cls._configs


def _read_configs():
    parser = configparser.ConfigParser()
    parser.read('./credentials.ini')
    project_configs = parser['credentials']

    project_configs['email'] = project_configs.get('email')
    project_configs['nome'] = project_configs.get('nome')
    project_configs['numero_matricula'] = project_configs.get('numero_matricula')
    project_configs['credencial_id'] = project_configs.get('credencial_id')

    return project_configs


configs = ProjectConfigs.configs()
