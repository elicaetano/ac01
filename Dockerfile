FROM python:3.7-slim
RUN pip install flask
RUN pip install flask-mysql
COPY form.py /app.py
RUN chmod -R a+rwx tampletes
CMD ["python","app.py"]
