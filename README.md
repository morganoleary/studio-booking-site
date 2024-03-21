# Soul Base Studio Booking App

This app will allow users to book classes for this pilates/dance studio.


# User Experience (UX)

## User Stories:
**Planning of user stories completed in Google sheets:
[Google sheet](https://docs.google.com/spreadsheets/d/13gqPIhIq3JW8bj4yZG445GtfKLTm_jc08hKC8qQwt5g/edit?usp=sharing)

**User Stories within Projects on GitHub Repository:
[Soul Base User Story Project](https://github.com/users/morganoleary/projects/4/views/1)

## Design:
- The design was taken from the already created logo of Soul Base Pilates.

## Wireframes:
[Figma wireframe](https://www.figma.com/file/XGDgyLpX0MTIs4UjGJEWSk/Studio-Booking-Site?type=design&node-id=0%3A1&mode=design&t=AFRhMGkel6QpeZO6-1)

## ERD:
[LucidChart ERD](https://lucid.app/lucidchart/e9b3c27f-07d4-4026-b261-0147bd63587b/edit?viewport_loc=-990%2C-136%2C2368%2C1186%2C0_0&invitationId=inv_e64b0370-8313-4ba3-ae26-527c2fb98352)

# Existing Features

## Future Features

- In future implementations, the admin will have the ability to send class reminder emails to all members with upcoming bookings.
- A gallery page will be implemented to provide the user with more understanding of the studio.
- The location of the studio will be displayed with a Google map view on the site's home page.
- As a future enhancement, as the studio begins to grow, class bookings will be limited by the capacity of members each class is able to hold.

# Testing

## Validator Testing:

- W3C CSS Validator:
- W3C Markup Validation:

## Manual Testing:

Testing the contact form:
- This was tested by submitting a contact request. When attempting to submit the form without the *required fields, the user is unable to submit and receives a request to fill in the missing, required field.
- The contact form works correctly for both logged in users as well as visitors who are not logged in.
- The admin site is updated correctly with the required fields and optional fields, when completed. All contact request details are stored in the admin dashboard under Contact Requests in the Contact section.

User login & logout:
- When a user logs out, they are automatically redirected to the home page. This applies for both site users as well as superusers.
- When a user logs into their previously created account, they are automatically redirected to the home page. From here the user can easily navigate the site to book a class, see their profile page or find out more about the studio from the navbar.

## Bugs/Unfixed Bugs:
- Fixed: When creating my apps, I decided I needed to separate my models for member details from the class details and booking models in a separate app. I changed the name of my original 'book' app to 'member' as this already contained my Member and MemberLogin models that had been migrated to the database and deployed on Heroku. I followed the steps and successfully changed the name of the app by utilizing the [django-rename-app](https://github.com/odwyersoftware/django-rename-app?tab=readme-ov-file).
- Fixed: When implementing Django signals into the "member" app when trying to create a user profile for each user that signs up, I received the following error: django.core.exceptions.ImproperlyConfigured: Application labels aren't unique, duplicates: member . After researching, I was able to fix the problem my removing the 'member' in INSTALLED_APPS of the Settings file. This was found using [Stack Overflow](https://stackoverflow.com/questions/24319558/how-to-resolve-django-core-exceptions-improperlyconfigured-application-labels).

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

Forking a repository allows you to create a copy to GitHub, and any changes made will not affect the original repository:

- Within GitHub, navigate to the repository page you are going to fork
- Click "Fork" on the top right corner of the page
- Wait for the copy to be created and you are then redirected to the forked repository

## Clone Repository

Cloning a repository allows you to create a local copy of a repository on your machine:

- Within GitHub, navigate to the repository you are wanting to clone
- Click the green "<>Code" button
- Within the "Local" tab, copy the HTTPS url
- In your IDE, open Git Bash and type in 'git clone' followed by the pasted url just copied from GitHub. Ex: git clone https://example.com/repository/project
- The clone has been created on your local machine

# Credits
- Student support on Slack was very helpful setting up database configurations in the settings.py file.
- [Creating a Database](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+2023_Q3/courseware/56a2da0940b4411d8a38c2b093a22c60/ed8c75412c784bbba17988f7efbe037b/?child=first) content in the "I Think Therefore I Blog" walkthrough was utilized to create the database. 
- From the 'I think therefore I blog' walkthrough project, [Django Walkthrough Project / Setting up the base template](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+2023_Q3/courseware/56a2da0940b4411d8a38c2b093a22c60/c592ed45498e440587b764e29891b2fc/?child=first) was helpful when creating the base template.
- [Django Documentation](https://docs.djangoproject.com/en/5.0/)
- From the 'I think therefore I blog' walkthrough project, [Deployment with static files](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+2023_Q3/courseware/56a2da0940b4411d8a38c2b093a22c60/c592ed45498e440587b764e29891b2fc/?child=first) was utilized to ensure successful deployment after creating static files.
- From the 'I think therefore I blog' walkthrough project, [Django AllAuth Authentication](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+2023_Q3/courseware/56a2da0940b4411d8a38c2b093a22c60/8354ed2193944d4ea9aa167849113da7/) and [Django Documentation](https://docs.allauth.org/en/latest/installation/quickstart.html) were used to install and wire up Django AllAuth. 
- [Django debug log](https://docs.djangoproject.com/en/5.0/topics/logging/#id5) was provided by tutor support to assist with finding specific issues in code.
- [Django Views URL Names](https://docs.allauth.org/en/latest/account/views.html#login) were found here, with the help of tutor support, to reference Django account files within custom templates.
- Understanding the Django User Model was found [here](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.User).
- The use of Django signals, specifically the 'post_save' signal was implemented with the idea from [Medium.com](https://medium.com/@abdullafajal/automating-user-profile-creation-with-default-data-using-django-signals-50abef9ce529) and assistance from [Django Signal Documentation](https://docs.djangoproject.com/en/5.0/ref/signals/).
- Understanding Django Forms was referenced using [this documentation](https://docs.djangoproject.com/en/5.0/topics/forms/) as well as from [creating model forms documentation](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/). Implementing cleaned_data was learned through [Django documentation](https://docs.djangoproject.com/en/5.0/ref/forms/validation/#:~:text=The%20clean()%20method%20on,and%20that%20error%20is%20raised.).
- Understanding the use of super() and __init __ came from [hubspot](https://blog.hubspot.com/website/python-super), [stack overflow](https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods) and [sentry](https://sentry.io/answers/super-and-init-in-python/#:~:text=__init__%20with%20Product,dependency%20injection%20and%20multiple%20inheritance.&text=This%20is%20equivalent%20to%20calling%20super()%20in%20Python%203.).
- Customizing the User profile in the admin dashboard was learned from [Customizing authentication in Django](https://docs.djangoproject.com/en/dev/topics/auth/customizing/).
- Implementing Bootstrap's pop-up modal came from this [Bootstrap Components Documentation](https://getbootstrap.com/docs/4.6/components/modal/).
- The ideaology of implementing the booking form's DateTimePicker came from [Django-Bootstrap-Datepicker-Plus](https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/customization.html). This wasn't rendering properly, so with the help of [this example](https://github.com/GJSayers/hobo-hatch-b2b/blob/main/checkout/forms.py) from tutor support, along with [letscodemore.com](https://www.letscodemore.com/blog/how-to-add-date-input-widget-in-django-forms/), I was able to implement DateInput & TimeInput.

### Content
Soul Base Pilates Studio - My sister's pilates studio based in Iowa, USA.

### Technologies Used
LucidChart = ERD
Figma = Wireframes
Django = Framework
HTML = mark up
CSS = styling
[Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/download/) = styling
Python
JavaScript
VS Code = IDE (Integrated Development Environment)
Heroku = Deployment
GitHub = store project
Git = version control
[PostgresSQL from Code Institute](https://dbs.ci-dbs.net/) = Production database 
[TinyPNG](https://tinypng.com/) used to compress images
[Favicon generator](https://gauger.io/fonticon/)

### Media & Layout

## Acknowledgements
