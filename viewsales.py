import sqlite3

db = sqlite3.connect('inventory.db')
c = db.cursor()

def main():
	response = []
	c.execute('SELECT * FROM sales')
	inventory = c.fetchall()
	#Get SQL response and save to a dictionarystu
	for row in inventory:
		item = {
			'id' : row[0],
			'itemid' : row[1],
			'buyer' : row[2],
			'platform' : row[3],
			'price' : row[4],
			'quantity' : row[5]
		}
		c.execute(f'SELECT type, capacity FROM inventory WHERE id = {item["itemid"]}')
		item['type'] = c.fetchall()[0][0]
		response.append(item)
	#Print formatted response
	for item in response:
		for key in item:
			if key == 'id':
				print(f"{item['id']}: {item['type'].upper()}")
			elif key != 'type' and key != 'itemid':
				print(f'     {key.upper()}: {item[key]}')


if __name__ == '__main__':
	main()
