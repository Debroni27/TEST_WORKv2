# pull official base image
FROM python:3.9.13-alpine

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install pillow dependencies
RUN apk add build-base py-pip jpeg-dev zlib-dev

# traslation
RUN apk add gettext

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt $APP_HOME
RUN pip install -r requirements.txt

# copy project
COPY . $APP_HOME

# run entrypoint.prod.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]