FROM python:3.8-slim
COPY $PWD /home/app/
WORKDIR /home/app/
RUN pip install -r requirements.txt
CMD uvicorn main:app --reload --host 0.0.0.0 --port 9000
