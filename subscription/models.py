from django.db import models
from django.utils.translation import ugettext_lazy as _

class Subscription(models.Model):
    name = models.CharField(_('nome'), max_length=100)
    cpf = models.CharField(_('CPF'), max_length=11, unique=True)
    email = models.EmailField(_('email'), unique=True)
    phone = models.CharField(_('telefone'), max_length=20, blank=True)
    created_at = models.DateTimeField(_('criado em'), auto_now_add=True)
    paid = models.BooleanField('Pago')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'inscricao')
        verbose_name_plural = _(u'inscricoes')