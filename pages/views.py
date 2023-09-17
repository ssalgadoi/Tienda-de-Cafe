from django.shortcuts import render, get_list_or_404
from .models import Page
# Create your views here.

def page(request, page_id):
    page = get_list_or_404(Page, id=page_id)
    return render(request, 'page/sample.html', { 'page': page })