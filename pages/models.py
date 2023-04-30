from django.db import models
<<<<<<< HEAD

# Create your models here.


=======
from precise_bbcode.fields import BBCodeTextField
from django.utils.translation import gettext_lazy as _
# Create your models here.

class BbCodeModel(models.Model):
    name = models.CharField(verbose_name=_('Название'), max_length=255)
    bbcode = BBCodeTextField(verbose_name=_('Содержание'), blank = True, null=True)
>>>>>>> b755f87e829ee1b394a3d1c7a5ae764b906e867e
