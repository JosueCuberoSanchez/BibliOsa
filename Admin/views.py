from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.http import JsonResponse
import isbnlib
from django.contrib.auth.models import User
from django.template import RequestContext
from django.urls import reverse

from SoftwareBiblio.models import Book, Author, UnregisteredUser, Administrator, RegisteredUser, BookCover
from django.core.mail import EmailMessage
from SoftwareBiblio.forms import ImageForm


def admin_save_book_cover(request):
    saved = False
    if request.method == "POST":
        # Get the posted form
        MyPhotoForm = ImageForm(request.POST, request.FILES)
        if MyPhotoForm.is_valid():
            image = BookCover()
            image.image = MyPhotoForm.cleaned_data["picture"]
            book_isbn = MyPhotoForm.cleaned_data["book_isbn"]
            image.save()
            book = Book.objects.get(ISBN=book_isbn)
            book.cover = image
            book.save()
            saved = True
    else:
        MyImageForm = ImageForm()

    return render(request, '../templates/Admin/admin-editBook.html', locals())


def admin_send_invite(request):
    email = request.GET.get('email', None)
    try:
        user = UnregisteredUser.objects.get(email=email)
        response = "Ya se ha enviado una invitación a esta dirección antes."
        data = {'response': response}
        return JsonResponse(data)
    except UnregisteredUser.DoesNotExist:
        try:
            user = User.objects.get(email=email)
            try:
                user = Administrator.objects.get(user=user)
                response = "Esta dirección corresponde a un administrador."
                data = {'response': response}
                return JsonResponse(data)
            except Administrator.DoesNotExist:
                response = "Se ha enviado una invitación a " + email
                data = {'response': response}
                unregisteredUser = UnregisteredUser(email=email)
                unregisteredUser.save()
                mail = EmailMessage('Invitación para ser administrador de BibliOsa',
                                    'Usted ha sido invitado como administrador'
                                    'de BibliOsa, por favor siga este enlace y proceda a entrar con'
                                    ' sus credenciales de Google:\n127.0.0.1:8000'
                                    '', to=[email])
                mail.send()
                return JsonResponse(data)
        except User.DoesNotExist:
            response = "Se ha enviado una invitación a " + email
            data = {'response': response}
            unregisteredUser = UnregisteredUser(email=email)
            unregisteredUser.save()
            mail = EmailMessage('Invitación para ser administrador de BibliOsa',
                                'Usted ha sido invitado como administrador'
                                'de BibliOsa, por favor siga este enlace'
                                'y proceda a entrar con sus credenciales '
                                'de Google:\n127.0.0.1:8000'
                                '', to=[email])
            mail.send()
            return JsonResponse(data)


@login_required
def admin_dashboard(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-dashboard.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_profile(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-profile.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_about(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-about.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_add_device(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-addDevice.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_admin_search(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-adminSearch.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_book(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-book.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_contact_admins(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-contactAdmins.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_contact_developers(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-contactDevelopers.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_devices(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-Devices.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_edit_admin_profile(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-editAdminProfile.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_edit_book(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-editBook.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_edit_my_profile(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-editMyProfile.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_edit_reader_profile(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-editReaderProfile.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_genre(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-genre.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_invite_admin(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-inviteAdmin.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_loan_page(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-loanPage.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_make_loan(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-makeLoan.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_manual_add(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-manualAdd.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_my_profile(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-myProfile.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_reader_profile(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-readerProfile.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_reader_search(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-readerSearch.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_search_results(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-readerSearchResults.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_terms_of_use(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-termsOfUse.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_view_loans(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-viewLoans.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_g_management(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin_g_management.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def admin_user_search(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-userSearch.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


@login_required
def book_management(request):
    user = request.user
    email = user.email
    try:
        admin = Administrator.objects.get(user=User.objects.get(email=email))
        return render(request, '../templates/Admin/admin-bookManagement.html')
    except Administrator.DoesNotExist:
        return HttpResponseForbidden()


def smart_add(request):
    isbn = request.GET.get('isbn', None)

    if isbnlib.notisbn(isbn):
        data = {
            'is_valid': False
        }
    else:
        bookInfo = isbnlib.meta(isbn)  # Datos que provee meta: Title Authors Publisher Language
        cover = isbnlib.cover(isbn)
        bookInfo = isbnlib.meta(isbn)  # Datos que provee meta: Title Authors Publisher Language
        try:
            alreadyAdded = False
            book = Book()
            book.title = bookInfo['Title']
            book.publisher = bookInfo['Publisher']
            book.ISBN = isbn
            if Book.objects.filter(ISBN=isbn).count() > 0:
                alreadyAdded = True
                print("repetido")
            else:
                book.save()
                handleAuthors(book, bookInfo['Authors'])

            if cover:  # COMPLETAR
                print("si")
            else:
                print("no")

            data = {
                'is_valid': True,
                'already_added': alreadyAdded,
                'title': bookInfo['Title'],
                'publisher': bookInfo['Publisher'],
                'isbn': isbn,
            }
        except TypeError:
            print("Type Error")
            data = {
                'is_valid': False,
                'publisher': bookInfo['Publisher']
            }
        except TypeError:
            data = {
                'is_valid': False
            }

    return JsonResponse(data)


def handleAuthors(book, authors):
    for author in authors:
        dbAuthor = Author.objects.filter(fullName=author)
        if dbAuthor.count() == 0:
            newAuthor = Author()
            newAuthor.fullName = author
            newAuthor.save()
            book.authors.add(newAuthor)
            book.save()
        else:
            dbAuthor = Author.objects.get(fullName=author)
            book.authors.add(dbAuthor)
            book.save()


'''def addBookCover(url, book):
    bookCover = BookCover()
    save_image_from_url(BookCover.image, url)
    book.save()

def save_image_from_url(field, url):
    bookCover = BookCover()
    bookCover.url = url
    bookCover.save()
    bookCover.get_remote_image()'''