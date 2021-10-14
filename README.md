# SD SALE CHART
### Video Demo: 
A video demo was posted [here](https://youtu.be/SmaunIgE5xE)
### Description: 
This is a webapp intended as an internal inventory management for a selling a small surplus of SD cards I happen to have.
The application utilizes python with flask, html, and javascript, and serves as a way to view inventory, post sales, view sales, and add listings for items. All changes are saved onto a database where it can be accessed from any device.
#### Python App
The application is created with python using flask.
The majority of the program is written in [here](app.py). This is where flask is run from and links to the various html templates to render from. 
The functions in the [app.py](app.py) primarily are used to link to their respective html templates, and typically use different funtions found in [helpers.py](helpers.py) to compute any value or create any kind of dictionary or table.
#### Inventory Page
The [inventory page](templates/inventory.html) is essentially also the index page. This is where you will see all the items saved, along with info about them such as their set price and quantity. Each item is accompanied by a photo of the item, and a place order button that redirects you to the sell page and preselects the item you clicked to sell.
This page displays each item in a block design that resizes a you adjust the size of the window, and as you shrink or grow the window, you will notice the page adjusting how many items are next to each other to make the page look good on any screen.
All items are added programmatically, and pulled from a dictionary created in [helpers.py](helpers.py)
#### Sell Item Page
The [sell page](templates/sell.html) allows you to add a transactions to the database and adjust the quantity of the item you sell respectively. 
This page has a few inputs it accepts: Item, Buyer, Platform, Price, and Quantity. 
The Item input is filled in programmatically with the available items in the database, so that you don't have to manually type which item you're selling. This select element can also be prefilled with a statement in the URL that some javascript on the page will use to choose which item you're selling automatically. Typically this will be used by clicking on the "Place Order" button on the inventory page.
#### Add Listing Page
The [add listing page](templates/addlisting.html) allows you to add a link to a new listing for your items whenever you post an item to a new site. This page is pretty simple, and just allows you to input the platform and link, but when you input the link, a funtion is ran to make sure the link is formatted correctly to take you to the site. That function can be found in [helpers.py](helpers.py).
#### View Sales Page
The [view sales page](templates/viewsales.html) shows a history of all of your transactions in chronological order. All info is layed out neatly in a table for you. All info is taken from a dictionary made in [helpers.py](helpers.py).