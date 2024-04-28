from typing import Dict
from pathlib import Path
import uuid

from litestar import Litestar, get, websocket_listener
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.template.config import TemplateConfig
from litestar.response import Template
from litestar.static_files import create_static_files_router

UID = uuid.uuid4()

@get("/")
async def index() -> Template:
    return Template(template_name="index.html.jinja")

@get("/user/{tag:str}")
async def user(tag: str) -> Template:
    return Template(template_name="user.html.jinja", context={
        "username": "Auden user",
        "usertag": tag,
        "about": "we are trampling through the bush!" "we are trampling through the bush!" "we are trampling through the bush!" "we are trampling through the bush!""we are trampling through the bush!""we are trampling through the bush!""we are trampling through the bush!""we are trampling through the bush!""we are trampling through the bush!"
    })

@get("/post/{id:str}")
async def post_(id: str) -> Template:
    return Template(template_name="post.html.jinja", context={
        "usertag": "PunBible",
        "caption": "Ligma"
    })

_app = Litestar(
    route_handlers=[
        index,
        user,
        post_,
        create_static_files_router(path="/static", directories=[".dist"]),
    ],
    template_config=TemplateConfig(
        directory=Path("templates"),
        engine=JinjaTemplateEngine,
    ),
)