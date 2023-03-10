from django.db import models


class Diplome(models.Model) :
    nomDiplome=models.CharField(max_length=25)
    lieuDiplome=models.CharField(max_length=25)
    dateDiplome=models.DateField()
    gen= models.ForeignKey('Genre', on_delete=models.CASCADE,)
    def __str__(self) -> str:
        return self.nomDiplome

class Stage(models.Model) :
    natureStage=models.CharField(max_length=20)
    lieuStage=models.CharField(max_length=20)
    dureeStage=models.IntegerField()

class Competence(models.Model) :
    nomCompetence=models.CharField(max_length=25)
    niveauCompetence=models.IntegerField()
    genre=models.CharField(max_length=25)

class Genre(models.Model) :
    nomGenre = models.TextField()
    descriptionGenre = models.TextField()
    def __str__(self) -> str:
        return self.nomGenre

