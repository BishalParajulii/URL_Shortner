from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


# Create your models here.
class ShortUrl(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='urls')
    original_url = models.URLField()
    short_code = models.CharField(max_length=20 , unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.PositiveBigIntegerField(default=0)
    expires_at = models.DateTimeField()
    
    def save(self, *args , **kwargs):
        if not self.pk:
            self.expires_at = timezone.now() + timedelta(minutes=5)
        super().save(*args , **kwargs)
    
    def is_expired(self):
        return timezone.now() > self.expires_at
    
    def __str__(self):
        return self.short_code