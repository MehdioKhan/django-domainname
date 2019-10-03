from django import forms
from .validators import domain_name_validator


class DomainNameField(forms.CharField):
    description = 'Domain name form field'
    default_validators = [domain_name_validator, ]

    def __init__(self,  *args, **kwargs):
        super(DomainNameField, self).__init__(*args, **kwargs)
