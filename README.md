# Soul Base Studio Booking App

This app will allow users to book classes for this pilates/dance studio.


# User Experience (UX)

## User Stories:
**Planning of user stories completed in Google sheets:
[Google sheet](https://docs.google.com/spreadsheets/d/13gqPIhIq3JW8bj4yZG445GtfKLTm_jc08hKC8qQwt5g/edit?usp=sharing)

**User Stories within Projects on GitHub Repository:
[Soul Base User Story Project](https://github.com/users/morganoleary/projects/4/views/1)

## Design:

## Wireframes:
[Figma wireframe](https://www.figma.com/file/XGDgyLpX0MTIs4UjGJEWSk/Studio-Booking-Site?type=design&node-id=0%3A1&mode=design&t=AFRhMGkel6QpeZO6-1)

## ERD:
[LucidChart ERD](https://lucid.app/lucidchart/e9b3c27f-07d4-4026-b261-0147bd63587b/edit?viewport_loc=-990%2C-136%2C2368%2C1186%2C0_0&invitationId=inv_e64b0370-8313-4ba3-ae26-527c2fb98352)

# Existing Features

## Future Features

# Testing

## Validator Testing:

## Manual Testing:

## Automated Testing:

## Bugs/Unfixed Bugs:
- Fixed: When creating my apps, I decided I needed to separate my models for member details from the class details and booking models in a separate app. I changed the name of my original 'book' app to 'member' as this already contained my Member and MemberLogin models that had been migrated to the database and deployed on Heroku. I followed the steps and successfully changed the name of the app by utilizing the [django-rename-app](https://github.com/odwyersoftware/django-rename-app?tab=readme-ov-file).

# Deployment

## Steps taken to deploy on Heroku:
Set up the workspace:
1. Install gunicorn in workspace for Heroku deployment
2. Add to requirements.txt and create Procfile
3. In settings.py set DEBUG = False
4. Git add, commit and push changes to GitHub
Deploy on Heroku:
5. Create the app on Heroku and connect to GitHub project
6. Set the Config Vars in the "Settings" Tab
7. Navigate to the "Deploy" tab and scroll down to click on "Deploy Branch" in the "Manual deploy" section

## Fork Repository

## Clone Repository

# Credits
### Help with settings.py:
- Student support on Slack was very helpful setting up database configurations in the settings.py file.
- [Creating a Database](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+2023_Q3/courseware/56a2da0940b4411d8a38c2b093a22c60/ed8c75412c784bbba17988f7efbe037b/?child=first) content in the "I Think Therefore I Blog" walkthrough was utilized to create the database. 
### Help with Django:
- [Django Documentation](https://docs.djangoproject.com/en/5.0/)

### Content
Soul Base Pilates Studio - My sister's pilates studio based in Iowa, USA.

### Technologies Used
LucidChart = ERD
Figma = Wireframes
Django = Framework
HTML = mark up
CSS = styling
Bootstrap = styling
Python
JavaScript
VS Code = IDE (Integrated Development Environment)
Heroku = Deployment
GitHub = store project
Git = version control
[PostgresSQL from Code Institute](https://dbs.ci-dbs.net/) = Production database 

### Media & Layout

## Acknowledgements
