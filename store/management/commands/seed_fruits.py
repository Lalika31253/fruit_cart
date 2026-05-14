from django.core.management.base import BaseCommand
from store.models import Fruit

class Command(BaseCommand):
    help = "Seed initial fruits into database"

    def handle(self, *args, **kwargs):
        fruits = [
            {"name": "Apple", "weight_kg": 0.2, "price_per_kg": 2.0},
            {"name": "Banana", "weight_kg": 0.15, "price_per_kg": 1.2},
            {"name": "Orange", "weight_kg": 0.25, "price_per_kg": 1.8},
            {"name": "Mango", "weight_kg": 1.5, "price_per_kg": 3.5},
            {"name": "Grape", "weight_kg": 0.5, "price_per_kg": 3.0},
            {"name": "Pomelo", "weight_kg": 1.5, "price_per_kg": 2.0},
            {"name": "Mandarins", "weight_kg": 0.5, "price_per_kg": 4.0},
            {"name": "Apricot", "weight_kg": 1.5, "price_per_kg": 7.0},
        ]

        for fruit in fruits:
            obj, created = Fruit.objects.get_or_create(
                name=fruit["name"],
                defaults=fruit
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created {obj.name}"))
            else:
                self.stdout.write(f"{obj.name} already exists")

        self.stdout.write(self.style.SUCCESS("Seeding complete!"))