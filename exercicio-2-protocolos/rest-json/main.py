import sys
from pathlib import Path
from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# Permite importar o banco.py a partir da pasta raiz
sys.path.append(str(Path(__file__).resolve().parent.parent))
import banco

app = FastAPI(
    title="Rede Social API - REST (JSON)",
    description="Implementação RESTful para o Exercício 2 de Protocolos",
    version="1.0.0"
)

class CriarUsuarioDTO(BaseModel):
    nome: str
    email: str

class CriarPostDTO(BaseModel):
    usuario_id: int
    texto: str

class ComentarDTO(BaseModel):
    usuario_id: int
    texto: str

class SeguirDTO(BaseModel):
    alvo_id: int

# comandos
@app.post("/usuarios", status_code=status.HTTP_201_CREATED, summary="1. criar_usuario(nome, email)")
def criar_usuario(payload: CriarUsuarioDTO):
    usuario = banco.criar_usuario(nome=payload.nome, email=payload.email)
    return usuario

@app.post("/posts", status_code=status.HTTP_201_CREATED, summary="2. criar_post(usuario_id, texto)")
def criar_post(payload: CriarPostDTO):
    post = banco.criar_post(usuario_id=payload.usuario_id, texto=payload.texto)
    if not post:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return post

@app.post("/posts/{post_id}/comentarios", status_code=status.HTTP_201_CREATED, summary="3. comentar(usuario_id, post_id, texto)")
def comentar(post_id: int, payload: ComentarDTO):
    comentario = banco.comentar(usuario_id=payload.usuario_id, post_id=post_id, texto=payload.texto)
    if not comentario:
        raise HTTPException(status_code=404, detail="Usuário ou Post não encontrado.")
    return comentario

@app.post("/posts/{post_id}/curtir", status_code=status.HTTP_200_OK, summary="4. curtir(usuario_id, post_id)")
def curtir(post_id: int, usuario_id: int):
    sucesso = banco.curtir(usuario_id=usuario_id, post_id=post_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Usuário ou Post não encontrado.")
    return {"mensagem": "Post curtido com sucesso."}

@app.post("/usuarios/{usuario_id}/seguir", status_code=status.HTTP_200_OK, summary="5. seguir(usuario_id, alvo_id)")
def seguir(usuario_id: int, payload: SeguirDTO):
    sucesso = banco.seguir(usuario_id=usuario_id, alvo_id=payload.alvo_id)
    if not sucesso:
        raise HTTPException(status_code=400, detail="Operação de seguir inválida (usuário inexistente ou auto-seguimento).")
    return {"mensagem": "Usuário seguido com sucesso."}

# consultas
@app.get("/usuarios/{usuario_id}", summary="6. buscar_usuario(id)")
def buscar_usuario(usuario_id: int):
    usuario = banco.buscar_usuario(usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return usuario

@app.get("/usuarios/{usuario_id}/posts", summary="7. posts_do_usuario(usuario_id)")
def posts_do_usuario(usuario_id: int):
    if not banco.buscar_usuario(usuario_id):
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return banco.posts_do_usuario(usuario_id)

@app.get("/posts/{post_id}", summary="8. buscar_post(id)")
def buscar_post(post_id: int):
    post = banco.buscar_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post não encontrado.")
    return post

@app.get("/usuarios/{usuario_id}/seguidores", summary="9a. seguidores_de(id)")
def seguidores_de(usuario_id: int):
    if not banco.buscar_usuario(usuario_id):
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return banco.seguidores_de(usuario_id)

@app.get("/usuarios/{usuario_id}/seguindo", summary="9b. seguindo_de(id)")
def seguindo_de(usuario_id: int):
    if not banco.buscar_usuario(usuario_id):
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return banco.seguindo_de(usuario_id)

@app.get("/usuarios/{usuario_id}/feed", summary="10. feed_do_usuario(usuario_id)")
def feed_do_usuario(usuario_id: int):
    if not banco.buscar_usuario(usuario_id):
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return banco.feed_do_usuario(usuario_id)