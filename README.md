# Eventing
An app to organize events with friends or groups.

I have always struggled with my friends to organize an event: a chaotic group chat with dates, lists of things to buy and activity ideas all jumbled together. To make organizing events easier and more efficient, I created this app specifically for managing group events in one focused place.

## Project Status
Currently, the project is a Django REST API that retrieves data from a PostgreSQL database.

The main features include:

- User registration and authentication with secure password encryption via Django's Auth libraries.
- Endpoints for creating and retrieving events and associated tasks.
- Email verification for new user registration.
- Automated tests for all endpoints using Django’s testing framework.
- Continuous integration setup through GitHub Actions with CircleCI.

## Future Features
Planned features include:

- Adding/removing members from event tasks.
- Google Account authentication.
- Integration with Google Calendar API.
- Email notifications for event reminders and updates.
- File management capabilities for sharing event-related files.

## Installation
To set up the project locally:

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
