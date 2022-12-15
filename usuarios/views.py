from django.shortcuts import render, HttpResponse
from rolepermissions.decorators import has_permission_decorator
from .models import Users

@has_permission_decorator('cadastrar')
def cadastrar(request):
    if request.method == 'GET':
        return render(request, 'cadastrar.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
    
    user = Users.objects.filter(email = email)
    
    if user.exists():
        return HttpResponse ('Usuário já existe')
    
    user = Users.objects.create_user(username = email, email = email, password = senha, perfil = 'Tecnico')
    return HttpResponse('Usuário Cadastrado com sucesso')
    