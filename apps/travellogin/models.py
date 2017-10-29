# Inside your app's models.py file
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt, datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'(.*)\s(.*)$')


class UserManager(models.Manager):
    def user_validator(self, post_data):
        errors = []
        if len(post_data['name']) < 3:
            errors.append("name should be at least 3 characters")
        # if len(post_data['Last_name']) < 2:
        #     errors.append("Last name should be at least 2 characters")
        if len(User.objects.filter(username=post_data['username'])) > 0:
            errors.append("User name (email) already in used")
        if not re.match(NAME_REGEX, post_data['name']): # or not re.match(NAME_REGEX, post_data['last_name']):
            errors.append('name fields must be letter characters only')
        if not re.match(EMAIL_REGEX, post_data['username']):
            errors.append("invalid email format")
        if len(post_data['password']) < 8:
            errors.append("password must be at least 8 characters")
        if post_data['password'] != post_data['passconf']:
            errors.append("passwords do not match")

        print ("***********  errors", errors)
        if not errors:
            hash1 = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())
            password = hash1
            print (hash1)
            new_register = self.create(
                name=post_data['name'],
                username=post_data['username'],
                password = hash1
            )
            # print ("added registerer")
            return new_register
        return errors

    def login_validator(self, post_data):
            errors = []
            # check DB for post_data['username']
            if len(self.filter(username=post_data['username'])) > 0:
                # check this user's password
                user = self.filter(username=post_data['username'])[0]
                # print (user_validator)
                # print (user_validator.password.encode())
                # print (post_data['password'].encode())
                if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                    errors.append('username/password incorrect - 1')
            else:
                    errors.append('username/password incorrect - 2')

            if errors:
                return errors
            return user


class User(models.Model):
        name = models.CharField(max_length=255)
        username = models.CharField(max_length=255)
        password = models.CharField(max_length=255)
        created_at = models.DateTimeField(auto_now_add = True)
        updated_at = models.DateTimeField(auto_now = True)
        objects = UserManager()

class TravelManager(models.Manager):
    def travel_validator(self, post_data):
        if len(post_data['item']) < 3:
            errors.append("item name should be at least 3 characters")
        if (post_data['end_date']) < post_data['start_date']:
            errors.append("End_date must be greater than trip start date")
        if (post_date['start_date']) <= today():
            errors.append("Start date must be greater that today's date")
        if errors:
            return errors

    def travelplanadd(self, post_data, user2):
       new_plan = self.create(
           plan=post_data['destination'],
           descr=post_data['description'],
           start_date=post_data['from_date'],
           end_date=post_data['end_date'],
           )
       user = User.objects.get(id=user2)
    #    awishlist.user.add(new_wish)
       user.planby.add(new_plan)
       new_plan.user.add(user)
       return new_plan

    #    return item



class Travel(models.Model):
       plan = models.TextField()
       descr= models.TextField()
       user = models.ManyToManyField(User, related_name = "planby")
       start_date = models.DateField()
       end_date   = models.DateField()
       created_at = models.DateTimeField(auto_now_add = True)
       updated_at = models.DateTimeField(auto_now = True)
       objects = TravelManager()
