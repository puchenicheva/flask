FROM python:3.6.2-alpine3.6

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80

COPY . .

CMD [ "python", "./main.py" ]
