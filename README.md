# Digital Automation Challenge: Parts Management, Quality Control and Storage

This project is a Python prototype that simulates a **production, quality control, and storage** system for parts in an industrial assembly line.

The system allows you to register parts, automatically evaluate whether they are approved or rejected according to predefined criteria, store approved parts in boxes with limited capacity, and generate consolidated reports.

---

## 1. System Objective 🎯

The goal of this project is to logically represent how automation can support **quality control** and **storage management** of parts in an industrial environment.

The Python system is capable of:

- Receiving data for each produced part:
  - `id`
  - `weight` (in grams)
  - `color`
  - `length` (in centimeters)
- Automatically evaluating whether the part is **approved** or **rejected**, based on the criteria:
  - Weight between **95g and 105g**
  - Color **blue** or **green**
  - Length between **10cm and 20cm**
- Storing **approved parts** in **boxes** with a capacity of **10 parts per box**
- Closing a box when it reaches its maximum capacity and starting a new one
- Generating reports with:
  - Total approved parts
  - Total rejected parts and their rejection reasons
  - Total number of boxes used

---

## 2. Menu Features 📋

The program provides an **interactive menu**, displayed in the terminal, with the following options:

1. **Register new part**  
   - Asks for the part data (id, weight, color, length)  
   - Automatically evaluates if the part is approved or rejected  
   - If approved, sends it to the box management logic

2. **List approved/rejected parts**  
   - Allows you to choose between:
     - List only approved parts
     - List only rejected parts (including reasons)
     - List all parts

3. **Remove registered part**  
   - Allows you to enter a **part ID** to remove it:
     - Removes the part from the main list
     - If it was approved, it is also removed from the box where it is stored (current box or a closed box)

4. **List closed boxes**  
   - Displays all closed boxes
   - For each box, shows:
     - Box number
     - Number of parts
     - IDs of the parts stored in it

5. **Generate final report**  
   - Shows:
     - Total registered parts
     - Total approved parts
     - Total rejected parts
     - Rejection reason(s) for each rejected part
     - Total number of boxes used
     - How many boxes are closed and how many parts are in the current (open) box

0. **Exit**  
   - Ends the program execution

---

## 3. Project Structure 🧱

Suggested file structure:

```text
.
├── main.py      # Main file with the system's source code
├── README.md    # This file
```

> Note: If you want, you can organize the code into multiple files (for example, separating functions into modules), but that is not required for this project.

---

## 4. How to Run the Program ▶️

### 4.1. Prerequisites

- Python 3 installed on your machine  
  - To check, run in the terminal:

    ```bash
    python --version
    ```
    or

    ```bash
    python3 --version
    ```

- A terminal or command prompt (PowerShell, CMD, VS Code integrated terminal, etc.)

### 4.2. Step-by-step execution

1. **Clone the repository** (or download the files)

   If the project is hosted on GitHub, run:

   ```bash
   git clone <REPOSITORY_URL>
   ```

   Then, go into the project folder:

   ```bash
   cd project-folder-name
   ```

2. **Run the program**

   In the terminal, from the folder where `main.py` is located, run:

   ```bash
   python main.py
   ```
   or, depending on your system configuration:

   ```bash
   python3 main.py
   ```

3. **Use the menu**

   The main menu will be displayed in the terminal, and you can select options by typing the corresponding number.

---

## 5. Example Execution 💻

Below is a simplified example of how the system can be used.

### 5.1. Registering parts

1. The user selects option **1 – Register new part** and enters:

   - ID: `P001`  
   - Weight: `100`  
   - Color: `blue`  
   - Length: `15`

   The system evaluates:

   - Weight within range (95 to 105)  
   - Valid color (blue/green)  
   - Length within range (10 to 20)

   Result:
   - Part `P001` is **approved** and stored in the current box.

2. The user registers a second part:

   - ID: `P002`  
   - Weight: `90`  
   - Color: `red`  
   - Length: `25`

   The system evaluates:

   - Weight out of range  
   - Invalid color  
   - Length out of range

   Result:
   - Part `P002` is **rejected**, with all rejection reasons displayed.

### 5.2. Listing parts

When selecting option **2 – List approved/rejected parts**:

- If the user chooses **“List only approved”**, they will see something like:

  - `ID: P001 | Weight: 100g | Color: blue | Length: 15cm`

- If the user chooses **“List only rejected”**, they will see, for example:

  - `ID: P002 | Weight: 90g | Color: red | Length: 25cm`  
    `Rejection reason: weight out of range (...); invalid color (...); length out of range (...)`

### 5.3. Box closing logic

When the **current box reaches 10 approved parts**, the system:

- Informs that the box has reached maximum capacity
- “Closes” this box by moving it to the `closed_boxes` list
- Automatically starts a new empty box

### 5.4. Final report

When selecting option **5 – Generate final report**, the system shows, for example:

- Total registered parts: `12`  
- Total approved parts: `10`  
- Total rejected parts: `2`  
- Details of the rejected parts with their reasons  
- Number of boxes used: `2` (1 closed + 1 currently in use)  
- Closed boxes: `1`  
- Parts in the current (open) box: `0` or another number, depending on usage

---

## 6. Technologies and Concepts Used 🧠

- **Language:** Python 3  
- **Core concepts of Algorithms and Programming Logic:**
  - Decision structures: `if`, `elif`, `else`
  - Loop structures: `while`, `for`
  - Functions for code modularization
  - Data structures:
    - Dictionaries to represent parts
    - Lists to store collections of parts and boxes

---

## 7. Possible Improvements and Extensions 🚀

This prototype could be expanded for a real industrial scenario by integrating:

- **Physical sensors** for automatic reading of weight, color, and length  
- **Computer vision and AI** for visual defect detection and advanced quality analysis  
- **Integration with industrial systems (MES/ERP)** to:
  - Record production in real time
  - Update inventory of approved parts
  - Generate dashboards and performance indicators

---

## 8. Author 👨‍💻

- Name: _Adriel Ogawa Osório_  
- Course: _AI and Digital Automation_  
- Subject: Algorithms and Programming Logic  
- Instructor: _André Noel_  
- GitHub Repository: _[Project repository](https://github.com/arhoo-dev/gerenciamento_de_pecas)_

# Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento

Este projeto é um protótipo em Python que simula um sistema de **controle de produção, qualidade e armazenamento** de peças em uma linha de montagem industrial.

O sistema permite cadastrar peças, avaliar automaticamente se elas estão aprovadas ou reprovadas segundo critérios pré-definidos, armazenar as peças aprovadas em caixas com capacidade limitada e gerar relatórios consolidados.

---

## 1. Objetivo do Sistema 🎯

A proposta deste projeto é representar, de forma lógica, como a automação pode auxiliar no **controle de qualidade** e no **armazenamento** de peças em um ambiente industrial.

O sistema desenvolvido em Python é capaz de:

- Receber os dados de cada peça produzida:
  - `id`
  - `peso` (em gramas)
  - `cor`
  - `comprimento` (em centímetros)
- Avaliar automaticamente se a peça está **aprovada** ou **reprovada**, com base nos critérios:
  - Peso entre **95g e 105g**
  - Cor **azul** ou **verde**
  - Comprimento entre **10cm e 20cm**
- Armazenar as **peças aprovadas** em **caixas** com capacidade de **10 peças por caixa**;
- Fechar a caixa quando atingir a capacidade máxima e iniciar uma nova;
- Gerar relatórios com:
  - Total de peças aprovadas
  - Total de peças reprovadas e o(s) motivo(s) da reprovação
  - Quantidade de caixas utilizadas

---

## 2. Funcionalidades do Menu 📋

O programa possui um **menu interativo**, exibido no terminal, com as seguintes opções:

1. **Cadastrar nova peça**  
   - Solicita os dados da peça (id, peso, cor, comprimento);  
   - Avalia automaticamente se a peça está aprovada ou reprovada;  
   - Se aprovada, envia para o controle de caixas.

2. **Listar peças aprovadas/reprovadas**  
   - Permite escolher entre:
     - Listar apenas peças aprovadas
     - Listar apenas peças reprovadas (incluindo os motivos)
     - Listar todas as peças

3. **Remover peça cadastrada**  
   - Permite informar o **ID da peça** para removê-la:
     - Remove a peça da lista geral;
     - Se ela for aprovada, também é removida da caixa em que estiver (caixa atual ou alguma caixa fechada).

4. **Listar caixas fechadas**  
   - Exibe todas as caixas já fechadas;
   - Para cada caixa, mostra:
     - Número da caixa
     - Quantidade de peças
     - IDs das peças armazenadas.

5. **Gerar relatório final**  
   - Mostra:
     - Total de peças cadastradas
     - Total de peças aprovadas
     - Total de peças reprovadas
     - Motivo(s) da reprovação de cada peça reprovada
     - Quantidade total de caixas utilizadas
     - Quantas caixas estão fechadas e quantas peças há na caixa atual (aberta).

0. **Sair**  
   - Encerra a execução do programa.

---

## 3. Estrutura do Projeto 🧱

Sugestão de estrutura de arquivos:

```text
.
├── main.py         # Arquivo principal com o código do sistema
├── README.md       # Este arquivo
```

> Obs.: Se preferir, você pode organizar o código em mais de um arquivo (por exemplo, separar funções em módulos), mas não é obrigatório para este trabalho.

---

## 4. Como Executar o Programa ▶️

### 4.1. Pré-requisitos

- Python 3 instalado na máquina  
  - Para verificar, execute no terminal:

    ```bash
    python --version
    ```
    ou

    ```bash
    python3 --version
    ```

- Um terminal ou prompt de comando (PowerShell, CMD, terminal do VS Code, etc.).

### 4.2. Passo a passo para execução

1. **Clone o repositório** (ou baixe os arquivos)

   Se o projeto estiver no GitHub, use:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

   Em seguida, entre na pasta do projeto:

   ```bash
   cd nome-da-pasta-do-projeto
   ```

2. **Execute o programa**

   No terminal, dentro da pasta onde está o arquivo `main.py`, execute:

   ```bash
   python main.py
   ```
   ou, dependendo da configuração do seu sistema:

   ```bash
   python3 main.py
   ```

3. **Utilize o menu**

   O menu principal será exibido no terminal, permitindo escolher as opções digitando o número correspondente.

---

## 5. Exemplo de Execução 💻

A seguir, um exemplo simplificado de uso do sistema.

### 5.1. Cadastro de peças

1. Usuário escolhe a opção **1 – Cadastrar nova peça** e informa:

   - ID: `P001`  
   - Peso: `100`  
   - Cor: `azul`  
   - Comprimento: `15`

   O sistema avalia:

   - Peso na faixa (95 a 105)  
   - Cor válida (azul/verde)  
   - Comprimento na faixa (10 a 20)

   Resultado:
   - Peça `P001` é **aprovada** e armazenada na caixa atual.

2. Usuário cadastra uma segunda peça:

   - ID: `P002`  
   - Peso: `90`  
   - Cor: `vermelho`  
   - Comprimento: `25`

   O sistema avalia:

   - Peso fora da faixa  
   - Cor inválida  
   - Comprimento fora da faixa

   Resultado:
   - Peça `P002` é **reprovada**, com os motivos informados.

### 5.2. Listagem de peças

Ao escolher a opção **2 – Listar peças aprovadas/reprovadas**:

- Se o usuário escolher **“Listar apenas aprovadas”**, verá algo como:

  - `ID: P001 | Peso: 100g | Cor: azul | Comprimento: 15cm`

- Se escolher **“Listar apenas reprovadas”**, verá, por exemplo:

  - `ID: P002 | Peso: 90g | Cor: vermelho | Comprimento: 25cm`  
    `Motivo da reprovação: peso fora da faixa (...); cor inválida (...); comprimento fora da faixa (...)`

### 5.3. Fechamento de caixas

Quando a **caixa atual atingir 10 peças aprovadas**, o sistema:

- Informa que a caixa atingiu a capacidade máxima;
- “Fecha” essa caixa, movendo-a para a lista de `caixas_fechadas`;
- Inicia automaticamente uma nova caixa vazia.

### 5.4. Relatório final

Ao escolher a opção **5 – Gerar relatório final**, o sistema apresenta, por exemplo:

- Total de peças cadastradas: `12`  
- Total de peças aprovadas: `10`  
- Total de peças reprovadas: `2`  
- Detalhes das peças reprovadas, com seus motivos  
- Quantidade de caixas utilizadas: `2` (1 fechada + 1 em uso)  
- Caixas fechadas: `1`  
- Peças na caixa atual (aberta): `0` ou outro número, dependendo do uso.

---

## 6. Tecnologias e Conceitos Utilizados 🧠

- **Linguagem:** Python 3  
- **Conceitos principais de Algoritmos e Lógica de Programação:**
  - Estruturas de decisão: `if`, `elif`, `else`
  - Estruturas de repetição: `while`, `for`
  - Funções para modularização do código
  - Estruturas de dados:
    - Dicionários para representar peças
    - Listas para armazenar conjuntos de peças e caixas

---

## 7. Possíveis Evoluções 🚀

Este protótipo poderia ser expandido para um cenário real de indústria, integrando:

- **Sensores físicos** para leitura automática de peso, cor e comprimento;  
- **Visão computacional e IA** para detecção de defeitos visuais e análise avançada de qualidade;  
- **Integração com sistemas industriais (MES/ERP)** para:
  - Registrar produção em tempo real;
  - Atualizar estoque de peças aprovadas;
  - Gerar dashboards e indicadores de desempenho.

---

## 8. Autor 👨‍💻

- Nome: _Adriel Ogawa Osório_  
- Disciplina: Algoritmos e Lógica de Programação  
- Curso: _IA e Automação Digital_  
- Professor(a): _André Noel_  
- Repositório GitHub: _[[link para o repositório do projeto]](https://github.com/arhoo-dev/gerenciamento_de_pecas)_
