# =============================================================================
#  ORBIS SENTINEL — Módulo de Dados Simulados
#  Disciplina: Computational Thinking With Python (CTWP)
#  Global Solution 2026 · FIAP · Engenharia de Software · 1º Ano
# =============================================================================
#
#  Este módulo centraliza os dados simulados que representam leituras dos
#  satélites NASA FIRMS (focos de calor), NDVI (vegetação) e umidade do solo
#  fornecida pelo INPE/Copernicus para regiões monitoradas pelo Orbis Sentinel.
#
#  Formato baseado no exemplo do enunciado CTWP:
#  {"regiao": str, "ndvi_index": float, "focos_calor": int,
#   "umidade_solo_percent": float}
#
#  Cada registro também inclui:
#   - lat / lon        : coordenadas centrais da região
#   - area_km2         : tamanho da região monitorada
#   - historico_focos  : lista com contagem dos últimos 7 dias
#   - timestamp        : data/hora da leitura orbital
# =============================================================================

REGIOES = [
    # ── Região 1 — CRÍTICO ────────────────────────────────────────────────────
    {
        "regiao": "Amazonia_AM_Setor_Norte",
        "lat": -3.1,
        "lon": -60.0,
        "area_km2": 4500,
        "ndvi_index": 0.21,
        "focos_calor": 18,
        "umidade_solo_percent": 11.0,
        "historico_focos": [2, 4, 6, 9, 12, 15, 18],
        "timestamp": "2026-06-01T08:00"
    },
    # ── Região 2 — CRÍTICO ────────────────────────────────────────────────────
    {
        "regiao": "Cerrado_MT_Setor_Leste",
        "lat": -13.5,
        "lon": -52.3,
        "area_km2": 3200,
        "ndvi_index": 0.18,
        "focos_calor": 23,
        "umidade_solo_percent": 8.5,
        "historico_focos": [5, 8, 11, 14, 18, 20, 23],
        "timestamp": "2026-06-01T08:00"
    },
    # ── Região 3 — ALERTA ─────────────────────────────────────────────────────
    {
        "regiao": "Pantanal_MS_Setor_Oeste",
        "lat": -18.0,
        "lon": -57.5,
        "area_km2": 6100,
        "ndvi_index": 0.35,
        "focos_calor": 7,
        "umidade_solo_percent": 29.0,
        "historico_focos": [0, 1, 2, 3, 5, 6, 7],
        "timestamp": "2026-06-01T08:00"
    },
    # ── Região 4 — ALERTA ─────────────────────────────────────────────────────
    {
        "regiao": "Caatinga_BA_Setor_Central",
        "lat": -10.8,
        "lon": -40.2,
        "area_km2": 2800,
        "ndvi_index": 0.29,
        "focos_calor": 9,
        "umidade_solo_percent": 22.0,
        "historico_focos": [1, 2, 3, 5, 7, 8, 9],
        "timestamp": "2026-06-01T08:00"
    },
    # ── Região 5 — ATENCAO ────────────────────────────────────────────────────
    {
        "regiao": "Cerrado_GO_Setor_Sul",
        "lat": -16.4,
        "lon": -49.2,
        "area_km2": 1900,
        "ndvi_index": 0.44,
        "focos_calor": 3,
        "umidade_solo_percent": 38.0,
        "historico_focos": [0, 0, 1, 1, 2, 2, 3],
        "timestamp": "2026-06-01T08:00"
    },
    # ── Região 6 — ATENCAO ────────────────────────────────────────────────────
    {
        "regiao": "MataAtlantica_SP_Setor_Vale",
        "lat": -22.9,
        "lon": -45.8,
        "area_km2": 1400,
        "ndvi_index": 0.49,
        "focos_calor": 2,
        "umidade_solo_percent": 43.0,
        "historico_focos": [0, 0, 0, 1, 1, 2, 2],
        "timestamp": "2026-06-01T08:00"
    },
    # ── Região 7 — NORMAL ─────────────────────────────────────────────────────
    {
        "regiao": "Pampa_RS_Setor_Sul",
        "lat": -31.7,
        "lon": -52.0,
        "area_km2": 2100,
        "ndvi_index": 0.72,
        "focos_calor": 0,
        "umidade_solo_percent": 61.0,
        "historico_focos": [0, 0, 0, 0, 0, 0, 0],
        "timestamp": "2026-06-01T08:00"
    },
    # ── Região 8 — NORMAL ─────────────────────────────────────────────────────
    {
        "regiao": "Amazonia_PA_Setor_Leste",
        "lat": -4.5,
        "lon": -49.0,
        "area_km2": 5800,
        "ndvi_index": 0.81,
        "focos_calor": 0,
        "umidade_solo_percent": 74.0,
        "historico_focos": [0, 0, 0, 0, 0, 0, 0],
        "timestamp": "2026-06-01T08:00"
    },
    # ── Região 9 — registro com DADOS INVÁLIDOS (teste de robustez) ───────────
    # {
    #     "regiao": "Sensor_Falha_RO_Setor_Norte",
    #     "lat": None,
    #     "lon": None,
    #     "area_km2": None,
    #     "ndvi_index": None,
    #     "focos_calor": None,
    #     "umidade_solo_percent": None,
    #     "historico_focos": [],
    #     "timestamp": "2026-06-01T08:00"
    # },
    # ── Região 10 — CRÍTICO ───────────────────────────────────────────────────
    {
        "regiao": "Cerrado_TO_Setor_Norte",
        "lat": -8.9,
        "lon": -48.1,
        "area_km2": 3700,
        "ndvi_index": 0.16,
        "focos_calor": 31,
        "umidade_solo_percent": 7.0,
        "historico_focos": [8, 12, 16, 20, 24, 28, 31],
        "timestamp": "2026-06-01T08:00"
    },
]

# Limiares das regras de negócio (espelham RN01 do Backlog do Produto)
LIMIARES = {
    "critico": {
        "focos_calor_min": 10,
        "umidade_max": 20.0,
        "ndvi_max": 0.30
    },
    "alerta": {
        "focos_calor_min": 5,
        "umidade_max": 35.0
    },
    "atencao": {
        "focos_calor_min": 1,
        "ndvi_max": 0.50
    }
}
