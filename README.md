# 💻 Desafio de Código - Sistema Bancário em Python | Bootcamp DIO

Durante o Bootcamp de Python da [DIO](https://www.dio.me/), fui desafiado a desenvolver um sistema bancário simples utilizando a linguagem Python. O projeto foi proposto com o objetivo de simular a implementação de funcionalidades básicas de um sistema financeiro, atendendo à demanda de um grande banco fictício que está em processo de modernização de suas operações.

---

## 🚀 Descrição do Desafio

**Cenário:**  
Fomos contratados por um grande banco que deseja modernizar seu sistema interno. A linguagem escolhida para essa modernização foi o **Python**, e para a primeira versão do sistema, precisamos implementar três funcionalidades principais: **depósito, saque e extrato**.

---

## 🧾 Funcionalidades Implementadas

### 🟢 Operação de Depósito
- Permite ao usuário realizar **depósitos de valores positivos**.
- O sistema considera apenas **um único usuário**, portanto, **não há necessidade de identificar agência ou número da conta**.
- Todos os depósitos são registrados e exibidos posteriormente na operação de extrato.

### 🔴 Operação de Saque
- O usuário pode realizar até **3 saques diários**.
- Cada saque possui o **limite máximo de R$ 500,00**.
- Caso o saldo da conta seja insuficiente, o sistema deve informar a impossibilidade do saque.
- Assim como os depósitos, todos os saques também são registrados e exibidos na operação de extrato.

### 📄 Operação de Extrato
- Exibe a **listagem completa de todos os depósitos e saques** realizados.
- Ao final, mostra o **saldo atual** da conta.
- Se **nenhuma movimentação** tiver sido feita, o sistema deve informar:  
  > *"Não foram realizadas movimentações."*
- Todos os valores são apresentados no seguinte formato:  
  `R$ xxx.xx`  
  Exemplo: `R$ 1500.45`

---

## 🧠 Aprendizados

Este desafio foi essencial para aplicar na prática os conceitos de:
- Estrutura de repetição e controle de fluxo
- Manipulação de strings e variáveis
- Lógica condicional
- Boas práticas de exibição de informações no terminal

---
