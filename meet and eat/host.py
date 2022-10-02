import mongoengine
from datetime import datetime


class Host(mongoengine.Document):
    register_time = mongoengine.DateTimeField(default=datetime.now) # NO (), might cose a problem
    name = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)
    country = mongoengine.StringField(required=True)
    city = mongoengine.StringField(required=True)
    is_vegan = mongoengine.BooleanField(required=True)
    is_vegetarian = mongoengine.BooleanField(required=True)
    is_kosher = mongoengine.BooleanField(required=True)
    is_halal = mongoengine.BooleanField(required=True)
    hobbies = mongoengine.StringField(required=True)
    can_you_host = mongoengine.BooleanField(required=True)


    meta = {
        'db_alias': 'core',
        'collection': 'hosts'
    }

  
