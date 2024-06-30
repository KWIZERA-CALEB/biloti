from django.db import models

from headteacher.models import ClassDetail

# Create your models here.

# Student Model
class Student(models.Model):
    student_name = models.CharField(max_length=255)
    student_gender = models.CharField(max_length=255)
    student_avatar = models.ImageField(null=True, default="avatar.jpg") # use pillow for image handling
    student_grade = models.ForeignKey(ClassDetail, on_delete=models.SET_NULL, null=True)
    # student_id = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name


# not migrated models
# class Math(models.Model):
#     teacher_name = models.CharField()
#     subject_name = models.CharField(max_length=200)
#     class_work = models.CharField()
#     home_work = models.CharField()
#     exams = models.CharField()
#     total = models.CharField()
#     comment = models.CharField()
#     effort = models.CharField()
#     attitude = models.CharField()
#     # course_content =  # a list of content

# class Science(models.Model):
#     teacher_name = models.CharField()
#     subject_name = models.CharField(max_length=200)
#     class_work = models.CharField()
#     home_work = models.CharField()
#     exams = models.CharField()
#     total = models.CharField()
#     comment = models.CharField()
#     effort = models.CharField()
#     attitude = models.CharField()
#     # course_content =  # a list of content

# class Kinyarwanda(models.Model):
#     teacher_name = models.CharField()
#     subject_name = models.CharField(max_length=200)
#     class_work = models.CharField()
#     home_work = models.CharField()
#     exams = models.CharField()
#     total = models.CharField()
#     comment = models.CharField()
#     effort = models.CharField()
#     attitude = models.CharField()
#     # course_content =  # a list of content

# class ICT(models.Model):
#     teacher_name = models.CharField()
#     subject_name = models.CharField(max_length=200)
#     class_work = models.CharField()
#     home_work = models.CharField()
#     exams = models.CharField()
#     total = models.CharField()
#     comment = models.CharField()
#     effort = models.CharField()
#     attitude = models.CharField()
#     # course_content =  # a list of content

# class French(models.Model):
#     teacher_name = models.CharField()
#     subject_name = models.CharField(max_length=200)
#     class_work = models.CharField()
#     home_work = models.CharField()
#     exams = models.CharField()
#     total = models.CharField()
#     comment = models.CharField()
#     effort = models.CharField()
#     attitude = models.CharField()
#     # course_content =  # a list of content

# class Library(models.Model):
#     teacher_name = models.CharField()
#     subject_name = models.CharField(max_length=200)
#     class_work = models.CharField()
#     home_work = models.CharField()
#     exams = models.CharField()
#     total = models.CharField()
#     comment = models.CharField()
#     effort = models.CharField()
#     attitude = models.CharField()
#     # course_content =  # a list of content


# class Art(models.Model):
#     teacher_name = models.CharField()
#     subject_name = models.CharField(max_length=200)
#     class_work = models.CharField()
#     home_work = models.CharField()
#     exams = models.CharField()
#     total = models.CharField()
#     comment = models.CharField()
#     effort = models.CharField()
#     attitude = models.CharField()
#     # course_content =  # a list of content


# class Edm(models.Model):
#     teacher_name = models.CharField()
#     subject_name = models.CharField(max_length=200)
#     class_work = models.CharField()
#     home_work = models.CharField()
#     exams = models.CharField()
#     total = models.CharField()
#     comment = models.CharField()
#     effort = models.CharField()
#     attitude = models.CharField()
#     # course_content =  # a list of content

# class ClassTeachersComments(models.Model):
#     # usually 
#     # sometimes
#     # rarely
#     pass

# class SchoolReport(models.Model):
#     math = models.ForeignKey(Math, on_delete=models.CASCADE)
#     science = models.ForeignKey(Science, on_delete=models.CASCADE)
#     kinyarwanda = models.ForeignKey(Kinyarwanda, on_delete=models.CASCADE)
#     ict = models.ForeignKey(ICT, on_delete=models.CASCADE)
#     french = models.ForeignKey(French, on_delete=models.CASCADE)
#     library = models.ForeignKey(Library, on_delete=models.CASCADE)
#     art = models.ForeignKey(Art, on_delete=models.CASCADE)
#     edm = models.ForeignKey(Edm, on_delete=models.CASCADE)
#     main_comment = models.CharField()
#     total_marks = models.CharField()
#     days_attend = models.CharField()
#     days_absent = models.CharField()
#     days_late = models.CharField()
#     pe_non_suit = models.CharField()
    

