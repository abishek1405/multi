
from textwrap import fill
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser



class infor(models.Model):
    val = models.CharField(max_length=4000)

class pub(models.Model):
    Sno            = models.IntegerField()
    papertitle                  = models.CharField(max_length=254)
    Author                   = models.CharField(max_length =100 )
    Journal                   = models.CharField(max_length = 100)
    Indexed                   = models.CharField(max_length=12)
    Factor                = models.CharField(max_length=100)
    Poru               = models.CharField(max_length=100)
    ISSN                =models.CharField(max_length=100)
    yearofpub               = models.CharField(max_length=100)
    TypeofJournal      =  models.CharField(max_length=100)


class bookpub(models.Model):
    book            = models.CharField(max_length =  40)
    Author                  = models.CharField(max_length=254)
    isbn                   = models.CharField(max_length =100 )
    publisher                   = models.CharField(max_length = 200)
    mandy                   = models.CharField(max_length=12)
    bookwra                = models.FileField()
    fill                   = models.FileField()


class bookchappub(models.Model):
    paper            = models.CharField(max_length =  40)
    author                  = models.CharField(max_length=254)
    isbn                   = models.CharField(max_length =100 )
    mandy                   = models.CharField(max_length=12)
    publication                   = models.CharField(max_length = 200)
    certifi                = models.FileField()


class researarticcal(models.Model):
    paper            = models.CharField(max_length =  40)
    author                  = models.CharField(max_length=254)
    artical                   = models.CharField(max_length =100 )
    title                   = models.CharField(max_length =500 )
    mandy                   = models.CharField(max_length=12)
    pageno                   = models.IntegerField()
    certifi                = models.FileField()

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_lecturer = models.BooleanField(default=False)
    phone = models.CharField(max_length=60,blank=True, null=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    email = models.EmailField(blank=True,null=True)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    id_number = models.CharField(max_length=255)

    def __str__(self):
        return self.id_number
    # def get_absolute_url(self):
    #     return reverse('profile')
class Lecturar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=255)

    def __str__(self):
        return self.id_number

    # def get_absolute_url(self):
    #     return reverse('profile')
class CourseALlocation(models.Model):
    lecturer = models.ForeignKey(User,on_delete=models.CASCADE)






class worksphop(models.Model):
    infor = models.CharField(max_length=2000)

class facultyAttended(models.Model):
    FacultyName            = models.CharField(max_length =  40)
    event                  = models.CharField(max_length=100)
    Title                  = models.CharField(max_length = 100)
    Place                  = models.CharField(max_length =100 )
    fdatee                 = models.DateField()
    tdate                  = models.DateField()
    certificate            = models.FileField()



class Conference(models.Model):
    author                = models.CharField(max_length =  400)
    noc                   = models.CharField(max_length=100)
    venue                 = models.CharField(max_length = 200)
    organizer             = models.CharField(max_length =100 )
    dayy                   = models.CharField(max_length=14)
    isbn                  = models.IntegerField()
    page                  = models.IntegerField()
    proof                 = models.FileField()




class ddd(models.Model):
    FacultyName            = models.CharField(max_length =  40)
    
    Place                  = models.CharField(max_length =100 )
    Title                  = models.CharField(max_length = 100)
    Datee                  = models.CharField(max_length=12)
    parpose                = models.CharField(max_length=100)
    personone              = models.CharField(max_length=100)
    persontwo              = models.CharField(max_length=100)
    persontree             = models.CharField(max_length=100)
    nops                   = models.CharField(max_length=100)
    nopt                   = models.CharField(max_length=100)
    fil                    = models.FileField()
    Upload_Photo_file      = models.FileField()
    Attendance             = models.FileField()
    Report                 = models.FileField()



class place(models.Model):
    sno                    = models.IntegerField()
    pno                    = models.IntegerField()
    regno                  = models.IntegerField()
    name                   = models.CharField(max_length=120)
    dep                    = models.CharField(max_length=100)
    compdet                = models.CharField(max_length=500)
    fullad                 = models.CharField(max_length=300)
    datee                  = models.CharField(max_length=14)
    fil                    = models.FileField()
    Upload_Photo_file      = models.FileField()
    Attendance             = models.FileField()
    

class placesel(models.Model):
    regno                    = models.IntegerField()
    name                   = models.CharField(max_length=120)
    datee                  = models.CharField(max_length=14)
    dep                    = models.CharField(max_length=100)
    compdet                = models.CharField(max_length=500)
    annu                 = models.CharField(max_length=30)
    fil                    = models.FileField()
   
class studet(models.Model):
    regno                    = models.IntegerField()
    name                   = models.CharField(max_length=120)
    dep                    = models.CharField(max_length=100)
    blood                 = models.CharField(max_length=30)
    datee                  = models.CharField(max_length=14)
    phone                  = models.IntegerField()
    email                = models.CharField(max_length=500)
    yearof               = models.CharField(max_length=20)
   
       