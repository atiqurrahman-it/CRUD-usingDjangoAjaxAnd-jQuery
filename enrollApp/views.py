from django.shortcuts import render
from .forms import StudentRegistrationForm
from .models import MyUser
from django.http import JsonResponse


# Create your views here.

def Homepage(request):
    form = StudentRegistrationForm()
    student_data = MyUser.objects.all()
    data = {
        "form": form,
        "student_data": student_data,
    }
    return render(request, "index.html", data)


def Send_database(request):
    if request.is_ajax():
        if request.method == 'POST':
            form = StudentRegistrationForm(request.POST)
            if form.is_valid():
                sid = request.POST.get("studId")

                if (sid == ""):
                    form.save()

                else:

                    name = request.POST['name']
                    email = request.POST['email']
                    password = request.POST['password']

                    user = MyUser(id=sid, name=name, email=email, password=password)
                    user.save()
                    # Edit button a click
                    # form.id = sid

                stu = MyUser.objects.values()  # index page a MyUser Data show er jonno
                st_data = list(stu)  # student_data data  convert list

                return JsonResponse({
                    'msg': 'save',  # mens 1
                    'st_data': st_data
                })
            else:
                return JsonResponse({
                    'msg': 0  # 0 mens error
                })


# second way
# if request.method == 'POST':
#     name = request.POST['name'],
#     email = request.POST['email'],
#     password = request.POST['password'],
#
#     MyUser.objects.create(name=name, password=password, email=email)
#     return HttpResponse("")
def DeleteData(request):
    if request.method == 'POST':
        ed = request.POST.get('sid')
        pi = MyUser.objects.get(pk=ed)
        pi.delete()
        return JsonResponse({'status': 1})
    else:
        return JsonResponse({'status': 0})


def Edit_data(request):
    if request.method == 'POST':
        getid = request.POST.get('sid')
        student = MyUser.objects.get(pk=getid)
        student_inf_data = {"id": student.id, "name": student.name, "email": student.email,
                            "password": student.password}
        return JsonResponse(student_inf_data)
