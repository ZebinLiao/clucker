from django.core.exceptions import ValidationError
from django.test import TestCase
from microblogs.models import User
from microblogs.forms import PostForm
from django import forms

class PostFormTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            '@johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.org',
            password='password123',
            bio='The quick brown fox jumps over the lazy dog.'
        )
        self.form_input = {
            'author': self.user,
            'text':'Hello my name is John.'
        }

    def test_valid_post_form(self):
        form = PostForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_has_necessary_fields(self):
        form = PostForm()
        self.assertIn('text', form.fields)
