from random import randint, choices

import requests

from django.conf import settings
from django.core.management import BaseCommand
from django.urls import reverse
from faker import Faker
from rest_framework import status

from post.models import Post

NUMBER_OF_USERS = 3
MAX_POST_PER_USER = 5
MAX_LIKES_PER_USER = 2


class Command(BaseCommand):
    help = """Test"""
    signup_url = settings.BASE_URL + reverse('register')
    login_url = settings.BASE_URL + reverse('login')
    create_post_url = settings.BASE_URL + reverse('create_post')
    faker = Faker()

    def signup_new_users(self):
        test_users = {}
        for user in range(NUMBER_OF_USERS):
            user_data = dict(
                first_name=self.faker.first_name(),
                last_name=self.faker.last_name(),
                email=self.faker.email(),
                password=self.faker.password())
            test_users.update({user_data['email']: user_data['password']})

            r = requests.post(self.signup_url, user_data)

        return test_users

    def user_activity(self, users):
        for email, password in users.items():
            post_capacity = randint(1, MAX_POST_PER_USER)
            print(f'User {email} is going to create some posts.')
            login = requests.post(self.login_url, data={'email': email,
                                                        'password': password})
            if login.status_code == status.HTTP_200_OK:
                auth_token = login.json()['access']
                header = {'Authorization': 'Bearer ' + auth_token}
                for i in range(post_capacity):
                    requests.post(self.create_post_url,
                                  data={'body': self.faker.text()},
                                  headers=header)
            else:
                print(f'Authorization problems for user {email}')

        posts = Post.objects.all()
        for email, password in users.items():
            likes_capacity = randint(1, MAX_LIKES_PER_USER)
            print(f'User {email} is going to like some posts.')
            login = requests.post(self.login_url, data={'email': email,
                                                        'password': password})
            if login.status_code == status.HTTP_200_OK:
                auth_token = login.json()['access']
                header = {'Authorization': 'Bearer ' + auth_token}
                for post in choices(posts, k=MAX_LIKES_PER_USER):
                    like_post_url = settings.BASE_URL + reverse(
                        'like_post', kwargs={'pk': post.id})
                    print(f'Post {post} is going to be liked by {email}.')
                    requests.post(like_post_url, headers=header)
            else:
                print(f'Authorization problems for user {email}')

    def handle(self, *args, **options):
       users = self.signup_new_users()
       self.user_activity(users)
