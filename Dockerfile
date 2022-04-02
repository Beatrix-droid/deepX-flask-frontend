FROM python:3.8.6-buster

COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY static /static
COPY templates /templates

COPY finalmodel.h5 /finalmodel.h5
COPY main.py /main.py
COPY generate_im.py /generate_im.py
COPY mask.py /mask.py
COPY predict.py /predict.py
ENV FLASK_APP main.py
ENV FLASK_ENV production
CMD flask run --host 0.0.0.0 --port $PORT
