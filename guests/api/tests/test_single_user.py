import conftest
import pytest

pytestmark = pytest.mark.django_db


class TestMain:

    def test_user(self, user):
        assert user.username == "bakery_user"

    def test_entry(self, entry):
        assert entry.subject == "bakery_subject"
        assert entry.message == "bakery_message"
        assert entry.user.username == "bakery_user"

    def test_entries_list_data(self, api_client, entry, user):
        response = api_client.get(conftest.ENDPOINT_ENTRY)
        assert response.status_code == 200  # indicates that request was successful
        assert len(response.data["entries"]) == 1
        assert response.data["entries"][0]["subject"] == "bakery_subject"
        assert response.data["entries"][0]["message"] == "bakery_message"
        assert response.data["entries"][0]["username"] == "bakery_user"

    def test_entries_list_pagination(self, api_client, entry, user):
        response = api_client.get(conftest.ENDPOINT_ENTRY)
        assert response.status_code == 200
        assert response.data["page_size"] == 3
        assert response.data["total_pages"] == 1
        assert response.data["current_page_number"] == 1
        assert response.data["links"]["next"] == None
        assert response.data["links"]["previous"] == None

    def test_users_list(self, api_client, user, entry):
        response = api_client.get(conftest.ENDPOINT_USER)
        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data["users"][0]["username"] == "bakery_user"
        assert (
            response.data["users"][0]["last_entry"] == "bakery_subject | bakery_message"
        )
