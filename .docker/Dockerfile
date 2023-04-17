FROM node:16.2.0-slim AS TW

WORKDIR /ir/tailwind

COPY ./tailwind.config.js ./tailwind.config.js

COPY ./input.css ./input.css

COPY ./templates ./templates

COPY ./static ./static

RUN yarn global add tailwindcss

RUN npx tailwind --input ./input.css --output ./static/dist/output.css --config ./tailwind.config.js 

FROM python:3.9.16-bullseye

WORKDIR /ir/app

COPY . .

ENV PORT=3000

EXPOSE ${PORT}

COPY --from=TW /ir/tailwind/static/dist/output.css /ir/app/static/dist/output.css

RUN pip install -r requirements.txt

RUN chmod +x ./scripts/run.sh

ENTRYPOINT [ "/ir/app/scripts/run.sh" ]