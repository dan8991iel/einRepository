# Webshop API

## Prerequisites

- Python 3.11.x

## Setting Up

Install all required dependencies:

```
pip install -r requirements.txt
```

Clone the `.env.template` file and rename it to `.env`.
In the new `.env` set all the required credentials.

For the Firebase Admin SDK, a service account is required.
Download the `firebase_service_account.json` from Teams and place it in the root directory of `api/`.
This file should not be publicly available in the repo.

## Running Dev Environment

```
flask --app api.py run
```
