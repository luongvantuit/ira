if [ -z "$(python3 --version)" ]; then
    echo "Python is not installed"
    exit 1
fi

if [ ! -d ${PWD}/env ]; then
    python3 -m venv env
fi

source ${PWD}/env/bin/activate

pip install -r ${PWD}/requirements.txt
pip install --upgrade pip
