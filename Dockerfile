FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /case-pb
WORKDIR /case-pb


RUN pip install --no-cache-dir --upgrade pip pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile

COPY ./src /case-pb/src
WORKDIR /case-pb/src

CMD ["uvicorn", "app.server:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000", "--reload"]
