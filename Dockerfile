FROM python:3.6-apline

WORKDIR /apline

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 4002

CMD [ "flask", "run", "--host=0.0.0.0", "port=4000"]