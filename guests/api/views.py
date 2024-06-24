import math

from django.db.models import CharField, F, Max, Value
from django.db.models.functions import Concat
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from guests.models import Entry, User

from .serializers import CreateEntrySerializer, EntrySerializer

from django.db import connection

# class based views are views as pyhton objects


# returns all entries according to their creation date
class EntriesListView(ListAPIView):

    # every user will be able to see all the messages, but only logged-in users will be able to add, change, or delete objects.
    permission_classes = (AllowAny,)
    pagination_class = PageNumberPagination
    serializer_class = EntrySerializer
    queryset = Entry.objects.all()

    def list(self, request, *args, **kwargs):
        # override list method provided by generics.ListAPIView, this method will be called when the view is accessed with a GET request
        page = self.paginate_queryset(self.queryset)  # pagination
        serializer_class = self.serializer_class(page, many=True)
        count = self.queryset.count()
        response_data = {
            "count": count,
            "page_size": self.pagination_class.page_size,
            "total_pages": math.ceil((count / self.pagination_class.page_size)),
            "current_page_number": (int)(self.request.query_params.get("page", 1)),
            "links": {
                "next": self.paginator.get_next_link(),
                "previous": self.paginator.get_previous_link(),
            },
            "entries": serializer_class.data,
        }

        return Response(response_data)


# returns each user's last entry
class UsersListView(ListAPIView):  # permission

    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):

        entries = (  # ------ main logic ---------
            (
                User.objects.prefetch_related(
                    "user_entries"
                )  # join using prefetch_related, reverse foreign key relationship
                .annotate(entry_date=Max("user_entries__created_entry"))
                .filter(user_entries__created_entry=F("entry_date"))
                .values("username", "user_entries__subject", "user_entries__message")
            )  # ---------------------------------
            .annotate(  # for concat subject and message
                last_entry=Concat(
                    "user_entries__subject",
                    Value(" | "),
                    "user_entries__message",
                    output_field=CharField(),
                ),
            )
            .values("username", "last_entry")
        )
        print(entries.query)
        entries = {"users": entries}
        return Response(entries)


class EntryCreateView(CreateAPIView):
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = CreateEntrySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"success": True}, status=status.HTTP_200_OK)


class UrlDataView(ListAPIView):  # using kwargs for getting data from url

    def list(self, request, *args, **kwargs):

        data = self.kwargs.get("data")  # get is more safe
        print(data)

        return Response(data)
