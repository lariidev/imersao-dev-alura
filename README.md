# 🧮 Calculadora Simples em Python

Uma calculadora simples desenvolvida em **Python**, capaz de realizar operações matemáticas básicas como adição, subtração, multiplicação, divisão e porcentagem.

O projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais da programação em Python, como funções, estruturas condicionais, entrada de dados e tratamento de situações específicas.

## 🚀 Funcionalidades

A calculadora permite realizar as seguintes operações:

- ➕ **Adição:** soma de dois números.
- ➖ **Subtração:** diferença entre dois números.
- ✖️ **Multiplicação:** produto de dois números.
- ➗ **Divisão:** divisão entre dois números, com verificação de divisão por zero.
- ％ **Porcentagem:** cálculo de porcentagem (ex: calcular y% de x).

Além disso, o programa conta com:

- Menu interativo no terminal.
- Validação da operação selecionada.
- Suporte a números inteiros e decimais.
- Exibição organizada dos resultados.
- Código estruturado em funções para facilitar a leitura e manutenção.

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **Git e GitHub** para versionamento e armazenamento do projeto.

## 📂 Estrutura do projeto

```text
imersao-dev-alura/
│
├── calculadora.py
└── README.md
```

## 💻 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/lariidev/imersao-dev-alura.git
```

### 2. Acesse a pasta do projeto

```bash
cd imersao-dev-alura
```

### 3. Execute o programa

Certifique-se de ter o Python 3 instalado.

```bash
python calculadora.py
```

Em alguns sistemas, pode ser necessário utilizar:

```bash
python3 calculadora.py
```

## 📌 Exemplo de utilização

Ao executar o programa, o seguinte menu será exibido:

```text
===================================
      CALCULADORA EM PYTHON        
===================================
1. Adição (+)
2. Subtração (-)
3. Multiplicação (*)
4. Divisão (/)
5. Porcentagem (%)
===================================

Escolha a operação desejada (1/2/3/4/5): 5
Digite o primeiro número (ou valor base): 200
Digite o segundo número (ou porcentagem %): 15

Resultado: 15.0% de 200.0 = 30.0
```

## 🧠 Conceitos aplicados

Durante o desenvolvimento deste projeto, foram utilizados os seguintes conceitos:

**1. Funções**
Cada operação matemática possui uma função específica, tornando o código mais organizado e reutilizável.

**2. Estruturas condicionais**
Utilização de `if`, `elif` e validação da opção escolhida pelo usuário.

**3. Entrada de dados**
Utilização da função `input()` para receber informações digitadas pelo usuário.

**4. Conversão de tipos**
Utilização de `float()` para permitir cálculos com números decimais.

**5. Validação de dados**
Verificação da opção selecionada e prevenção de divisões por zero.

## 🔮 Possíveis melhorias

Como forma de continuar evoluindo o projeto, algumas funcionalidades poderão ser implementadas futuramente:

- [ ] Permitir realizar várias operações sem reiniciar o programa (loop contínuo).
- [ ] Adicionar tratamento para entradas não numéricas (`try/except`).
- [ ] Implementar operações de potência e raiz quadrada.
- [ ] Criar um histórico de cálculos.
- [ ] Desenvolver uma interface gráfica para a calculadora.

## 🎯 Objetivo do projeto

Este projeto foi criado para colocar em prática conhecimentos iniciais de **lógica de programação e desenvolvimento em Python** durante a **Imersão Dev Alura**.

A proposta é desenvolver um programa simples, funcional e organizado, aplicando boas práticas de programação e construindo uma base sólida para projetos mais complexos.

## 📄 Licença

Este projeto foi desenvolvido para fins de estudo e aprendizado.
