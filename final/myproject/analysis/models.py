# Create your models here.
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class BusinessDetail(models.Model):
    ACCOUNT_STATES = ((0, 'active'), (1, 'closed'))
    account_state = models.CharField(("Account_state"), max_length=90)
    account_id = models.FloatField()
    activated_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateField(blank=True, null=True)
    current_period_started_at = models.DateTimeField(blank=True, null=True)
    current_period_ends_at = models.DateTimeField(blank=True, null=True)
    plan_name = models.CharField(max_length=256, null=True, blank=True)
    business_id = models.IntegerField(null=True, blank=True)
    enterprise_id = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField()
    category_id = models.IntegerField()
    parent_category_name = models.CharField(("Parent Category Name"), max_length=256)
    count = models.IntegerField()
    avg_monthly_rating = models.FloatField()

    def __unicode__(self):
        return "%s " % (str(self.account_id))
