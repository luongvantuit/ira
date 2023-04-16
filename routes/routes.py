from flask import Blueprint, Flask

routes: Blueprint = Blueprint('routes', __name__, url_prefix='/')


def useRoute() -> None:
    pass


def _useRoute(app: Flask, route: any) -> None:
    pass
