FROM python:3.11-slim-buster

WORKDIR /app

# copy everything from current directory to /app in the container
COPY . .       

# install dependencies
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver