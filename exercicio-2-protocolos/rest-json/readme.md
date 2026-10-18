# API REST (JSON) - Rede Social

Esta é a implementação completa da API para o domínio de **Rede Social** utilizando o protocolo **REST** com transferência de dados em formato **JSON**. O projeto foi construído utilizando o framework **FastAPI** em Python.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI**: Framework web moderno e de alta performance.
- **Uvicorn**: Servidor ASGI para execução do servidor local.
- **Pydantic**: Validação dos tipos de dados de entrada e saída.

---

## 🚀 Como Executar do Zero

### 1. Pré-requisitos
Certifique-se de ter o Python 3.10 ou superior instalado na sua máquina.

### 2. Instalar as dependências
A partir do terminal, acesse a pasta `rest-json` e instale os pacotes:

```bash
cd rest-json
pip install fastapi uvicorn

### 3. Iniciar o servidor
Ainda dentro da pasta `rest-json`, execute o comando:

```bash
uvicorn main:app --reload
```

O servidor iniciará localmente e estará acessível em: `http://127.0.0.1:8000`

### 4. Interagir via Interface Visual (Swagger UI)
O FastAPI gera a documentação OpenAPI/Swagger automaticamente. Você pode testar e disparar todas as requisições direto pelo navegador acessando:

- **Swagger UI**: `http://127.0.0.1:8000/docs`

---

## 📋 Mapeamento de Rotas e Exemplos Copiáveis

Abaixo estão listadas todas as **10 operações obrigatórias** (5 comandos e 5 consultas) com seus respectivos métodos HTTP, URLs, campos necessários e exemplos de requisição e resposta.

---

### 🟢 COMANDOS (Escrita / Alteração de Estado)

#### 1. `criar_usuario(nome, email)`
Cria um novo usuário na rede social.

- **Campos do Corpo:**
  - `nome` (string, obrigatório): Nome do usuário
  - `email` (string, obrigatório): E-mail do usuário

**Exemplo 1 (Primeiro Usuário - ID 1):**
- **Método:** `POST`
- **URL:** `http://127.0.0.1:8000/usuarios`
- **Request Body:**
```json
{
  "nome": "Hiakewve",
  "email": "hiakewve@email.com"
}
```
- **Response Body (Status 201 Created):**
```json
{
  "id": 1,
  "nome": "Hiakewve",
  "email": "hiakewve@email.com",
  "perfil": {
    "bio": "",
    "foto_url": ""
  }
}
```

**Exemplo 2 (Segundo Usuário - ID 2):**
- **Método:** `POST`
- **URL:** `http://127.0.0.1:8000/usuarios`
- **Request Body:**
```json
{
  "nome": "Ericles",
  "email": "ericles@email.com"
}
```
- **Response Body (Status 201 Created):**
```json
{
  "id": 2,
  "nome": "Ericles",
  "email": "ericles@email.com",
  "perfil": {
    "bio": "",
    "foto_url": ""
  }
}
```

---

#### 2. `criar_post(usuario_id, texto)`
Publica um novo post associado ao ID de um usuário existente.

- **Campos do Corpo:**
  - `usuario_id` (integer, obrigatório): ID do autor do post
  - `texto` (string, obrigatório): Conteúdo da publicação

- **Método:** `POST`
- **URL:** `http://127.0.0.1:8000/posts`
- **Request Body:**
```json
{
  "usuario_id": 1,
  "texto": "Meu primeiro post na rede social!"
}
```
- **Response Body (Status 201 Created):**
```json
{
  "id": 1,
  "usuario_id": 1,
  "texto": "Meu primeiro post na rede social!"
}
```

---

#### 3. `comentar(usuario_id, post_id, texto)`
Adiciona um comentário em um post específico.

- **Campos na URL:**
  - `post_id` (integer, no caminho da URL): ID do post a ser comentado
- **Campos do Corpo:**
  - `usuario_id` (integer, obrigatório): ID de quem comenta
  - `texto` (string, obrigatório): Conteúdo do comentário

- **Método:** `POST`
- **URL:** `http://127.0.0.1:8000/posts/1/comentarios`
- **Request Body:**
```json
{
  "usuario_id": 2,
  "texto": "Muito bom seu post, Hiakewve!"
}
```
- **Response Body (Status 201 Created):**
```json
{
  "id": 1,
  "usuario_id": 2,
  "post_id": 1,
  "texto": "Muito bom seu post, Hiakewve!"
}
```

---

#### 4. `curtir(usuario_id, post_id)`
Registra a curtida de um usuário em determinado post.

- **Campos na URL / Query Parameters:**
  - `post_id` (integer, no caminho da URL): ID do post curtido (`1`)
  - `usuario_id` (integer, parâmetro de query): ID de quem curte (`2`)

- **Método:** `POST`
- **URL:** `http://127.0.0.1:8000/posts/1/curtir?usuario_id=2`
- **Request Body:** *(Sem corpo)*
- **Response Body (Status 200 OK):**
```json
{
  "mensagem": "Post curtido com sucesso."
}
```

---

#### 5. `seguir(usuario_id, alvo_id)`
Faz com que o usuário de origem passe a seguir o usuário de destino (`alvo_id`).

- **Campos na URL:**
  - `usuario_id` (integer, no caminho da URL): ID do usuário seguidor (`1` - Hiakewve)
- **Campos do Corpo:**
  - `alvo_id` (integer, obrigatório): ID do usuário a ser seguido (`2` - Ericles)

- **Método:** `POST`
- **URL:** `http://127.0.0.1:8000/usuarios/1/seguir`
- **Request Body:**
```json
{
  "alvo_id": 2
}
```
- **Response Body (Status 200 OK):**
```json
{
  "mensagem": "Usuário seguido com sucesso."
}
```

---

### 🔵 CONSULTAS (Leitura de Dados)

#### 6. `buscar_usuario(id)`
Busca os dados cadastrais de um usuário pelo seu ID.

- **Campos na URL:**
  - `usuario_id` (integer, no caminho da URL): ID do usuário pesquisado (`1`)

- **Método:** `GET`
- **URL:** `http://127.0.0.1:8000/usuarios/1`
- **Response Body (Status 200 OK):**
```json
{
  "id": 1,
  "nome": "Hiakewve",
  "email": "hiakewve@email.com",
  "perfil": {
    "bio": "",
    "foto_url": ""
  }
}
```

---

#### 7. `posts_do_usuario(usuario_id)`
Retorna a lista de todas as postagens criadas por um determinado usuário.

- **Campos na URL:**
  - `usuario_id` (integer, no caminho da URL): ID do autor (`1`)

- **Método:** `GET`
- **URL:** `http://127.0.0.1:8000/usuarios/1/posts`
- **Response Body (Status 200 OK):**
```json
[
  {
    "id": 1,
    "usuario_id": 1,
    "texto": "Meu primeiro post na rede social!"
  }
]
```

---

#### 8. `buscar_post(id)`
Busca as informações detalhadas de um post pelo seu ID.

- **Campos na URL:**
  - `post_id` (integer, no caminho da URL): ID do post pesquisado (`1`)

- **Método:** `GET`
- **URL:** `http://127.0.0.1:8000/posts/1`
- **Response Body (Status 200 OK):**
```json
{
  "id": 1,
  "usuario_id": 1,
  "texto": "Meu primeiro post na rede social!"
}
```

---

#### 9. `seguidores_de(id)` / `seguindo_de(id)`
Retorna a lista de quem segue o usuário ou quem o usuário segue.

- **Campos na URL:**
  - `usuario_id` (integer, no caminho da URL): ID do usuário para consulta

- **Seguidores do Ericles (ID 2):**
  - **Método:** `GET`
  - **URL:** `http://127.0.0.1:8000/usuarios/2/seguidores`
  - **Response Body (Status 200 OK):**
  ```json
  [
    {
      "id": 1,
      "nome": "Hiakewve",
      "email": "hiakewve@email.com",
      "perfil": {
        "bio": "",
        "foto_url": ""
      }
    }
  ]
  ```

- **Quem o Hiakewve (ID 1) está seguindo:**
  - **Método:** `GET`
  - **URL:** `http://127.0.0.1:8000/usuarios/1/seguindo`
  - **Response Body (Status 200 OK):**
  ```json
  [
    {
      "id": 2,
      "nome": "Ericles",
      "email": "ericles@email.com",
      "perfil": {
        "bio": "",
        "foto_url": ""
      }
    }
  ]
  ```

---

#### 10. `feed_do_usuario(usuario_id)`
Retorna a lista de posts das contas que o usuário segue somada às suas próprias publicações.

- **Campos na URL:**
  - `usuario_id` (integer, no caminho da URL): ID do usuário visualizando o feed (`1`)

- **Método:** `GET`
- **URL:** `http://127.0.0.1:8000/usuarios/1/feed`
- **Response Body (Status 200 OK):**
```json
[
  {
    "id": 1,
    "usuario_id": 1,
    "texto": "Meu primeiro post na rede social!"
  }
]