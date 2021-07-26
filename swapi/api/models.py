from django.db import models

class Planet(models.Model):
    created = models.CharField(max_length=100)
    modified = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    rotation_period = models.CharField(max_length=100)
    orbital_period = models.CharField(max_length=100)
    diameter = models.CharField(max_length=100)
    climate = models.CharField(max_length=100)
    gravity = models.CharField(max_length=100)
    terrain = models.CharField(max_length=100)
    surface_water = models.CharField(max_length=100)
    population = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class People(models.Model):
    created =  models.CharField(max_length=100, null=True, blank=True)
    modified =  models.CharField(max_length=100, null=True, blank=True)
    name =  models.CharField(max_length=100, null=True, blank=True)
    height =  models.CharField(max_length=100, null=True, blank=True)
    mass =  models.CharField(max_length=100, null=True, blank=True)
    hair_color =  models.CharField(max_length=100, null=True, blank=True)
    skin_color =  models.CharField(max_length=100, null=True, blank=True)
    eye_color =  models.CharField(max_length=100, null=True, blank=True)
    birth_year =  models.CharField(max_length=100, null=True, blank=True)
    gender =  models.CharField(max_length=50, null=True, blank=True)
    homeworld = models.ForeignKey(Planet,on_delete=models.CASCADE, related_name='residents')

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Producer(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Film(models.Model):
    created =  models.CharField(max_length=100)
    modified =  models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    episode_id = models.IntegerField()
    opening_crawl = models.TextField(max_length=1000)
    director  = models.ManyToManyField(
        Director,
        related_name="films",
        blank=True
    ),
    producer = models.ManyToManyField(
        Producer,
        related_name="films",
        blank=True
    ),
    release_date = models.DateField()
    characters = models.ManyToManyField(
        People,
        related_name="films",
        blank=True
    )
    planets = models.ManyToManyField(
        Planet,
        related_name="films",
        blank=True
    )

    def __str__(self):
        return self.title

