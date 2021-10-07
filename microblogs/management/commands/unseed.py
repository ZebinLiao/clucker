from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from microblogs.models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        user_set = User.objects.all()
        for i in user_set.iterator():
            if(i.is_superuser == False):
                i.delete()
