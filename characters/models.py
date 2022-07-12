from django.db import models

class Location(models.Model):
    title = models.CharField(max_length=250)
    izmerenie = models.CharField(max_length=250)
    desc = models.TextField()
    img = models.ImageField(upload_to='location_rick_morti', blank=True, null=True)

    def __str__(self):
        return self.title

class Character(models.Model):
    male = 'ml'
    female = 'fl'
    genderless = 'gl'
    choices_live = [
        ('al', 'alive'),
        ('dd', 'dead'),
        ('un', 'unknown'),
    ]
    choices_gender = [
        ('ml' , 'male'),
        ('fm', 'female'),
        ('gl', 'genderless'),
        ('un', 'unknown'),
    ]

    img = models.ImageField(upload_to='Characters_rick_morti', blank=True, null=True)
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=250, choices=choices_live)
    desc = models.TextField()
    race = models.CharField(max_length=250)
    gender = models.CharField(max_length=250, choices=choices_gender)
    loc = models.ForeignKey(Location, on_delete=models.CASCADE)
    birth_loc = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location_birth')

    def __str__(self):
        return self.name

class Episode(models.Model):
    title = models.CharField(max_length=250)
    numb_episode = models.IntegerField(verbose_name='серия:')
    desc = models.TextField()
    characters = models.ManyToManyField(Character, blank=True, null=True)
    img = models.ImageField(upload_to='episode_rick_morty', blank=True, null=True)