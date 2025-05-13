from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Gretting Command"
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Add name")
        
        
    def handle(self, *args, **kwargs):
        # write the logic
        name = kwargs['name']
        greeting = f'Hi {name}, Good Morning!'
        self.stdout.write(self.style.SUCCESS(greeting))