from django.db import models
class Event(models.Model):
    CATEGORY_CHOICES = [
        ('Seminar', 'Seminar'),
        ('Workshop', 'Workshop'),
        ('Cultural', 'Cultural Feast'),
        ('Concert', 'Concert'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Seminar')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

