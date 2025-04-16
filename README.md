# 💻 Desafio de Código - Sistema Bancário em Python | Bootcamp DIO

Durante o Bootcamp de Python da [DIO](https://www.dio.me/), fui desafiado a desenvolver um sistema bancário simples utilizando a linguagem Python. O projeto foi proposto com o objetivo de simular a implementação de funcionalidades básicas de um sistema financeiro, atendendo à demanda de um grande banco fictício que está em processo de modernização de suas operações.

---

## 🚀 Descrição do Desafio

**Cenário:**  
Fomos contratados por um grande banco que deseja modernizar seu sistema interno. A linguagem escolhida para essa modernização foi o **Python**, e o projeto foi dividido em **três versões principais**, cada uma com novos requisitos e evoluções técnicas.

---

## 📂 Estrutura do Repositório

O repositório contém três versões distintas do projeto:

1. `v1/` - Versão inicial procedural básica
2. `v2/` - Versão modular com funções
3. `v3/` - Versão com Programação Orientada a Objetos

Cada versão está contida em seu próprio arquivo correspondente, permitindo comparar a evolução da implementação.

---

# 🧩 Versão 1 — Sistema Bancário Básico

Na **primeira versão do projeto**, a proposta era implementar um sistema que simulasse uma única conta bancária, permitindo as operações básicas de depósito, saque e extrato, com regras de negócio simples.

---

## 🧾 Funcionalidades Implementadas — V1

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

## 🧠 Aprendizados — V1

Esta primeira etapa do projeto foi essencial para aplicar na prática os conceitos de:
- Estrutura de repetição e controle de fluxo
- Manipulação de strings e variáveis
- Lógica condicional e estrutura sequencial
- Implementação de regras de negócio simples
- Formatação de saída no terminal com mensagens informativas

---

# 🔁 Versão 2 — Sistema Modular com Usuários e Contas

A **segunda versão do sistema** foi uma continuação direta da V1, com um novo conjunto de requisitos que exigiu **modularização do código** e a criação de **múltiplos usuários e contas bancárias**. Além disso, as funções foram reestruturadas para seguir boas práticas de organização e reutilização.

---

## 🧾 Funcionalidades Implementadas — V2

### 🟢 Depósito (Função `depositar`)
- Agora encapsulado em uma função que recebe argumentos apenas **posicionais**.
- Mantém a lógica de aceitar apenas valores positivos.
- Atualiza o saldo e registra a movimentação no extrato.

### 🔴 Saque (Função `sacar`)
- Reescrita como função com argumentos **apenas nomeados**, promovendo clareza no uso.
- Continua com limite de **3 saques diários** e **R$ 500 por saque**.
- Verificações de saldo, limite de valor e limite de saques diários.
- Atualiza o saldo e registra a movimentação no extrato.

### 📄 Extrato (Função `exibir_extrato`)
- Refatorada com argumentos posicionais e nomeados combinados.
- Apresenta o histórico de movimentações e o saldo atual, com mensagens claras para o usuário.

### 👤 Cadastro de Usuário (Função `criar_usuario`)
- Recebe os dados do novo cliente: nome completo, CPF, data de nascimento e endereço.
- Verifica se já existe um usuário com o CPF informado antes de criar um novo registro.
- Armazena os dados em uma lista de dicionários.

### 🏦 Criação de Conta (Função `criar_conta`)
- Gera uma nova conta com número sequencial e agência fixa (`0001`).
- Exige CPF de um usuário previamente cadastrado para vincular a conta.
- Armazena as contas em uma lista, cada uma associada ao usuário correspondente.

### 📋 Listagem de Contas (Função `listar_contas`)
- Exibe todas as contas criadas com suas respectivas informações:
  - Número da conta
  - Agência
  - Nome do titular

---

## 🧠 Aprendizados — V2

A segunda fase do projeto permitiu um avanço significativo em termos de organização de código e domínio de conceitos mais avançados, como:

- Criação e uso de **funções reutilizáveis**
- Diferenciação entre **argumentos posicionais e nomeados**
- Armazenamento e manipulação de dados com **listas e dicionários**
- Aplicação de **validação de dados** (como CPF único)
- Separação de responsabilidades e estruturação lógica do sistema
- Utilização do módulo `textwrap` para formatar a exibição no terminal

---

# 🏛️ Versão 3 — Sistema Bancário com POO (Programação Orientada a Objetos)

A **terceira versão do sistema** representou uma evolução arquitetural significativa, migrando da abordagem procedural para a **Programação Orientada a Objetos (POO)**. Esta versão introduziu classes e conceitos avançados de POO para melhor organização e escalabilidade do código.

---

## 🧾 Funcionalidades Implementadas — V3

### 👥 Modelagem de Classes
- **Cliente**: Classe base para representar usuários do sistema
- **PessoaFisica**: Subclasse de Cliente com dados específicos (CPF, nome, data de nascimento)
- **Conta**: Classe abstrata representando uma conta bancária
- **ContaCorrente**: Implementação concreta de conta com limites de saque
- **Historico**: Classe para gerenciar o registro de transações
- **Transacao**: Classe abstrata base para operações bancárias
- **Deposito/Saque**: Classes concretas que implementam transações específicas

### 🔄 Princípios de POO Aplicados
- **Abstração**: Uso de classes abstratas (ABC) para Transacao e Conta
- **Encapsulamento**: Atributos protegidos com propriedades (@property)
- **Herança**: Relação entre Cliente → PessoaFisica e Conta → ContaCorrente
- **Polimorfismo**: Métodos registrar() com implementações específicas em Deposito/Saque

### 🆕 Novas Funcionalidades
- Sistema de histórico de transações mais robusto com datas e tipos
- Separação clara de responsabilidades entre classes
- Melhor tratamento de erros e mensagens ao usuário
- Padronização de operações através da classe Transacao

### 🛠️ Melhorias Técnicas
- Uso de datetime para registro preciso de transações
- Métodos de classe (@classmethod) para criação de contas
- Formatação melhorada de saídas usando textwrap
- Implementação do padrão Strategy para transações

---

## 🧠 Aprendizados — V3

A terceira fase do projeto representou um salto qualitativo na arquitetura do sistema, introduzindo:

- Princípios fundamentais de **Programação Orientada a Objetos**
- Uso de **classes abstratas** e **métodos abstratos**
- Aplicação dos **quatro pilares da POO**: Abstração, Encapsulamento, Herança e Polimorfismo
- Padrões de projeto como **Strategy** para transações
- Melhor organização e **baixo acoplamento** entre componentes
- **Manutenibilidade** e escalabilidade do código
- Uso de **properties** para acesso controlado a atributos
- Implementação de **métodos de classe** para factories

---

## 🏁 Conclusão

Esse desafio prático foi uma excelente oportunidade de consolidar fundamentos da programação em Python ao mesmo tempo em que simulava um cenário realista do mundo corporativo. A evolução desde a **versão 1** (procedural básica) até a **versão 3** (POO avançada) demonstra claramente:

1. A importância de escrever códigos limpos e organizados
2. Os benefícios da modularização e separação de conceitos
3. A vantagem de usar paradigmas adequados para cada estágio de complexidade
4. A evolução natural de um sistema que começa simples mas precisa escalar

Cada versão representou um marco de aprendizado, desde estruturas básicas até conceitos avançados de POO, preparando para desafios mais complexos de desenvolvimento de software.

---
