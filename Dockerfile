FROM python:3.12-alpine3.20
LABEL authors="odivalneto"

# SAVE BYTECODE (.pyc) in disk, 1 = NOT 0 = YES
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

COPY DesafioApp /DesafioApp
COPY scripts /scripts

RUN apk add nodejs
RUN apk add npm

WORKDIR /DesafioApp
EXPOSE 8000

RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /DesafioApp/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts


ENV PATH="/scripts:/venv/bin:$PATH"

USER duser

CMD ["commands.sh", "node"]