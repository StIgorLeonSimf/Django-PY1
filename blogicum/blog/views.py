from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from unicodedata import category

from .models import Post, Category
from .forms import BlogForm, PostForm

# posts = [
#     {'id': 1,
#      'title': 'Пост первый',
#      'text': """Однажды в студенную зимнюю пору
#                 я из лесу вышел был сильный мороз...""",
#      'category': 'Стихотворение'
#      },
#     {'id': 2,
#      'title': 'Собаке Качалова',
#      'text': """Дай Джим на счастье лапу мне
#              такую лапу не видал я сроду,
#              Давай с тобой полаем при луне ...""",
#      'category': 'Стихотворение'
#      },
#      {'id': 3,
#      'title': 'Белая гвардия',
#      'text': """«Всё пройдет. Страдания, муки, кровь,
#                 голод и мор. Меч исчезнет, а вот
#                 звезды останутся, когда и тени наших
#                 тел и дел не останется на земле».""",
#      'category': 'Роман'
#      },
# ]


def index(request):
    template = 'blog/index.html'
    # context = {'id': 1, 'name': 'Fist request'}
    # posts = Post.objects.all()
    posts = Post.objects.values('id', 'title', 'text' , 'category__title')
    posts = Post.objects.select_related('category')

    context = {'page_obj': posts}
    return render(request, template, context)

    #
    # return JsonResponse(d)
def detail(request, pk):
    template = 'blog/detail.html'
    object = Post.objects.get(pk=pk)
    context = {'object': object}
    return render(request, template, context)


def category(request, pk):
    template = 'blog/category_detail.html'
    object = Category.objects.get(pk=pk)
    context = {'object': object}
    return render(request, template, context)


def post_seek(request):
    template = 'blog/post_seek.html'
    form = BlogForm(request.GET or None)
    context = {'form': form}
    if form.is_valid():
        template = 'blog/index.html'
        page_obj = Post.objects.filter(title__contains=request.GET['title'])
        context = {'page_obj': page_obj}


    return render(request, template, context)


def post(request, pk=None):
    template = 'blog/post.html'
    if pk:
        instance = get_object_or_404(Post, pk=pk)
    else:
        instance = None
    form = PostForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        instance.save()
        # template = 'blog/index.html'
        # page_obj = Post.objects.all()
        # context = {'page_obj': page_obj}
        return redirect('blog:index')
    return render(request, template, context)


def delete_post(request, pk=None):
    template = 'blog/post.html'
    if pk:
        instance = get_object_or_404(Post, pk=pk)
    else:
        instance = None
    form = PostForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        instance.save()
        # template = 'blog/index.html'
        # page_obj = Post.objects.all()
        # context = {'page_obj': page_obj}
        return redirect('post:index')
    return render(request, template, context)
