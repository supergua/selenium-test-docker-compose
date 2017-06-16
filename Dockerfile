FROM python:3.5-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
ADD webdriver.py /usr/local/lib/python3.5/site-packages/selenium/webdriver/remote/webdriver.py
CMD ["python", "test.py"]
