FROM python:3.8-slim
WORKDIR /var/www/
RUN mkdir /app
ADD . /var/www/
RUN pip3 install -r requirements.txt
ADD . /app
RUN chmod +x ./entrypoint.sh
EXPOSE 5000
ENTRYPOINT ["sh", "entrypoint.sh"]