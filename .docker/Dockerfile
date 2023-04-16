FROM python:3.9.16-bullseye

WORKDIR /ir/app

COPY . .

ENV PORT=3000

EXPOSE ${PORT}

RUN pip install -r requirements.txt

RUN chmod +x ./scripts/run.sh

ENTRYPOINT [ "/ir/app/scripts/run.sh" ]