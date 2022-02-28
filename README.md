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
1. [(screenshot evidence)](testing/images/paid-host.png)
2. [(screenshot evidence)](testing/images/nonpaid-host.png)
3. [(screenshot evidence)](testing/images/paid-worker.png)
4. [(screenshot evidence)](testing/images/nonpaid-worker.png)
5. [(screenshot evidence)](testing/images/annonymous.png)

Test: Signup as a new user.
Result: Takes the user to the profile page with the navbar hidden.
[(screenshot evidence)](testing/images/profile-no-nav.png)

Test: Click save changes buttom.
Result: Saves the input and reveals the navbar.
[(screenshot evidence)](testing/images/profile-nav.png)

Test: When logged in a host, navigate to "Workers" page.
Result: The "Workers" page correctly displays all workers that have submitted a profile.
[(screenshot evidence)](testing/images/worker-profiles.png)

Test: When logged in a worker, navigate to "Hosts" page.
Result: The "Hosts" page correctly displays all hosts that have submitted a profile.
[(screenshot evidence)](testing/images/host-profiles.png)

Test: Logged in as a worker, on the "Hosts" Page, click "more details" of a given host profile. 
Result: Host details page is displaying all information relating to the host whose profile was clicked on.  There are 3 other DIFFERENT hosts displayed in thumnails with introductory information.
[(screenshot evidence)](testing/images/host-details.png)

Test: Logged in as a host, on the "Workers" Page, click "more details" of a given worker profile. 
Result: Worker details page is displaying all information relating to the worker whose profile was clicked on.  There are 3 other DIFFERENT workers displayed in thumnails with intorductory information.
[(screenshot evidence)](testing/images/worker-details.png)

Test: Naviagte to "More Details" page of a given host when logged in as a (1.)nonpaid worker and (2.)paid worker.
Result: 
1. The "Email" field displays this message: "Upgrade your account to access hosts's email!"
[(screenshot evidence)](testing/images/paid-email.png)
2. The "Email" field displays the host's email.
[(screenshot evidence)](testing/images/nonpaid-email.png)

Test:  Naviagte to "More Details" page of a given worker when logged in as a nonpaid host and a (2.)paid host.
Result: 
1. The "Email" field displays this message: "Upgrade your account to access worker's email!"
[(screenshot evidence)](testing/images/paid-email.png)
2. The "Email" field displays the worker's email.
[(screenshot evidence)](testing/images/nonpaid-email.png)

Test: Logged in as either host or worker, click upgrade button.
Result: Brings up modal that contains a link to Stripe checkout page.
[(screenshot evidence)](testing/images/upgrade-modal.png)

Test: Correctly fill in details in Stripe checkout page.
Result: Redirects to success page.
[(screenshot evidence)](testing/images/success-page.png)

Test: Incorrectly fill in details in Stripe checkout page.
Result: Redirects to cancelled page.
[(screenshot evidence)](testing/images/cancelled-page.png)

User Story Testing

As a first time user, I want to have a positive emotional response when visiting the site (be impressed with the quality of the website) so that I am encourgaed to return.
The website uses a high-contrast colour schemata as well as various bootstrap components such as cards, forms, navbars and buttons in order to give the impression of quality.  The are also images interspered throughout the site that are both added to the website as default and that are uploaded by the user.  As a result of variuous user roles (Host/Worker) and statuses (paid/nonpaid), the navbar is extremely important in the UX as it should only display links to pages that the user has access to.  This feat is achieved by a combination of javascript and Jinja2. 
[(screenshot evidence)](testing/images/profile-no-nav.png)
[(screenshot evidence)](testing/images/paid-email.png)
[(screenshot evidence)](testing/images/worker-profiles.png)

As a first time user, I want to be able to easily understand the aim and idea behind the site.
Given that the concept behind the site is not something that exists already in any major way, I felt that it was necessary to devote an entire page to an explainantion of the project.  This is split into three sections (Story, Concept, Deal) and uses images, clean, engaging text and responsive design to convey the thinking behind this site.  
[(screenshot evidence)](testing/images/user-testing-2.png)

As a first time user, I want to be able to navigate through the site and to create an account and a profile.
The "Signup" page has a striking background coupled with high contrast inputs and text that ensure the page functionality is clear whilst being appealing to a user.  As previosuly mentioned, the key to the ease of navigation of the site is the navbar: both its links that change depending on user role and status as well as the fact that it is hidden if the user has not yet completed their profile.
[(screenshot evidence)](testing/images/nonpaid-host.png)
[(screenshot evidence)](testing/images/user-testing-3.png)

As a first time user, I would like to be able to navigate to and look through the lists of "Workers" or "Hosts".
Navigating to the Hosts/Workers page is facilitated by the navbar.  In terms of scrolling through the lists of "Workers" or "Hosts", for each host/worker there is displayed a picture and some introductory information so that the user is able to garner enough information about each in order to make a decision as to which host/worker they would like to find out more about.
[(screenshot evidence)](testing/images/worker-profiles.png)

Returning-users
As a Returning visitor, I would like to be able to login using my username and password and then to be able to look at the details of a Host/Worker.
In terms of user UX/UI, The "Login" page has a nearly identical design to the "Signup" page so functionality of the page is maximised whilst making it visually striking.  The details page itself has a main image and clear, well-spaced text as well as a 'taster' of other host/worker profiles, these features give the user a variety of content to interact with and thus encouraging them to stay on the page (or the details pages of other users!).
[(screenshot evidence)](testing/images/return-testing-1.png)

As a Returning visitor, I would like to be able to buy a subscription to Language-Stay so that I can access other users' email details.
The navbar displays a clear "upgrade" button that triggers a modal.  The objective of the modal is to explain to the user the benefits and specifics of a premium subscription.  The modal also has a button that calls a Stripe checkout page.  By filling out your details in Stripe checkout and paying, you are redirected to a success page.  On payment completion, the stripe-checkout-view in this project is sent a response that updates the user's Host/Worker model which, in turn, allows them to view the email addresses of other users.   
[(screenshot evidence)](testing/images/nonpaid-host.png)
[(screenshot evidence)](testing/images/modal.png)


As a Returning Visitor, I want to be able to access the website on various different screen sizes and for it to evoke a positive response.

Features
The site uses a combination of Bootstrap responsive design and media queries in order to ensure UX remains consistent and of high quality on any screen-size. The navbar uses a toggle button to show/hide the navbar links when the screensize is narrower. 

Automated testing
The HTML and the CSS code were put through the W3C schools HTML and CSS BeautifyTools validators to eliminated any potential syntax errors. (HTML: https://validator.w3.org/) (CSS: https://beautifytools.com/css-validator.php)

The javascript code was put through a code beautifier also to eliminate syntax errors (link:https://beautifytools.com/javascript-validator.php).

Main Bugs

Bug: When building my app via Heroku, each build would fail with the error: TypeError: can only concatenate str (not 'Nonetype') to str. 
Fix: I had written AWS_SECRET_ACCESS_KEY_ID instead of AWS_SECRET_ACCESS_KEY in my config vars.

Bug:  When I uploaded an image as a host/worker in the profile page post deployment, it would not be rendered in the front end after clicking "Save Changes".
Fix: The image was being saved to a bucket in S3, however, the link to render the image in the HTML was only poiting to a folder in Gitpod (where I stored my images pre-deployment).  The solution was to change this link so that it pointed to the correct bucket in S3.

Bug:  The links in the navbar were not rendering at all.  
Fix:  Originally, I was passing values through from views.py to my javascript via Jinja2.  The idea was that depending on the values that are passed through, I would use the javascript to assign the correct navbar links.  I set this code up before realising that you cannot read pure Jinja2 in javascript, hence the error.  I changed the system to the current one in which I render the innerHTML of the links directly into the HTML and then get the innerHTML values of these links and add the correct href values to the links using JS.

Technologies
Languages
HTML5 was used in order to provide the text content the structure of the site.
CSS3 was used to add styling. Javascript (ECMAScript 2018) was used in order to assign the correct href values to the navbar links. Jinja template language was used in order to inject the content from the database into the HTML templates so that it could be displayed to the user. Python programming language was used in order to be able to run the Django framework.

Frameworks, Libraries and Programs
Bootstrap: was used to add responsivess and to aid with the structure of the site. (link: https://getbootstrap.com/docs/4.4/getting-started/introduction/)

Hover.CSS3: was used on the media links in the header and the social media links in the footer in order that they take on a different colour when hovered over. (link: https://ianlunn.github.io/Hover/)

Git: was used to save changes in the website's files. Gitpod terminal was used to save changes to Git and Push to send these changes to GitHub. (link: https://git-scm.com/)

GitHub: where the files are stored after being "pushed". (link: https://github.com/)

Django framework (written in Python programming language): is used to run the backend of the application. That is, it deals with requests from the browser and sends back the correct HTML template as an HTTP response.  Django also communicates with the database through its "models" class and can populate HTML templates with data from the databse via Jinja.

Stripe API: an integration with Stripe was used in this project in order to be able to take payments from customers.  My Stripe inegration was set up by roughly following the steps in this tutorial: https://www.youtube.com/watch?v=722A27IoQnk&t=2539s.  As mentioned above, my project connects to a Stripe checkout page that allows the customer to fill in their details.  These details are then checked by Stripe and, if correct, Stripe send a request to my StripeWebhook view which makes the necessary changes to the database.  That is, the user's payment_status attribute in the Host/Worker model is changed to "paid".

Storage

The site uses a relational SQL database (see above for move information about database structure).  For production, the database used was SQLite, however, the database was migrated to a Postgres database hosted on Heroku for deployment.

During production, static and media files were stored inside the Gitpod project itself.  For deployment, however, I created a bucket in S3 to store static and media files as Heroku does not have any permanent file storage.  Inside the S3 bucket, there is one folder for static files (images and css) and one folder for media files (images).  S3 hosting allows access of static files through "{% static path/to/file %}", however, the equivalent does not exist for files stored in the media folder.  Thus, the media files are accessed from the S3 bucket using a hardcoded URL.  This is not best practice so any future versions of this app would look at how to deal with this.

Typography
The two fonts used in this project were 'Arvo' and 'Poppins-Regular' in order to convey a relaxed but pragmatic feel to the website.

Color-Calculator was used to find a harmonious and high-contrast colour scheme: (link: https://www.sessions.edu/color-calculator/)

Design
Colour Scheme
There are three main colours: white, dark grey, blue/grey. These colours was chosen both for their colour harmony and to allow for high levels of contrast for UX purposes.

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


Use the following code to run the project in server: python3 -m http.server