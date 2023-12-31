from configs import read_configs
from utils import *

configs = read_configs()

session, auth = get_auth(configs['credencial_id'], configs['nome'], configs['email'], configs['numero_matricula'])

session, usuario = get_usuario(auth, session)

session, temporadas = get_temporadas(session)

session, vagas_compra, disopnivel_compra = check_disponibilidade(temporadas, session)

session, vagas_sorteio, disopnivel_venda = check_disponibilidade(temporadas, session, tipo="SORTEIO")

with open("resultado_compra.env", "w") as f:
    f.write(f"RESULTADO={disopnivel_compra}")
