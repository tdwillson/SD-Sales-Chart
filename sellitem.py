import sqlite3
from datetime import date, datetime

###GLOBAL VARIABLES###
db = sqlite3.connect('inventory.db')
c = db.cursor()


def main():
	print('Sell and Item')
	try:
		itemid = int(input('Item ID -> '))
		quantity = int(input('Quantity -> '))
		buyer = input('Buyer -> ')
		platform = input('Platform -> ')
		price = float(input('Price -> '))
	except:
		print('Invalid Args')
		return
		

	update_db(itemid, buyer, platform, price, quantity)

def update_db(itemid, buyer, platform, price, quantity):
	timestamp = datetime.now().strftime('%m/%d/%y %I:%M:%S %p')
	c.execute(f'INSERT INTO sales (itemid,buyer,platform,price,quantity,timestamp) VALUES ({itemid},"{buyer}","{platform}",{price},{quantity},{timestamp})')
	c.execute(f'UPDATE inventory SET amount = amount - {quantity} WHERE id = {itemid}')
	db.commit()


if __name__ == '__main__':
	main()


'INSERT INTO sales (itemid,buyer,platform,price,quantity) VALUES (2,"Tyler","Personal",20.0,10);'