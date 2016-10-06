from django.shortcuts import render, get_object_or_404
from .models import Author
from verse.models import Verse

# Create your views here.
def author_detail(request, author_id, author_slug=None):
    author = None
    authors = Author.objects.all()
    verses = Verse.objects.all()
    if author_slug:
        author = get_object_or_404(Author, id=author_id, slug=author_slug)
        verses = verses.filter(author = author)
    return render(request, "author/detail.html", {"author": author,
                                                  "authors": authors,
                                                  "verses": verses,
                                                  "section": "author_list"})
