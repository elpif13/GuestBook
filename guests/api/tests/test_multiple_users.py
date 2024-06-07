import conftest
import pytest

pytestmark = pytest.mark.django_db


class TestMain:

    def test_entries_list_pagination(self, api_client, entries_with_diff_users, users):
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

    # test users of each entries and also check whether order is correct
    def test_entries_users(self, api_client, entries_with_diff_users, users):
        response = api_client.get(conftest.ENDPOINT_ENTRY)
        assert response.status_code == 200
        assert (
            response.data["entries"][0]["username"] == "user_04"
        )  # latest user is the first by order
        assert response.data["entries"][1]["username"] == "user_03"
        assert response.data["entries"][2]["username"] == "user_02"
