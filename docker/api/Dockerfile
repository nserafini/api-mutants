FROM python:3.8.2

ENV PYTHONPATH=/app
EXPOSE ${PORT:-8090}

RUN groupadd --gid 1000 user && useradd --uid 1000 --gid 1000 -m user

RUN pip install --upgrade pip

COPY . /app
WORKDIR /app

ARG requirements=/app/requirements.txt
RUN pip install -r ${requirements}

ENTRYPOINT ["./docker/api/entrypoint.sh"]