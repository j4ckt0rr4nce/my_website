# My Django portfolio website

Live site example:

- http://j4ckt0rr4nce.pythonanywhere.com

## What's included?

- A full responsive, portfolio website
- Catalog of services and tools I use
- Email framework for sending mails
- Simple Python code samples
- Website´s blog section with recent blogs
- Comment section for individual blogs

## Installation

This is developed for Python 3 and Django 3.1.

It's recommended that you setup a virtualenv before development.

Then just install requirements, migrate, and runserver to get started:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Customization

I recommend forking this project and just manually modifying it by hand to replace everything with what you want.
Searching for the text on a page in the repository is a great way to find where something lives.

### Sending email

This application uses Django's email framework for sending mail. 
You need to modify the `EMAIL_HOST`, `EMAIL_PORT` and other associated variables in `settings.py` in order
to hook it into a real server.

This [thread on stack overflow](https://stackoverflow.com/questions/6367014/how-to-send-email-via-django)
is a good starting place for learning how to connect to a real mail service.
