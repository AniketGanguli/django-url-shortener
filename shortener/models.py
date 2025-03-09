from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.utils.timezone import now
from datetime import timedelta

class ShortenedURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=15, unique=True)  # Allow custom short codes
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)  # Optional expiration
    click_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        """Ensure unique short code and set expiration date if needed."""
        if not self.short_code:
            self.short_code = self.generate_unique_code()
        if not self.expires_at:
            self.expires_at = now() + timedelta(days=30)  # Default: Expires in 30 days
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        """Generate a unique short code."""
        while True:
            code = get_random_string(6)  # Generates a random 6-character code
            if not ShortenedURL.objects.filter(short_code=code).exists():
                return code

    def is_expired(self):
        """Check if the shortened URL has expired."""
        return self.expires_at and now() > self.expires_at

    def __str__(self):
        return f"{self.short_code} → {self.original_url}"
