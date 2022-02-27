Language Stay

So you've been learning Spanish for a while now and you have a strong grasp of the vocabularly and grammar.  You decide to spend a few months in Madrid and you'll be fluent in no time, right?  Wrong.  In reality you spend your entire time with English-speaking friends and, even worse, whenever you speak to the waiter in Spanish, you are replied to in English.  Well, look no further than Language-Stay.  This is the app that allows you to integrate seemlessly into a linguistic community and, by speaking the target language 24/7 you are ACTUALLY fluent in a matter of months.

This site targets targets anyone and everyone who has ever tried to learn a language and although they have put however many hours in on Duolingo or evening classes, the waiter still replies to them in English.

The site aims to achieve its goal by having good, crisp UX which produces a positive reaction in the user, a well-designed database of "hosts" and "volunteers" and wide-ranging functionality.

User Stories
First-time-users
As a first time user, I want to have a positive emotional response when visiting the site (be impressed with the quality of the website) so that I am encourgaed to return.
As a first time user, I want to be able to easily understand the aim and idea behind the site.
As a first time user, I want to be able to navigate through the site and to create an account and a profile.
As a first time user, I would like to be able to navigate to and look through the lists of "Workers" or "Hosts".
Returning-users
As a Returning visitor, I would like to be able to login using my username and password and then to be able to look at the details of a Host/Worker.
As a Returning visitor, I would like to be able to buy a subscription to Language-Stay.
As a Returning Visitor, I want to be able to find a Host/Worker and access their email address after paying.
As a Returning Visitor, I want to be able to access the website on various different screen sizes and for it to evoke a positive response.
Features
The site is formed of five pages each of which have a header, footer and main body.

Header
This exists across all pages and contains the below.

Responsive nabar
This allows users to quickly and intuitively navigate between pages of the site. On larger screen sizes the links are organised across the width of the navbar but on smaller screen sizes this is replaced by a 'burger' toggle which displays links vertically when toggled thus allowing for smooth transition across pages even with smaller screen sizes.  There is 
also an "upgrade" button that displays if users are using the free version of the site.  Furthermore, on first entry into the site (directly after signing up) the navbar is hidden until the user completes their profile.

Footer
This also exists across all pages and contains both copyright information as well as phonenumber and a email address in order to encourage users to get in contact.

Homepage
This page introduces the users to the basic idea behind this app.  There are three main sections: 
1.  Jonah's Story - this section explains to the user how the idea for the app came into being.
2.  The Concept - this section explains the aim of the app or, in other words, the type of situation that this app aims to engender. 
3.  The Deal - this section explains the specifics of the arrangement between host and worker.

Hosts/Workers Page
This page either shows a list of worker profiles (logged in as a host) or a list of host profiles (logged in as a worker).  The for each worker/host, the user is shown the host/worker's uploaded picture as well as some basic details.  The idea behind this page is so that users can browse the various hosts/workers and select any that appeal to them.

More Details Page
This page can be navigated to from the Hosts/Workers page and displays all of the details of a given Host/Worker.  The idea behind this page is to allow users to peruse all of the information relating to a paricular Host/Worker and to decide whether or not they would like to contact them.  The More Details page also contains the email address of said Host/Worker to allow contact to be made.  Note that this is only visible to the user if they have a premium subscription.

Upgrade Modal
There is a button that triggers a modal in the navbar for all users that do not hold a premium subscription.  Inside this modal is an explaination of the premium subscription and a link that takes the user to the Stripe checkout page.  Once the user has paid, the "email address" value in the More Details page will be visible.

Login Page
This page contains a 'card' and within that a form that requires both a username and password. There are also two buttons: 'login' which submits the inputted data to be checked against the data in the database and 'register' which takes the user to the Register Page (see below) if they don't aleready have an account. This is designed to be as easy and intuitive as possible and to make the authentication process as straightforward as possible.  There is also a landscape background on this page in order to play into the "travelling" theme of the app as well as to improve UX generally.  The background is also visible on the Register page.

Register Page
This page is similarly laid out to the Login Page. The difference is that the submit button uses the inputted data to create a new user and the second button takes the user to the Login Page.

Profile Page
The profile page is where a Worker/Host can input all of their details, which are then saved to the database and can then be viewed by other hosts/workers.  Note that directly after signing up, users are redirected straight to the profile page in order that they create a profile before accessing the rest of the site.  In order to ensure that this occurs, the navbar is hidden from the user until they save their profile so that the user cannot navigate to anther page before they have completed their profile.

Note on the site structure
The site is formed of four different Django "apps" which, taken together, deliver the full functionality of the site.  Django recommends splitting a project into various apps as it allows programmers to quickly and easily reuse code that has been written for one project, in another project.  The apps in this project are the following:
1.  accounts - deals with user creation and authentication.
2.  hostofferings - deals with a given host's proposal i.e. what they are offering to a worker.
3.  products - deals with the premium subscription that is available to users.
4.  users - deals with details to do with both hosts and workers e.g. desired language, work experience or whether or not they have paid for the premium subscription.

Note on the database

As detailed above, the site is split in to various different apps, each of which deals with different aspects of the site.  One of the most important parts of each app is its models, in other words, the way it arranges, interacts with, and stores data in the database.

This site uses a Postgres SQL database that is hosted on Heroku and which has six different models split across the four apps.  As mentioned above, these models allow the Django apps to store the necessary information in the database and access it when required to fulfil functionality of the app.  The models in this project are as follows:
1.  accounts
- Roles (whether host or worker)
- Users (general info e.g. username, email)
2.  hostofferings
- Offerings (info about host's proposal)
3.  products
-  Product (info about the subscription e.g. price)
4.  users
- Hosts (more info about the host and whether or not they have bought the premium subscription)
- Workers (same as above but for worker)

As mentioned above, these modules are linked together in order to reflect the way in which the concepts and things interrelate in real life.  The is done by using Django primary keys.  The interrelation schemata is show below.
- Role has a one-to-one relationship with User
- Host has a one-to-one relationship with User
- Worker has a one-to-one relationship with User
- Host has a one-to-one relationship with Offering
As you can see, with the exception of Product and Offering (which is indirectly linked to User via Host) the idea is to relate each module back to User in a one-to-one relationship.  Again, this is to reflect the links between these concepts and things in reality e.g. a logged-in User on the website must necessarily also be either a Host or a Worker.  Furthermore, a Host is not the same thing as what they are offering (accomadation/food) hence the distinction between Host and Offering.


Testing
Manual Testing
This app has various moving parts as well as a complex database schemata so I have devised a variety of manual tests in other to ensure the app is bug-free.

Test: Click on all the links in navbar. Ensure that they change colour when hovered over and take the user to the corresponding page.
Result:
Home (including homepage graphic) link - pass
Profile link - pass
Workers link - pass
Hosts link - pass
Login - pass
Logout - pass 

Test: Navigate to the homepage as a (1.)paid host, (2.)non-paid host, (3.)a paid worker, (4.)a non-paid worker and as (5.)an anonymous user.  Each of these should cause different links to be displayed in the navbar.
Result: 
1. [(screenshot evidence)](testing/images/manual-test-5/edit-button.png)
2.
3.
4.
5.

Test: Click and hover over all links in footer. they take the user to the correct social media site/open an email address to jonasitoelprogramdor and change colour when hovered over.
Facebook link result: Open a new Facebook tab on click and change colour on hover. Instagram link result: Open a new Instagram tab on click and change colour on hover. Twitter link result: Open a new Twitter tab on click and change colour on hover. Youtube link result: Open a new Youtube tab on click and change colour on hover. Here link result: Open an email address to jonasitoelprogramdor on click and change colour on hover.

Test: Click 'more details' button. Homepage result: It takes the user to the More Details page. Userpage result: It takes the user to the More Details page. (screenshot evidence)

Test: Click the 'edit', 'delete' and 'like' buttons on the More Details Page. Edit button result: Takes the user to the Edit Recipe Page. Delete button result: Delete the recipe entirely. Like button result: Add the user to the list of users that have liked this page. (screenshot evidence) (screenshot evidence) (screenshot evidence) (screenshot evidence) (screenshot evidence) (screenshot evidence)

Test: Fill in the form on the Add Recipes Page and then click submit. Result: Input values are saved in the recipes collection in the Mongo database. (screenshot evidence) (screenshot evidence)

Test: Click the 'Next Ingredient' and 'Next Step' on the form on the Add Recipes Page. Result: A new input is created for the 'ingredients' and 'method' section of the form respectively. (screenshot evidence) (screenshot evidence)

Test: Click the 'Next Ingredient' and 'Next Step' on the form on the Edit Recipes Page. Result: A new input is created for the 'ingredients' and 'method' section of the form respectively. (screenshot evidence) (screenshot evidence)

Test: Click the 'done', 'edit' and 'delete' buttons for the inputs on both the Add Recipes Page and the Edit Recipes Page. Result: The 'done' and 'edit' buttons make the input 'readonly' and not 'readonly' respectively and the 'delete' button deletes the new input, this does not cause the numbering to be disrupted. (screenshot evidence) (screenshot evidence)

Test: Click the logout button followed by the home button on the navbar. Then click the 'more details' button of a given recipe. Result: The recipe's More Details Page does not give the user the option to edit, add or delete the recipe as the user is logged out. (screenshot evidence)

Test: Click the logout button. Result: The navbar only shows the 'Home', 'Register' and 'Login' links. (screenshot evidence)

Test: On the Login Page input a username and password that do not match a value in the database. Result: The user is not granted entry and a message is displayed on the title of the login page telling the user either the username or password are incorrect. (screenshot evidence)

Test: On the Login Page the username and/or password fields are left blank. Result: Both fields display a "Please fill out this field" message if nothing is inputted. (screenshot evidence)

Test: On the Login Page input a username and password that match a value in the database. Result: The user's Userpage is displayed and the navbar displays "Logout", "Home", "Username" and "Add Recipe" links. (screenshot evidence)

Test: On the Login Page click on the 'sign up' button. Result: The user is taken to the Register Page. (screenshot evidence)

Test: Click on the 'more details' button when logged in as a user. Result: The buttons 'delete', 'edit' and 'like' are displayed to the user. (screenshot evidence)

Test: On the Register Page input a username and password that do not match a value in the database. Result: The user is taken to the Userpage and a new user is created in the database. (screenshot evidence) (screenshot evidence)

Test: On the Register Page the username and/or password fields are left blank. Result: Both fields display a "Please fill out this field" message if nothing is inputted. (screenshot evidence)

Test: On the Register Page input a username and password that match a value in the database. Result: The user remains on the same page and the message "This user already exists!" is displayed as the page title. (screenshot evidence)

Test: On the Register Page click on the 'Already Registered?' button. Result: The user is taken to the Login Page. (screenshot evidence)

User Story Testing
As a first time user, I want to have a positive emotional response when visiting the site (be impressed with the quality of the website) so that I am encourgaed to return.

The website uses a high-contrast colour schemata as well as various bootstrap components such as cards, forms, navbars and buttons in order to give the impression of quality. One example of a boostrap card is the below link: (screenshot evidence)
As a first time user, I want to be able to easily understand the aim and idea behind the site.

The homepage of the site allows users to directly browse through recipes and there is a clear 'more details' button that provides more information about each recipe.
There is a clear title and subtitle that introduces the auim of the website (screenshot evidence)
As a first time user, I want to be able to navigate through the site and use the 'more details' button to find out more information about a given recipe.

On the homepage and the Userpage, on each card which corresponds to one recipe, there is a clear 'more details' button which changes colour when hovered over to provide visual feedback to the user. screenshot evidence
As a first time user, I would like to be able to use the register page to create myself an account.

There is a clear navbar link to 'register' when the user is not logged in.
If the user finds themselves on the Login Page but has not yet made a username and password, there is a 'Sign Up' to the register page. screenshot evidence
As a Returning visitor, I would like to be able to login using my username and password and then to be able to make use of the full CRUD functionality as well as the 'like recipe' function.

Clear link in the navbar to the Login page.
On the More Details Page (see user story 3) there is a clear 3-button set that allows a logged-in user to like, edit or delete the given recipe.
Clear link in the navbar for logged-in users to 'Add Recipe'. screenshot evidence
As a Returning Visitor, I want to be able to access the website on various different screen sizes and for it to evoke a positive response.

The site uses a combination of Bootstrap responsive design and media queries in order to ensure UX remains consistent and of high quality on any screen-size. The navbar uses a toggle button to show/hide the navbar links when the screensize is narrower. The screenshot evidence does not show the Login, Edit Recipe and Profile pages as these are structually the same as the Register, Add Recipe and Home Pages respectively.
screenshot evidence
Please note that the image evidence for the user story testing was taken before a final change in the colour schemata of the application. All interactive/functional parts of the website remain the same, however.

Automated testing
The HTML and the CSS code were put through the W3C schools HTML and CSS validators respectively to eliminated any potential syntax errors. (HTML: https://validator.w3.org/) (CSS: https://jigsaw.w3.org/css-validator/)

The javascript code was put through a code beautifier also to eliminate syntax errors (link:https://beautifytools.com/javascript-validator.php).

Bugs
Bug: After changing the bootstrap file from being local to a CDN, the CSS behaved slightly differently. Fix: The problem occured as a result of specificity so I created several new classes in my CSS to target (with a lower specificity) the classes that were not functioning as they had done before.

Bug: Everytime that a recipe was edited, the users in its "liked by" attribute would be deleted. Fix: Add an extra hidden input to the Edit Recipes page that passes the users that have liked the recipe to the database on submission of the Edit Recipe form.

Bug: The "Home" navbar link would not be white when the page was loaded for the first time. On subsequent loads it would show up white. Fix: Add logic to the JS code that adds a class to the "Home" link element on the first load of the page as long as other conditions have not been met.

Bug: Clicking the "Next Step" button on the Edit Recipe page would add an extra input to the ingredients section but not to the method section. Fix: The logic in the javascript, specifically the "next_input" function, needed to be modified in order for the code to target either the "method" section or the "ingredients" section depending on which button was pressed.

Technologies
Languages
HTML5 was used in order to provide the text content the structure of the site.
CSS3 was used to add styling. Javascript (ECMAScript 2018) was used in order to add interactivity and to create the interactive forms for the Edit Recipe and the Add Recipe pages. Jinja template language was used in order to inject the content from the database into the HTML templates so that it could be displayed to the user. Python programming language was used in order to be able to run the Flask framework.

Frameworks, Libraries and Programs
Bootstrap: was used to add responsivess and to aid with the structure of the site. (link: https://getbootstrap.com/docs/4.4/getting-started/introduction/)

Hover.CSS3: was used on the media links in the header and the social media links in the footer in order that they take on a different colour when hovered over. (link: https://ianlunn.github.io/Hover/)

Git: was used to save changes in the website's files. Gitpod terminal was used to save changes to Git and Push to send these changes to GitHub. (link: https://git-scm.com/)

GitHub: where the files are stored after being "pushed". (link: https://github.com/)

Flask framework (written in Python programming language): is used to run the backend of the application. That is, it deals with requests from the browser and send back the correct HTML template as an HTTP response.

PyMongo: is a module containing tools that are used to connect with MongoDB when working in python.

Color-Calculator was used to find a harmonious and high-contrast colour scheme: (link: https://www.sessions.edu/color-calculator/)

Design
Colour Scheme
There are three main colours: off white, green and dark blue. These colours was chosen both for their colour harmony and to allow for high levels of contrast for UX purposes.

Typography
Wireframes
Wireframes image link

Deployment
The project was deployed to Heroku via Github pages using the following steps...

Create a file called requirements.txt (pip3 freeze --local > requirements.txt). See file here for contents of this file. This is a list of the dependencies that are required to run Flask.
Create a file called Procfile and write the following into the file: web: python app.py (echo web: python app.py). This tells Heroku which file is responsible for running the app.
Create an account for Heroku and from the dashboard click 'new' -> 'create a new app'.
Give your app a name and chose the corresponding region.
Set up automatic deployment from our Github repository by clicking "connect to Github" and folloing the steps to search for and connect to the app.
Accessibility
The aim of this project with regards to accessibility is to ensure that there is text explanation across all features to build a site that is usable for people that use screen readers. If a feature already has a title/text explaining its function there is no need to add additional text. However, in certain cases, such as in the case of the media links, there is no text explaining the function of the link. Therefore, an aria-label has been added to each link to explain its function.

In addition, there are several input fields in the site, each of which corresponds to a label element. The relationship between these two elements can be unclear for a user with a screen reader so the class "labelledby" has been added to all of the input fields in order to show their relationship to their respective label elements.

Credits
Content
Please see the inline comments across the CSS, HTML, python and JS files for any code that has been taken from third parties. Any borrowed code is clearly labelled as such.

ReadMe
The "Deployment" section of the Readme file is obtained from the Code Institue SampleREADME document which can be found:(https://github.com/Code-Institute-Solutions/SampleREADME/blob/master/README.md). Much of the CSS is taken from bootstrap templates. In these cases this is clearly indicated and a link to the corresponding bootstrap page is provided.

Use the following code to run the project in server: python3 -m http.server