from django.core.management import BaseCommand
from a_dataentry.models import Student

class Command(BaseCommand):
    help = "To add data to the database"

    def handle(self, *args, **kwargs):
        dataset = [
            {'no': 1001, 'name': 'Olayemi', 'age': 28},
            {'no': 1002, 'name': 'Opeyemi', 'age': 30},
            {'no': 1003, 'name': 'Victor', 'age': 29},
            {'no': 1004, 'name': 'Omotolani', 'age': 28},
        ]

        if not dataset:
            self.stdout.write(self.style.ERROR("❌ No data to add"))
            return

        for data in dataset:
            roll_no = data.get('no')  # ← Fix here
            if not Student.objects.filter(roll_no=roll_no).exists():
                Student.objects.create(
                    roll_no=roll_no,
                    name=data.get('name'),
                    age=data.get('age')
                )
                self.stdout.write(self.style.SUCCESS(f"✅ Added student: {roll_no}"))
            else:
                self.stdout.write(self.style.WARNING(f"⚠️ Student {roll_no} already exists"))

        self.stdout.write(self.style.SUCCESS("🎉 All done! Data processed successfully."))
