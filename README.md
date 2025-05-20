# Image Microservice Communication Contract

## A. Requesting Data
To request data from the image microservice, write a digit corresponding to the current image set being diplayed to imgSrv.txt
```
with open('imgSrv.txt','w') as file:
  file.write(num)
```

## B. Receiving Data
To receive data from the image microservice, read the file paths for all images in a set from imgPath.txt
```
with open('imgPath.txt','r') as file:
  paths = file.read()
```
![UML Sequence Diagram](Image Microservice UML.png)
