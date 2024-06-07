import conftest
import pytest

pytestmark = pytest.mark.django_db


class TestMain:

    # check if pagination is true
    def test_entries_list_pagination(self, api_client, entries_with_same_user, user):
        response = api_client.get(conftest.ENDPOINT_ENTRY)
        assert response.status_code == 200
        assert response.data["page_size"] == 3
        assert response.data["total_pages"] == 2
        assert response.data["current_page_number"] == 1
        assert (
            response.data["links"]["next"]
            == "http://testserver/api/get-entries-list?page=2"
        )
        assert response.data["links"]["previous"] == None

    # check if the users of entries are the same
    def test_entries_users(self, api_client, entries_with_same_user, user):
        response = api_client.get(conftest.ENDPOINT_ENTRY)
        assert response.status_code == 200
        assert response.data["entries"][0]["username"] == "bakery_user"
        assert response.data["entries"][1]["username"] == "bakery_user"
        assert response.data["entries"][2]["username"] == "bakery_user"

    def test_entries_order(
        self, api_client, entries_with_same_user, user
    ):  # check entries and order
        response = api_client.get(conftest.ENDPOINT_ENTRY)
        assert response.status_code == 200
        assert response.data["entries"][0]["subject"] == "subject_04"
        assert response.data["entries"][1]["subject"] == "subject_03"
        assert response.data["entries"][2]["subject"] == "subject_02"
        assert response.data["entries"][0]["message"] == "message_04"
        assert response.data["entries"][1]["message"] == "message_03"
        assert response.data["entries"][2]["message"] == "message_02"
