from django.db import models


# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=200)
    flag = models.ImageField(
        upload_to="images/flags/",
        default="images/flags/default.png",
        blank=True,
        null=True,
    )
    recorded_by = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.country_name

    class Meta:
        ordering = ("country_name",)
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class Goal(models.Model):
    goal_number = models.CharField(max_length=200)
    goal_name = models.CharField(max_length=200)
    goal_country = models.ForeignKey("Country", on_delete=models.CASCADE)
    recorded_by = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.goal_name

    class Meta:
        ordering = ("id",)
        verbose_name = "Goal"
        verbose_name_plural = "Goals"


class Indicator(models.Model):
    indicator_name = models.CharField(max_length=500)
    indicator_description = models.TextField(null=True, blank=True)
    indicator_goal = models.ForeignKey("Goal", on_delete=models.CASCADE)
    long_term_objective = models.TextField(null=True, blank=True)
    recorded_by = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.indicator_name

    class Meta:
        ordering = ("id",)
        verbose_name = "Indicator"
        verbose_name_plural = "Indicators"


class Performance(models.Model):
    indicator_id = models.ForeignKey("Indicator", on_delete=models.CASCADE)
    year = models.IntegerField()
    value = models.FloatField()
    reference = models.TextField()
    source = models.CharField(max_length=200)
    recorded_by = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.indicator_id.indicator_name + " " + str(self.year)

    class Meta:
        ordering = ("indicator_id", "year")
        verbose_name = "Performance"
        verbose_name_plural = "Performances"
        unique_together = ("indicator_id", "year")
