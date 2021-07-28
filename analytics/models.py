from django.db import models

# Create your models here.
class Recommendation(models.Model):

    class Meta:
        db_table = "recommendation"
        verbose_name= "Recommendation"
        verbose_name_plural= "Recommendation"

    users_response = models.IntegerField(default=0, verbose_name="Response from users", null=False)
    searched_query = models.CharField(max_length=500, verbose_name="Query from the user", null=True)
    first = models.CharField(max_length=500, verbose_name="Highest recommendation", null=True)
    first_score = models.FloatField(null=True)
    second = models.CharField(max_length=500, verbose_name="Second Highest recommendation", null=True)
    second_score = models.FloatField(null=True)
    third = models.CharField(max_length=500, verbose_name="Third Highest recommendation", null=True)
    third_score = models.FloatField(null=True)