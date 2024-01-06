import click
from flask import Blueprint
from rq import Connection, Worker
from app.utils.funcs_util import funcs_util
from app.utils.redis_util import redis_util

# ==============================


def configure(app):
    print(">>>Init CLI")
    app.register_blueprint(cli, cli_group="cli")


# ==============================
cli = Blueprint("cli", __name__)

# ==============================


@cli.cli.command("workers")
def workers():
    print(">>>START cli workers")
    with Connection(redis_util.get_conn_queue()):
        worker = Worker("default")
        worker.work()


# ==============================


@cli.cli.command("test_cli")
@click.argument("input")
def test1_print(input):

    funcs_util.print("cli test_cli", f"executing param[{input}]")


# ==============================


@cli.cli.command("update_from_google_sheet")
def update_from_google_sheet():
    from app.modules.sys.sys_translate_service import sys_translate_service

    srv = sys_translate_service()
    result = srv.update_from_google_sheet()
    funcs_util.print("Finish update_from_google_sheet", result)
