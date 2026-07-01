from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='gallery/')
    client = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Order in which gallery items appear (0-11 for 12 items)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order']
        verbose_name_plural = 'Gallery Items'

    def __str__(self):
        return f"{self.title} - {self.client}"
