from django.test import TestCase
from .models import DomainExample
from django.db import transaction
from django.core.exceptions import ValidationError


class DomainFieldTestCase(TestCase):
    def setUp(self):
        self.valid_domain = 'domain.net'
        self.invalid_domain = 'domain.net/some_stuff'
        self.objects = DomainExample.objects

    def test_insert_valid_domain(self):
        obj = DomainExample(domain=self.valid_domain)
        obj.save()
        self.assertEquals(obj.domain, self.valid_domain)
        self.assertEquals(obj, self.objects.get(domain=self.valid_domain))
        self.assertEquals(self.objects.count(), 1)

    def test_insert_invalid_domain(self):
        with transaction.atomic():
            obj = DomainExample()
            with self.assertRaises(ValidationError):
                obj.domain = self.invalid_domain
                obj.save()
        self.assertEquals(self.objects.count(), 0)
