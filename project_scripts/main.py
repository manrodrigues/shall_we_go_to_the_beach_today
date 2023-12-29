from configs import ProjectConfigs
from utils import *

configs = ProjectConfigs.configs()

session, auth = get_auth(configs['credencial_id'], configs['nome'], configs['email'], configs['numero_matricula'])

session, usuario = get_usuario(auth, session)

session, temporadas = get_temporadas(session)

session, vagas_compra, disopnivel_compra = check_disponibilidade(temporadas, session)

session, vagas_sorteio, disopnivel_venda = check_disponibilidade(temporadas, session, tipo="SORTEIO")

print(disopnivel_compra, disopnivel_venda)
