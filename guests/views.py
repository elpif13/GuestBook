import math

from django.core.paginator import Paginator
from django.db.models import Count, F, Max
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import EntryForm
from .models import Entry, User


def home(request):

    return render(request, "home.html")


def create_entry(request):  # form for creating a new entry

    form = EntryForm()

    if request.method == "POST":
        username = request.POST.get("username")
        user, created = User.objects.get_or_create(
            username=username
        )  # if the user already exists then it will not be created

        Entry.objects.create(
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
            user=user,  # Assigning the user object retrieved or created
        )
        return redirect(
            "home"
        )  # after click the submit button, user will be redirected to the home page

    return render(
        request,
        "entry_form.html",
        {"form": form},
    )


def entries_list(
    request,
):  # list all entries according to creation date, pagination: 3 items per page

    entries = Entry.objects.all().order_by("-created_entry")
    paginator = Paginator(entries, 3)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "entries_list.html",
        {"page_obj": page_obj, "entries": entries},
    )


def get_user_data(request, pk):  # return single user's latest entry

    try:
        user = User.objects.get(id=pk)
    except (
        User.DoesNotExist
    ):  # if the user with given id does not exist we will redirect to the home page
        return redirect("home")
    except Exception as e:  # for other exceptions
        return HttpResponse("Exception: " + str(e))

    countOfMessages = Entry.objects.filter(user=user).count

    latest_entry = (
        Entry.objects.filter(user=user)
        .order_by("-created_entry")
        .values("subject", "message")
        .first()
    )

    context = {
        "username": user.username,
        "countOfMessages": countOfMessages,
        "subjectOfLastEntry": latest_entry["subject"],
        "messageOfLastEntry": latest_entry["message"],
    }

    return render(request, "user_data.html", context)


def users_list(request):  # return all users' latest entry

    entries = (
        User.objects.prefetch_related("user_entries")  # join using prefetch_related
        .annotate(entry_date=Max("user_entries__created_entry"))
        .filter(user_entries__created_entry=F("entry_date"))
        .values("username", "user_entries__subject", "user_entries__message")
    )

    return render(
        request,
        "users_list.html",
        {"entries": entries},
    )
