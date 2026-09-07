from django.db import models


class Household(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Roommate(models.Model):
    household = models.ForeignKey(
        Household, on_delete=models.CASCADE, related_name="roommates"
    )
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
