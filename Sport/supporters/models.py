from django.db import models

# Create your models here.

class Adresse(models.Model):
    id_adresse = models.AutoField(primary_key=True)
    rue = models.CharField(max_length=50)
    num_rue = models.IntegerField()
    ville = models.CharField(max_length=50)
    code_postal = models.IntegerField()
    pays = models.CharField(max_length=50)

# table intermidiaire 

class Equipe(models.Model):
    id_equipe = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)


class Stade(models.Model):
    id_stade = models.AutoField(primary_key=True)
    nom_stade = models.CharField(max_length=50)
    capacite = models.IntegerField()
    adresse = models.OneToOneField(Adresse, on_delete=models.CASCADE)

class Game(models.Model):
    id_match = models.AutoField(primary_key=True)
    date_match = models.DateTimeField()
    stade = models.ForeignKey(Stade, on_delete=models.CASCADE)
    equipe_away = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='equipe_away_id')
    equipe_home = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name='equipe_home_id')

class Ticket(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    type_ticket = models.CharField(max_length=50)
    emplacement = models.CharField(max_length=50)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    match = models.ForeignKey(Game, on_delete=models.CASCADE)


class Acces(models.Model):
    id_acces = models.AutoField(primary_key=True)
    zone_acces = models.CharField(max_length=50)
    description = models.TextField()


class Supporter(models.Model):
    id_supporter = models.AutoField(primary_key=True)
    cin = models.IntegerField()
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=50)
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    stade = models.ForeignKey(Stade, on_delete=models.CASCADE)
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    acces = models.ForeignKey(Acces, on_delete=models.CASCADE, default=None) # Ajout de la clé étrangère





