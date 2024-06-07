import conftest
import pytest

pytestmark = pytest.mark.django_db


class TestMain:
    def test_entry_without_subject(self, api_client, entry_without_subject):
        data = {
            "username": entry_without_subject.user.username,
            "user_entry": {"message": entry_without_subject.message},
        }
        response = api_client.post(conftest.ENDPOINT_CREATE, data, format="json")
        assert response.status_code == 400
        print(response.data)
        assert response.json() == {
            "user_entry": {"subject": ["This field is required."]}
        }

    def test_entry_with_empty_subject(self, api_client, entry_with_empty_subject):
        data = {
            "username": entry_with_empty_subject.user.username,
            "user_entry": {
                "subject": entry_with_empty_subject.subject,
                "message": entry_with_empty_subject.message,
            },
        }
        response = api_client.post(conftest.ENDPOINT_CREATE, data, format="json")
        assert response.status_code == 400
        print(response.data)
        assert response.json() == {
            "user_entry": {"subject": ["This field may not be blank."]}
        }

    def test_entry_without_message(self, api_client, entry_without_message):
        data = {
            "username": entry_without_message.user.username,
            "user_entry": {
                "subject": entry_without_message.subject,
            },
        }
        response = api_client.post(conftest.ENDPOINT_CREATE, data, format="json")
        assert response.status_code == 400
        assert response.json() == {
            "user_entry": {"message": ["This field is required."]}
        }

    def test_entry_with_empty_message(self, api_client, entry_with_empty_message):
        data = {
            "username": entry_with_empty_message.user.username,
            "user_entry": {
                "subject": entry_with_empty_message.subject,
                "message": entry_with_empty_message.message,
            },
        }
        response = api_client.post(conftest.ENDPOINT_CREATE, data, format="json")
        assert response.status_code == 400
        assert response.json() == {
            "user_entry": {"message": ["This field may not be blank."]}
        }

    def test_entry_without_user(self, api_client, entry_without_user):
        data = {
            "user_entry": {
                "subject": entry_without_user.subject,
                "message": entry_without_user.message,
            }
        }
        response = api_client.post(conftest.ENDPOINT_CREATE, data, format="json")
        assert response.status_code == 400
        assert response.json() == {"username": ["This field is required."]}

    def test_entry_without_username(self, api_client, entry_without_username):
        data = {
            "username": entry_without_username.user.username,
            "user_entry": {
                "subject": entry_without_username.subject,
                "message": entry_without_username.message,
            },
        }
        response = api_client.post(conftest.ENDPOINT_CREATE, data, format="json")
        assert response.status_code == 400
        assert response.json() == {
            "username": ["Ensure this field has no more than 127 characters."]
        }

    def test_entry_with_empty_username(self, api_client, entry_with_empty_username):
        data = {
            "username": entry_with_empty_username.user.username,
            "user_entry": {
                "subject": entry_with_empty_username.subject,
                "message": entry_with_empty_username.message,
            },
        }
        response = api_client.post(conftest.ENDPOINT_CREATE, data, format="json")
        assert response.status_code == 400
        assert response.json() == {"username": ["This field may not be blank."]}
