FROM python
COPY app.py .
RUN pip3 install flask
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
