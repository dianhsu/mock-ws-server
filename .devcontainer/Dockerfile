FROM python:3.12


ENV POETRY_HOME=/opt/poetry
ENV TZ='Asia/Shanghai'
RUN apt-get -y install curl
RUN curl -sSL https://install.python-poetry.org | python - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false