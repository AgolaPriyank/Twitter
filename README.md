
# Twitter

A simple Twitter-like application built using the Django framework in Python. This project allows users to register, log in, create, edit, and delete tweets. It also features authentication, a home button for easy navigation, and a user-friendly interface.

## Features

- **User Authentication:**
  - Users can register for a new account.
  - Users can log in and log out securely.
  
- **Tweet Management:**
  - Authenticated users can create, read, edit, and delete tweets.
  - Tweets are displayed in an easy-to-read format.

- **Navigation:**
  - Home button available for quick navigation to the main page.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/AgolaPriyank/Twitter.git
    cd twitter
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate    # On Windows, use: .venv\Scripts\activate
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the Server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the Application:**
    Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

- **Register**: Create a new account by providing your details.
- **Login**: Log in using your registered credentials.
- **Create Tweet**: Post a new tweet from the dashboard.
- **Edit/Delete Tweet**: Modify or delete your tweets.
- **Logout**: Log out securely when done.

## Requirements

- Python 3.8+
- Django 4.x
- Other dependencies listed in `requirements.txt`



