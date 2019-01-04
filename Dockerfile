FROM python:stretch

ARG APP_DIR=/app
WORKDIR "$APP_DIR"

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv
RUN pipenv install --system

COPY . $APP_DIR/

ENTRYPOINT ["python", "bot.py"]
