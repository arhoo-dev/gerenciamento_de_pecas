\# Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento



Este projeto é um protótipo em Python que simula um sistema de \*\*controle de produção, qualidade e armazenamento\*\* de peças em uma linha de montagem industrial.



O sistema permite cadastrar peças, avaliar automaticamente se elas estão aprovadas ou reprovadas segundo critérios pré-definidos, armazenar as peças aprovadas em caixas com capacidade limitada e gerar relatórios consolidados.



\---



\## 1. Objetivo do Sistema 🎯



A proposta deste projeto é representar, de forma lógica, como a automação pode auxiliar no \*\*controle de qualidade\*\* e no \*\*armazenamento\*\* de peças em um ambiente industrial.



O sistema desenvolvido em Python é capaz de:



\- Receber os dados de cada peça produzida:

&#x20; - `id`

&#x20; - `peso` (em gramas)

&#x20; - `cor`

&#x20; - `comprimento` (em centímetros)

\- Avaliar automaticamente se a peça está \*\*aprovada\*\* ou \*\*reprovada\*\*, com base nos critérios:

&#x20; - Peso entre \*\*95g e 105g\*\*

&#x20; - Cor \*\*azul\*\* ou \*\*verde\*\*

&#x20; - Comprimento entre \*\*10cm e 20cm\*\*

\- Armazenar as \*\*peças aprovadas\*\* em \*\*caixas\*\* com capacidade de \*\*10 peças por caixa\*\*;

\- Fechar a caixa quando atingir a capacidade máxima e iniciar uma nova;

\- Gerar relatórios com:

&#x20; - Total de peças aprovadas

&#x20; - Total de peças reprovadas e o(s) motivo(s) da reprovação

&#x20; - Quantidade de caixas utilizadas



\---



\## 2. Funcionalidades do Menu 📋



O programa possui um \*\*menu interativo\*\*, exibido no terminal, com as seguintes opções:



1\. \*\*Cadastrar nova peça\*\*  

&#x20;  - Solicita os dados da peça (id, peso, cor, comprimento);  

&#x20;  - Avalia automaticamente se a peça está aprovada ou reprovada;  

&#x20;  - Se aprovada, envia para o controle de caixas.



2\. \*\*Listar peças aprovadas/reprovadas\*\*  

&#x20;  - Permite escolher entre:

&#x20;    - Listar apenas peças aprovadas

&#x20;    - Listar apenas peças reprovadas (incluindo os motivos)

&#x20;    - Listar todas as peças



3\. \*\*Remover peça cadastrada\*\*  

&#x20;  - Permite informar o \*\*ID da peça\*\* para removê-la:

&#x20;    - Remove a peça da lista geral;

&#x20;    - Se ela for aprovada, também é removida da caixa em que estiver (caixa atual ou alguma caixa fechada).



4\. \*\*Listar caixas fechadas\*\*  

&#x20;  - Exibe todas as caixas já fechadas;

&#x20;  - Para cada caixa, mostra:

&#x20;    - Número da caixa

&#x20;    - Quantidade de peças

&#x20;    - IDs das peças armazenadas.



5\. \*\*Gerar relatório final\*\*  

&#x20;  - Mostra:

&#x20;    - Total de peças cadastradas

&#x20;    - Total de peças aprovadas

&#x20;    - Total de peças reprovadas

&#x20;    - Motivo(s) da reprovação de cada peça reprovada

&#x20;    - Quantidade total de caixas utilizadas

&#x20;    - Quantas caixas estão fechadas e quantas peças há na caixa atual (aberta).



0\. \*\*Sair\*\*  

&#x20;  - Encerra a execução do programa.



\---



\## 3. Estrutura do Projeto 🧱



Sugestão de estrutura de arquivos:



```text

.

├── main.py         # Arquivo principal com o código do sistema

├── README.md       # Este arquivo

```



\---



\## 4. Como Executar o Programa ▶️



\### 4.1. Pré-requisitos



\- Python 3 instalado na máquina  

&#x20; - Para verificar, execute no terminal:



&#x20;   ```bash

&#x20;   python --version

&#x20;   ```

&#x20;   ou



&#x20;   ```bash

&#x20;   python3 --version

&#x20;   ```



\- Um terminal ou prompt de comando (PowerShell, CMD, terminal do VS Code, etc.).



\### 4.2. Passo a passo para execução



1\. \*\*Clone o repositório\*\* (ou baixe os arquivos)



&#x20;  Se o projeto estiver no GitHub, use:



&#x20;  ```bash

&#x20;  git clone <URL\_DO\_REPOSITORIO>

&#x20;  ```



&#x20;  Em seguida, entre na pasta do projeto:



&#x20;  ```bash

&#x20;  cd nome-da-pasta-do-projeto

&#x20;  ```



2\. \*\*Execute o programa\*\*



&#x20;  No terminal, dentro da pasta onde está o arquivo `sistema\_de\_gerenciamento\_de\_pecas.py`, execute:



&#x20;  ```bash

&#x20;  python sistema\_de\_gerenciamento\_de\_pecas.py

&#x20;  ```

&#x20;  ou, dependendo da configuração do seu sistema:



&#x20;  ```bash

&#x20;  python3 sistema\_de\_gerenciamento\_de\_pecas.py

&#x20;  ```



3\. \*\*Utilize o menu\*\*



&#x20;  O menu principal será exibido no terminal, permitindo escolher as opções digitando o número correspondente.



\---



\## 5. Exemplo de Execução 💻



A seguir, um exemplo simplificado de uso do sistema.



\### 5.1. Cadastro de peças



1\. Usuário escolhe a opção \*\*1 – Cadastrar nova peça\*\* e informa:



&#x20;  - ID: `P001`  

&#x20;  - Peso: `100`  

&#x20;  - Cor: `azul`  

&#x20;  - Comprimento: `15`



&#x20;  O sistema avalia:



&#x20;  - Peso na faixa (95 a 105)  

&#x20;  - Cor válida (azul/verde)  

&#x20;  - Comprimento na faixa (10 a 20)



&#x20;  Resultado:

&#x20;  - Peça `P001` é \*\*aprovada\*\* e armazenada na caixa atual.



2\. Usuário cadastra uma segunda peça:



&#x20;  - ID: `P002`  

&#x20;  - Peso: `90`  

&#x20;  - Cor: `vermelho`  

&#x20;  - Comprimento: `25`



&#x20;  O sistema avalia:



&#x20;  - Peso fora da faixa  

&#x20;  - Cor inválida  

&#x20;  - Comprimento fora da faixa



&#x20;  Resultado:

&#x20;  - Peça `P002` é \*\*reprovada\*\*, com os motivos informados.



\### 5.2. Listagem de peças



Ao escolher a opção \*\*2 – Listar peças aprovadas/reprovadas\*\*:



\- Se o usuário escolher \*\*“Listar apenas aprovadas”\*\*, verá algo como:



&#x20; - `ID: P001 | Peso: 100g | Cor: azul | Comprimento: 15cm`



\- Se escolher \*\*“Listar apenas reprovadas”\*\*, verá, por exemplo:



&#x20; - `ID: P002 | Peso: 90g | Cor: vermelho | Comprimento: 25cm`  

&#x20;   `Motivo da reprovação: peso fora da faixa (...); cor inválida (...); comprimento fora da faixa (...)`



\### 5.3. Fechamento de caixas



Quando a \*\*caixa atual atingir 10 peças aprovadas\*\*, o sistema:



\- Informa que a caixa atingiu a capacidade máxima;

\- “Fecha” essa caixa, movendo-a para a lista de `caixas\_fechadas`;

\- Inicia automaticamente uma nova caixa vazia.



\### 5.4. Relatório final



Ao escolher a opção \*\*5 – Gerar relatório final\*\*, o sistema apresenta, por exemplo:



\- Total de peças cadastradas: `12`  

\- Total de peças aprovadas: `10`  

\- Total de peças reprovadas: `2`  

\- Detalhes das peças reprovadas, com seus motivos  

\- Quantidade de caixas utilizadas: `2` (1 fechada + 1 em uso)  

\- Caixas fechadas: `1`  

\- Peças na caixa atual (aberta): `0` ou outro número, dependendo do uso.



\---



\## 6. Tecnologias e Conceitos Utilizados 🧠



\- \*\*Linguagem:\*\* Python 3  

\- \*\*Conceitos principais de Algoritmos e Lógica de Programação:\*\*

&#x20; - Estruturas de decisão: `if`, `elif`, `else`

&#x20; - Estruturas de repetição: `while`, `for`

&#x20; - Funções para modularização do código

&#x20; - Estruturas de dados:

&#x20;   - Dicionários para representar peças

&#x20;   - Listas para armazenar conjuntos de peças e caixas



\---



\## 7. Possíveis Evoluções 🚀



Este protótipo poderia ser expandido para um cenário real de indústria, integrando:



\- \*\*Sensores físicos\*\* para leitura automática de peso, cor e comprimento;  

\- \*\*Visão computacional e IA\*\* para detecção de defeitos visuais e análise avançada de qualidade;  

\- \*\*Integração com sistemas industriais (MES/ERP)\*\* para:

&#x20; - Registrar produção em tempo real;

&#x20; - Atualizar estoque de peças aprovadas;

&#x20; - Gerar dashboards e indicadores de desempenho.



\---



\## 8. Autor 👨‍💻



\- Nome: \_Adriel Ogawa Osório\_  

\- Disciplina: Algoritmos e Lógica de Programação  

\- Curso: \_Inteligência Artificial e Automação Digital\_  

\- Professor(a): \_André Noel\_  

\- Repositório GitHub: \_\[link para o repositório do projeto]\_
