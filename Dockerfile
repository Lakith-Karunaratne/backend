FROM --platform=linux/amd64 python:3.11.5 as pybase
RUN set -xe
RUN pip install fastapi uvicorn poetry wheel gunicorn psycopg2-binary

# COPY . backend/
# COPY poetry.lock /backend/
# COPY pyproject.toml /backend/
COPY requirements.txt /backend/
WORKDIR /backend
# RUN poetry config virtualenvs.create false \
#   && poetry install
RUN pip install -r requirements.txt

FROM pybase as py-pg-odbc
# RUN apt update
# RUN apt -y install postgresql-client

FROM py-pg-odbc as py-poetry-env

COPY . /backend/
WORKDIR /backend

ENV PORT 8000
ENV HOST "0.0.0.0"

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
