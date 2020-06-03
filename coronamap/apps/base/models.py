from django.db import models


class Entry(models.Model):

    date_reported = models.DateField(auto_now=False, auto_now_add=False)
    country_code = models.CharField(max_length=10)
    country = models.CharField(max_length=255)
    who_region = models.CharField(max_length=255)
    new_cases = models.IntegerField()
    cumulative_cases = models.IntegerField()
    new_deaths = models.IntegerField()
    cumulative_deaths = models.IntegerField()
