from django.db import models

class game(models.Model):
    difficulty_level = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard')
    ]
    user_input = models.IntegerField()
    difficulty = models.CharField(max_length=10, choices=difficulty_level, default='Easy')
    attempts = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_input)