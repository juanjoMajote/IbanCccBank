FROM python:alpine
MAINTAINER Juanjo Martinez "juanjo.majote@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SUPER_USER="admin" \
    DJANGO_PASS="Default.2019" \ 
    DJANGO_EMAIL="admin@IbanCccBank.es" 
# Creating working directory
RUN mkdir /code && mkdir /code/requirements/
WORKDIR /code

# Copying requirements
COPY ./requirements/ ./requirements/

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev bash \
    mysql-client \
    sqlite-libs \
    libffi-dev jpeg-dev zlib-dev \
    && pip install --upgrade pip \
    && pip install -r ./requirements/requirements.txt \
    && find /usr/local \
        \( -type d -a -name test -o -name tests \) \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps
COPY ./IbanCccBank/. ./
COPY ./docker-entrypoint.sh .
RUN chmod 755 docker-entrypoint.sh
ENTRYPOINT ["/code/docker-entrypoint.sh"]

