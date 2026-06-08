# Orbis Sentinel - Sistema de Monitoramento de Incêndios

## Global Solution 2026 · FIAP · Engenharia de Software · 1º Ano

Este é um sistema de **alerta de incêndios** que recebe informações digitadas pelo usuário, como latitude, longitude, área monitorada, NDVI, focos de calor, umidade do solo, histórico de focos e data, ele então processa esses dados com base em **limiares** para então, classificar o nível de risco da região e gerar alertas com base no nível de risco.

O sistema também possui funções que permitem a **coleta de dados de regiões pré-definidas**, a **geração de relatórios** e a **exibição de alertas** com base no nível de risco. Além disso, o sistema possui um **sistema de validação de inputs** para garantir que o usuário insira apenas dados válidos.

O projeto foi desenvolvido ao longo do primeiro semestre da graduação em Engenharia de Software, como parte da disciplina de **Computational Thinking With Python**, e é um trabalho que busca aplicar os conhecimentos adquiridos em sala de aula no desenvolvimento de um sistema real, com:

### Contexto da problemática

No atual cenário de mudanças climáticas e aumento das emissões de gases de efeito estufa, o Brasil tem enfrentado **desafios crescentes relacionados aos incêndios florestais**. As queimadas, agravadas por fatores como **desmatamento**, **secas prolongadas** e **práticas agrícolas inadequadas**, representam uma ameaça significativa não apenas ao **meio ambiente**, mas também à **saúde pública**, à **economia** e à **segurança da população**. A dificuldade em monitorar e combater esses incêndios de forma ágil e eficiente tem gerado **impactos devastadores**, com perdas inestimáveis para a **biodiversidade**, para as **comunidades locais** e para o país como um todo.

Nesse viés, o desenvolvimento de **ferramentas tecnológicas** que auxiliem no monitoramento e combate aos incêndios se torna fundamental. O sistema "Orbis Sentinel" surge como uma **solução inovadora**, capaz de receber dados de diversas regiões, processá-los e gerar alertas com base no nível de risco. Essa abordagem permite uma **resposta mais rápida e eficiente** por parte das equipes de campo, contribuindo para a mitigação dos impactos causados pelas queimadas.

A utilização de Python para o desenvolvimento do Orbis Sentinel justifica-se pela sua **versatilidade**, permitindo a **integração com diversas fontes de dados** e a **implementação de algoritmos complexos** de forma eficiente, como os que envolvem o **processamento de dados georreferenciados** e a **geração de relatórios detalhados**.

### Variáveis
- **regiao (String)**: <ins>região</ins> - Utilizado para identificar a região que será simulada
- **lat (Float)**: <ins>latitude</ins> - Utilizado para identificar a posição da região
- **lon (Float)**: <ins>longitude</ins> - Utilizado para identificar a posição da região
- **area (Int)**: <ins>área monitorada</ins> - Utilizado para identificar a área monitorada
- **ndvi (Float)**: <ins>Índice de Vegetação por Diferença Normalizada</ins> - Utilizado para identificar a saúde da vegetação. O índice varia de -1 a 1, onde valores negativos indicam baixa saúde da vegetação e valores positivos indicam alta saúde da vegetação.
- **focos (Int)**: <ins>focos de calor</ins> - Utilizado para identificar focos de calor
- **umidade (Int)**: <ins>umidade do solo</ins> - Utilizado para identificar a umidade do solo
- **historico (List[Int])**: <ins>histórico de focos</ins> - Utilizado para identificar o histórico de focos
- **data (String)**: <ins>data</ins> - Utilizado para identificar a data e hora da coleta
- **timestamp (String)**: <ins>timestamp</ins> - Utilizado para identificar o momento da coleta. Esta variável é gerada automaticamente pelo programa e se encontra de acordo com o padrão ISO 8601.

### Funções
- **ler_float(mensagem)**: Função responsável por solicitar ao usuário um valor float e validar se o valor informado é realmente um float.
- **ler_int(mensagem)**: Função responsável por solicitar ao usuário um valor int e validar se o valor informado é realmente um int.
- **ler_texto(mensagem)**: Função responsável por solicitar ao usuário um valor string e validar se o valor informado é realmente uma string.
- **ler_data()**: Função responsável por solicitar ao usuário uma data e validar se o valor informado é realmente uma data.
- **coleta_simulada()**: Função responsável por solicitar ao usuário informações sobre uma região e retornar um dicionário com os dados coletados.
- **validar_dados()**: Função responsável por validar se os dados coletados são válidos e retornar um dicionário com os dados processados.
- **processar_dados()**: Função responsável por processar os dados coletados e retornar um dicionário com os dados processados.
- **gerar_alerta()**: Função responsável por gerar um alerta com base em variáveis pré-definidas e retornar um dicionário com os dados processados.
- **main()**: Função principal responsável por executar o programa.

### Listas
- **REGIOES (List[str])**: Lista contendo os nomes das regiões pré-definidas.

### Dicionários
- **ICONE_NIVEL (Dict[str, str])**: Dicionário contendo os ícones dos níveis de risco.
- **DESCRICAO_RISCO (Dict[str, str])**: Dicionário contendo as descrições dos níveis de risco.
- **REGIOES (Dict[str, List[str]])**: Dicionário contendo as regiões pré-definidas.
- **LIMIARES (Dict[str, Dict[str, float]])**: Dicionário contendo os limiares das regras de negócio.

### Condicionais
- **if/elif/else**: Utilizado para verificar se os valores informados pelo usuário são válidos e para gerar alertas com base no nível de risco.

### Laços de Repetição
- **while**: Utilizado para garantir que os valores informados pelo usuário sejam válidos e para gerar alertas com base no nível de risco.

## Funcionalidades
- **Coleta de dados**: Coleta de dados de diversas regiões.
- **Processamento de dados**: Processa os dados coletados e retorna um dicionário com os dados processados.
- **Geração de alertas**: Gera um alerta com base em variáveis pré-definidas.
- **Exibição de relatórios**: Exibe relatórios com os dados coletados e os alertas gerados.

## Autores
- [Marcos Vinícios Corrêa dos Santos](https://github.com/mrcscorrea)

## Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/mrcscorrea/python-global-solutions.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd python-global-solutions
   ```

3. Execute o programa:
   ```bash
   python main.py
   ```
