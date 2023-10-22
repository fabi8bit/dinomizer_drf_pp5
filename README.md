# DINOMIZER

(foto)

nota foto

Dinomizer is built using Django Rest Framework for the backend and React JS for the frontend. This project was created as my fifth portfolio project for my Diploma in Web Application Development at Code Institute.

Dinomizer is a web application designed to assist Creative Agencies with teams dispersed globally or working remotely. This application streamlines asset retrieval for projects by centralizing all assets in one location. This ensures that all project stakeholders can access the latest version of required assets, thus minimizing time loss.

## Project Goals

- Full featured assets sharing service
- Create and partecipate to a project
- Upload assets like images, videos, audio and text
- Contribute to a project
- Get approvals by the project manager (project owner) on the assets uploaded

## Table of contents
- [Dinomizer](#dinomizer)
  * [Project goals](#project-goals)
  * [Table of contents](#table-of-contents)
  * [Planning and ideas](#planning)
  * [API endpoints](#api-endpoints)
    + [**Data models**](#data-models)
      - [Profile]()
      - [Project]()
      - [Asset](#--event--)
      - [Participant](#--notification--)
      - [Checks](#--contact--)
  
  * [Frameworks, libraries and dependencies](#frameworks--libraries-and-dependencies)
    + [django-cloudinary-storage](#django-cloudinary-storage)
    + [dj-rest-auth](#dj-rest-auth)
    + [djangorestframework-simplejwt](#djangorestframework-simplejwt)
    + [dj-database-url](#dj-database-url)
    + [psychopg2](#psychopg2)
    + [django-cors-headers](#django-cors-headers)
  * [Testing](#testing)
    + [Manual testing](#manual-testing)
    + [Automated tests](#automated-tests)
    + [Python validation](#python-validation)
    + [Bugs and Issues](#resolved-bugs)
  * [Deployment](#deployment)
  * [Credits](#credits)

## Planning and ideas
Dinomizer is based on the walkthrough project of the Code Institute Frontend module. The idea comes from my background experience in video production and comunication. I've immagined a comunication agency where all the members working on the same comunication project are dispersed in different physical places. They need to be on the same page and share all the contents they are working on. Dinomizer is the platform where they can share files, assets and ideas to carry out projects.
As a first step for the planning I streamlined all the project goals and tried to immagine all the possible user stories for the frontend application. Those are described in details in the [README](https://github.com/fabi8bit/dinomizer_react_pp5/blob/main/README.md) of the frontend application.
In order to support the user stories, and therefore the functionality of the application, I started to lay down the API endpoints.

## API Endpoints

| RESOURCE | URL       | END POINT                                                                              | CRUD / METHOD  | DATA                       | DESCRIPTION                                                                                               | MVP | USER STORIES                                                                                                   | NOTES                   |
| -------- | --------- | -------------------------------------------------------------------------------------- | -------------- | -------------------------- | --------------------------------------------------------------------------------------------------------- | --- | -------------------------------------------------------------------------------------------------------------- | ----------------------- |
| Profiles | /profiles | id,<br>owner,<br>created_at,<br>updated_at,<br>name,<br>content,<br>image,<br>is_owner | create/POST    | name,<br>content,<br>image | A profile is authomatically crated upon user creation when signing up                                     | YES | [#1](https://github.com/fabi8bit/dinomizer_react_pp5/issues/1),<br>[#2](),<br>[#3](),<br>[#6](),<br>[#7]()<br> |                         |
| Profiles | /profiles |                                                                                        | retrieve/GET   |                            | When a user clicks on the profile icon, can see the detail of the clicked profile                         | YES | [#28]()                                                                                                        |                         |
| Profiles | /profiles |                                                                                        | update/PUT     | name,<br>content,<br>image | If the user is the owner of the profile, can edit the details for his profile                             | YES | [#31](),<br>[#32]()                                                                                            |                         |
| Profiles | /profiles |                                                                                        | destroy/DELETE |                            | N/A implemented in the future                                                                             | NO  |                                                                                                                | Due to time constraints |
| Profiles | /profiles |                                                                                        | list/GET       |                            | It's used and filtered in the project page details, to list all the profiles contributing to that project | YES |                                                                                                                |




Permissions
The default permission policy is set globally, using the DEFAULT_PERMISSION_CLASSES setting in settings.py file:

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}


In order to acces the API the user must be logged in
In order to take advantage of the CRUD functionality the user must be logged in and be the owner of the object


Asset Model
An Asset is strictly connected to a project via a One to One relation.

Checks Model
The check is a special function inside the application, that allows a project manager to check a new asset or a new asset's update. If the logged in user is also the project owner of the project associated with the asset, then can give his thumb up with the check.


At the moment the option to delete profiles is not implemented due to time constraints

future implementations
- create an Organization that contains projects
- set a local storage to store original files (large size)
- create authomatic lowres file to display inside the app
- evaluate team capacity
- diagram that displays how busy a user is so as a project manager I can decide to whom assign a task
- side navbar for a more appealing user experience


side navbar
https://www.youtube.com/watch?v=IathdVB65Lw&t=217s