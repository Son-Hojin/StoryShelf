from django.shortcuts import render

from app_storyshelf.models import W_Saying
from app_storyshelf.models import Content

from . import quote
import random
import datetime

from app_storyshelf.forms import ContentForm
from django.http import HttpResponseRedirect

from django.core.paginator import Paginator

# Create your views here.



def main(request):
    if W_Saying.objects.count() == 0 or \
            W_Saying.objects.first().created_at.month != datetime.datetime.now().month:
        if W_Saying.objects.count() != 0:
            for i in range(W_Saying.objects.count()):
                item = W_Saying.objects.get(pk=i+1)
                item.delete()

        saying_list = quote.make_list()
        for s in saying_list:
            # if W_Saying.objects.filter(saying =s["saying"]).values() == None:
            W_Saying(saying=s["saying"], author=s["author"]).save()

    rand_num = random.randrange(W_Saying.objects.count())
    saying = W_Saying.objects.get(pk=rand_num+1).saying
    author = W_Saying.objects.get(pk=rand_num+1).author
    while len(saying) > 150:
        rand_num = random.randrange(1, W_Saying.objects.count() + 1)
        saying = W_Saying.objects.get(pk=rand_num).saying
        author = W_Saying.objects.get(pk=rand_num).author

    context = {
        "saying": saying,
        "author": author,
    }
    return render(request, 'app_storyshelf/main.html', context)


def write(request):
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            new_content = form.save()
        return HttpResponseRedirect('/app_storyshelf/read')
    form = ContentForm()
    return render(request, 'app_storyshelf/write.html', {'form': form})

def read(request):
    Content.objects.order_by("-created_at")
    contents = Content.objects.all()
    paginator = Paginator(contents, 4)

    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'contents': items
    }
    return render(request, "app_storyshelf/read.html", context)