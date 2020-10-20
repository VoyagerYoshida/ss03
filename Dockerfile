FROM python:3.8
LABEL maintainer="voyagerwy130 <voyager.yoshida@gmail.com>"

ENV WORKSPACE /var/www
WORKDIR $WORKSPACE

RUN pip install pytest
    
CMD ["python"]
