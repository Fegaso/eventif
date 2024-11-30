from django.db import models


class Contacts(models.Model):
    name = models.CharField('nome', max_length=100)

    email = models.EmailField('e-mail')

    phone = models.CharField('telefone', max_length=20)

    message = models.CharField('message', max_length=900)

    created_at = models.DateTimeField('criado em', auto_now_add=True)


    class Meta:
        verbose_name_plural = 'contactar'

        verbose_name = 'contactar'
        
        ordering = ('-created_at',)

    def __str__(self):
        return self.name