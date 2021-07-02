from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
import json

class Content(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    text = models.TextField(blank=True)
    author = models.CharField(max_length=255, blank=True)
    posted_on = models.DateTimeField(blank=True)
    keywords = models.CharField(max_length=255, blank=True)
    names = models.CharField(max_length=255, blank=True)
    organization = models.CharField(max_length=255, blank=True)
    dates = models.CharField(max_length=255, blank=True)
    products = models.CharField(max_length=255, blank=True)
    countries = models.CharField(max_length=255, blank=True)
    locations = models.CharField(max_length=255, blank=True)
    money = models.CharField(max_length=255, blank=True)
    percentile = models.CharField(max_length=255, blank=True)
    summary = models.TextField(blank=True)

    def set_author(self, x):
        self.author = json.dumps(x)

    def get_author(self):
        return json.loads(self.author)

    def set_keywords(self, x):
        self.author = json.dumps(x)

    def get_keywords(self):
        return json.loads(self.keywords)

    def set_names(self, x):
        self.names = json.dumps(x)

    def get_names(self):
        return json.loads(self.names)
    
    def set_organization(self, x):
        self.organization = json.dumps(x)

    def get_organization(self):
        return json.loads(self.organization)

    def set_dates(self, x):
        self.organization = json.dumps(x)

    def get_dates(self):
        return json.loads(self.dates)
    
    def set_products(self, x):
        self.organization = json.dumps(x)

    def get_products(self):
        return json.loads(self.products)
    
    def set_countries(self, x):
        self.countries = json.dumps(x)

    def get_countries(self):
        return json.loads(self.countries)
    
    def set_locations(self, x):
        self.locations = json.dumps(x)

    def get_locations(self):
        return json.loads(self.locations)
    
    def set_money(self, x):
        self.locations = json.dumps(x)

    def get_money(self):
        return json.loads(self.money)
    
    def set_percentile(self, x):
        self.percentile = json.dumps(x)

    def get_percentile(self):
        return json.loads(self.percentile)
    
    def get_absolute_url(self):
        return reverse('content_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Content, self).save(*args, **kwargs)