from django.core.exceptions import ValidationError


class FileSizeValidator:
    """
    Validator for checking the maximum file size in MB.
    """

    def __init__(self, max_mb=5):
        self.max_mb = max_mb
        self.max_bytes = max_mb * 1024 * 1024

    def __call__(self, file):
        if file.size > self.max_bytes:
            raise ValidationError(
                f"File size must be under {self.max_mb} MB. "
                f"Current file size is {(file.size / (1024 * 1024)):.2f} MB."
            )

    def __eq__(self, other):
        return isinstance(other, FileSizeValidator) and self.max_mb == other.max_mb

    def deconstruct(self):
        return (
            f"{self.__class__.__module__}.{self.__class__.__qualname__}",
            [],
            {"max_mb": self.max_mb},
        )
