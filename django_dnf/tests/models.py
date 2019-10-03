"""
A model for testing
"""
from django.db import models
from django_dnf.fields import DomainNameField


class DomainExample(models.Model):
    domain = DomainNameField(blank=True)

    def __unicode__(self):
        return "%s" % self.domain
