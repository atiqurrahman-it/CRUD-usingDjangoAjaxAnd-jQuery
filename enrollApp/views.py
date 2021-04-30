from django.shortcuts import render, HttpResponse
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
                form.save()
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
