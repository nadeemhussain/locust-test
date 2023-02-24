From python:3

COPY locust.py .
COPY run.sh .

RUN chmod +x run.sh


RUN pip install --no-cache-dir locust

CMD [ "run.sh" ]


