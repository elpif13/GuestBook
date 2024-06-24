# GuestBook Backend API

This repository contains the backend implementation of a GuestBook. It provides functionalities to create and manage guestbook entries and users.

## Features

 + Create guestbook entries
 + Fetch latest guestbook entries with pagination
 + Fetch user data including the total count of messages and details of the user's last entry
 + Table Structure

### User
 + Name: string - The name of the user
 + Created Date: datetime - The date the user was created
### Entry
 + Subject: string - The subject of the entry
 + Message: string - The message content of the entry
 + Created Date: datetime - The date the entry was created
 + User: foreign key - A reference to the user who created the entry

## Testing
 This project uses [pytest](https://docs.pytest.org/en/8.2.x/) for testing and [model_bakery](https://model-bakery.readthedocs.io/en/latest/#) for generating test data.

## API Endpoints

1. Create Entry : This endpoint allows the end user to add a new entry by providing a name, subject, and message. For each new unique name, a new user is created in the database.
 + Endpoint: /api/create-entry
 + Method: POST

**Request Body:**
```
{
  "name": "John Doe",
  "subject": "Hello World",
  "message": "This is a test message"
}
```

2. Get Entries : This endpoint returns a list of the latest guestbook entries, with pagination (3 items per page). The entries are ordered by the created date in descending order.
 + Endpoint: /api/get-entries-list
 + Method: GET

 Query Parameters:
  + page: The page number to retrieve (default is 1)

**Response:**
```
{
  "count": 3,
  "page_size": 3,
  "total_pages": 1,
  "current_page_number": 1,
  "links": {
    "next": null,
    "previous": null
  },
  "entries": [
    {
      "user": "John Doe",
      "subject": "Hello World",
      "message": "This is a test message"
    },
    {
      "user": "Jane Smith",
      "subject": "Greetings",
      "message": "Nice to meet you"
    }
  ]
}
```

3. Get Users Data : This endpoint returns data for each user, including the total count of messages and details of the user's last entry. The last entry includes the subject and message concatenated by a '|'. Pagination is not applied to this endpoint.
 + Endpoint: /api/users
 + Method: GET

**Response:**
```
{
  "users": [
    {
      "username": "John Doe",
      "last_entry": "Hello World | This is a test message"
    },
    {
      "username": "Jane Smith",
      "last_entry": "Greetings | Nice to meet you"
    }
  ]
}

```
