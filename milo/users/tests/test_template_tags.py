import datetime

from django.conf import settings

from users.templatetags.user_tags import is_allowed, bizzfuzz
from users.tests.factories import UserFactory


class TestTemplateTags:

    def test_is_allowed(self):
        """
        User is > 13 years old
        """
        user = UserFactory.build(birthday=datetime.datetime(datetime.date.today().year -
                                                            settings.USER_ALLOWED_AGE - 1, 1, 1))
        return is_allowed(user) == 'allowed'

    def test_is_blocked(self):
        """
        User is < 13 years old
        """
        user = UserFactory.build(birthday=datetime.datetime(datetime.date.today().year -
                                                            settings.USER_ALLOWED_AGE + 1, 1, 1))
        return is_allowed(user) == 'blocked'

    def test_bizzfuzz(self):
        """
        User random_number is multiples of 3 and 5
        """
        user = UserFactory.build(random_number=15)
        return bizzfuzz(user) == 'BizzFuzz'

    def test_fuzz(self):
        """
        User random_number is multiples of 5 but not 3
        """
        user = UserFactory.build(random_number=25)
        return bizzfuzz(user) == 'Fuzz'

    def test_bizz(self):
        """
        User random_number is multiples of 3 but not 5
        """
        user = UserFactory.build(random_number=21)
        return bizzfuzz(user) == 'Bizz'

    def test_bizzfuzz_number(self):
        """
        User random_number is not multiples of 5 or 3
        """
        user = UserFactory.build(random_number=26)
        return bizzfuzz(user) == 26
