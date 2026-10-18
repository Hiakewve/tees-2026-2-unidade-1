# API GraphQL (JSON) - Rede Social

Esta é a implementação completa da API para o domínio de **Rede Social** utilizando o protocolo **GraphQL**. O projeto foi construído utilizando **Python**, **FastAPI** e a biblioteca **Strawberry GraphQL**.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI**: Framework web base para expor a rota GraphQL.
- **Strawberry GraphQL**: Biblioteca fortemente tipada baseada em dataclasses para definição de schemas, Queries e Mutations.
- **Uvicorn**: Servidor ASGI para execução local.

---

## 🚀 Como Executar do Zero

### 1. Pré-requisitos
Certifique-se de ter o Python 3.10 ou superior instalado no seu ambiente.

### 2. Instalar as dependências
Navegue até a pasta `graphql` e instale os pacotes necessários:

```bash
cd graphql
pip install fastapi uvicorn "strawberry-graphql[fastapi]"`)*

### 3. Iniciar o servidor
Ainda na pasta `graphql`, inicie o servidor:

```bash
uvicorn main:app --reload
```

O servidor iniciará no endereço local: `http://127.0.0.1:8000`

### 4. Interagir via Interface Visual (GraphiQL)
Diferente do REST que possui múltiplos endpoints, o GraphQL roda sobre **um único endpoint HTTP POST**:

- **GraphiQL IDE**: `http://127.0.0.1:8000/graphql`

Acesse esta URL no navegador para abrir o ambiente interativo de testes, onde você pode executar todas as *Queries* e *Mutations* e navegar no schema de tipos.

---

## 📋 Mapeamento de Operações e Exemplos Copiáveis

Todas as requisições no GraphQL são enviadas para a URL `http://127.0.0.1:8000/graphql`. Abaixo estão os códigos prontos para copiar e colar na interface do GraphiQL, com o detalhamento dos argumentos necessários.

---

### 🟢 MUTATIONS (Comandos / Operações de Escrita)

#### 1. `criar_usuario(nome, email)`
Cria um novo usuário na rede social.

- **Argumentos Obrigatórios:**
  - `nome` (String): Nome do usuário
  - `email` (String): E-mail do usuário

**Exemplo 1 (Primeiro Usuário - ID 1):**
* **GraphQL Mutation:**
```graphql
mutation {
  criarUsuario(nome: "Hiakewve", email: "hiakewve@email.com") {
    id
    nome
    email
    perfil {
      bio
      fotoUrl
    }
  }
}
```
* **Resposta JSON:**
```json
{
  "data": {
    "criarUsuario": {
      "id": 1,
      "nome": "Hiakewve",
      "email": "hiakewve@email.com",
      "perfil": {
        "bio": "",
        "fotoUrl": ""
      }
    }
  }
}
```

**Exemplo 2 (Segundo Usuário - ID 2):**
* **GraphQL Mutation:**
```graphql
mutation {
  criarUsuario(nome: "Ericles", email: "ericles@email.com") {
    id
    nome
    email
    perfil {
      bio
      fotoUrl
    }
  }
}
```
* **Resposta JSON:**
```json
{
  "data": {
    "criarUsuario": {
      "id": 2,
      "nome": "Ericles",
      "email": "ericles@email.com",
      "perfil": {
        "bio": "",
        "fotoUrl": ""
      }
    }
  }
}
```

---

#### 2. `criar_post(usuario_id, texto)`
Publica um novo post associado ao autor.

- **Argumentos Obrigatórios:**
  - `usuarioId` (Int): ID do autor do post
  - `texto` (String): Conteúdo do post

* **GraphQL Mutation:**
```graphql
mutation {
  criarPost(usuarioId: 1, texto: "Meu primeiro post na rede social!") {
    id
    usuarioId
    texto
  }
}
```
* **Resposta JSON:**
```json
{
  "data": {
    "criarPost": {
      "id": 1,
      "usuarioId": 1,
      "texto": "Meu primeiro post na rede social!"
    }
  }
}
```

---

#### 3. `comentar(usuario_id, post_id, texto)`
Cria um comentário de um usuário em determinado post.

- **Argumentos Obrigatórios:**
  - `usuarioId` (Int): ID de quem comenta (`2` - Ericles)
  - `postId` (Int): ID do post recebendo o comentário (`1`)
  - `texto` (String): Conteúdo do comentário

* **GraphQL Mutation:**
```graphql
mutation {
  comentar(usuarioId: 2, postId: 1, texto: "Muito bom seu post, Hiakewve!") {
    id
    usuarioId
    postId
    texto
  }
}
```
* **Resposta JSON:**
```json
{
  "data": {
    "comentar": {
      "id": 1,
      "usuarioId": 2,
      "postId": 1,
      "texto": "Muito bom seu post, Hiakewve!"
    }
  }
}
```

---

#### 4. `curtir(usuario_id, post_id)`
Registra a curtida de um usuário em um post.

- **Argumentos Obrigatórios:**
  - `usuarioId` (Int): ID de quem curte (`2` - Ericles)
  - `postId` (Int): ID do post curtido (`1`)

* **GraphQL Mutation:**
```graphql
mutation {
  curtir(usuarioId: 2, postId: 1)
}
```
* **Resposta JSON:**
```json
{
  "data": {
    "curtir": true
  }
}
```

---

#### 5. `seguir(usuario_id, alvo_id)`
Faz um usuário seguir outro.

- **Argumentos Obrigatórios:**
  - `usuarioId` (Int): ID do seguidor (`1` - Hiakewve)
  - `alvoId` (Int): ID de quem será seguido (`2` - Ericles)

* **GraphQL Mutation:**
```graphql
mutation {
  seguir(usuarioId: 1, alvoId: 2)
}
```
* **Resposta JSON:**
```json
{
  "data": {
    "seguir": true
  }
}
```

---

### 🔵 QUERIES (Consultas / Operações de Leitura Declarativas)

#### 6. `buscar_usuario(id)`
Consulta os dados de um usuário escolhendo declarativamente os campos desejados.

- **Argumentos Obrigatórios:**
  - `id` (Int): ID do usuário pesquisado (`1`)

* **GraphQL Query:**
```graphql
query {
  buscarUsuario(id: 1) {
    id
    nome
    email
  }
}
```
* **Resposta JSON:**
```json
{
  "data": {
    "buscarUsuario": {
      "id": 1,
      "nome": "Hiakewve",
      "email": "hiakewve@email.com"
    }
  }
}
```

---

#### 7. `posts_do_usuario(usuario_id)`
Retorna todos os posts de um autor específico.

- **Argumentos Obrigatórios:**
  - `usuarioId` (Int): ID do autor (`1`)

* **GraphQL Query:**
```graphql
query {
  postsDoUsuario(usuarioId: 1) {
    id
    texto
  }
}
```
* **Resposta JSON:**
```json
{
  "data": {
    "postsDoUsuario": [
      {
        "id": 1,
        "texto": "Meu primeiro post na rede social!"
      }
    ]
  }
}
```

---

#### 8. `buscar_post(id)`
Busca os detalhes de uma publicação específica pelo ID.

- **Argumentos Obrigatórios:**
  - `id` (Int): ID do post (`1`)

* **GraphQL Query:**
```graphql
query {
  buscarPost(id: 1) {
    id
    usuarioId
    texto
  }
}
```
* **Resposta JSON:**
```json
{
  "data": {
    "buscarPost": {
      "id": 1,
      "usuarioId": 1,
      "texto": "Meu primeiro post na rede social!"
    }
  }
}
```

---

#### 9. `seguidores_de(id)` e `seguindo_de(id)`
Consulta a rede de relacionamentos do usuário.

- **Argumentos Obrigatórios:**
  - `id` (Int): ID do usuário para a busca

* **Seguidores do Ericles (ID 2):**
```graphql
query {
  seguidoresDe(id: 2) {
    id
    nome
    email
  }
}
```
* **Resposta JSON:**
```json
{
  "data": {
    "seguidoresDe": [
      {
        "id": 1,
        "nome": "Hiakewve",
        "email": "hiakewve@email.com"
      }
    ]
  }
}
```

* **Quem o Hiakewve (ID 1) está seguindo:**
```graphql
query {
  seguindoDe(id: 1) {
    id
    nome
  }
}
```
* **Resposta JSON:**
```json
{
  "data": {
    "seguindoDe": [
      {
        "id": 2,
        "nome": "Ericles"
      }
    ]
  }
}
```

---

#### 10. `feed_do_usuario(usuario_id)`
Busca o feed composto pelos posts de quem o usuário segue e seus próprios posts.

- **Argumentos Obrigatórios:**
  - `usuarioId` (Int): ID do usuário que lê o feed (`1`)

* **GraphQL Query:**
```graphql
query {
  feedDoUsuario(usuarioId: 1) {
    id
    usuarioId
    texto
  }
}
```
* **Resposta JSON:**
```json
{
  "data": {
    "feedDoUsuario": [
      {
        "id": 1,
        "usuarioId": 1,
        "texto": "Meu primeiro post na rede social!"
      }
    ]
  }
}