FROM ubuntu:latest
COPY . /app
RUN apt-get update && apt-get install -y python3 python3-pip x11-apps
RUN pip3 install flyt_python
RUN apt-get install -y xvfb
ENV DISPLAY=:0
CMD xvfb-run python3 /app/Square_path.py
