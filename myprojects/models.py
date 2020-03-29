from django.db import models

# Create your models here.
class Program(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True, default='')
    description = models.TextField()
    owner = models.ForeignKey(
        'auth.User', related_name='programs', on_delete=models.CASCADE)
    highlighted = models.TextField()
    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
