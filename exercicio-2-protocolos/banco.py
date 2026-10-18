from dataclasses import dataclass, field
from typing import List, Optional

# 1. estrutura das entidades (modelos de dados)
@dataclass
class Perfil:
    bio: str = ""
    foto_url: str = ""

@dataclass
class Usuario:
    id: int
    nome: str
    email: str
    perfil: Perfil = field(default_factory=Perfil)

@dataclass
class Post:
    id: int
    usuario_id: int
    texto: str

@dataclass
class Comentario:
    id: int
    usuario_id: int
    post_id: int
    texto: str

@dataclass
class Curtida:
    usuario_id: int
    post_id: int

@dataclass
class Seguidor:
    seguidor_id: int  # Quem está seguindo
    alvo_id: int      # Quem está sendo seguido

# 2. armazeanemtno em memória (a ideia é simular um banco)
db_usuarios: List[Usuario] = []
db_posts: List[Post] = []
db_comentarios: List[Comentario] = []
db_curtidas: List[Curtida] = []
db_seguidores: List[Seguidor] = []

_contador_id = {
    "usuario": 1,
    "post": 1,
    "comentario": 1
}

def _proximo_id(entidade: str) -> int:
    novo_id = _contador_id[entidade]
    _contador_id[entidade] += 1
    return novo_id

# 3. comandos de escrita
def criar_usuario(nome: str, email: str) -> Usuario:
    novo_usuario = Usuario(id=_proximo_id("usuario"), nome=nome, email=email)
    db_usuarios.append(novo_usuario)
    return novo_usuario

def criar_post(usuario_id: int, texto: str) -> Optional[Post]:
    # valida se o usuário existe antes de criar o post
    if not buscar_usuario(usuario_id):
        return None
    novo_post = Post(id=_proximo_id("post"), usuario_id=usuario_id, texto=texto)
    db_posts.append(novo_post)
    return novo_post

def comentar(usuario_id: int, post_id: int, texto: str) -> Optional[Comentario]:
    if not buscar_usuario(usuario_id) or not buscar_post(post_id):
        return None
    novo_comentario = Comentario(
        id=_proximo_id("comentario"),
        usuario_id=usuario_id,
        post_id=post_id,
        texto=texto
    )
    db_comentarios.append(novo_comentario)
    return novo_comentario

def curtir(usuario_id: int, post_id: int) -> bool:
    if not buscar_usuario(usuario_id) or not buscar_post(post_id):
        return False
    # Evita curtidas duplicadas do mesmo usuário no mesmo post
    for c in db_curtidas:
        if c.usuario_id == usuario_id and c.post_id == post_id:
            return True # Já curtiu
    db_curtidas.append(Curtida(usuario_id=usuario_id, post_id=post_id))
    return True

def seguir(usuario_id: int, alvo_id: int) -> bool:
    if usuario_id == alvo_id:
        return False  # Não pode seguir a si mesmo
    if not buscar_usuario(usuario_id) or not buscar_usuario(alvo_id):
        return False
    # Evita seguir duas vezes a mesma pessoa
    for s in db_seguidores:
        if s.seguidor_id == usuario_id and s.alvo_id == alvo_id:
            return True
    db_seguidores.append(Seguidor(seguidor_id=usuario_id, alvo_id=alvo_id))
    return True

# 4. comandos de leitura
def buscar_usuario(id: int) -> Optional[Usuario]:
    for u in db_usuarios:
        if u.id == id:
            return u
    return None

def posts_do_usuario(usuario_id: int) -> List[Post]:
    return [p for p in db_posts if p.usuario_id == usuario_id]

def buscar_post(id: int) -> Optional[Post]:
    for p in db_posts:
        if p.id == id:
            return p
    return None

def seguidores_de(id: int) -> List[Usuario]:
    # Retorna a lista de usuários que seguemn o usuário do 'id' informado
    ids_seguidores = [s.seguidor_id for s in db_seguidores if s.alvo_id == id]
    return [u for u in db_usuarios if u.id in ids_seguidores]

def seguindo_de(id: int) -> List[Usuario]:
    # Retorna a lista de usuários que o usuário do 'id' informado está seguindo
    ids_alvos = [s.alvo_id for s in db_seguidores if s.seguidor_id == id]
    return [u for u in db_usuarios if u.id in ids_alvos]

def feed_do_usuario(usuario_id: int) -> List[Post]:
    usuarios_que_sigo = seguindo_de(usuario_id)
    ids_para_o_feed = [u.id for u in usuarios_que_sigo]
    ids_para_o_feed.append(usuario_id)  # Inclui os próprios posts no feed

    return [p for p in db_posts if p.usuario_id in ids_para_o_feed]