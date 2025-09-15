import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Crea un superusuario si no existe, usando DJANGO_SUPERUSER_*."

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")
        if not all([username, email, password]):
            self.stdout.write(self.style.ERROR("Faltan DJANGO_SUPERUSER_USERNAME/EMAIL/PASSWORD"))
            return
        if User.objects.filter(username=username).exists():
            self.stdout.write("Superusuario ya existe; no se crea de nuevo.")
            return
        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f"Superusuario '{username}' creado."))
