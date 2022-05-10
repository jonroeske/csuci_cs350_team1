FROM python:3.10
WORKDIR /code
COPY . .
RUN python -m pip install --upgrade pip
RUN pip3 install colorama
RUN pip3 install Faker
CMD ["python","./main.py"]