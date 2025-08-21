import random
import string

from django.core.validators import FileExtensionValidator
from django.db import models

from uploads.validators import FileSizeValidator

ALLOWED_FILE_EXTENSIONS = ["jpg", "jpeg", "png", "gif", "pdf", "docx", "txt"]


def generate_random_slug():
    return "".join(random.choices(string.ascii_letters + string.digits, k=16)).lower()


class Upload(models.Model):
    slug = models.SlugField(max_length=16, unique=True, default=generate_random_slug)
    file = models.FileField(
        validators=[
            FileExtensionValidator(allowed_extensions=ALLOWED_FILE_EXTENSIONS),
            FileSizeValidator(max_mb=5),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]
