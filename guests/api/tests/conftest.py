import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from guests.models import Entry, User

ENDPOINT_ENTRY = "/api/get-entries-list"
ENDPOINT_USER = "/api/get-users-list"
ENDPOINT_CREATE = "/api/create-user"


@pytest.fixture
def api_client():
    yield APIClient()


@pytest.fixture
def user():  # create single user
    yield baker.make(User, username="bakery_user")


@pytest.fixture
def users():  # create multiple users
    users = []
    users.append(baker.make(User, username="user_01"))
    users.append(baker.make(User, username="user_02"))
    users.append(baker.make(User, username="user_03"))
    users.append(baker.make(User, username="user_04"))
    yield users


@pytest.fixture
def user_without_username():
    yield baker.make(User)


@pytest.fixture
def user_with_empty_username():
    yield baker.make(User, username="")


@pytest.fixture
def entry_without_user():
    yield baker.make(Entry, subject="bakery_subject", message="bakery_message")


@pytest.fixture
def entry_without_username(user_without_username):
    yield baker.make(
        Entry,
        user=user_without_username,
        subject="bakery_subject",
        message="bakery_message",
    )


@pytest.fixture
def entry_with_empty_username(user_with_empty_username):
    yield baker.make(
        Entry,
        user=user_with_empty_username,
        subject="bakery_subject",
        message="bakery_message",
    )


@pytest.fixture
def entry_without_subject(user):
    yield baker.make(Entry, user=user, message="bakery_message")


@pytest.fixture
def entry_with_empty_subject(user):
    yield baker.make(Entry, user=user, subject="", message="bakery_message")


@pytest.fixture
def entry_without_message(user):
    yield baker.make(Entry, user=user, subject="bakery_subject")


@pytest.fixture
def entry_with_empty_message(user):
    yield baker.make(Entry, user=user, subject="bakery_subject", message="")


@pytest.fixture
def entry(user):  # create single entry
    yield baker.make(
        Entry, user=user, subject="bakery_subject", message="bakery_message"
    )


@pytest.fixture
def entries_with_same_user(user):  # create multiple entries with same user
    entries = []
    entries.append(
        baker.make(Entry, user=user, subject="subject_01", message="message_01")
    )
    entries.append(
        baker.make(Entry, user=user, subject="subject_02", message="message_02")
    )
    entries.append(
        baker.make(Entry, user=user, subject="subject_03", message="message_03")
    )
    entries.append(
        baker.make(Entry, user=user, subject="subject_04", message="message_04")
    )
    yield entries


@pytest.fixture
def entries_with_diff_users(users):  # create multiple entries with different users
    entries = []
    entries.append(
        baker.make(Entry, user=users[0], subject="subject", message="message")
    )
    entries.append(
        baker.make(Entry, user=users[1], subject="subject", message="message")
    )
    entries.append(
        baker.make(Entry, user=users[2], subject="subject", message="message")
    )
    entries.append(
        baker.make(Entry, user=users[3], subject="subject", message="message")
    )
    yield entries
