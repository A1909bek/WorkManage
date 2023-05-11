from django.shortcuts import render,HttpResponse
from  .models import Ishchi
# Create your views here.
def index(request):
    ishchi = Ishchi.objects.all()
    context = {
        'ishchi':ishchi
    }
    return render(request,'index.html',context)

def add(request):
    if request.method =='POST':
        ismi = request.POST['ismi']
        yoshi = request.POST['yoshi']
        vazifasi = request.POST['vazifasi']
        maoshi = int(request.POST['maoshi'])
        bonusi = int(request.POST['bonusi'])
        karyera = int(request.POST['karyera'])
        ish_vaqti = int(request.POST['ish_vaqti'])
        yangi_ishchi=Ishchi(ismi = ismi,yoshi = yoshi,vazifasi = vazifasi,maoshi = maoshi,bonusi = bonusi,karyera = karyera,ish_vaqti =ish_vaqti)
        yangi_ishchi.save()
        return HttpResponse("Yangi ishchi qo'shildi")
    elif request.method == 'GET':
        return render(request,'add.html')
    else:
        return HttpResponse("Xodim qo'shishda muammo bor!!")

def remove(request,ish_id=0):
    if ish_id:
        try :
            ish_ochir = Ishchi.objects.get(id=ish_id)
            ish_ochir.delete()
            return HttpResponse("Bu hodim ishdan bo'shatildi")
        except:
            return HttpResponse("Bu hodimni o'chirasizmi")
    ishchi = Ishchi.objects.all()
    context = {
        'ishchi':ishchi
    }
    return render(request,'remove.html',context)
