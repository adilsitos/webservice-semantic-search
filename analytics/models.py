from django.db import models

# Create your models here.
class Recommendation(models.Model):

    class Meta:
        db_table = "recommendation"
        verbose_name= "Recommendation"
        verbose_name_plural= "Recommendation"

    users_response = models.IntegerField(default=0, verbose_name="Response from users")
    searched_query = models.CharField(max_length=500, verbose_name="Query from the user")
    first = models.CharField(max_length=500, verbose_name="Highest recommendation")
    second = models.CharField(max_length=500, verbose_name="Second Highest recommendation")
    third = models.CharField(max_length=500, verbose_name="Third Highest recommendation")
