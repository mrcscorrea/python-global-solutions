# ── Constantes de exibição (Visualização do código) ────────────────────────────────────────────────────
from dados import REGIOES

LINHA_DUPLA  = "=" * 72
LINHA_SIMPLES = "-" * 72
LINHA_TRACEJADA = "·" * 72

# Mapa de emojis por nível (fallback seguro para terminais sem unicode)
ICONE_NIVEL = {
    "CRITICO":  "[!!!]",
    "ALERTA":   "[!! ]",
    "ATENCAO":  "[ ! ]",
    "NORMAL":   "[ OK]",
    "INVALIDO": "[ERR]"
}

DESCRICAO_RISCO = {
    "CRITICO": "Situação de incêndios críticas. Acione a equipe de campo imediatamente!",
    "ALERTA": "Incêndios eminentes. Redobre a atenção e mantenha a equiipe de campo em prontidão.",
    "ATENCAO": "Atenção redobrada. Mantenha a vigilância.",
    "NORMAL": "Região sob controle. Continue monitorando.",
    "INVALIDO": "Dados inválidos. Verifique as informações."
}

# Falta colocar condicionais para evitar que o usuário insira strings onde deveriam ser números, números onde deveriam ser floats, etc.
def coleta_simulada():
    while True:
        regiao = input("Digite a região que você vai simular e pressione ENTER: ")
        lat = float(input("Digite a Latitude desejada e pressione ENTER: "))

        if lat < -90 or lat > 90:
            print("Latitude inválida. Digite novamente.")
            continue
        
        lon = float(input("Digite a Longitude desejada e pressione ENTER: "))

        if lon < -180 or lon > 180:
            print("Longitude inválida. Digite novamente.")
            continue
        
        area = float(input("Digite a área em km² desejada e pressione ENTER: "))

        if area <= 0:
            print("Área inválida. Digite novamente.")
            continue
        
        ndvi = float(input("Digite o NDVI (Índice de Vegetação por Diferença Normalizada) desejado e pressione ENTER (deve ser decimal!): "))

        if ndvi < 0 or ndvi > 1:
            print("NDVI inválido. Digite novamente.")
            continue

        focos_input = int(input("Digite um número inteiro para o foco de calor e pressione ENTER: "))

        if focos_input < 0:
            print("Focos de calor inválidos. Digite novamente.")
            continue

        umidade = int(input("Digite o percentual (sem porcentagem) da umidade do solo e pressione ENTER: "))

        if umidade < 0 or umidade > 100:
            print("Umidade do solo inválida. Digite novamente.")
            continue

        if umidade < 0 or umidade > 100:
            print("Umidade do solo inválida. Digite novamente.")
            continue

        historico = [int(x) for x in input("Digite o histórico de focos dos últimos 7 dias separados por espaço: ").split()]
        
        if (foco < 0 for foco in historico):
            print("Histórico inválido. Digite novamente.")
            continue

        if len(historico) != 7:
            print("Histórico de focos inválido. Digite novamente.")
            continue

        datainput = input("Digite a data completa do registro (DD/MM/AAAA HH:MM) e pressione ENTER: ")

        data, hora = datainput.split(" ")
        dia, mes, ano = data.split("/")
        timestamp = f"{ano}-{mes}-{dia}T{hora}"

        return regiao, lat, lon, area, ndvi, focos_input, umidade, historico, datainput, timestamp

def classificar_risco(dados):
    lat = float(dados["lat"])
    lon = float(dados["lon"])
    area = int(dados["area_km2"])
    ndvi = float(dados["ndvi_index"])
    focos_input = int(dados["focos_calor"])
    umidade = int(dados["umidade_solo_percent"])
    historico = [int(x) for x in (dados["historico_focos"])]

    if lat < -90 or lat > 90 or lon < -180 or lon > 180 or area <= 0 or ndvi < 0 or ndvi > 1 or focos_input < 0 or umidade < 0 or umidade > 100 or len(historico) != 7:
        return "INVALIDO"
    
    if focos_input >= 10 or (umidade <= 10 and ndvi <= 0.3):
        return "CRITICO"
    
    if focos_input >= 5 or (umidade <= 20 and ndvi <= 0.5):
        return "ALERTA"
    
    if focos_input >= 2 or (umidade <= 30 and ndvi <= 0.7):
        return "ATENCAO"
    
    return "NORMAL"

def gerar_alerta(dados, nivel_risco):
    regiao = dados["regiao"]
    lat = dados["lat"]
    lon = dados["lon"]
    area = dados["area_km2"]
    ndvi = dados["ndvi_index"]
    focos_input = dados["focos_calor"]
    umidade = dados["umidade_solo_percent"]
    historico = dados["historico_focos"]
    timestamp = dados["timestamp"]
    
    print(LINHA_DUPLA)
    print(f"Sistema de Alerta: {ICONE_NIVEL[nivel_risco]} {nivel_risco}")
    print(LINHA_DUPLA)
    print(f"{DESCRICAO_RISCO[nivel_risco]}")
    print()
    print(f"Região: {regiao}")
    print(f"Latitude: {lat}")
    print(f"Longitude: {lon}")
    print(f"Área: {area}")
    print(f"NDVI: {ndvi}")
    print(f"Focos de calor: {focos_input}")
    print(f"Umidade do solo: {umidade}%")
    print(f"Histórico de focos: {historico}")
    print(f"Timestamp: {timestamp}")


def processar_dados():
    for regiao in REGIOES:
        risco = classificar_risco(regiao)
        gerar_alerta(regiao, risco)


def main():

    print()
    print(LINHA_DUPLA)
    print("          ██████  ██████  ██████  ██ ███████     ")
    print("         ██    ██ ██   ██ ██   ██ ██ ██          ")
    print("         ██    ██ ██████  ██████  ██ ███████     ")
    print("         ██    ██ ██   ██ ██   ██ ██      ██     ")
    print("          ██████  ██   ██ ██████  ██ ███████     ")
    print("          S  E  N  T  I  N  E  L  —  2 0 2 6       ")
    print(LINHA_DUPLA)
    print("M e n u    d e    I n t e r a ç õ e s")
    print()
    print("1 - Coleta de queimadas simulada (Você insere)")
    print("2 - Coleta de queimadas de arquivos (a partir de nosso banco de dados)")
    print()

    while True:
        escolha = input("Digite uma opção do menu interativo e pressione ENTER: ")
        if escolha.isdigit():
            escolha = int(escolha)
            if 1 <= escolha <= 2:
                break
        print("Opção inválida. Digite novamente")

    match escolha:
        case 1:
            regiao, lat, lon, area, ndvi, focos_input, umidade, historico, datainput, timestamp = coleta_simulada()

            dados = { "regiao": regiao, "lat": lat, "lon": lon, "area_km2": area, "ndvi_index": ndvi, "focos_calor": focos_input,
            "umidade_solo_percent": umidade, "historico_focos": historico, "data": datainput, "timestamp": timestamp }
            risco = classificar_risco(dados)
            gerar_alerta(dados, risco)
        case 2:
            print("Processando dados do banco de dados...")
            processar_dados()
        case _:
            print("Opção inválida. Digite novamente")

    print(LINHA_DUPLA)


if __name__ == "__main__":
    main()