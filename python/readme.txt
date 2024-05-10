Bellow commands for creating docker image:
 
Build image : docker buildx build --platform=linux/amd64 -t <imageName> .
For Developer: docker run -d -it -v ${PWD}:/usr/run/py <imageName> tail -f

* To run this image and check the code, run below commands
- go the docker terminal
- type below command
- python3 index.py