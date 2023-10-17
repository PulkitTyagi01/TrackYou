FROM python:3.10.5

WORKDIR /TrackYou

COPY ./requirements.txt requirements.txt

COPY . .


RUN pip3 install -r requirements.txt

ENV  PYTHONUNBUFFERED=1

CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]

EXPOSE 8000
