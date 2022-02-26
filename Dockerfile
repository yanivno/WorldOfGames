FROM python:3.8.12
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD python MainScores.py