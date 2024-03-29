# Soul Base Studio Booking App

Welcome to Soul Base Pilates Studio! This app will allow users to book classes for this pilates/dance studio. The classes are run by my sister, which is where the inspiration came from for this app. This project was created using Django for my very first time. The site remains simple, yet functional and contains great user experience with easy navigation. Enjoy! 
![Am I Responsive view of app](static/images/readme/am-i-responsive.png)

# User Experience (UX)

## User Stories:
**Planning of user stories completed in Google sheets:
[Google sheet](https://docs.google.com/spreadsheets/d/13gqPIhIq3JW8bj4yZG445GtfKLTm_jc08hKC8qQwt5g/edit?usp=sharing)

- As a first time user I can navigate the site so that I can learn about the business.
- As a first time user I can click on the business' social media links so that I can further research the business and connect.
- As a first time user I want to be able to register for an account so that I can access the studio booking platform.
- As a first time user I can send queries to the business so that I can find out more about them.
- As a user I can book a class so that I can attend a class that suits my schedule.
- As a user I can receive confirmation of a booking so that I know it was successfully booked.
- As a user I can see the weekly class schedule so that I can find a class that suits my schedule.
- As a returning visitor I can login to my account so that I can see my bookings.
- As a returning visitor I can login to my account so that I can cancel a booked class.
- As a returning visitor I can login to my account so that I can update my personal details.
- As a site owner I can receive queries from users so that I can respond to potential clients.
- As a site owner I can see class bookings so that I can plan accordingly for the scheduled classes.

**User Stories within Projects on GitHub Repository:
[Soul Base User Story Project](https://github.com/users/morganoleary/projects/4/views/1)

## Design:
- The design was taken from the already created logo of Soul Base Pilates.

## Wireframes:
[Figma wireframe](https://www.figma.com/file/XGDgyLpX0MTIs4UjGJEWSk/Studio-Booking-Site?type=design&node-id=0%3A1&mode=design&t=AFRhMGkel6QpeZO6-1)
![Wireframes](static/images/readme/wireframes.png)

## ERD Diagram:
[LucidChart ERD](https://lucid.app/lucidchart/e9b3c27f-07d4-4026-b261-0147bd63587b/edit?viewport_loc=-990%2C-136%2C2368%2C1186%2C0_0&invitationId=inv_e64b0370-8313-4ba3-ae26-527c2fb98352)
![ERD Diagram](static/images/readme/erd.png)

# Existing Features

- Dynamic navbar for all device sizes, clear for users to see and easy to navigate:
![Navbar](static/images/readme/navbar.png)
![Navbar small screens](static/images/readme/navbar-small.png)

- The home page displays clear information about the studio along with an image of the class space:
![About page](static/images/readme/about.png)
![Studio image](static/images/readme/studio-pic-min.png)

- The class schedule page displays the classes available and their specific times as well as the class descriptions so the user knows what to expect from a class:
![Class schedule](static/images/readme/class-schedule.png)
![Class descriptions](static/images/readme/class-descriptions.png)

- The contact page provides visitors and/or users of the site to submit their information to make a query to the business. The form also allows the user to choose a specific class they are querying, if desired:
![Contact form](static/images/readme/contact1.png)
![Contact class dropdown](static/images/readme/contact2.png)

- If a site visitor attempts to book a class from clicking on 'Booking' in the navbar, it will request that they either register a new account or sign in with an existing account:
![Booking error](static/images/readme/booking-not-logged-in.png)
![Register](static/images/readme/register.png)
![Sign in](static/images/readme/sign-in.png)

- When a user is logged in, the navbar options change to allow bookings and view their member profile page:
![Logged in navbar](static/images/readme/user-logged-in-navbar.png)

- When logged in the Booking page allows the user to choose a specific class date & time to book a class:
![Booking page](static/images/readme/booking-page.png)

- When logged in the user can visit the member profile page to view and cancel their booked classes as well as view and update their personal details:
![Member profile](static/images/readme/member-profile.png)

- When logged in the user has to option to logout:
![Logout](static/images/readme/logout.png)

- The footer is consistent throughout the entire site and allows the user to visit the studio's social media platforms. There are currently no social media sites set up or connected for this business.
![Footer](static/images/readme/footer.png)

- The admin site is fully functional for the site owner to navigate through contact requests, member/user details, and class & booking details:
![Admin dashboard](static/images/readme/admin.png)

## Future Features

- In future I plan to implement a 'table of contents' for README files of this length.

- In future implementations, the admin will have the ability to send class reminder emails to all members with upcoming bookings.

- A gallery page will be implemented to provide the user with more understanding of the studio.

- The location of the studio will be displayed with a Google map view on the site's home page.

- As a future enhancement, and as the studio begins to grow, class bookings will be limited by the capacity of members each class is able to hold.

- In future enhancements, I plan to implement a confirmation step to confirm a class booking before the user can fully cancel a class.

- In future implementations, the user will have the option to delete their account/profile. Currently, the user must contact the studio to cancel their account.

# Testing

## Validator Testing:

- CI Python Linter: Each python file for all apps were run through the python linter. There were a few lines exceeding the line limit and those are documented in my 'Bugs'. Otherwise, everything passed with no errors. 
![CI Python Linter](static/images/readme/ci-python-linter.png)

- JSHint: No JavaScript was needed for the implementation of the current features in this project.

- W3C CSS Validator: No issues were found in the CSS validator.
![W3C CSS Validator](static/images/readme/w3c-css.png)

- W3C Markup Validation: 
(Unfixed Bug) After fixing the issues the W3C Markup Validator was showing, I re-deployed and ran into the same errors. The warning is how I ensured there is no horizontal scrolling on smaller devices and it works perfectly. I don't have any `li's in my .html documents that are direct children of divs. After running out of time to submit, I was not able to solve these errors.
![W3C Markup](static/images/readme/w3c-markup.png)
No major issues were found when testing the source code of the authorized user pages.
![HTML Authorized User pages](static/images/readme/html-authorised-pages.png)

- Lighthouse: 
(Unfixed Bug) Unfortunately, I have errors in the Lighthouse report that I ran out of time to look into to see why the errors occurred. I am thinking this might have to do with Django as I have never run into issues with a Lighthouse report in past projects.
![Lighthouse Report](static/images/readme/lighthouse.png)

## Manual Testing:

Testing the Home page & Class Schedule page:
- Both these pages are purely made up of HTML & CSS and work well on all device sizes. I found no issues when adjusting the width of the screen size in the browser's Dev Tools.

Testing the contact form:
- This was tested by submitting a contact request. When attempting to submit the form without the *required fields, the user is unable to submit and receives a request to fill in the missing, required field.
- The contact form works correctly for both logged in users as well as visitors who are not logged in.
- The admin site is updated correctly with the required fields and optional fields, when completed. All contact request details are stored in the admin dashboard under Contact Requests in the Contact section.

Testing user login & logout:
- When a user logs out, they are automatically redirected to the home page. This applies for both site users as well as superusers.
- When a user logs into their previously created account, they are automatically redirected to the home page. From here the user can easily navigate the site to book a class, see their profile page or find out more about the studio from the navbar.
- I found no way to book a class without being a logged in user.
- The contact form works whether the user is logged in or not.

Testing functionality of booking & canceling a class:
- I tested trying to book a class when not logged in as a registered user and it correcly brings you to the option to login or register a new account.
- As a logged in user, the booking is successful when a correct class day and time are chosen.
- Upen successful bookings, a success message appears.
- If the class date or time is incorrect, an error message is shown to the user.
- All bookings and relevant details work correctly when viewing bookings on the admin dashboard.
- CRUD functionality has been implemented and works on all aspects of the users side. The user can successfully cancel a class booking that has already boon booked and appears on the member's profile page. The cancelations are immediately reflected on the admin dashboard and I could not find a way to break this.

Testing the layout & spacing:
- The site looks well on all device sizes thanks to Bootstrap. This was tested using the browser's Dev Tools.

Testing navbar & footer links:
- The menu navbar's layout works well on all screen sizes and shrinks to a functional, collapsible menu dropdown on small devices.
- All links in the navbar direct the user to the correct page.
- The footer's social media links all work and open the respected social media site in a new tab for better user experience.

Testing the admin dashboard:
- The superuser is able to view all models with the correct details in each. 
- The logged in admin is able to create, view and delete, bookings, users & user profiles, contact requests and class details.
- I was unable to access the admin dashboard without proper superuser login credentials.

## Bugs/Unfixed Bugs:
- Fixed: When creating my apps, I decided I needed to separate my models for member details from the class details and booking models in a separate app. I changed the name of my original 'book' app to 'member' as this already contained my Member and MemberLogin models that had been migrated to the database and deployed on Heroku. I followed the steps and successfully changed the name of the app by utilizing the [django-rename-app](https://github.com/odwyersoftware/django-rename-app?tab=readme-ov-file).

- Fixed: When implementing Django signals into the "member" app when trying to create a user profile for each user that signs up, I received the following error: django.core.exceptions.ImproperlyConfigured: Application labels aren't unique, duplicates: member . After researching, I was able to fix the problem my removing the 'member' in INSTALLED_APPS of the Settings file. This was found using [Stack Overflow](https://stackoverflow.com/questions/24319558/how-to-resolve-django-core-exceptions-improperlyconfigured-application-labels).

- Fixed: I ran into a bug when trying to implement the class cancellation function. Daisy helped debug and I now understand that Django provides built-in primary keys, where I had overidden the automatic PK with booking_id. Once I implemented the correct key into the code, it works well.

- Unfixed: When testing my .py files with the CI Python Linter, this line was proven to be too long. However, even after adding parentheses and entering to the next line and trying multiple options, I was unable to fix the result 'continuation line with same indent as next logical line': 
    if selected_datetime.strftime('%A %H:%M') not in available_options[booked_class.class_name]:   

    The same issue occured with this path, however I was unable to fix and feared ruining my url path:
        path('cancel/booking/<int:booking_id>/', cancel_booking, name='cancel_booking'),

    Same issue with this line:
        return f"{self.member} booked {self.booked_class} on {self.class_date} beginning at {self.class_time}."

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

- [Django debug log](https://docs.djangoproject.com/en/5.0/topics/logging/#id5) was provided by tutor support to assist with finding specific issues in code. This was removed for deployment.

- [Django Views URL Names](https://docs.allauth.org/en/latest/account/views.html#login) were found here, with the help of tutor support, to reference Django account files within custom templates.

- Understanding the Django User Model was found [here](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.User).

- The use of Django signals, specifically the 'post_save' signal was implemented with the idea from [Medium.com](https://medium.com/@abdullafajal/automating-user-profile-creation-with-default-data-using-django-signals-50abef9ce529) and assistance from [Django Signal Documentation](https://docs.djangoproject.com/en/5.0/ref/signals/).

- Understanding Django Forms was referenced using [this documentation](https://docs.djangoproject.com/en/5.0/topics/forms/) as well as from [creating model forms documentation](https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/). Implementing cleaned_data was learned through [Django documentation](https://docs.djangoproject.com/en/5.0/ref/forms/validation/#:~:text=The%20clean()%20method%20on,and%20that%20error%20is%20raised.).

- Understanding the use of super() and __init __ came from [hubspot](https://blog.hubspot.com/website/python-super), [stack overflow](https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods) and [sentry](https://sentry.io/answers/super-and-init-in-python/#:~:text=__init__%20with%20Product,dependency%20injection%20and%20multiple%20inheritance.&text=This%20is%20equivalent%20to%20calling%20super()%20in%20Python%203.).

- Customizing the User profile in the admin dashboard was learned from [Customizing authentication in Django](https://docs.djangoproject.com/en/dev/topics/auth/customizing/).

- Implementing Bootstrap's pop-up modal came from this [Bootstrap Components Documentation](https://getbootstrap.com/docs/4.6/components/modal/).

- The ideaology of implementing the booking form's DateTimePicker came from [Django-Bootstrap-Datepicker-Plus](https://django-bootstrap-datepicker-plus.readthedocs.io/en/latest/customization.html). This wasn't rendering properly, so with the help of [this example](https://github.com/GJSayers/hobo-hatch-b2b/blob/main/checkout/forms.py) from tutor support, along with [letscodemore.com](https://www.letscodemore.com/blog/how-to-add-date-input-widget-in-django-forms/), I was able to implement DateInput & TimeInput.

- Figuring out how to cancel a booked class was referenced from the 'I think therefore I blog' walkthrough video for [Editing and deleting records](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FSD101_WTS+2023_Q3/courseware/56a2da0940b4411d8a38c2b093a22c60/24613de4bafc4032882cc1b8799bd4f0/). I also received great feedback from Daisy on Slack to get it working properly.

- Assistance with defining UserProfileInline to include UserProfile fields in the User admin
[source](https://docs.djangoproject.com/en/dev/topics/auth/customizing/) & assistance from Tutor Support.

- Implementing the signals.py file was sourced from [here](https://medium.com/@abdullafajal/automating-user-profile-creation-with-default-data-using-django-signals-50abef9ce529) in order to create a user profile for each new user.

### Content
- The content for this site came directly from Soul Base Pilates Studio. This is my sister's pilates studio based in Iowa, USA.

### Technologies Used
- LucidChart = ERD
- Figma = Wireframes
- Django = Framework
- HTML = mark up language
- CSS = styling
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/download/) = styling
- Python = functionality
- VS Code = IDE
- Heroku = Deployment
- GitHub = Used to store the project
- Git = version control
- [PostgresSQL from Code Institute](https://dbs.ci-dbs.net/) = Production database 
- [TinyPNG](https://tinypng.com/) used to compress images
- [Favicon generator](https://gauger.io/fonticon/) to create the favicon
- [Am I Responsive](https://ui.dev/amiresponsive) = multiple screen size views

### Media & Layout

- The media for this project was provided directly by Soul Base Pilates Studio.

## Acknowledgements

- I would like to thank my mentor, Narender, for his great support and advice throughout this project. 
- I would like to thank tutor support and the community on Slack for their assistance in understanding the different aspects of this project. 
- I would also like to thank my sister, Sydney, for providing the material for the project from her new business, Soul Base Pilates Studio!