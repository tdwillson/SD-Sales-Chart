from sys import platform
from flask import Flask, render_template, request, redirect
from datetime import datetime
import sqlite3

from helpers import inv, sa, makelink

app = Flask(__name__)

# Index
@app.route("/")
def index():
    return redirect('/inventory')

# View Inventory Page
@app.route("/inventory", methods=["GET"])
def view_inventory():
    inventory = inv()
    return render_template('inventory.html', inventory=inventory)

# Add a sale to the database and remove that amount from DB
@app.route("/sell", methods=["GET", "POST"])
def sell():
    if request.method == "GET":
        inventory = inv()
        print (inventory)
        return render_template('sell.html', inventory=inventory)
    else:
        db = sqlite3.connect('inventory.db')
        c = db.cursor()
        try:
            itemid = int(request.form.get("item"))
        except:
            return("Invalid Item")
        buyer = request.form.get("buyer")
        platform = request.form.get("platform")
        try:
            price = float(request.form.get("price"))
        except:
            return("Invalid Price")
        try:
            quantity = int(request.form.get("quantity"))
        except:
            return("Invalid Quantity")

        if not buyer or buyer == "":
            return("Must enter a buyer")
        if not platform or platform == "":
            return("Must enter a platform")
        
        timestamp = datetime.now().strftime('%m/%d/%y %I:%M:%S %p')
        c.execute(f'INSERT INTO sales (itemid,buyer,platform,price,quantity,timestamp) VALUES ({itemid},"{buyer}","{platform}",{price},{quantity},"{timestamp}")')
        c.execute(f'UPDATE inventory SET amount = amount - {quantity} WHERE id = {itemid}')
        db.commit()

        return redirect("/")
        
# View all sales
@app.route("/sales")
def sales():
    # Get sales as a dict
    s = sa()
    return render_template('sales.html', sales=s)

@app.route("/addlisting", methods=["GET", "POST"])
def addlisting():
    if request.method == "GET":
        inventory = inv()
        return render_template("addlisting.html", inventory=inventory)
    else:
        db = sqlite3.connect("inventory.db")
        c = db.cursor()
        try:
            itemid = int(request.form.get("item"))
        except:
            return "Invalid Item"
    platform = request.form.get("platform")
    link = request.form.get("link")

    if not platform or platform == "":
        return "Invalid Platform"
    if not link or link == "":
        return "Invalid Link"
    link = makelink(link)

    if link == "INVALID":
        return "Invalid Link ll"

    c.execute(f'INSERT INTO listings (itemid,platform,link) VALUES ({itemid},"{platform}","{link}")')
    db.commit()

    return redirect("/")