# ===========================================================================
#  ORBIS SENTINEL — Módulo principal de interação com o usuário
#
#  Disciplina: Computational Thinking With Python (CTWP)
#  Aluno: Marcos Vinícios Corrêa dos Santos
#  Matrícula: RM571080
#
#  Global Solution 2026 · FIAP · Engenharia de Software · 1º Ano
# ===========================================================================
#
#  Este módulo implementa as funções principais do sistema:
#   - ler_float()
#   - ler_int()
#   - ler_texto()
#   - ler_data()
#   - coleta_simulada()
#   - processar_dados()
#   - gerar_alerta()
#   - main()
#
#  Ele interage com o módulo de dados e executa a lógica principal
#  do sistema de alerta de incêndios.
# ===========================================================================
from dados import REGIOES

# ── Constantes de exibição (Visualização do código) ────────────────────────────
LINHA_DUPLA  = "=" * 72
LINHA_SIMPLES = "-" * 72
LINHA_TRACEJADA = "·" * 72

# ── Mapa de emojis por nível (fallback seguro para terminais sem unicode) ────────
ICONE_NIVEL = {
    "CRITICO":  "[!!!]",
    "ALERTA":   "[!! ]",
    "ATENCAO":  "[ ! ]",
    "NORMAL":   "[ OK]",
    "INVALIDO": "[ERR]"
}

# ── Descrições de risco ───────────────────────────────────────────────────────────
DESCRICAO_RISCO = {
    "CRITICO": "Situação de incêndios críticas. Acione a equipe de campo imediatamente!",
    "ALERTA": "Incêndios eminentes. Redobre a atenção e mantenha a equiipe de campo em prontidão.",
    "ATENCAO": "Atenção redobrada. Mantenha a vigilância.",
    "NORMAL": "Região sob controle. Continue monitorando.",
    "INVALIDO": "Dados inválidos. Verifique as informações."
}

# ===========================================================================
# ler_float(mensagem) - Verificação de inputs para o tipo primitivo FLOAT.
#
#  Trata entradas inválidas (como letras, símbolos ou strings vazias)
#  garantindo que a função retorne sempre um valor numérico válido.
#
#  Argumentos:
#    mensagem: texto exibido ao usuário solicitando o valor
#
#  Retorna:
#    float: número decimal válido informado pelo usuário
# =============================================================================
def ler_float(mensagem):
    while True:
        valor = input(mensagem)

        valor_teste = valor.replace(".", "", 1).replace("-", "", 1)

        if valor_teste.isdigit():
            return float(valor)

        print("Valor inválido. Digite um número decimal.")

# =============================================================================
# ler_int(mensagem) - Verificação de inputs para o tipo primitivo INT.
#
#  Trata entradas inválidas (como letras, símbolos ou strings vazias)
#  garantindo que a função retorne sempre um número inteiro válido.
#
#  Argumentos:
#    mensagem: texto exibido ao usuário solicitando o valor
#
#  Retorna:
#    int: número inteiro válido informado pelo usuário
# =============================================================================
def ler_int(mensagem):
    while True:
        valor = input(mensagem)

        valor_teste = valor.replace("-", "", 1)

        if valor_teste.isdigit():
            return int(valor)

        print("Valor inválido. Digite um número inteiro.")

# =============================================================================
# ler_texto(mensagem) - Verificação de inputs para o tipo primitivo STRING.
#
#  Trata entradas inválidas (como strings vazias) garantindo que a função
#  retorne sempre uma string válida.
#
#  Argumentos:
#    mensagem: texto exibido ao usuário solicitando o valor
#
#  Retorna:
#    str: string válida informada pelo usuário
# =============================================================================
def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto:
            return texto

        print("Texto inválido. Digite novamente.")

# =============================================================================
# ler_data() - Verificação de inputs para o tipo primitivo STRING.
#
#  Trata entradas inválidas (como strings vazias) garantindo que a função
#  retorne sempre uma string válida.
#
#  Argumentos:
#    N/A
#
#  Retorna:
#    str: string válida informada pelo usuário
# =============================================================================
def ler_data():
    while True:
        data = input(
            "Digite a data completa (DD/MM/AAAA HH:MM) e pressione ENTER: "
        )

        if len(data) != 16:
            print("Formato inválido.")
            continue

        if "/" not in data or ":" not in data:
            print("Formato inválido.")
            continue

        return data

# =============================================================================
# coleta_simulada() - Coleta de dados simulados.
#
#  Solicita ao usuário informações sobre uma região e retorna um dicionário
#  com os dados coletados.
#
#  Argumentos:
#    N/A, executado dentro do main() com base em sua escolha
#
#  Retorna:
#    dict: dicionário com os dados coletados
# =============================================================================
def coleta_simulada():
    while True:
        regiao = ler_texto("Digite a região que você vai simular e pressione ENTER: ")
        lat = ler_float("Digite a Latitude desejada e pressione ENTER: ")

        if lat < -90 or lat > 90:
            print("Latitude inválida. Digite novamente.")
            continue
        
        lon = ler_float("Digite a Longitude desejada e pressione ENTER: ")

        if lon < -180 or lon > 180:
            print("Longitude inválida. Digite novamente.")
            continue
        
        area = ler_int("Digite a área em km² desejada e pressione ENTER: ")

        if area <= 0:
            print("Área inválida. Digite novamente.")
            continue
        
        ndvi = ler_float("Digite o NDVI (Índice de Vegetação por Diferença Normalizada) desejado e pressione ENTER (deve ser decimal!): ")

        if ndvi < 0 or ndvi > 1:
            print("NDVI inválido. Digite novamente.")
            continue

        focos_input = ler_int("Digite um número inteiro para o foco de calor e pressione ENTER: ")

        if focos_input < 0:
            print("Focos de calor inválidos. Digite novamente.")
            continue

        umidade = ler_int("Digite o percentual (sem porcentagem) da umidade do solo e pressione ENTER: ")

        if umidade < 0 or umidade > 100:
            print("Umidade do solo inválida. Digite novamente.")
            continue

        historico = [int(x) for x in ler_texto("Digite o histórico de focos dos últimos 7 dias separados por espaço: ").split()]

        if len(historico) != 7:
            print("Histórico de focos inválido. Digite novamente.")
            continue

        datainput = ler_data()
        data, hora = datainput.split(" ")
        dia, mes, ano = data.split("/")
        timestamp = f"{ano}-{mes}-{dia}T{hora}"

        return regiao, lat, lon, area, ndvi, focos_input, umidade, historico, datainput, timestamp

# =============================================================================
# classificar_risco(dados) - Classifica o nível de risco da região.
#
#  Recebe um dicionário com os dados da região e retorna o nível de risco.
#
#  Argumentos:
#    dados: dicionário com os dados da região
#
#  Retorna:
#    str: nível de risco (CRITICO, ALERTA, ATENCAO, NORMAL, INVALIDO)
# =============================================================================
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

    if focos_input >= 10 or (umidade <= 20 and ndvi <= 0.3):
        return "CRITICO"

    if focos_input >= 5 or (umidade <= 35 and ndvi <= 0.3):
        return "ALERTA"

    if focos_input >= 1 or ndvi <= 0.5:
        return "ATENCAO"

    return "NORMAL"

# =============================================================================
# gerar_alerta(dados, nivel_risco) - Gera um alerta com base no nível de risco.
#
#  Recebe um dicionário com os dados da região e o nível de risco, e retorna
#  um dicionário com os dados formatados para exibição.
#
#  Argumentos:
#    dados: dicionário com os dados da região
#    nivel_risco: nível de risco (CRITICO, ALERTA, ATENCAO, NORMAL, INVALIDO)
#
#  Retorna:
#    dict: dicionário com os dados formatados para exibição
# =============================================================================
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

# =============================================================================
# processar_dados() - Processa os dados das regiões.
#
#  Recebe um dicionário com os dados da região importados do arquivo 
#  dados.py e retorna o nível de risco para cada uma.
#
#  Retorna:
#    dict: dicionário com os dados da região e o nível de risco
# =============================================================================
def processar_dados():
    for regiao in REGIOES:
        risco = classificar_risco(regiao)
        gerar_alerta(regiao, risco)

# =============================================================================
# main() - Função principal do programa.
#
#  Exibe o menu de interações e permite que o usuário escolha uma opção.
#
#  Argumentos:
#    N/A
#
#  Retorna:
#    N/A
# =============================================================================
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