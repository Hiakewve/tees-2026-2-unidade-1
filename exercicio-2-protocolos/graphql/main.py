import sys
from pathlib import Path
from typing import List, Optional
import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI

# Permite importar o banco.py a partir da pasta raiz
sys.path.append(str(Path(__file__).resolve().parent.parent))
import banco

# 1. definição dos tipos

@strawberry.type
class PerfilType:
    bio: str
    foto_url: str

@strawberry.type
class UsuarioType:
    id: int
    nome: str
    email: str
    perfil: PerfilType

@strawberry.type
class PostType:
    id: int
    usuario_id: int
    texto: str

@strawberry.type
class ComentarioType:
    id: int
    usuario_id: int
    post_id: int
    texto: str

def _converter_usuario(u) -> Optional[UsuarioType]:
    if not u:
        return None
    return UsuarioType(
        id=u.id,
        nome=u.nome,
        email=u.email,
        perfil=PerfilType(bio=u.perfil.bio, foto_url=u.perfil.foto_url)
    )

def _converter_post(p) -> Optional[PostType]:
    if not p:
        return None
    return PostType(id=p.id, usuario_id=p.usuario_id, texto=p.texto)

def _converter_comentario(c) -> Optional[ComentarioType]:
    if not c:
        return None
    return ComentarioType(id=c.id, usuario_id=c.usuario_id, post_id=c.post_id, texto=c.texto)

# 2. consultas
@strawberry.type
class Query:
    @strawberry.field(description="6. buscar_usuario(id)")
    def buscar_usuario(self, id: int) -> Optional[UsuarioType]:
        u = banco.buscar_usuario(id)
        return _converter_usuario(u)

    @strawberry.field(description="7. posts_do_usuario(usuario_id)")
    def posts_do_usuario(self, usuario_id: int) -> List[PostType]:
        posts = banco.posts_do_usuario(usuario_id)
        return [_converter_post(p) for p in posts]

    @strawberry.field(description="8. buscar_post(id)")
    def buscar_post(self, id: int) -> Optional[PostType]:
        p = banco.buscar_post(id)
        return _converter_post(p)

    @strawberry.field(description="9a. seguidores_de(id)")
    def seguidores_de(self, id: int) -> List[UsuarioType]:
        seguidores = banco.seguidores_de(id)
        return [_converter_usuario(u) for u in seguidores]

    @strawberry.field(description="9b. seguindo_de(id)")
    def seguindo_de(self, id: int) -> List[UsuarioType]:
        seguindo = banco.seguindo_de(id)
        return [_converter_usuario(u) for u in seguindo]

    @strawberry.field(description="10. feed_do_usuario(usuario_id)")
    def feed_do_usuario(self, usuario_id: int) -> List[PostType]:
        posts = banco.feed_do_usuario(usuario_id)
        return [_converter_post(p) for p in posts]

# 3. comandos
@strawberry.type
class Mutation:
    @strawberry.mutation(description="1. criar_usuario(nome, email)")
    def criar_usuario(self, nome: str, email: str) -> UsuarioType:
        u = banco.criar_usuario(nome=nome, email=email)
        return _converter_usuario(u)

    @strawberry.mutation(description="2. criar_post(usuario_id, texto)")
    def criar_post(self, usuario_id: int, texto: str) -> Optional[PostType]:
        p = banco.criar_post(usuario_id=usuario_id, texto=texto)
        return _converter_post(p)

    @strawberry.mutation(description="3. comentar(usuario_id, post_id, texto)")
    def comentar(self, usuario_id: int, post_id: int, texto: str) -> Optional[ComentarioType]:
        c = banco.comentar(usuario_id=usuario_id, post_id=post_id, texto=texto)
        return _converter_comentario(c)

    @strawberry.mutation(description="4. curtir(usuario_id, post_id)")
    def curtir(self, usuario_id: int, post_id: int) -> bool:
        return banco.curtir(usuario_id=usuario_id, post_id=post_id)

    @strawberry.mutation(description="5. seguir(usuario_id, alvo_id)")
    def seguir(self, usuario_id: int, alvo_id: int) -> bool:
        return banco.seguir(usuario_id=usuario_id, alvo_id=alvo_id)

# 4. criação da aplicação
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)

app = FastAPI(title="Rede Social API - GraphQL")
app.include_router(graphql_app, prefix="/graphql")