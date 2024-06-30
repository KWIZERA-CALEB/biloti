from django.db import models

# Create your models here.
class ClassDetail(models.Model):
    # class teacher
    class_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.class_name
    
class SchoolYear(models.Model):
    year_name = models.CharField(max_length=255)
    started = models.DateTimeField(auto_now_add=True)
    # terms

    def __str__(self):
        return self.year_name


class SchoolTerm(models.Model):
    term_name = models.CharField(max_length=255)
    term_year_link = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)

    def __str__(self):
        return self.term_name