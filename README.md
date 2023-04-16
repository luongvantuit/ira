
### Development

```sh
chmod +x ./scripts/bootstrap.sh

source ./scripts/bootstrap.sh

python3 server.py
```

### Production

```sh
uwsgi --http 127.0.0.1:3000 --module server:app
```