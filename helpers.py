import sqlite3

def cash(value):
    # Format number as cash
    return f"${value:,.2f}"

# Get Inventory as a list of dictionaries
def inv():
    #Connect DB
    db = sqlite3.connect('inventory.db')
    cursor = db.cursor()

    inventory = []

    runs = 0
    cursor.execute("SELECT * FROM inventory")
    i = cursor.fetchall()
    for row in i:
        #Change SQL from List to Dictionary with correct values
        item = {
            'id' : row[0],
			'type' : row[1],
			'capacity' : row[2],
			'amount' : row[3],
			'upc' : row[4],
			'price' : cash(row[5]),
			'paid' : cash(row[6])
        }
        #Add all online listings for item to said item's dictionary
        cursor.execute(f"SELECT * FROM listings WHERE itemid = {int(item['id'])}")
        j = cursor.fetchall()
        listings = []
        for li in j:
            listing = {
                'platform' : li[2],
                'link' : li[3]
            }
            listings.append(listing)
        item['listings'] = listings
        #Add image link for each item
        if item['id'] == 1:
            item['image'] = "/static/SD32.jpg"
        elif item['id'] == 2:
            item['image'] = "/static/MicroSD128.jpg"
        elif item['id'] == 3:
            item['image'] = "/static/FlashDrives64.jpg"
        elif item['id'] == 4:
            item['image'] = "/static/MicroSD32.jpg"
        inventory.append(item)
    return inventory

# Get Sales as a list of dictionaries
def sa():
    db = sqlite3.connect('inventory.db')
    cursor = db.cursor()

    sales = []

    cursor.execute("SELECT * FROM sales")
    i = cursor.fetchall()
    for row in i:
        # Get Data from SQL query and put it in a dictionary
        sale = {
            'id': row[0],
            'itemid': row[1],
            'buyer': row[2],
            'platform': row[3],
            'price': cash(row[4]),
            'quantity': row[5],
            'timestamp': row[6]
        }
        # Use information from last query to get item type and capacity
        cursor.execute("SELECT type, capacity FROM inventory WHERE id = {}".format(sale['itemid']))
        j = cursor.fetchall()
        # Add those items to the dictionary
        sale['type'] = j[0][0]
        sale['capacity'] = j[0][1]
        sales.append(sale)
    
    return sales


def makelink(link):
    domains = [".com", ".net", ".org"]
    test = False
    for domain in domains:
        if domain in link:
            test = True
    if test:
        if link.startswith("www."):
            print("www.")
            link = "https://" + link
        elif link.startswith("https://"):
            print("https://")
            return link
        elif link.startswith("http://"):
            print("http://")
            return link
        else:
            return "https://" + link
    else:
        return "INVALID"