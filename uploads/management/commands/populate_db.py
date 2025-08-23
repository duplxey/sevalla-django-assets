import os
import shutil

from django.contrib.auth.models import User
from django.core.files import File
from django.core.management import BaseCommand

from core import settings
from uploads.models import Upload

DEMO_UPLOADS_PATH = settings.BASE_DIR / "static" / "demo"


class Command(BaseCommand):
    help = "Creates a superuser and a few demo uploads"

    def __init__(self, stdout=None, stderr=None, no_color=False, force_color=False):
        super().__init__(stdout, stderr, no_color, force_color)

    def handle(self, *args, **kwargs):
        self.stdout.write("Started the database population process...")
        self.create_superuser()
        self.create_demo_uploads()
        self.stdout.write(self.style.SUCCESS("Successfully populated the database."))

    def create_superuser(self):
        self.stdout.write(self.style.SUCCESS("Creating superuser..."))

        # Create the superuser if it doesn't exist
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                password="password",
            )

        self.stdout.write(self.style.SUCCESS("Successfully created the superuser."))

    def create_demo_uploads(self):
        self.stdout.write(
            self.style.SUCCESS("Clearing media files & creating demo uploads...")
        )

        # Clear media files
        if os.path.exists(settings.MEDIA_ROOT):
            shutil.rmtree(settings.MEDIA_ROOT)

        # Create demo uploads
        for filename in os.listdir(DEMO_UPLOADS_PATH):
            file_path = DEMO_UPLOADS_PATH / filename
            with open(file_path, "rb") as f:
                Upload.objects.create(file=File(f, name=filename))

        self.stdout.write(self.style.SUCCESS("Successfully created the demo uploads."))
