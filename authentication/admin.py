from django.contrib import admin
from .models import  Lecturar
from authentication.models import Student, User,CourseALlocation
from authentication.models import ddd,facultyAttended,Conference,bookchappub,bookpub,researarticcal
from.models import pub,place,placesel,studet,infor
from import_export.admin import ImportExportModelAdmin

# Register your models here.




admin.site.register(User)
admin.site.register(Student)
admin.site.register(Lecturar)

class AllocattionAdmin(admin.ModelAdmin):
    list = ['lecturer']
admin.site.register(CourseALlocation,AllocattionAdmin)

class inforad(admin.ModelAdmin):
    list = ['val']
admin.site.register(infor,inforad)

class gfht(admin.ModelAdmin):
    list=[
    'sno              ',        
    'pno              ',
    'regno            ',
    'name             ',
    'dep              ',
    'compdet          ',
    'fullad           ',
    'datee            ',
    'fil              ',
    'Upload_Photo_file',
    'Attendance       ',
    ]
admin.site.register(place,gfht)

@admin.register(studet)
class ViewAdmin(ImportExportModelAdmin):
    pass


# class kfkk(admin.ModelAdmin):
#     list=[
#         'regno',
#         'name ',
#         'dep  ',
#         'blood',
#         'datee',
#         'phone',
#         'email',
#         'yearof',
#     ]
# admin.site.register(studet,kfkk)
class sfdads(admin.ModelAdmin):
    list=[
        'regno  ',
        'name   ',
        'datee  ',
        'dep    ',
        'compdet',
        'annu   ',
        'fil    '
    ]
admin.site.register(placesel,sfdads)

class asd(admin.ModelAdmin):
    list = [
        'book     ',
        'Author   ',
        'isbn     ',
        'publisher',
        'mandy    ',
        'bookwra  ',
        'fill'
    ]
admin.site.register(bookpub,asd)

class lop(admin.ModelAdmin):
    list = [
        'paper      ',
        'author     ',
        'isbn       ',
        'mandy      ',
        'publication',
        'certifi    '
    ]
admin.site.register(bookchappub,lop)

class kml(admin.ModelAdmin):
    list = [
        'paper  ',
        'author ',
        'artical',
        'mandy  ',
        'pageno ',
        'title',
        'certifi'
    ]
admin.site.register(researarticcal,kml)


# Register your models here.
class frf(admin.ModelAdmin):
    list=['FacultyName','Place','Title','Datee','Seminar',' parpose','fil','Upload_Photo_file''personone','persontwo ','persontree','nops','nopt']
admin.site.register(ddd,frf)

class gerr(admin.ModelAdmin):
    list=['FacultyName','event','Title','Place','fdatee','tdate','certificate']
admin.site.register(facultyAttended,gerr)

class jkkkl(admin.ModelAdmin):
    list=[
        'author   ',
        'noc      ',
        'venue    ',
        'organizer',
        'day      ',
        'isbn     ',
        'page     ',
        'proof    '
    ]
admin.site.register(Conference,jkkkl)

class bubad(admin.ModelAdmin):
    list = [
        'Sno          ',
        'papertitle   ',
        'Author       ',
        'Journal      ',
        'Indexed      ',
        'Factor       ',
        'Poru         ',
        'ISSN         ',
        'yearofpub    ',
        'TypeofJournal'
    ]

admin.site.register(pub,bubad)
