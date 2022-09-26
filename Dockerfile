FROM python:3.7-slim
RUN pip install flask
RUN pip install flask-mysql
RUN mkdir tampletes
COPY form.py /app.py
COPY tampletes/* /tampletes/
RUN chmod -R a+rwx tampletes
CMD ["python","app.py"]
