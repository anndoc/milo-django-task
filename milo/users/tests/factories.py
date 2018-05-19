import factory
from django.conf import settings
from django.contrib.auth.hashers import make_password


TEST_USER_PASSWORD = 'P4ssw0rd'


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Sequence(lambda n: 'user_{0}'.format(n))
    email = factory.Sequence(lambda n: 'user_{0}@email.com'.format(n))
    password = make_password(TEST_USER_PASSWORD)
    birthday = factory.Faker('date')
