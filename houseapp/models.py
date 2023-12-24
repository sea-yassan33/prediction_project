from django.db import models
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator

class HouseModel(models.Model):
	testfile = models.FileField(validators=[FileExtensionValidator(['csv'])])
	area = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999)])
	distance = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(99999)])
