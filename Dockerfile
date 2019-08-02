FROM python:3.6
ENV PATH /usr/local/bin:$PATH
ADD . /blog
WORKDIR /blog
RUN pip install -r requirements.txt
CMD [ "python", "manage.py", "runserver", "0.0.0.0:80"]