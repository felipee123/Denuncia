from django.db import models # type: ignore

class Denuncia(models.Model):
    ANONIMA = 'AN'
    IDENTIFICADA = 'ID'
    TIPOS_REPORTE = [
        (ANONIMA, 'Anônima'),
        (IDENTIFICADA, 'Identificada'),
    ]

    tipo_reporte = models.CharField(
        max_length=2,
        choices=TIPOS_REPORTE,
        default=ANONIMA
    )
    nome = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    arquivo_anexo = models.FileField(upload_to='anexos/', blank=True, null=True)

    def __str__(self):
        return f"Denúncia #{self.id} - {self.tipo_reporte}"
