from django import forms
from .models import Product
import re


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        
        error_messages = {
            "comany_name": {
                "unique": "A Razão Social já existe.",
                "max_length": "O tamanho máximo da razão social é 255 caracteres."
            }
        }
        
        # clean_<nome_campo>
    def clean_cnpj(self):
            # Obtendo o valor que foi digitado no formulário
            cnpj = self.cleaned_data.get("cnpj", "")
            
            #removendo valores não numericos
            cnpj = re.sub("[^0-9]", "", cnpj)
            
            return cnpj
        
        
    def clean_phone(self):
            phone = self.cleaned_data.get("phone", "")
            
            #removendo valores não numericos
            phone = re.sub("[^0-9]", "", phone)
            
            return phone
        
        
    def clean_zipcode(self):
            zipcode = self.cleaned_data.get("zipcode", "")
            
            #removendo valores não numericos
            phone = re.sub("[^0-9]", "", zipcode)
            
            return phone