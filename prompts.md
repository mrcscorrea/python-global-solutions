# Orbis Sentinel - Sistema de Monitoramento de Incêndios
## Global Solution 2026 · FIAP · Engenharia de Software · 1º Ano
Aqui estão os prompts que usei para auxiliar no desenvolvimento do projeto Orbis Sentinel. Todo o sistema foi desenvolvido utilizando IA generativa como um
copiloto de desenvolvimento, utilizando em casos complexos onde eu não consegui encontrar a solução para o problema com facilidade.

### Prompt inicial para desenvolvimento do projeto Orbis Sentinel
Você é um professor de programação Python para iniciantes. Analise meu código, e principalmente minha função de coleta de dados em Python e identifique possíveis falhas de validação. O sistema recebe informações digitadas pelo usuário, como latitude, longitude, área monitorada, NDVI, focos de calor, umidade do solo, histórico de focos e data. Verifique situações em que o programa possa encerrar por erro de conversão ou entrada inválida. Sugira correções utilizando apenas conceitos básicos de Python, como if, elif, else, while, listas, dicionários e funções. Priorize soluções compatíveis com o nível de um estudante do primeiro período e explique claramente cada alteração proposta.

### Prompt para criação do dados.py para testes com dados reais
Crie um arquivo dados.py contendo uma lista de dicionários, onde cada dicionário representa uma região monitorada pelo Orbis Sentinel. Cada dicionário deve conter as seguintes informações: "regiao", "lat", "lon", "area_km2", "ndvi_index", "focos_calor", "umidade_solo_percent", "historico_focos" e "timestamp". Utilize informações reais ou simuladas de forma crível para representar as condições das regiões. Evite usar dados muito discrepantes com a realidade. Tenha em consideração que as regiões monitoradas são:
1. Amazonia_AM_Setor_Norte
2. Cerrado_MT_Setor_Leste
3. Pantanal_MS_Setor_Oeste
4. Caatinga_BA_Setor_Central
5. Cerrado_GO_Setor_Sul
6. MataAtlantica_SP_Setor_Vale
7. Pampa_RS_Setor_Sul
8. Amazonia_PA_Setor_Leste
9. Cerrado_TO_Setor_Norte

### Prompt para auxílio no problema de importação dos dados.py
Estou tendo problemas com a importação dos dados, veja bem, a principio, o sistema deveria receber informações digitadas pelo usuário, como latitude, longitude, área monitorada, NDVI, focos de calor, umidade do solo e histórico de focos e está recebendo, porém, está com problemas de leitura nas funções.

### Prompt para auxílio na validação de inputs (tratamento de erro)
Observe o código acima, quero que você me ajude adicionando sistemas de verificação nos inputs, para que o código não quebre se o usuário não seguir a lógica (exemplo, coloco uma letra onde é um float).

### Prompt para auxílio no README.md
Me ajuda a escrever o README.md para o projeto da discipliina de Python. O projeto "Orbis Sentinel" é um sistema de alerta de incêndios que recebe informações digitadas pelo usuário, como latitude, longitude, área monitorada, NDVI, focos de calor, umidade do solo, histórico de focos e data. O sistema processa esses dados com base em limiares para gerar alertas de risco. O projeto também possui funções que permitem a coleta de dados de regiões pré-definidas, geração de relatórios e exibição de alertas. O sistema foi desenvolvido ao longo do primeiro semestre da graduação em Engenharia de Software, como parte da disciplina de Computational Thinking With Python, e é um trabalho que busca aplicar os conhecimentos adquiridos em sala de aula no desenvolvimento de um sistema para combater queimadas.