from django.urls import path
from authentication import views
#from django.contrib import admin
from django.urls import path
from. import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [

    path('',views.come, name = "come"),
    path('placement/',views.placement),
    path('tm/',views.time, name= 'time'),
    path('timee/',views.time),
    path('shome/',views.shome),
    path('about/',views.aboutt),
    path('hhh/', views.regoutcome, name="regoutcome"),
    path('home/',views.come, name = "come"),
    path('',views.homelog,name='homelog'),
    path('student/signup/',views.StudentSignUp, name = 'StudentSignup'),
    path('lecturar/signup/',views.LecturerSignUp, name = 'LecturerSignup'),
    path('login/',views.SignInView,name = 'login'),
    path('logout/',views.logout_view,name = 'logout_view'),
    path('ttime/',views.ttime,name = 'ttime'),
    path('ghg/',views.tsing),
    path('tlog/',views.tlog,name = 'tlog'),
    path('slog/',views.slog,name = 'tlog'),
    path('ret/',views.retrieve_view),
    path('faculty/',views.facultyAttendedview),
    path('facrep/',views.facrep),
    path('pulica/',views.pulica),
    path('pubreb/',views.pubreb),
    path('repts/',views.repts),
    path('Conference/', views.Conferencer),
    path('conferrep/',views.conferrep),    
    path('bookchappub/',views.bookchappubb),
    path('bookpub/',views.bookpubb),
    path('researarticcal/',views.researarticcall),
    path('bookchappubrebb/',views.bookchappubrebb),
    path('bookpubbrepp/',views.bookpubbrepp),
    path('researarticcallrebbu/',views.researarticcallrebb),
    path('stime/',views.stime),
    path('place/',views.placerep),
    path('placesel/',views.placeselectt),
    path('placeselrep/',views.placeselrep),
    path('studet/',views.studdeet),
    path('studrep/',views.sturep),
    path('inf/',views.infr)
   # path('retrievet/',views.retrievet),




] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
