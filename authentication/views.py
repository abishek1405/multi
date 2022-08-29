from distutils.log import fatal
from email import message
from urllib import request


from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,  login
from django.contrib.auth import logout
from authentication.models import worksphop,bookchappub,researarticcal
from authentication.models import bookpub
from .forms import worksphopform,facultyAttendedform
from Multiple_authentications import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .forms import StudentAddForm,LecturerAddForm, pubform,Conferenceform,bookpubform,bookchappubform,researarticcalform
from .decorators import student_required,lecturer_required
from .models import ddd,facultyAttended, place,pub,Conference, studet,infor
from authentication.forms import staf,placeform,placeselform,studetform,inforform
from .models import Lecturar,placesel
import datetime

from Multiple_authentications import settings
from django.core.mail import send_mail



def infr(request):
    formdd = inforform()
    if request.method== 'POST':
        formdd = inforform(request.POST)
        if formdd.is_valid():
            sn  = request.POST['val']
            
            infor.objects.create( val= sn)
            messages.success(request,'saved successfully')
            return redirect('/tlog/')
    return render(request, 'authentication/innn.html')


def aboutt(request):
    return render(request,'authentication/about.html')


def homelog(request):
    gfg = infor.objects.all()
    return render(request,'authentication/home.html',{'gj':gfg})







def bookchappubb(request):
    formdd = bookchappubform()
    if request.method== 'POST':
        formdd = bookchappubform(request.POST,request.FILES)
        if formdd.is_valid():
            sn  = request.POST['paper']
            pap = request.POST['author']
            aut = request.POST['isbn']
            may = request.POST['mandy']
            jou = request.POST['publication']
            ind = request.FILES["certifi"]
            bookchappub.objects.create( paper= sn ,  author =pap, isbn =aut,mandy=may,  publication= jou,certifi =  ind)
            messages.success(request,'saved successfully')
            return redirect('/tlog/')
    return render(request, 'authentication/bookchappub.html')

def bookchappubrebb(request):
    if request.method== 'POST':
        pup = request.POST['publication']
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']

        altt1  = pup and fdate and tdate
        altt2  = fdate and tdate
        altt3 = pup
        if bool(altt1):
            need= bookchappub.objects.raw(' SELECT* FROM authentication_bookchappub where publication = "'+pup+'" AND mandy BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/bookchappubrep.html',{'student':need})
        elif bool(altt2):
            print(2)
            need= bookchappub.objects.raw(' SELECT* FROM authentication_bookchappub where mandy BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/bookchappubrep.html',{'student':need})
        else:
            need= bookchappub.objects.raw(' SELECT* FROM authentication_bookchappub where publication = "'+pup+'";')
            return render(request,'authentication/bookchappubrep.html',{'student':need})
    else:
        need= bookchappub.objects.raw('select * from authentication_bookchappub ORDER BY mandy ASC')
        return render(request,'authentication/bookchappubrep.html',{'student':need})






def bookpubb(request):
    formdd = bookpubform()
    if request.method== 'POST':
        formdd = bookpubform(request.POST,request.FILES)
        if formdd.is_valid():
            sn  = request.POST['book']
            pap = request.POST['Author']
            aut = request.POST['isbn']
            jou = request.POST['publisher']
            ind = request.POST['mandy']
            fac = request.FILES['bookwra']
            fa = request.FILES['fill']

            bookpub.objects.create(book = sn, Author =pap, isbn =aut, publisher= jou, mandy=ind,bookwra  =  fac,fill = fa)
            messages.success(request,'saved successfully')
            return redirect('/tlog/')
    return render(request, 'authentication/bookpub.html')

def bookpubbrepp(request):
    if request.method== 'POST':
        pup = request.POST['publisher']
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']


        altt1  = pup and fdate and tdate
        altt2  = fdate and tdate


        if bool(altt1):
            need= Conference.objects.raw(' SELECT* FROM authentication_bookpub where publisher = "'+pup+'" AND mandy BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/bookpubrep.html',{'student':need})
        elif bool(altt2):
            print(2)
            need= bookpub.objects.raw(' SELECT* FROM authentication_bookpub where mandy BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/bookpubrep.html',{'student':need})
        else:
            need= bookpub.objects.raw(' SELECT* FROM authentication_bookpub where publisher = "'+pup+'";')
            return render(request,'authentication/bookpubrep.html',{'student':need})
    else:

        need= bookpub.objects.raw('select * from authentication_bookpub ORDER BY mandy ASC')
        return render(request,'authentication/bookpubrep.html',{'student':need})

def researarticcall(request):
    formdd = researarticcalform()
    if request.method== 'POST':
        formdd = researarticcalform(request.POST,request.FILES)
        if formdd.is_valid():
            sn  = request.POST['paper']
            pap = request.POST['author']
            aut = request.POST['artical']
            tiiii = request.POST['title']
            
            may = request.POST['mandy']
            jou = request.POST['pageno']

            ind = request.FILES['certifi']
            researarticcal.objects.create(paper = sn , author=pap,mandy=may, artical=aut,title = tiiii, pageno = jou,certifi =  ind)
            messages.success(request,'saved successfully')
            return redirect('/tlog/')
    return render(request, 'authentication/researarticcal.html')



def researarticcallrebb(request):
    if request.method== 'POST':
       pup = request.POST['Author']
       fdate = request.POST['fdate']
       tdate = request.POST['tdate']
       art = request.POST['Article']

       altt = pup and fdate and tdate and art
       altt1  = pup and fdate and tdate
       alll = art and fdate and tdate
       altt2  = fdate and tdate
       altt3 = pup
       men = art

       if bool(altt):
           need= researarticcal.objects.raw(' SELECT* FROM authentication_researarticcal where artical = "'+art+'" author = "'+pup+'" AND mandy BETWEEN "'+fdate+'" and "'+tdate+'";')
           return render(request,'authentication/researarticcalrep.html',{'student':need})
       elif bool(altt1):
           need= researarticcal.objects.raw(' SELECT* FROM authentication_researarticcal where  author = "'+pup+'" AND mandy BETWEEN "'+fdate+'" and "'+tdate+'";')
           return render(request,'authentication/researarticcalrep.html',{'student':need})
       elif bool(alll):
           need= researarticcal.objects.raw(' SELECT* FROM authentication_researarticcal where  artical = "'+art+'"  AND mandy BETWEEN "'+fdate+'" and "'+tdate+'";')
           return render(request,'authentication/researarticcalrep.html',{'student':need})
       elif bool(altt2):
           print(2)
           need= researarticcal.objects.raw(' SELECT* FROM authentication_researarticcal where mandy BETWEEN "'+fdate+'" and "'+tdate+'";')
           return render(request,'authentication/researarticcalrep.html',{'student':need})
       elif bool(altt3):
           need= researarticcal.objects.raw(' SELECT* FROM authentication_researarticcal where author = "'+pup+'";')
           return render(request,'authentication/researarticcalrep.html',{'student':need})
       else:
            print(art)
            need= researarticcal.objects.raw(' SELECT* FROM authentication_researarticcal where artical = "'+art+'";')
            return render(request,'authentication/researarticcalrep.html',{'student':need})    
    else:
        need= researarticcal.objects.raw('select * from authentication_researarticcal ORDER BY mandy ASC')
        return render(request,'authentication/researarticcalrep.html',{'student':need}) 






def pubreb(request):

    if request.method== 'POST':
        parp = request.POST['ind']
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        jou = request.POST['jour']
        fac = request.POST['FacultyName']

        fp  = fac and parp
        fj  = fac and jou
        jp = jou and parp
        fe = fdate and tdate
        fen = fdate and tdate and parp
        lit = fdate and tdate and fac
        tlit = fdate and tdate and jou
        fenn = jou and fac and parp
        fd = fdate and tdate and parp and fac
        fdfd = fdate and tdate and jou and fac
        fdd = fdate and tdate and parp and fac and jou

        sta = fac


        if bool(fdd):
            need= pub.objects.raw(' SELECT* FROM authentication_pub where Author = "'+fac+'" AND Indexed= "'+parp+'" AND TypeofJournal = "'+jou+'" AND yearofpub BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/pubreb.html',{'student':need})
        elif bool(fd):
            need= pub.objects.raw(' SELECT* FROM authentication_pub where Author = "'+fac+'" AND Indexed= "'+parp+'" AND yearofpub BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/pubreb.html',{'student':need})
        elif bool(fdfd):
            need= pub.objects.raw(' SELECT* FROM authentication_pub where Author = "'+fac+'" AND TypeofJournal = "'+jou+'" AND yearofpub BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/pubreb.html',{'student':need})
        elif bool(fen):
            need= pub.objects.raw(' SELECT* FROM authentication_pub where Indexed= "'+parp+'" AND yearofpub BETWEEN "'+fdate+'" AND "'+tdate+'";')
            return render(request,'authentication/pubreb.html',{'student':need})
        elif bool(fenn):
            need= pub.objects.raw(' SELECT* FROM authentication_pub where Indexed= "'+parp+'" AND Author = "'+fac+'" AND TypeofJournal = "'+jou+'";')
            return render(request,'authentication/pubreb.html',{'student':need})
        elif bool(lit):
           #print(parp)
           neeud= pub.objects.raw('select * from authentication_pub where  Author = "'+fac+'" AND  yearofpub between "'+fdate+'" AND "'+tdate+'";')
           return render(request,'authentication/pubreb.html',{'student':neeud})
        elif bool(tlit):
           #print(parp)
           neeud= pub.objects.raw('select * from authentication_pub where  TypeofJournal = "'+jou+'" AND  yearofpub between "'+fdate+'" AND "'+tdate+'";')
           return render(request,'authentication/pubreb.html',{'student':neeud})
        elif bool(fe):
           neeud= pub.objects.raw('select * from authentication_pub where yearofpub between "'+fdate+'" AND "'+tdate+'" ORDER BY yearofpub ASC')
           return render(request,'authentication/pubreb.html',{'student':neeud})

        elif bool(fp):
           neeud= pub.objects.raw('select * from authentication_pub where  Author = "'+fac+'" AND Indexed= "'+parp+'" ORDER BY yearofpub ASC')
           return render(request,'authentication/pubreb.html',{'student':neeud})
        elif bool(fj):
           neeud= pub.objects.raw('select * from authentication_pub where  Author = "'+fac+'" AND TypeofJournal = "'+jou+'" ORDER BY yearofpub ASC')
           return render(request,'authentication/pubreb.html',{'student':neeud})
        elif bool(jp):
           neeud= pub.objects.raw('select * from authentication_pub where  TypeofJournal = "'+jou+'"  AND Indexed= "'+parp+'" ORDER BY yearofpub ASC')
           return render(request,'authentication/pubreb.html',{'student':neeud})
        elif bool(sta):
            need= pub.objects.raw('SELECT * FROM authentication_pub WHERE Author = "'+fac+'" ;')
            return render(request,'authentication/pubreb.html',{'student':need})

        elif bool(jou):
            need= pub.objects.raw('SELECT * FROM authentication_pub WHERE TypeofJournal = "'+jou+'" ;')
            return render(request,'authentication/pubreb.html',{'student':need})

        else:
            parp = request.POST['ind']
            need= pub.objects.raw('SELECT * FROM authentication_pub WHERE Indexed = "'+parp+'";')

            return render(request,'authentication/pubreb.html',{'student':need})

    else:

        ned= pub.objects.raw('select * from authentication_pub ORDER BY yearofpub ASC')
        return render(request,'authentication/pubreb.html',{'student':ned})




def pulica(request):
    formdd = pubform()
    if request.method== 'POST':
        formdd = pubform(request.POST)
        if formdd.is_valid():
            sn  = request.POST['Sno']
            pap = request.POST['papertitle']
            aut = request.POST['Author']
            jou = request.POST['Journal']
            ind = request.POST['Indexed']
            fac = request.POST['Factor']
            por = request.POST['Poru']
            iss = request.POST['ISSN']
            yea = request.POST['yearofpub']
            typ = request.POST['TypeofJournal']
            print(typ)
            pub.objects.create(Sno = sn ,papertitle   =  pap,Author       =  aut,Journal      =  jou,Indexed      =  ind,Factor       =  fac,Poru         =  por,ISSN         =  iss,yearofpub    =  yea,TypeofJournal=  typ )
            messages.success(request,'saved successfully')
            return redirect('/tlog/')
    return render(request, 'authentication/bubrig.html')





def homelog(request):
    return render(request,'templates/home.html')




# Create your views here.

def regoutcome(request):
    formdd = staf()
    if request.method== 'POST':
        formdd = staf(request.POST,request.FILES)
        if formdd.is_valid():
            par = request.POST['parpose']
            ne = request.POST['FacultyName']
            ti = request.POST['Title']
            pone = request.POST['personone']
            ptwo = request.POST['persontwo']
            ptree = request.POST['persontree']
            da = request.POST['Datee']
            pl = request.POST['Place']
            nos = request.POST['nops']
            nopt = request.POST['nopt']
            fi = request.FILES["fil"]
            file2 = request.FILES["Upload_Photo_file"]
            att = request.FILES["Attendance"]
            repp = request.FILES["Report"]

            ddd.objects.create(parpose=par, FacultyName = ne ,Title = ti ,personone=pone, persontwo=ptwo ,persontree=ptree, Datee = da, Place = pl,    nops=nos, nopt=nopt, fil = fi, Upload_Photo_file=file2, Attendance=att,Report=repp)
            messages.success(request,'saved successfully')
            return redirect('/tlog/')
    return render(request, 'authentication/regoutcome.html')



def placement(request):
    formdd = placeform()
    if request.method== 'POST':
        formdd = placeform(request.POST,request.FILES)
        if formdd.is_valid():
            par  = request.POST['sno']
            ne   = request.POST['pno']
            ti   = request.POST['regno']
            pone = request.POST['name']
            ptwo = request.POST['dep']
            ptree= request.POST['compdet']
            da   = request.POST['fullad']
            pl   = request.POST['datee']
            fi   = request.FILES["fil"]
            file2 = request.FILES["Upload_Photo_file"]
            att = request.FILES["Attendance"]
           

            place.objects.create(sno=par, pno = ne ,regno = ti ,name=pone, dep=ptwo ,compdet=ptree, fullad = da, datee = pl, fil = fi, Upload_Photo_file=file2, Attendance=att)
            messages.success(request,'saved successfully')
            return redirect('/slog/')
    return render(request, 'authentication/placement.html')


def placerep(request):
    if request.method== 'POST':
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        dep = request.POST['dep']

        altt1 = fdate and tdate and dep
        ttt = fdate and tdate
        altt2 = dep
        if bool(altt1):
            need= Conference.objects.raw(' SELECT* FROM authentication_place where dep = "'+dep+'" AND  datee BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/placerep.html',{'student':need})
        elif bool(ttt):

            need= Conference.objects.raw(' SELECT* FROM authentication_place where datee BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/placerep.html',{'student':need})
        else:

            need= Conference.objects.raw(' SELECT* FROM authentication_place where  dep = "'+dep+'" ')
            return render(request,'authentication/placerep.html',{'student':need})
    
    else:
        ned= place.objects.raw('select * from authentication_place ORDER BY datee ASC')
        return render(request,'authentication/placerep.html',{'student':ned})


def sturep(request):
    if request.method== 'POST':
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        dep = request.POST['dep']

        altt1 = fdate and tdate and dep
        ttt = fdate and tdate
        altt2 = dep
        if bool(altt1):
            need= placesel.objects.raw(' SELECT* FROM authentication_studet    where dep = "'+dep+'" AND  yearof BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/studrepp.html',{'student':need})
        elif bool(ttt):

            need= placesel.objects.raw(' SELECT* FROM authentication_studet where yearof BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/studrepp.html',{'student':need})
        else:

            need= placesel.objects.raw(' SELECT* FROM authentication_studet where  dep = "'+dep+'" ')
            return render(request,'authentication/studrepp.html',{'student':need})
    
    else:  
      
        ned= studet.objects.raw('select * from authentication_studet; ')
        return render(request,'authentication/studrepp.html',{'student':ned})

    


def facultyAttendedview(request):
    formdd = facultyAttendedform()
    if request.method== 'POST':
        formdd = facultyAttendedform(request.POST,request.FILES)
        if formdd.is_valid():
            fa = request.POST['FacultyName']
            eve = request.POST['event']
            tit = request.POST['Title']
            pla = request.POST['Place']
            fda = request.POST['fdatee']
            tda = request.POST['tdate']
            cer = request.FILES['certificate']
            facultyAttended.objects.create(FacultyName = fa, event = eve, Title = tit, Place = pla, fdatee=fda, tdate = tda, certificate = cer)
            messages.success(request,'saved successfully')
            return redirect('/tlog/')
    return render(request, 'authentication/facultyAttended.html')

def Conferencer(request):
    formdd = Conferenceform()
    if request.method== 'POST':
        formdd = Conferenceform(request.POST,request.FILES)
        if formdd.is_valid():
            fa = request.POST['author']
            eve = request.POST['noc']
            tit = request.POST['venue']
            pla = request.POST['organizer']
            fda = request.POST['day']

            tda = request.POST['isbn']
            pa = request.POST['page']
            cer = request.FILES['proof']
            Conference.objects.create(author = fa, noc = eve, venue = tit, organizer = pla, day=fda, isbn = tda, page = pa,proof = cer)
            messages.success(request,'saved successfully')
            return redirect('/tlog/')
    return render(request, 'authentication/conferencep.html')



def conferrep(request):
    if request.method== 'POST':
        org = request.POST['organizer']
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        con = request.POST['Conference']
        ven = request.POST['venue']

        altt1  = org and fdate and tdate and con and ven
        altt2  = org and ven and fdate and tdate
        altt  = con and ven and fdate and tdate
        altt4  = org and con and fdate and tdate
        altt5  = ven and fdate and tdate
        altt6  = org and fdate and tdate
        altt7 = con and fdate and tdate
        altt8  = org and ven
        altt9  = org and con
        altt12  = con and ven
        altt13  = fdate and tdate
        altt14  = ven
        altt15 = con



        if bool(altt1):
            need= Conference.objects.raw(' SELECT* FROM authentication_conference where organizer = "'+org+'" AND venue= "'+ven+'" AND noc = "'+con+'" AND dayy BETWEEN "'+fdate+'" and "'+tdate+'";')
            print(org)
            print(fdate)
            print(ven)
            print(con)
            print(tdate)
            return render(request,'authentication/conferrep.html',{'student':need})
        elif bool(altt2):
            print(2)
            need= Conference.objects.raw(' SELECT* FROM authentication_Conference where organizer = "'+org+'" AND venue= "'+ven+'" AND  dayy BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/conferrep.html',{'student':need})
        elif bool(altt):
            print(3)
            need= Conference.objects.raw(' SELECT* FROM authentication_conference where venue= "'+ven+'" AND  noc = "'+con+'" AND dayy BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/conferrep.html',{'student':need})
        elif bool(altt4):
            need= Conference.objects.raw(' SELECT* FROM authentication_conference where organizer = "'+org+'"  AND noc = "'+con+'" AND dayy BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/conferrep.html',{'student':need})
        elif bool(altt5):
            need= Conference.objects.raw(' SELECT* FROM authentication_conference where venue = "'+ven+'"  AND dayy BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/conferrep.html',{'student':need})
        elif bool(altt6):
            need= Conference.objects.raw(' SELECT* FROM authentication_conference where organizer = "'+org+'" AND dayy BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/conferrep.html',{'student':need})
        elif bool(altt7):
            need= Conference.objects.raw(' SELECT* FROM authentication_conference where  noc = "'+con+'" AND dayy BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/conferrep.html',{'student':need})
        elif bool(altt8):
            need= Conference.objects.raw(' SELECT* FROM authentication_conference where organizer = "'+org+'" AND venue= "'+ven+'";')
            return render(request,'authentication/conferrep.html',{'student':need})
        elif bool(altt9):
            need= Conference.objects.raw(' SELECT* FROM authentication_conference where organizer = "'+org+'" AND noc = "'+con+'";')
            return render(request,'authentication/conferrep.html',{'student':need})
        elif bool(altt12):
            need= Conference.objects.raw(' SELECT* FROM authentication_conference where venue= "'+ven+'" AND noc = "'+con+'";')
            return render(request,'authentication/conferrep.html',{'student':need})
        elif bool(altt13):
            need= Conference.objects.raw(' SELECT* FROM authentication_conference where dayy BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/conferrep.html',{'student':need})
        elif bool(altt14):
            need= Conference.objects.raw(' SELECT* FROM authentication_conference where  venue= "'+ven+'";')
            return render(request,'authentication/conferrep.html',{'student':need})
        elif bool(altt15):
            need= Conference.objects.raw(' SELECT* FROM authentication_conference where  noc = "'+con+'";')
            return render(request,'authentication/conferrep.html',{'student':need})
        else:
            need= Conference.objects.raw(' SELECT* FROM authentication_conference where organizer = "'+org+'";')
            return render(request,'authentication/conferrep.html',{'student':need})
    else:

        ned= Conference.objects.raw('select * from authentication_conference ORDER BY dayy ASC')
        return render(request,'authentication/conferrep.html',{'student':ned})



def facrep(request):
    if request.method== 'POST':
        parp = request.POST['event']
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        fac = request.POST['FacultyName']

        fp  = fac and parp
        fen = fdate and tdate and parp
        fe = fdate and tdate
        fd = fdate and tdate and parp and fac
        lit = fdate and tdate and fac
        sta = fac

        if bool(fd):
            print(fdate)
            print(tdate)
            print(parp)
            print(fd)
            need= facultyAttended.objects.raw(' SELECT* FROM authentication_facultyAttended where FacultyName = "'+fac+'" AND event= "'+parp+'" AND fdatee BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/facrep.html',{'student':need})
        elif bool(fen):
            print(fdate)
            print(tdate)
            print(parp)
            need= facultyAttended.objects.raw(' SELECT* FROM authentication_facultyAttended where event= "'+parp+'" AND fdatee BETWEEN "'+fdate+'" AND "'+tdate+'";')
            return render(request,'authentication/facrep.html',{'student':need})
        elif bool(lit):
           print(fdate)
           print(tdate)
           print(fac)
           #print(parp)
           neeud= facultyAttended.objects.raw('select * from authentication_facultyAttended where  FacultyName = "'+fac+'" AND  fdatee between "'+fdate+'" AND "'+tdate+'";')
           return render(request,'authentication/facrep.html',{'student':neeud})
        elif bool(fe):
           print(fdate)
           print(tdate)
           #print(parp)
           neeud= facultyAttended.objects.raw('select * from authentication_facultyAttended where fdatee between "'+fdate+'" AND "'+tdate+'" ORDER BY fdatee ASC')
           return render(request,'authentication/facrep.html',{'student':neeud})

        elif bool(fp):
           print(parp)
           print(fac)
           #print(parp)
           neeud= facultyAttended.objects.raw('select * from authentication_facultyAttended where  FacultyName = "'+fac+'" AND event= "'+parp+'" ORDER BY fdatee ASC')
           return render(request,'authentication/facrep.html',{'student':neeud})
        elif bool(sta):
            print(sta)
            need= facultyAttended.objects.raw('SELECT * FROM authentication_facultyAttended WHERE FacultyName = "'+fac+'" ;')
            return render(request,'authentication/facrep.html',{'student':need})

        else:
            parp = request.POST['event']
            print(parp)
            need= facultyAttended.objects.raw('SELECT * FROM authentication_facultyAttended WHERE event = "'+parp+'";')
            return render(request,'authentication/facrep.html',{'student':need})
    else:
        ned= facultyAttended.objects.raw('select * from authentication_facultyAttended ORDER BY fdatee ASC')
        return render(request,'authentication/facrep.html',{'student':ned})





def retrieve_view(request):
    if request.method== 'POST':
        parp = request.POST['parpose']
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        fac = request.POST['FacultyName']

        fp  = fac and parp
        fen = fdate and tdate and parp
        fe = fdate and tdate
        fd = fdate and tdate and parp and fac
        lit = fdate and tdate and fac
        sta = fac

        if bool(fd):
           
            need= ddd.objects.raw(' SELECT* FROM authentication_ddd where FacultyName = "'+fac+'" AND parpose= "'+parp+'" AND datee BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/report.html',{'student':need})
        elif bool(fen):
           
            need= ddd.objects.raw(' SELECT* FROM authentication_ddd where parpose= "'+parp+'" AND datee BETWEEN "'+fdate+'" AND "'+tdate+'";')
            return render(request,'authentication/report.html',{'student':need})
        elif bool(lit):
          
        
           neeud= ddd.objects.raw('select * from authentication_ddd where  FacultyName = "'+fac+'" AND  Datee between "'+fdate+'" AND "'+tdate+'";')
           return render(request,'authentication/report.html',{'student':neeud})
        elif bool(fe):
          
           neeud= ddd.objects.raw('select * from authentication_ddd where Datee between "'+fdate+'" AND "'+tdate+'" ORDER BY datee ASC')
           return render(request,'authentication/report.html',{'student':neeud})

        elif bool(fp):
         
           neeud= ddd.objects.raw('select * from authentication_ddd where  FacultyName = "'+fac+'" AND parpose= "'+parp+'" ORDER BY datee ASC')
           return render(request,'authentication/report.html',{'student':neeud})
        elif bool(sta):

         print(sta)
         need= ddd.objects.raw('SELECT * FROM authentication_ddd WHERE FacultyName = "'+fac+'" ;')
         return render(request,'authentication/report.html',{'student':need})

        else:
            parp = request.POST['parpose']
            print(parp)
            need= ddd.objects.raw('SELECT * FROM authentication_ddd WHERE parpose = "'+parp+'";')

            return render(request,'authentication/report.html',{'student':need})

    else:

        ned= ddd.objects.raw('select * from authentication_ddd ORDER BY datee ASC')
        return render(request,'authentication/report.html',{'student':ned})






def StudentSignUp(request):
    if request.method == "POST":
        email = request.POST['email']
        uname = request.POST['username']
        passs = request.POST['password1']

        form = StudentAddForm(request.POST or None)
        if form.is_valid():
            student = form.save(commit=False)
            student.user_type = 'student'
            student.save()
            
            
            messages.success(request,'your account was created successfully.')
            subject = "welcome to gfg django login"
            
            message = "hello "+ uname +"!!  \n" + "welcome to pmu tech!! \n" + "your account was created sucessfull \n log in with the below the username and password. \n\n thanking you \n\n Username:" +uname +"\n password:" +passs + " "
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            send_mail(subject, message, from_email, to_list, fail_silently = True)

            return redirect('http://127.0.0.1:8000/login/')
    else:
       form = StudentAddForm()
    return render(request,'authentication/Student_signup.html',{'form':form})




def LecturerSignUp(request):
    if request.method == "POST":
        email = request.POST['email']
        uname = request.POST['username']
        passs = request.POST['password1']
        form = LecturerAddForm(request.POST or None)
        if form.is_valid():
            lecturer = form.save(commit=False)
            lecturer.user_type = 'lecturer'
            lecturer.save()
            
            messages.success(request,'your account was created successfully.')
            subject = "welcome to gfg django login"
            message = "hello "+ uname +"!!  \n" + "welcome to pmu tech!! \n" + "your account was created sucessfull \n log in with the below the username and password. \n\n thanking you \n\n Username:" +uname +"\n password:" +passs + " "
            from_email = settings.EMAIL_HOST_USER
            to_list = [email]
            send_mail(subject, message, from_email, to_list, fail_silently = True)            

            return redirect('http://127.0.0.1:8000/login/')
    else:
       form = LecturerAddForm()
    return render(request,'authentication/Student_signup.html',{'form':form})


def shome(request):
    return render(request, 'authentication/student.html')

x = datetime.datetime.now()
 
def SignInView(request):
    
    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST['password']
       
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            if request.user.is_authenticated:
                if request.user.is_student:
                    c = x.strftime("%H")
                    if int(c)>=19:
                        tt = ("Good Night! ")
                        messages.success(request,'your account was login successfully ,'+tt +''+username+'. ')
                        
                    elif int(c)>=16:
                        tt = ("Good evening! ")
                        messages.success(request,'your account was login successfully ,'+tt +''+username+'. ')
                    elif int(c)>=12:
                        tt = ("Good afternoon! ")
                        messages.success(request,'your account was login successfully ,'+tt +''+username+'. ')
                    else:
                        tt = ("Good morning! ")
                        messages.success(request,'your account was login successfully ,'+tt +''+username+'. ')
                    request.session.set_expiry(800)
                    return redirect ('/slog/')
                else:
                    fl = "***your username or password is wrong***"
                    return render(request, 'authentication/login_form.html',{'jk':fl})
            
                    
                      

                       
        else:
            fl = "***your username or password is wrong***"
            return render(request, 'authentication/login_form.html',{'jk':fl})
    return render(request, 'authentication/login_form.html')

def tsing(request):
    if request.method == "POST":
        
        username = request.POST['username']
        password = request.POST['password']
       
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            if request.user.is_authenticated:
                if request.user.is_lecturer:
                    c = x.strftime("%H")
                    
                    if int(c)>=19:
                        tt = ("Good Night! ")
                        messages.success(request,'your account was login successfully ,'+tt +' '+username+'. ')

                    elif int(c)>=16:
                        tt = ("Good evening! ")
                        messages.success(request,'your account was login successfully ,'+tt +''+username+'. ')
                    elif int(c)>=12:
                        tt = ("Good afternoon! ")
                        messages.success(request,'your account was login successfully ,'+tt +' '+username+'. ')
                    else:
                        tt = ("Good morning! ")
                        messages.success(request,'your account was login successfully ,'+tt +''+username+'. ')
                    request.session.set_expiry(800)
                    return redirect ('/tlog/')
                else:
                    fl = "***your username or password is wrong***"
                    return render(request, 'authentication/login_form.html',{'jk':fl})
                
        else:
            fl = "***your username or password is wrong***"
            return render(request, 'authentication/login_form.html',{'jk':fl})
        
    return render(request, 'authentication/login_form.html')


def tlog(request): 
    return render(request,'authentication/teacher.html')
def slog(request):
    return render(request,'authentication/student.html')    

def ttime(request):
    return render(request,'authentication/ttime.html')
def stime(request):
    return render(request,'authentication/stime.html')

def logout_view(request):
    logout(request)
    messages.success(request,'logout successfully')
    return redirect('http://127.0.0.1:8000/')



def studdeet(request):
    formdd = studetform()
    if request.method== 'POST':
        formdd = studetform(request.POST)
        if formdd.is_valid():
            par  = request.POST['regno']
            ne   = request.POST['name']
            pone = request.POST['dep']
            ti   = request.POST['datee']
            blo  = request.POST['blood']
            ptree= request.POST['phone']
            da   = request.POST['email']
            ya   = request.POST['yearof']

            studet.objects.create(regno=par, name = ne ,datee = ti ,dep=pone,phone=ptree, blood = blo,  email = da,yearof = ya)
            messages.success(request,'saved successfully')
            return redirect('/tlog/')
    return render(request, 'authentication/stud.html')



def placeselectt(request):
    formdd = placeselform()
    if request.method== 'POST':
        formdd = placeselform(request.POST,request.FILES)
        if formdd.is_valid():
            par  = request.POST['regno']
            ne   = request.POST['name']
            ti   = request.POST['datee']
            pone = request.POST['dep']
            ptree= request.POST['compdet']
            da   = request.POST['annu']
            fi   = request.FILES["fil"]

            placesel.objects.create(regno=par, name = ne ,datee = ti ,dep=pone,compdet=ptree, annu = da,  fil = fi)
            messages.success(request,'saved successfully')
            return redirect('/slog/')
    return render(request, 'authentication/placementsel.html')


def placeselrep(request):
    if request.method== 'POST':
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        dep = request.POST['dep']

        altt1 = fdate and tdate and dep
        ttt = fdate and tdate
        altt2 = dep
        if bool(altt1):
            need= placesel.objects.raw(' SELECT* FROM authentication_placesel    where dep = "'+dep+'" AND  datee BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/placeselrep.html',{'student':need})
        elif bool(ttt):

            need= placesel.objects.raw(' SELECT* FROM authentication_placesel where datee BETWEEN "'+fdate+'" and "'+tdate+'";')
            return render(request,'authentication/placeselrep.html',{'student':need})
        else:

            need= placesel.objects.raw(' SELECT* FROM authentication_placesel where  dep = "'+dep+'" ')
            return render(request,'authentication/placeselrep.html',{'student':need})
    
    else:  
        ned= placesel.objects.raw('select * from authentication_placesel ORDER BY datee ASC')
        return render(request,'authentication/placeselrep.html',{'student':ned})
    



def fen(request):
    detail = worksphop.objects.all()
    da = {'keyy':detail}
    return render(request,'authentication/dropdown.html',context = da)

def create_view(request):
    form = worksphopform()
    if request.method== 'POST':
        form = worksphopform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/work')
    return render(request, 'authentication/fun.html' ,{'form': form})

def come(request):
    gfg = infor.objects.all()
    return render(request,'authentication/home.html',{'gj':gfg})
    



def time(request):
    return render(request,'authentication/time.html')
def repts(request):
    return render(request,'authentication/repts.html')
