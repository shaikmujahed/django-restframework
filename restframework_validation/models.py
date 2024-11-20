from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
                _("%(value)s is not an even number"),
                params={"value":value},
                )
        return {"msg":f'{value} is even number.'}

class Number(models.Model):
    even_field = models.IntegerField(validators=[validate_even])
    

    



    
