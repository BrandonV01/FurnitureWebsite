<h1>Furniture Store</h1>
<h2>Overview</h2>
A basic webstore for an imaginary furniture store using flask as a framework along with flask-sqlalchemy and sqlite3 for a built in database. 
Users are able to create and log into an acccount, add items to a cart which will be saved per session or into the databse if logged in, and of course purchase items. 
There is an admin user created when the application is ran which has access to an admin panel manually accessible by going to the /admin subpage.

<h2>Improvements that I could make</h2>
<ul>
    <li>Actually upload application to a cloud service to host it</li>
    <li>Along side the above, use a image hosting API instead of saving them locally</li>
    <li>Learn how the logic for checkout pages actually works instead of having just the front-end with non-practical logic behind it</li>
    <li>Better alerts when user does action (e.g. when an item is added to cart, page reloads to where the user was instead of going to the top)</li>
    <li>Doing smaller thing's I got lazy with (e.g. adding the number bubble to the cart to show how many items are in it, correcting way dropdown shows up, etc)</li>
    <li>Better adaptive layouts for smaller/mobile screens</li>
</ul>

<h3>Things to know</h3>
<ul>
    <li>The database that is created with the app will refresh to the base state I created when the server is ran. To remove this you can go to the main.py file and remove the db.drop_all() line.</li>
    <li>The create_db.py file creates the base database in order for someone to quickly test the application. It creates tables for users, products, and categories. Most importantly it creates 3 users you can use.</li>
    <li>2 user profiles which can be logged into by using useraccount@email.com or useraccount2@email.com as the email and for the password use us3rpassword and passw0rduser respectively</li>
    <li>The last profile is an admin profile which can be logged into using adminaccount@email.com and adminpassw0rd. This is mainly to use the admin pages. </li>
</ul>
