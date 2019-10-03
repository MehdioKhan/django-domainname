django-domainname
===============
django-dominname is a simple django app including a model field and a form field to deal with Domain names.

Getting Started
===============
1.Clone project and install it:

      git clone https://github.com/MehdioKhan/django-domainname
      cd djanago-domainname
      python setup.py install

2.Add django_dnf to installed list in settings file:
      
      INSTALLED_APPS = [
        ...
        'django_dnf',
      ]

3.Use DomainNameField in your models and forms:

models.py

      from django.db import models
      from django_dnf.fields import DomainNameField
      
      class MyModel(models.Model):
        doamin = DomainNameField(blank=True)
        ...
        
forms.py
      
      from django import forms
      from django_dnf.formfields import DomainNameField
      
      class MyForm(forms.Form):
        doamin = DomainNameField(blank=True)
        ...
