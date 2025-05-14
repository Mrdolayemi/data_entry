from django.core.management import BaseCommand
from django.apps import apps
import csv

# Proposed command - python manage.py importdata file_ path and model name
class Command(BaseCommand):
    help = "To add data to the database"
    
    def add_arguments(self, parser):
        parser.add_argument("filepath", type=str, help="import file from CSV")
        parser.add_argument("model_name", type=str, help="Dynamically adding model names")
        
    def handle(self, *args, **kwargs):
        filepath = kwargs.get("filepath")
        model_name = kwargs.get("model_name").capitalize()
    
        
        
        try:
            Model = apps.get_model("a_dataentry", model_name)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Could not load model {model_name}"))
                
        try:
            with open(filepath, 'r') as file:
                dataset = csv.DictReader(file)
                count = 0
                for data in dataset:
                    roll_no = data.get('roll_no', "").strip()
                         
                    if not Model.objects.filter(roll_no=roll_no).exists():
                        Model.objects.create(**data)
                        self.stdout.write(self.style.SUCCESS(f"✅ Added {model_name}: {roll_no}"))
                        count +=1
                    else:
                        self.stdout.write(self.style.WARNING(f"⚠️ {model_name} {roll_no} already exists"))       
                self.stdout.write(self.style.SUCCESS(f"🎉 All done! {count} Data processed successfully."))
        except FileNotFoundError:
                self.stdout.write(self.style.ERROR("❌ File Not Found"))
            