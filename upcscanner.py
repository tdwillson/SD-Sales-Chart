import sqlite3
from sys import argv


###GLOBAL VARIABLES###
db = sqlite3.connect('inventory.db')
c = db.cursor()
contquery = """
To continue type on of the following:
add ~ Add to the amount in inventory
rem ~ Remove from the amount in inventory
set ~ Set the amount in inventory
price ~ Set price of product
ENTER to leave program"""

###MAIN###
def main():

    if '-id' in argv:
        #Enter Product ID and convert to UPC
        prod_id = input('Product ID -> ')
        c.execute(f'SELECT upc FROM inventory WHERE id = "{prod_id}"')
        upc = c.fetchall()[0][0]
    else:
        #Enter product UPC
        upc = input('UPC -> ')

    try:
        #Values that will be outputted from SQL query
        values = {
            'type' : '',
            'capacity' : '',
            'amount' : '',
            'price' : ''
        }
        #Select and print each value in values dictionary
        print()
        for key in values:
            c.execute(f'SELECT {key} FROM inventory WHERE upc = "{upc}"')
            values[key] = c.fetchall()[0][0]

            print(f'{key.upper()}: {values[key]}')
    except:
        print("INVALID UPC")
        return

    #Ask if they want to modify any values
    print(contquery)
    cont = input("-> ")
    if cont.lower() == 'add':
        add_amount(upc)
    elif cont.lower() == 'rem':
        rem_amount(upc)
    elif cont.lower() == 'set':
        change_amount(upc)
    elif cont.lower() == 'price':
        change_price(upc)


#Add specified amount to inventory of typed in UPC
def add_amount(upc):
    try:
        amount = int(input('Add How Much? -> '))
    except:
        print('INVALID AMOUNT')
        return
    c.execute(f'UPDATE inventory SET amount = amount + {amount} WHERE upc = "{upc}"')
    db.commit()


#Remove specified amount from inventory of typed in UPC
def rem_amount(upc):
    try:
        amount = int(input('Revmove How Much? -> '))
    except:
        print('INVALID AMOUNT')
        return
    c.execute(f'UPDATE inventory SET amount = amount - {amount} WHERE upc = "{upc}"')
    db.commit()


#Change amount in inventory of typed UPC to specified amount
def change_amount(upc):
    try:
        amount = int(input('Set amount to -> '))
    except:
        print('INVALID AMOUNT')
        return
    c.execute(f'UPDATE inventory SET amount = {amount} WHERE upc = "{upc}"')
    db.commit()


#Change price of specified item to inputted amount
def change_price(upc):
    try:
        price = float(input('Set price to -> '))
    except:
        print('INVALID AMOUNT')
        return
    c.execute(f'UPDATE inventory SET price = {price} WHERE upc = "{upc}"')
    db.commit()


if __name__ == '__main__':
    main()

db.close()