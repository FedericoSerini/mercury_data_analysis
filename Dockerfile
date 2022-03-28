FROM python:3.8-slim-buster


ADD ./ ./mercury-data-analysis

RUN pip install Flask
RUN pip install colorlog
RUN pip install numpy
RUN pip install pandas

EXPOSE 5000
WORKDIR /mercury-data-analysis
CMD [ "python", "/mercury-data-analysis/api.py" ]

