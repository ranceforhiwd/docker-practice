# Download base with Ubuntu and php 8.2
 
FROM amd64/php:8.2-cli
COPY . /usr/run/php 
 
#Update Ubuntu Software repository
RUN apt-get update
 
# Install packages
RUN set -x \
  && apt-get install -y wget \
    software-properties-common \
    build-essential \
    git \
    nano \
    libpng-dev

RUN apt-get update && apt-get install -y \
    zip \
    unzip
 
WORKDIR /usr/run/php
CMD [ "php", "index.php" ]