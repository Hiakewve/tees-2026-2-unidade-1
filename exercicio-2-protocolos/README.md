# Exercício 2: APIs e Protocolos - Rede Social

Este projeto explora a exposição de um mesmo domínio de **Rede Social** através de dois protocolos de comunicação distintos: **REST (JSON)** e **GraphQL (JSON)**.

---

## 📁 Estrutura da Entrega

* [`banco.py`](./banco.py): Camada de dados em memória e regras de negócio compartilhadas entre ambos os projetos.
* [`rest-json/`](./rest-json/): Implementação da API no padrão REST (JSON) com FastAPI.
* [`graphql/`](./graphql/): Implementação da API GraphQL (JSON) com Strawberry e FastAPI.

---

## ⚖️ Comparação Final dos Protocolos

> **O que o REST (JSON) faz melhor que o GraphQL neste domínio:**  
> O REST destaca-se pela simplicidade de implementação, facilidade de caching HTTP nativo por URL de recurso e padronização direta dos métodos HTTP para comandos e consultas simples.

> **O que o GraphQL faz melhor que o REST neste domínio:**  
> O GraphQL destaca-se por permitir consultas declarativas em um único endpoint, onde o cliente especifica exatamente os campos que deseja receber, evitando o excesso (*over-fetching*) ou escassez (*under-fetching*) de dados ao montar recursos complexos como feeds e perfis.

---

## 🚀 Como Executar os Projetos

As instruções completas e os exemplos copiáveis de requisições e respostas para todas as 10 operações estão disponíveis nos READMEs específicos de cada subpasta:

1. [Instruções do Projeto REST (JSON)](./rest-json/readme.md)
2. [Instruções do Projeto GraphQL (JSON)](./graphql/README.md)
