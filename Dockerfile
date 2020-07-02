FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /ilibrary
RUN pip install Django==3.0.8 
RUN pip install psycopg2-binary
CMD ["bash"]