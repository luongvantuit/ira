#!/bin/bash

while true; do
    case $1 in
    -p | --port)
        shift
        PORT="$1"
        ;;
    *)
        break
        ;;
    esac
    shift
done

if [ -z $PORT ]; then
    export PORT=3000
fi

uwsgi --http 0.0.0.0:${PORT} --module server:app
