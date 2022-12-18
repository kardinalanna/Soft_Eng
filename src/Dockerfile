FROM python:3.8
RUN mkdir -p /usr/src/app/
COPY . /app
WORKDIR /app
RUN pip install -r requirements
CMD ["python3", "main.py"]
