from django.db import models

class Project(models.Model):
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('ongoing', 'Ongoing'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    client = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    number = models.CharField(max_length=10, help_text="e.g., 01, 02, OG1, OG2")
    badge_color = models.CharField(
        max_length=50,
        default='bg-blue-soft',
        help_text="CSS class for badge color (bg-blue-soft, bg-orange-soft, bg-green-soft, badge-purple)"
    )
    text_color = models.CharField(
        max_length=50,
        default='text-blue',
        help_text="CSS class for text color (text-blue, text-orange, text-green)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['number']
        verbose_name_plural = 'Projects'

    def __str__(self):
        return f"{self.number} - {self.title}"
