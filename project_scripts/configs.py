import os


def read_configs():
    project_configs = {'email': os.environ['EMAIL'], 'nome': os.environ['NOME'],
                       'numero_matricula': os.environ['NUMERO_MATRICULA'], 'credencial_id': os.environ['CREDENCIAL_ID']}

    return project_configs


configs = read_configs()
