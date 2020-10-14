from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login, logout


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Успішно зареєстровано')
            return redirect('home')
        else:
            messages.error(request, 'Помилка реєстрації')
    else:
        form = UserRegisterForm()
    return render(request, 'NewsApp/registration.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вхід успішний')
            return redirect('home')
    else:
        form = UserLoginForm()
        # messages.error(request, 'Помилка входу')
    return render(request, 'NewsApp/login.html', {"form": form})


# Create your views here.
class HomeNews(ListView):
    model = News
    template_name = 'NewsApp/index_class.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 5

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


# def index(request):
#     news = News.objects.filter(is_published=True)
#     context = {
#         'news': news,
#         'title': 'Список Новин',
#     }
#     return render(request, 'NewsApp/index.html', context)

class NewsCategory(ListView):
    model = News
    template_name = 'NewsApp/index_class.html'
    context_object_name = 'news'
    allow_empty = True
    paginate_by = 2

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
    #     return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'NewsApp/category.html', {'news': news, 'category': category})


# def view_news(request, news_id):
#     news_item = get_object_or_404(News, pk=news_id)
#     # news_item = News.objects.get(pk=news_id)
#     return render(request, 'NewsApp/view_news.html', {"news_item": news_item})


class ViewNews(DetailView):
    model = News
    pk_url_kwarg = 'news_id'
    template_name = 'NewsApp/class_news.html'
    context_object_name = 'news_item'


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'NewsApp/add_news.html', {'form': form})


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'NewsApp/add_news.html'
    login_url = '/admin/'
