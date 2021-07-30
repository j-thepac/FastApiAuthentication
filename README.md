# FASTAPI AUTHORIZATION in DOCKER


##You can excute in 2 Ways :
### Locally :
######  PRE-REQ:
- create virtual environment
- `pip install -r requirements.txt`

######  Steps:
- cd to main.py
- `$python main.py`
- open browser : 0.0.0.0:9000/docs

### In Container:

###### pre-req:
Make sure Docker is installed

###### steps:
- cd to dockerfile in this project
- ` docker build -t fastapiauth:v1 .`
- ` docker run -it -p 9000:9000 image_id`
- open browser : 0.0.0.0:9000/docs




