from django.shortcuts import render
from .models import Post

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts': posts})

def category(recuest, category_id):
    category = Ctegory.objects.get(id=catgory_id)
    return render (request, "blog/category.html", { 'category': category })