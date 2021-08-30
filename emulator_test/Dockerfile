FROM python:3
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DEBUG 0



RUN mkdir -p /usr/src/emulator_test
WORKDIR /usr/src/emulator_test


COPY requirements.txt /usr/src/emulator_test/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /usr/src/emulator_test/

