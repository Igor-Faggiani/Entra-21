from django.forms import ModelForm
from .models import Cluent

class ClientForm(ModelForm):
    class Meta:
        model = Cluent
        fields = ["name", "email", "cpf", "zipcode", "phone", "street", "city", "state", "enabled"]