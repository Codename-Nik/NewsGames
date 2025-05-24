from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

from .models import Newa, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')
            user = form.save()
            login(request, user)
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'Newa/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('Login')

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
    else:
        form = UserLoginForm()
    return render(request, 'Newa/login.html', {'form': form})

class HomeNewa(ListView, MyMixin):
    model = Newa
    context_object_name = 'newa'
    template_name ='Newa/home_newa_list.html'
    extra_context = {'title':'Главная'}
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= 'Главная страница'
        return context

    def get_queryset(self):
        return Newa.objects.filter(is_published=True).select_related('category')

class NewaByCategory(ListView, MyMixin):
    model = Newa
    template_name = 'Newa/home_newa_list.html'
    context_object_name = 'newa'
    allow_empty = False
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']= Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Newa.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

class ViewNewa(DetailView):
    model = Newa
    context_object_name = 'newa_item'
    template_name = 'Newa/view_newa.html'

class AddNewa(CreateView):
    form_class = NewsForm
    template_name = 'Newa/add_newa.html'
    login_url = '/admin/'

#def index(request):
#    newa = Newa.objects.all()
#    categories = Category.objects.all()
#    context = {
#        'newa' : newa,
#        'title' : 'Список новостей',

#   }
#    return render(request, 'Newa/index.html', context=context)

#def get_category(request, category_id):
#    newa = Newa.objects.filter(category_id=category_id)
#    categories = Category.objects.all()
#    category = Category.objects.get(pk=category_id)
#    context = {
#        'newa' : newa,
#        'category':category
#    }
#    return render(request, 'Newa/category.html', context=context)

#def view_newa(request, news_id):
    #newa_item = Newa.objects.get(pk=news_id)
#    newa_item = get_object_or_404(Newa, pk=news_id)
#    context = {
#        'newa_item': newa_item
#    }
#    return render(request, 'Newa/view_newa.html', context=context)

#def add_newa(request):
#    if request.method == 'POST':
#        form = NewsForm(request.POST)
#        if form.is_valid():
            # newa = Newa.objects.create(**form.cleaned_data)
#            newa = form.save()
#            return redirect(newa)
#    else:
#        form = NewsForm()
#    return render(request, 'Newa/add_newa.html', {'form': form})

# def test(request):
#     objects = ['john', 'paul', 'george', 'ringo', 'john2', 'paul2', 'george2', 'ringo2']
#     paginator = Paginator(objects, 2)
#     page_num = request.GET.get('page', 1)
#     page_objects = paginator.get_page(page_num)
#     return render(request, 'Newa/test.html', {'page_obj': page_objects})