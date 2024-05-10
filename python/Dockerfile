FROM python:3.11
COPY . /usr/run/py
 
# Installing packages
RUN pip3 install requests pandas

# WORKDIR
WORKDIR /usr/run/py

# Script
CMD [ "python3", "index.py" ]
