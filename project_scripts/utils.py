import requests

auth_endpoint = "https://reservabertioga.sescsp.org.br/bertioga-web/usuario/meu-perfil/authenticate"
base_availability_endpoint = "https://reservabertioga.sescsp.org.br/bertioga-web/periodo/ano/"
usuario_endpoint = "https://reservabertioga.sescsp.org.br/bertioga-web/usuario"
temporadas_endpoint = "https://reservabertioga.sescsp.org.br/bertioga-web/temporadas"


def get_auth(credencial_id, nome, email, numero_matricula, session=None):
    payload = {
        'id': credencial_id,
        'nome': nome,
        'email': email,
        'numeroMatricula': numero_matricula
    }

    if session is None:
        s = requests.Session()
    else:
        s = session
    auth = s.post(auth_endpoint, json=payload)
    assert auth.status_code == 200
    return s, auth.json()


def get_usuario(payload, s):
    usuario = s.get(usuario_endpoint, json=payload)
    assert usuario.status_code == 200
    return s, usuario.json()


def get_temporadas(s):
    temporadas = s.get(temporadas_endpoint)
    assert temporadas.status_code == 200
    return s, temporadas.json()


def check_disponibilidade(temporadas, s, tipo="COMPRA"):
    vagas = list()
    disponivel = False
    for ano in temporadas.keys():
        print(ano)
        endpoint_ano = f"{base_availability_endpoint}{ano}/mes/"
        for mes in temporadas[ano]:
            endpoint_mes = f"{endpoint_ano}{mes}?tipo={tipo}"
            print(f"{endpoint_mes}")
            disponibilidade = s.get(endpoint_mes)
            assert disponibilidade.status_code == 200
            if len(disponibilidade.json()) > 0:
                disponivel = True
            vagas.append(disponibilidade.json())
    return s, vagas, disponivel
