from flask import Flask
from routes.routes import routes
from os import getenv
from configs.env import load_env_cfg

load_env_cfg()

app: Flask = Flask(__name__)

# Use blueprint routes
app.register_blueprint(routes)

# Run server
if __name__ == '__main__':
    port: any = getenv('PORT')
    _port: int = int(port) if port != None else 3000
    debug: any = getenv('DEBUG')
    _debug: bool = bool(debug) if debug != None else True
    app.run(port=_port, debug=_debug)
    print('Launcher server is successfully!')
