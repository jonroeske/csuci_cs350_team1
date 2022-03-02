FROM python:3.10
WORKDIR /code
COPY src/ .
CMD ["python","./main.py"]