Bellow commands for creating docker image:
 
Build image : docker build -t <imageName> .
For Developer: docker run -d -it -v ${PWD}:/usr/run/php <imageName> tail -f

* To run this image and check the code, run below commands
- go the docker terminal
- type below command 
- php index.php