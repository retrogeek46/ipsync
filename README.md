# IPSync
This project aims to help in automatically syncing devices on local network by fetching the IP address of server from cloud.

When a user logs into a server using IPSync, the server's localIP will be saved on a cloud IPSync instance against user+server project details.

For example, if there is a local project Retro's Utility Server running on 192.168.1.4:4200, then IPSync will save 192.168.1.4.

The user can then log into the client application that connects to the local server and fetch connection details from IPSync.

### Installation
- Create virtual environment with `python3 -m venv venv`
- Activate venv with
    - Windows: `source venv/Scripts/activate` 
    - Macos/Linux: `source venv/bin/activate`
- **TODO**: have requirements.txt for pip install
- Install `django` and `djangorestframwework` in the venv
    - `pip install django djangorestframework`
- Run migrations with `python manage.py makemigrations && python manage.py migrations`

### Run
- Run the django server with `python manage.py runserver`

### Endpoints
- getData: test endpoint
- getUser: for debugging only, I guess
- getProject: gets project for user after logging in
- getIP: gets server IP based on user and project
- setIP: sets serverIP based on user and project
