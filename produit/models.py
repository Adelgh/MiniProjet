from django.db import models
from django.contrib.auth.models import Permission, User
import datetime

class Boutique(models.Model):
    name = models.CharField(max_length=250)
    user = models.ForeignKey(User, default=1)
    logo = models.FileField(max_length=250)

    def __str__(self):
        return self.name

now = datetime.datetime.now()

def group_based_upload_to(instance, filename):
    return "image//media/ali/{}/{}".format(instance.boutique.name, filename)
def group_based_upload_to_seconder(instance, filename):
    return "image//media/ali/secondaire/{}/{}".format(instance.boutique.name, filename)
class Image(models.Model):
    image1 = models.ImageField(upload_to=group_based_upload_to_seconder, default=None)
    image2 = models.ImageField(upload_to=group_based_upload_to_seconder, default=None)
    image3 = models.ImageField(upload_to=group_based_upload_to_seconder, default=None)

class Produit(models.Model):
    etat_choix = (('active', 'active'),('desactive','desactive'),)
    user = models.ForeignKey(User, default=1)
    choix_categorie = (('bijoux', 'bijoux'), ('maison et ameublement', 'maison et ameublement'), ('vetements', 'vetements'),('art et collections', 'art et collections'),('accessoires', 'accessoires'),('sacs et bagages', 'sacs et bagages'),('mariage', 'mariage'),)
    prix = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    type = models.CharField(max_length=250, default=None)
    etat = models.CharField(max_length=250, choices=etat_choix, default="desactive" )
    descreption = models.CharField(max_length=250)
    boutique = models.ForeignKey(Boutique, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to=group_based_upload_to)
    image1 = models.ImageField(upload_to=group_based_upload_to_seconder, default=None)
    image2 = models.ImageField(upload_to=group_based_upload_to_seconder, default=None)
    image3 = models.ImageField(upload_to=group_based_upload_to_seconder, default=None)
    categorie = models.CharField(max_length=250, choices=choix_categorie, default="bijoux")
    is_favorite = models.BooleanField(default=False)
    is_smile = models.BooleanField(default=False)





    def __str__(self):
        return self.title+' - ' +self.prix

    def __str__(self):  # __unicode__ on Python 2
        return self.title

    class Meta:
        ordering = ('title',)

