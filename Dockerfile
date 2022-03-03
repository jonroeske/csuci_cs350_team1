FROM python:3.10
WORKDIR /code
COPY . .
CMD ["python","./main.py"]