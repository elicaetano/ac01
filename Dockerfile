FROM python:3.7-slim
RUN python -m pip install --upgrade pip
RUN pip install flask
RUN pip install flask_sqlalchemy
RUN pip install psycopg2-binary
RUN mkdir templates
COPY form.py /app.py
COPY templates/*  /templates/
RUN chmod -R a+rwx templates
CMD ["python","app.py"]

