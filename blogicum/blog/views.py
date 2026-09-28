from django.shortcuts import render
from django.http import JsonResponse

posts = [
    {'id': 1,
     'title': 'Пост первый',
     'text': """Однажды в студенную зимнюю пору 
                я из лесу вышел был сильный мороз...""",
     'category': 'Стихотворение'
     },
    {'id': 2,
     'title': 'Собаке Качалова',
     'text': """Дай Джим на счастье лапу мне
             такую лапу не видал я сроду,
             Давай с тобой полаем при луне ...""",
     'category': 'Стихотворение'
     },
     {'id': 3,
     'title': 'Белая гвардия',
     'text': """«Всё пройдет. Страдания, муки, кровь, 
                голод и мор. Меч исчезнет, а вот 
                звезды останутся, когда и тени наших 
                тел и дел не останется на земле».""",
     'category': 'Роман'
     },
]


def index(request):
    template = 'blog/index.html'
    # context = {'id': 1, 'name': 'Fist request'}
    context = {'page_obj': posts}
    return render(request, template, context)

    #
    # return JsonResponse(d)
def detail(request, pk):
    template = 'blog/detail.html'
    context = {'object': posts[pk-1]}
    return render(request, template, context)