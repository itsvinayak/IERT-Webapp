FROM django

ADD . /src

WORKDIR /src

RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 172.0.0.1:8000" ]


