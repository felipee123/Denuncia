from django.db import models
import uuid

class Denuncia(models.Model):
    CATEGORY_CHOICES = [
        ('vulnerability', 'Vulnerabilidade'),
        ('data_breach', 'Vazamento de dados'),
        ('other', 'Outro'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pendente'),
        ('in_progress', 'Em analise'),
        ('resolved', 'Resolvido'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_anonymous = models.BooleanField(default=True)
    reporter_email = models.EmailField(blank=True, null=True)
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title