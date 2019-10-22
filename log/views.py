from django.views import generic
from .models import Article

class top(generic.ListView):
    model = Article
