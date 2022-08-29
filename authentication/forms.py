
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.models import User as U
from django.db import transaction
from authentication.models import Student,Lecturar,bookpub,researarticcal,bookchappub
from authentication.models import  worksphop
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

# Create your models here.
class worksphopform(forms.ModelForm):
    class Meta:
        model = worksphop
        fields = '__all__'

class bookpubform(forms.Form):
    book                    = forms.CharField(label="book",max_length =  40)
    Author                  = forms.CharField(label="Author",max_length=254)
    isbn                    = forms.CharField(label="isbn",max_length =100 )
    publisher               = forms.CharField(label="publisher",max_length = 200)
    mandy                   = forms.CharField(label="mandy",max_length=12)
    bookwra                 = forms.FileField(label="bookwra")
    fill                    = forms.FileField(label="fill")


class inforform(forms.Form):
    val = forms.CharField(max_length=4000)

class bookchappubform(forms.Form):
    paper                  = forms.CharField(label="paper",max_length =  40)
    author                 = forms.CharField(label="author",max_length=254)
    isbn                   = forms.CharField(label="isbn",max_length =100 )
    mandy                  = forms.CharField(label="mandy",max_length=12)
    publication            = forms.CharField(label="publication",max_length = 200)
    certifi                = forms.FileField(label="certifi",)

class placeselform(forms.Form):
    regno                  = forms.IntegerField(label="regno")
    name                   = forms.CharField(label="name",max_length=120)
    datee                  = forms.CharField(label="datee",max_length=14)
    dep                    = forms.CharField(label="dep",max_length=100)
    compdet                = forms.CharField(label="compdet",max_length=500)
    annu                   = forms.CharField(label="annu",max_length=30)
    fil                    = forms.FileField(label="fil")


class studetform(forms.Form):
    regno                  = forms.IntegerField()
    name                   = forms.CharField(max_length=120)
    dep                    = forms.CharField(max_length=100)
    blood                  = forms.CharField(max_length=30)
    datee                  = forms.CharField(max_length=14)
    phone                  = forms.IntegerField()
    email                  = forms.CharField(max_length=500)
    yearof               = forms.CharField(max_length=20)
   

class researarticcalform(forms.Form):
    paper            = forms.CharField(label="paper",max_length =  40)
    author           = forms.CharField(label="author",max_length=254)
    artical          = forms.CharField(label="artical",max_length =100 )
    title                    = forms.CharField(label="title", max_length=100)
    mandy            = forms.CharField(label="mandy",max_length=12)
    pageno        = forms.IntegerField(label="pageno")

    certifi          = forms.FileField(label="certifi")

class pubform(forms.Form):
    Sno                  = forms.IntegerField(label= 'Sno          '   )
    papertitle       =    forms.CharField(label=     'papertitle   ' ,max_length=500  )
    Author             = forms.CharField(label=      'Author       '   ,max_length=100)
    Journal             = forms.CharField(label=     'Journal      '   ,max_length=500)
    Indexed            = forms.CharField(label=      'Indexed      '  ,max_length=500)
    Factor             = forms.CharField(label=     'Factor       '  ,max_length=500)
    Poru                  =forms.CharField(label =   'Poru         '   ,max_length=500)
    ISSN                  =forms.CharField(label =   'ISSN         '   ,max_length=500)
    yearofpub             =forms.CharField(label =   'yearofpub    '  )
    TypeofJournal         =forms.CharField(label= 'TypeofJournal'  ,max_length=500)

class Conferenceform(forms.Form):
    author                = forms.CharField(label='author',max_length =  400)
    noc                   = forms.CharField(label='noc',max_length=100)
    venue                 = forms.CharField(label='venue',max_length = 200)
    organizer             = forms.CharField(label='organizer',max_length =100 )
    day                   = forms.DateField(   label = 'day')
    isbn                  = forms.IntegerField(label = 'isbn')
    page                  = forms.IntegerField(label = 'page')
    proof                 = forms.FileField(   label = 'proof')

class staf(forms.Form):
    FacultyName = forms.CharField(label= 'FacultyName', max_length=100)
    Place = str(forms.CharField(label='Place'))
    Title            = forms.CharField(label='Title',max_length=100)
    Datee             = forms.CharField(label='Datee',max_length=100)
    parpose          = forms.CharField(label='parpose',max_length=100)
    
    personone           =forms.CharField(label = 'personone',max_length=100)
    persontwo           =forms.CharField(label = 'personone',max_length=100)
    persontree          =forms.CharField(label = 'personone',max_length=100)
    nops                =forms.IntegerField(label='nops')
    nopt                =forms.IntegerField(label='nopt')
    fil              = forms.FileField(label='fil')
    Upload_Photo_file= forms.FileField(label='Upload_Photo_file')
    Attendance =forms.FileField(label='Attendance')
    Report    =forms.FileField(label='Report')

class facultyAttendedform(forms.Form):
    FacultyName  = forms.CharField(label= 'FacultyName', max_length=100)
    event        = forms.CharField(label='event', max_length=100)
    Title        = forms.CharField(label='Title',max_length=100)
    Place        = forms.CharField(label='Place',max_length=100)
    fdatee        = forms.DateField(label='fdatee')
    tdate        = forms.DateField(label='tdate')
    certificate     =forms.FileField(label='certificate')

class placeform(forms.Form):
    sno                    = forms.IntegerField(label='sno')
    pno                    = forms.IntegerField(label='pno')
    regno                  = forms.IntegerField(label='regno' )
    name                   = forms.CharField(label='name',max_length=120)
    dep                    = forms.CharField(label='dep',max_length=100)
    compdet                = forms.CharField(label='compdet',max_length=500)
    fullad                 = forms.CharField(label='fullad',max_length=300)
    datee                  = forms.CharField(label='datee',max_length=14)
    fil                    = forms.FileField(label='fil')
    Upload_Photo_file      = forms.FileField(label='Upload_Photo_file')
    Attendance             = forms.FileField(label='Attendance')










class LecturerAddForm(UserCreationForm):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs = {'class':'form-control'}),label='Username',)
    address = forms.CharField(max_length=30,widget=forms.TextInput(attrs = {'class':'form-control'}),label="Address")
    phone = forms.CharField(max_length=30, widget=forms.TextInput(attrs = {'class':'form-control'}),label='Mobile No')
    firstname = forms.CharField(max_length=30,widget=forms.TextInput(attrs = {'class':'form-control'}),label="Firstname")
    lastname = forms.CharField(max_length=30, widget=forms.TextInput(attrs = {'class':'form-control'}), label="Lastname")
    email = forms.CharField(max_length=30, widget=forms.TextInput(attrs = {'class':'form-control'}), label="Email")

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_lecturer = True
        user.first_name = self.cleaned_data.get('firstname')
        user.last_name = self.cleaned_data.get('lastname')
        user.phone = self.cleaned_data.get('phone')
        user.email = self.cleaned_data.get('email')
        user.save()
        # if commit:
        #     user.save()
        # return user
        lecturer = Lecturar.objects.create(user=user, id_number=user.username)
        lecturer.save()
        return lecturer

class StudentAddForm(UserCreationForm):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs = {'class':'form-control'}),label='Username',)
    Address = forms.CharField(max_length=30, widget=forms.TextInput(attrs = {'class':'form-control'}), label='Address')
    phone = forms.CharField(max_length=30, widget=forms.TextInput(attrs = {'class':'form-control'}), label='Mobile No')
    firstname = forms.CharField(max_length=30, widget=forms.TextInput(attrs = {'class':'form-control'}), label="Firstname")
    lastname = forms.CharField(max_length=30, widget=forms.TextInput(attrs = {'class':'form-control'}), label="Lastname")
    email = forms.CharField(max_length=30, widget=forms.TextInput(attrs = {'class':'form-control'}), label="Email")

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic()
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('firstname')
        user.last_name = self.cleaned_data.get('lastname')
        user.phone = self.cleaned_data.get('phone')
        user.email = self.cleaned_data.get('email')
        user.save()
        student = Student.objects.create(user=user,id_number=user.username)
        student.save()
        return student
