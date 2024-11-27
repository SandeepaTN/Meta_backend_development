from django.db import models


# Create your models here.


# class Department(models.Model):
#     Department_name=models.CharField(max_length=150)


# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=150, unique=True)
#     password = models.CharField(max_length=150)
#     dept_id = models.ForeignKey(Department,on_delete=models.PROTECT,default=None)
#     salary=models.DecimalField(max_digits=7,decimal_places=2,default=1000)
#     joined_date=models.DateTimeField(default='2020-04-01')

# class College(models.Model):
#     CollegeID = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#     strength = models.IntegerField(auto_created=True)
#     website = models.URLField()


# class Principal(models.Model):
#     CollegeID = models.OneToOneField(College,on_delete=models.CASCADE)
#     Qualification = models.CharField(max_length=50)
#     email = models.EmailField(max_length=50)


# class Teacher(models.Model):
#     TeacherID = models.IntegerField(primary_key=True)
#     Qualification = models.CharField(max_length=50)
#     email = models.EmailField(max_length=50)


# class Subject(models.Model):
#     Subjectcode = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=30)
#     credits = models.IntegerField()
#     teacher=models.ManyToManyField(Teacher)


jobs = [("Developer", "Developer"), ("Tester", "Tester"),  # (value stored, wshown in page)
        ("DevOps engineer", "DevOps engineer")]

class Application(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(help_text="college mail",unique=True)
    password = models.CharField(max_length=200)
    passout_year = models.IntegerField()  # default True
    about = models.CharField(max_length=200)
    available_on = models.DateField()
    applying_to = models.CharField(max_length=200, choices=jobs)
    resume = models.FileField()
    class Meta:
        permissions=[('can_change_resume',"Can change resume")]

    def __str__(self):
        return f'{self.name},{self.applying_to}'