from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    attachment = models.FileField(
        upload_to='attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
