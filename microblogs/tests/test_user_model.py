from django.core.exceptions import ValidationError
from django.test import TestCase
from microblogs.models import User

class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.org',
            password='password123',
            bio='The quick brown fox jumps over the lazy dog.'
        )

    def test_valid_user(self):
        self._assert_user_is_valid()

# Username tests
    def test_username_cannot_be_blank(self):
        self.user.username = ''
        self._assert_user_is_invalid()

    def test_username_can_be_30_characters_long(self):
        self.user.username = '@' + 'x' * 29
        self._assert_user_is_valid()

    def test_username_cannot_be_over_30_characters_long(self):
        self.user.username = '@' + 'x' * 30
        self._assert_user_is_invalid()

    def test_username_must_be_unique(self):
        second_user = self.create_second_user()
        self.user.username = second_user.username
        self._assert_user_is_invalid()

    def test_username_must_start_with_at_symbol(self):
        self.user.username = 'johndoe'
        self._assert_user_is_invalid()

    def test_username_must_contain_only_alphanumericals_after_at(self):
        self.user.username = '@john!doe'
        self._assert_user_is_invalid()

    def test_username_must_contain_at_least_3_alphanumericals_after_at(self):
        self.user.username = '@jo'
        self._assert_user_is_invalid()

    def test_username_may_contain_numbers(self):
        self.user.username = '@j0hndoe2'
        self._assert_user_is_valid()

    def test_username_must_contain_only_1_at(self):
        self.user.username = '@@johndoe'
        self._assert_user_is_invalid()

# first_name tests
    def test_first_name_cannot_be_blank(self):
        self.user.first_name = ''
        self._assert_user_is_invalid()

    def test_first_name_need_not_be_unique(self):
        second_user = self.create_second_user()
        self.user.first_name = second_user.first_name
        self._assert_user_is_valid()

    def test_first_name_can_be_50_characters_long(self):
        self.user.first_name = 'x' * 50
        self._assert_user_is_valid()

    def test_first_name_cannot_be_over_50_characters_long(self):
        self.user.first_name = 'x' * 51
        self._assert_user_is_invalid()

# last_name tests
    def test_last_name_cannot_be_blank(self):
        self.user.last_name = ''
        self._assert_user_is_invalid()

    def test_last_name_need_not_be_unique(self):
        second_user = self.create_second_user()
        self.user.last_name = second_user.last_name
        self._assert_user_is_valid()

    def test_last_name_can_be_50_characters_long(self):
        self.user.last_name = 'x' * 50
        self._assert_user_is_valid()

    def test_last_name_can_be_over_50_characters_long(self):
        self.user.last_name = 'x' * 51
        self._assert_user_is_invalid()

# email test
    def test_email_must_be_unique(self):
        second_user = self.create_second_user()
        self.user.email = second_user.email
        self._assert_user_is_invalid()

    def test_email_must_have_only_1_at(self):
        self.user.email = 'johndoe@@example.org'
        self._assert_user_is_invalid()

    def test_email_must_have_username(self):
        self.user.email = '@example.org'
        self._assert_user_is_invalid()

    def test_email_must_have_domain_name(self):
        self.user.email = 'johndoe@.org'
        self._assert_user_is_invalid()

    def test_email_must_have_only_1_at(self):
        self.user.email = 'johndoe@example.'
        self._assert_user_is_invalid()

    def test_email_must_have_dot(self):
        self.user.email = 'johndoe@exampleorg'
        self._assert_user_is_invalid()

# bio tests
    def test_bio_can_be_blank(self):
        self.user.bio = ""
        self._assert_user_is_valid()

    def test_bio_can_be_520_characters_long(self):
        self.user.bio = 'x' * 520
        self._assert_user_is_valid()

    def test_bio_cannot_be_over_520_characters_long(self):
        self.user.bio = 'x' * 530
        self._assert_user_is_invalid()

    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except(ValidationError):
            self.fail('Test user should be valid.')

    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

    def create_second_user(self):
        user = User.objects.create_user(
            username='@janedoe',
            first_name='jane',
            last_name='Doe',
            email='janedoe@example.org',
            password='password123',
            bio='Hi, my name is Jane.'
        )
        return user
