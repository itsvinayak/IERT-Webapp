FROM python:3.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \ 
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/spider/Documents/iert_site/
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
