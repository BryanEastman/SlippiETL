FROM python:3.10-slim

RUN adduser --system nonroot
USER nonroot

WORKDIR /home/nonroot
RUN mkdir /home/nonroot/app

COPY ./requirements.txt ./
COPY ./containers/slippi_parser ./

RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python", "slippi_parser.py"]