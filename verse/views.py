from django.shortcuts import render, get_object_or_404
from .models import Verse
from author.models import Author
from comment.models import Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from comment.forms import CommentModelForm
from django.views.decorators.http import require_POST
from django.contrib import messages
# Create your views here.

authors = Author.objects.all()

def verse_list(request, author_slug=None):
    author = None
    # section = "main"
    verses = Verse.objects.all()
    section = "verse_list"
    if author_slug:
        author = get_object_or_404(Author, slug = author_slug)
        verses = verses.filter(author = author)
        section = "verse_list_by_author"
    return render(request, "verse/list.html", {"author": author,
                                               "authors": authors,
                                               "verses": verses,
                                               "section": section})

def verse_detail(request, verse_id, verse_slug):
    verse = get_object_or_404(Verse,
                              id = verse_id,
                              slug = verse_slug)
    # handles even with verses that do not contain comments
    comments = Comment.objects.filter(verse=verse, active=True)
    return render(request, "verse/detail.html", {"author": verse.author,
                                                 "authors": authors,
                                                 "verse": verse,
                                                 "comments": comments})

@login_required
@require_POST
def verse_comment(request, verse_id, verse_slug):
    text = request.POST["text"]
    verse = get_object_or_404(Verse, id=verse_id, slug=verse_slug)
    user = get_object_or_404(User, id=request.session["user_id"], username=request.session["username"])
    Comment.objects.create(verse = verse,
                           user = user,
                           text = text)
    messages.info(request, "Добавлен комментарий пользователем {}".format(user))
    return JsonResponse({"status": "comment added"})


@login_required
@require_POST
def verse_like(request, verse_id, verse_slug):
    verse = get_object_or_404(Verse, id=verse_id, slug=verse_slug)
    user = get_object_or_404(User, id=request.session["user_id"], username=request.session["username"])
    action = request.POST.get("action")
    if verse and action:
        try:
            if action == "like":
                verse.users_like.add(user)
                messages.info(request, 'Вам нравится произведение "{}"'.format(verse))
            else:
                verse.users_like.remove(user)
                messages.info(request, 'Вам больше не нравится произведение "{}"'.format(verse))
            return JsonResponse({"status": "ok"})
        except:
            pass
    return JsonResponse({"status": "not ok"})


@login_required
@require_POST
def send_verse_by_email(request, verse_id, verse_slug):
    """
    from django.core.mail import send_mail

    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
    """
    user = User.objects.get(username = request.session["username"], id = request.session['user_id'])
    verse = Verse.objects.get(id = verse_id, slug = verse_slug)
    author = verse.author
    mail = send_mail("//Verses. {}".format(verse.title), verse.text, 'cestusss@gmail.com', [user.email,], fail_silently=False,)
    if mail:
        messages.success(request, "Письмо было успешно отрпавлено на {}".format(user.email))
        return JsonResponse({"status": "Email sent successfully"})
    else:
        messages.error(request, "Произошла ошибка при отправке письма!")
        return JsonResponse({"status": 'An error occured during email sending. Please, check email address and settings'})
