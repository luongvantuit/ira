from dotenv import load_dotenv
from os import path, getenv, getcwd, walk


def load_env_cfg():
    path_env_default = path.join(getcwd(), '.env')

    if path.exists(path=path_env_default):
        load_dotenv(dotenv_path=path_env_default)
    else:
        fs = []
        for _, _, filenames in walk(getcwd()):
            fs.extend([str(f) for f in filenames if str(f).startswith('.env')])
            break
        env: any = getenv('ENV')
        if env != None:
            _env: str = str(env)
            if _env.startswith('prod'):
                fs_prod = [str(f)
                           for f in fs if str(f).startswith('.env.prod')]
                if len(fs_prod) != 0:
                    load_dotenv(dotenv_path=path.join(getcwd(), fs_prod[0]))
            elif _env.startswith('dev'):
                fs_dev = [str(f) for f in fs if str(f).startswith('.env.dev')]
                if len(fs_dev) != 0:
                    load_dotenv(dotenv_path=path.join(getcwd(), fs_dev[0]))
            elif _env.startswith('test'):
                fs_test = [str(f)
                           for f in fs if str(f).startswith('.env.test')]
                if len(fs_test) != 0:
                    load_dotenv(dotenv_path=path.join(getcwd(), fs_test[0]))
