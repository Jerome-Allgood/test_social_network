# Social Network test task
This project was created using Python 3.8 and Django 3.1

## Basic models:
* User
* Post

## Basic features:
* User sign-up
* User log in
* Post creation
* Post like/unlike

### For required token authentication was used [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

### For functionality demonstration use command:
> **./manage.py simulate_activity**

This command would create Users and simulate User actions like Login, Create Post, Like Post

#### Email validation via emailhunter.co was implemented but disabled to avoid exceeding using limits.
To enable it set **DEMONSTRATION = False** in *settings.py*.
