FROM python:2

RUN mkdir -p /usr/src/fib
WORKDIR /usr/src/fib

COPY requirements.txt /usr/src/fib/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
COPY fib /usr/src/fib/

ENTRYPOINT [ "gunicorn", "app:app" ]
CMD ["-b", "0.0.0.0:8000" ]
EXPOSE 8000
