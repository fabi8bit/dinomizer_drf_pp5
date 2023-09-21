README.md

DINOMIZER

(foto)

nota foto
Dinomizer is built using Django Rest Framework for the backend and React JS for the frontend. This project was created as my fifth portfolio project for my Diploma in Web Application Development at Code Institute.

Dinomizer is a web application designed to assist Creative Agencies with teams dispersed globally or working remotely. This application streamlines asset retrieval for projects by centralizing all assets in one location. This ensures that all project stakeholders can access the latest version of required assets, thus minimizing time loss.

Project Goals

- Full featured assets sharing service
- Create and partecipate to a project
- Create and Upload assets like images, videos, texts
- Contribute to a project
- Get comments and approvals on your contributions


Permissions
The default permission policy is set globally, using the DEFAULT_PERMISSION_CLASSES setting in settings.py file:

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}


In order to acces the API the user must be logged in
In order to take advantage of the CRUD functionality the user must be logged in and be the owner of the object


future implementations
- create an Organization that contains projects
- set a local storage to store original files (large size)
- create authomatic lowres file to display inside the app
- evaluate team capacity
- diagram that displays how busy a user is so as a project manager I can decide to whom assign a task


side navbar
https://www.youtube.com/watch?v=IathdVB65Lw&t=217s