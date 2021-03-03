# Django orm watching storage.

This is a virtual watching storage project. It shows work with django orm. This is a website that simulates
a security console, it shows who is in the storage of the bank now, a list of active passes and who and when was in the storage.

## How to install.

Download code. For this project you need such environment variables: `DATABASE_HOST, DATABASE_NAME, DATABASE_USER,
DATABASE_PASSWORD, SECRET_KEY, DEBUG`. Put them into .env file, and assign them according values. It should 
look like this:

```
 - DATABASE_HOST=checkpoint.devman.org 
 - DATABASE_NAME=checkpoint
 - DATABASE_USER=guard
 - DATABASE_PASSWORD=osim5
 - SECRET_KEY=REPLACE_ME
 - DEBUG=True
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```

## How to run. 

- Run scripts in command line:
```
python3 manage.py runserver
```
- Open the URL http://127.0.0.1:8000/ in your browser.


### Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org)
