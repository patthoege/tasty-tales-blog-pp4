<h1 align="center">TastyTales</h1>
<div align="center"><img src="docs/img/main.png"></div>

TastyTales is a web application built using the Django framework, designed to create an engaging and user-friendly platform for food enthusiasts to share, discover, and interact with a diverse range of recipes. Whether you're a food enthusiast sharing recipes or a home cook looking for new ideas, TastyTales is the perfect platform to connect and explore the world of flavors.


You can view the live site here - <a href="#" target="_blank" rel="noopener">TastyTales</a>

## Table of Contents

* [**UX**](<#ux>)
    * [Project Goal](#project-goal)
    * [User Stories](#user-stories)
    * [Agile Methodology](#agile-methodology)
* [**Design**](<#design>)
  + [Wireframes](#wireframes)
  + [Typography](#typography)
* [**Features**](<#features>)

* [**Testing**](<#testing>)
   * [Validator testing](<#validator-testing>)
   * [Manual testing](<#manual-testing>)
* [**Browser Compatibility**](<#browser-compatibility>)
   * [Browser Testing](<#browser-testing>)
   * [Functionality](<#functionality>)
* [**Bugs**](<#bugs>)
   * [Fixed Bugs](<#bugs>)
   * [Media Query - Responsive Web Design](<#media-query---responsive-web-design>)
* [**Deployment**](<#deployment>)
   * [Running the project by using Gitpod](#running-the-project-by-using-gitpod)
   * [Deploying with Heroku](#deploying-with-heroku)
* [**Installation**](<#installation>)
* [**Technologies Used**](<#technologies-used>)
   * [Languages](#languages)
   * [Frameworks Libraries Programs](#frameworks-libraries-programs)
* [**Credits**](<#credits>)
    * [**Content**](<#content>)
    * [**Frameworks and Code**](<#frameworks-and-code>)
*  [**Acknowledgments**](<#acknowledgments>)

## UX
-   ### Project goal  
TastyTales is a Django web application designed to unite food enthusiasts in a collaborative space. The goal is to facilitate the seamless sharing of recipes, experiences, and culinary creativity. Whether you're here to showcase your own unique dishes or explore a world of flavors curated by fellow community members, TastyTales provides a rich and interactive environment.

-   ### User stories
### Admin User Stories

-  **User Authentication**
   - User Registration and Login: As an admin, I want to manage user accounts securely.

- **Blog Management**
   - Manage Posts: As an admin, I want the ability to create, edit, and delete any recipe posts.
   - Approve Posts: As an admin, I want to review and approve posts before they are published to maintain content quality.

### User User Stories

- **User Authentication**
   - User Registration and Login: As a user, I want to create accounts and log in securely.

- **Recipe Management**
   - Create and Edit Recipes: As a user, I want to create new recipes and edit existing ones with a user-friendly interface.
   - Image Upload: As a user, I want to add delicious images to my recipes to entice other users.
   - Categorization and Tags: As a user, I want to organize my recipes by categories and add tags for easy searching.

- **User Profiles**
   - UserProfile Model: TastyTales includes a UserProfile model to enhance the user experience.
   - User Information: As a user, I want to provide additional details such as first name, last name, and a profile image.
   - Biography: As a user, I want to share my culinary journey through a bio field.
   - Posted Recipes: As a user, I want to associate myself with the recipes I have created.

- **Social Interaction**
   - Comments and Likes: As a user, I want to engage with the community by commenting on and liking recipes.
   - View Comments: As a user, I want to easily view and interact with comments on posts.
   - Like / Unlike: As a user, I want to express my appreciation for recipes by liking or unliking them.

- **Blog Management**
   - Manage Posts: As an user, I want the ability to create, edit, and delete my recipes.

- **Notifications**
   - Notifications: As a user, I want to receive notifications to stay informed about my recent actions.

- **Search and Discovery**
   - Advanced Search: As a user, I want to find recipes based on ingredients, cuisine, or user profiles.
   - Most Common Tags: As a user, I want to discover popular and trending tags on the platform.

- ### Anonymous User Stories

- **Search and Discovery**
   - View Recipes: As an anonymous user, I want to browse and view recipes on the platform without the ability to engage with them.


### Agile Methodology

The principles of the Agile methodology were applied in an individual capacity during the project development. As the sole contributor, I took on the responsibilities of creating GitHub issues, defining user stories, and utilizing the GitHub Kanban board for project management. Key aspects of the Agile methodology in TastyTales include:

- **User Stories and Issues** (<a href="https://github.com/patthoege/tasty-tales-blog-pp4/issues" target="_blank" rel="noopener">GitHub Issues</a>): Project tasks were organized into user stories, each corresponding to specific functionalities or improvements. These user stories were then translated into GitHub issues, providing a clear and manageable way to track progress.

- **MoSCoW Prioritization**: The MoSCoW method was employed to prioritize project requirements and features based on their importance. In the context of TastyTales, these priorities were categorized as follows:

   - **Must-Have Features:** Essential functionalities crucial for the basic operation and success of the project. These were identified and prioritized to ensure their inclusion in the initial release.

   - **Should-Have Features:** Important features that, while not critical for the initial release, significantly enhance the project's value. These were prioritized for subsequent releases.

   - **Could-Have Features:** Desirable features that add value but can be deferred to future releases. These were considered as potential enhancements to enrich the user experience.

   - **Won't-Have Features:** Features explicitly decided not to include in the project at its current stage. This ensures a focused development approach.

- **GitHub Kanban Board** (<a href="https://github.com/patthoege/tasty-tales-blog-pp4/projects?query=is%3Aopen" target="_blank" rel="noopener">GitHub Project</a>): The GitHub Kanban board was leveraged to visualize and manage the project's workflow. It facilitated the organization of tasks, from backlog to completion, providing a visual representation of the project's status.


By adopting Agile principles, it helped me to developed with a focus on adaptability and responsiveness, resulting in a platform that aligns with user needs and delivers a satisfying user experience.


[Back to top](<#table-of-contents>)

## Design

### Wireframes  
   - A separate document for the wireframes can be viewed here: 
      - [For Desktop view](docs/WIREFRAMES.md)
      - [For Mobile view](docs/WIREFRAMES-MOBILE.md)    

[Back to top](<#table-of-contents>)

### Typography

[Back to top](<#table-of-contents>)

## Features



[Back to top](<#table-of-contents>)

## Testing  
A separate document for testing can be viewed here: [TESTING.md](docs/TESTING.md)

* ## Code Validation





* ## Browser Compatibility
        
### Browser Testing
* The website has had manual and responsive tests conducted on the below browsers. Ensuring functions are working as expected throughout browsers.

| Browser     | Layout      | Functionality |
| :---------: | :----------:| :-----------: |
| Chrome      | ✔          | ✔             |
| Firefox     | ✔          | ✔             |
| Safari      | ✔          | ✔             |

[Back to top](<#table-of-contents>)

### Functionality
- Testing the complete functionality of the page. This includes:


[Back to top](<#table-of-contents>)

# Bugs

## Fixed bugs
### 1. "RelatedObjectDoesNotExist" Error
- I encounter the "RelatedObjectDoesNotExist" error at /members/edit_profile/ stating, "User has no profile," I was trying to access a related UserProfile object for a User that does not exist. I ensure using the signals method to create a profile upon user registration. Additionally, the `MembersConfig` class in the apps.py file in the members app, ensures that signals, including user profile creation signals, are appropriately registered during the Django application setup.

### 2. Tags in Footer not Displaying
- Tags declared in the footer base.html were not displaying as I entended using same methods for other templates as tags_page.html, post_detail.html and search_results.html, so I've created a context processors file to declare the tags logic and in the views.py file (blog app), import and include this processor to enable the global display of tags in all templates within the app.

### 3. Tags Input Field Displaying Signs and Brackets
- To address the issue of the tags input field displaying signs and brackets, I fix this by adding the `TagWidget` in the NewPost form. This modification to the TagWidget class ensures that when rendering the widget, it will display a comma-separated string of tags, ensuring a clean and user-friendly appearance.

### 4. Profile Image Upload Issue
- I encountered issues with the profile image being unable to upload. To enable image uploads for the `profile_image` field in the UserProfile model, I updated it to use the `ImageField` and installed the Pillow library. 

### 5. Display of Users Draft Posts in Search Results and Profile
- An issue I identified wherein draft posts were erroneously appearing in the search results and the profile page. To prevent this behavior, drafts are now excluded from the search results in the class view when a user conducts a search and in the Profile class view.

### 6. ProgrammingError at /admin/blog/post/
- An issue occurred when attempting to change the `category` field to a ForeignKey from the Post model to establish a relationship with the Category Model.  After running command `python manage.py migrate` did not successfully create the category_id field as expected. I reset the migrations `python3 manage.py migrate your_app_name zero` in this case, to get a fresh start on these. This action effectively clears the existing migration files and the database schema.

### 7. Most Common Tags Not Displaying Updated Information
- The common tags feature, the tags were not displaying the most recent and common ones. I realized that after resetting the database schema and creating new posts with updated tags, the old most common tags continued to be displayed. The issue stemmed from the context processor that was fetching the first four tags without considering the number of associated posts. To resolve this, I modified the context processor to use the same logic applied in the SearchResults view. The context processor now annotates the tags with the count of associated posts and orders them accordingly, ensuring that only the top four most common tags are retrieved.



## Media Query - Responsive Web Design
-

## Unfixed bugs
-

[Back to top](<#table-of-contents>)

## Deployment

### Running the project by using Gitpod:
1. Go to the [project repository](https://github.com/patthoege/tasty-tales-blog-pp4)
2. Click the green button that says "Gitpod" and the project will now open up in Gitpod.

### Deploying with Heroku

I followed the below steps using the Code Institute tutorial:

The following command in the Gitpod CLI will create the relevant files needed for Heroku to install your project dependencies `pip3 freeze --local > requirements.txt`. Please note this file should be added to a .gitignore file to prevent the file from being committed.

1. Go to [Heroku.com](https://dashboard.heroku.com/apps) and log in; if you do not already have an account then you will need to create one.
2. Click the `New` dropdown and select `Create New App`.
3. Enter a name for your new project, all Heroku apps need to have a unique name, you will be prompted if you need to change it.
4. Select the region you are working in.

#### Heroku Settings  
You will need to set your Environment Variables - this is a key step to ensuring your application is deployed properly.
1. In the Settings tab, click on `Reveal Config Vars` and set the following variables:
    - Add key: `PORT` & value `8000`
    - Add key: DATABASE_URL, this should have been created automatically by Heroku.
    - Add key: CLOUDINARY_URL and the value as your cloudinary API Environment variable e.g.
    - Add key: SECRET_KEY and the value as a complex string which will be used to provide cryptographic signing.

2. Buildpacks are also required for proper deployment, simply click `Add buildpack` and search for the ones that you require.
    - For this project, I needed to add `Python`.

####  Heroku Deployment  
In the Deploy tab:
1. Connect your Heroku account to your Github Repository following these steps:
    - Click on the `Deploy` tab and choose `Github-Connect to Github`.
    - Enter the GitHub repository name and click on `Search`.
    - Choose the correct repository for your application and click on `Connect`.
2. You can then choose to deploy the project manually or automatically, automatic deployment will generate a new application every time you push a change to Github, whereas manual deployment requires you to push the `Deploy Branch` button whenever you want a change made.
3. Once you have chosen your deployment method and have clicked `Deploy Branch` your application will be built and you should now see the `View` button, click this to open your application.

[Back to top](<#table-of-contents>)

## Installation

To run TastyTales on the local machine, I follow these steps:


### Run the repository
- Go to the [project repository](https://github.com/patthoege/tasty-tales-blog-pp4)
- Click the green button that says "Gitpod" and the project will now open up in Gitpod.

### Install dependencies
- `pip install -r requirements.txt`

### Apply database migrations
- `python manage.py migrate`

### Create a superuser account
- `python manage.py createsuperuser`

### Start the development server
- `python manage.py runserver`


[Back to top](<#table-of-contents>)

# Technologies Used
### Programming Languages
* HTML5
* CSS3
* Python
* JavaScript

### Frameworks, Libraries, Programs
- Python Built-in Modules:
  - [os](https://docs.python.org/3/library/os.html) 

- External Packages
  - [cloudinary](https://pypi.org/project/cloudinary/1.29.0/) 
  - [dj-database-url](https://pypi.org/project/dj-database-url/0.5.0/) 
  - [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/0.0.6/) 
  - [Django](https://pypi.org/project/Django/3.2.14/) 
  - [django-allauth](https://pypi.org/project/django-allauth/0.51.0/)
  - [gunicorn](https://pypi.org/project/gunicorn/20.1.0/)
  - [psycopg2](https://pypi.org/project/psycopg2/2.9.3/) 
  - [Pillow](https://pypi.org/project/Pillow/)
  - [Django CKEditor](https://django-ckeditor.readthedocs.io/en/latest/)
  - [Django Summernote](https://pypi.org/project/django-summernote/)
  - [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/1.14.0/)

### Programs & Tools

- [Google Fonts:](https://fonts.google.com/)
  - Was used to to incorporate font styles.  
- [Bootstrap](https://getbootstrap.com/)
  - Was used to create the front-end design.
- [GitPod:](https://gitpod.io/)
  - Gitpod was used as IDE to commit and push the project to GitHub.
- [GitHub:](https://github.com/)
  - Was used for all storing and backup of the code pertaining to the project.
- [Balsamiq:](https://balsamiq.com/)
  - Was used to create wireframes
- [LucidCharts:](https://www.lucidchart.com/)
  - Was used to create the database schema.
- [Favicon:](https://favicon.io/favicon-generator/ )
  - Was used to create the favicon logo.
- [Looka:](https://looka.com/editor/157809201)
  - Was used to create the logo image for the project.
- [Freepik:](https://www.freepik.com/)
  - Was used to search images for the project. 
- [Colorlib:](https://colorlib.com/wp/template/bootstrap-footer-14/)
  - Was used to find inspiration footer layout.
- [CloudConvert:](https://cloudconvert.com/png-to-webp )
  - Was used to convert WEBP images formats for the project. 
 
[Back to top](<#table-of-contents>)

# Credits
### Content


[Back to top](<#table-of-contents>)

### Frameworks and Code
*


[Back to top](<#table-of-contents>)

# Acknowledgments


Patricia Höge 2023.

[Back to top](<#table-of-contents>)
