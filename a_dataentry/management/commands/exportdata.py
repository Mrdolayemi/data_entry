from django.core.management.base import BaseCommand
from django.apps import apps
import csv
import os

class Command(BaseCommand):
    help = "Export data from a model in a_dataentry app to a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("model_name", type=str, help="Name of the model to export (e.g., Teacher)")

    def handle(self, *args, **kwargs):
        model_name = kwargs.get("model_name")
        app_label = "a_dataentry"

        try:
            Model = apps.get_model(app_label, model_name)
            if not Model:
                self.stdout.write(self.style.ERROR(f"Model '{model_name}' not found in app '{app_label}'"))
                return
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error loading model: {str(e)}"))
            return

        # Define file path
        filename = f"{model_name.lower()}.csv"
        filepath = os.path.join(os.getcwd(), filename)

        try:
            queryset = Model.objects.all()
            if not queryset.exists():
                self.stdout.write(self.style.WARNING("No data found in the model."))
                return

            # Get all field names dynamically
            fieldnames = [field.name for field in Model._meta.fields]

            with open(filepath, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(fieldnames)

                for obj in queryset:
                    row = [getattr(obj, field) for field in fieldnames]
                    writer.writerow(row)

            self.stdout.write(self.style.SUCCESS(f"Data exported to {filename} successfully."))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred during export: {str(e)}"))
