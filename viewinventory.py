import sqlite3

db = sqlite3.connect('inventory.db')
c = db.cursor()

def main():
	response = []
	c.execute('SELECT * FROM inventory')
	inventory = c.fetchall()
	#Get SQL response and save to a dictionarystu
	for row in inventory:
		item = {
			'id' : row[0],
			'type' : row[1],
			'capacity' : row[2],
			'amount' : row[3],
			'upc' : row[4],
			'price' : row[5],
			'paid' : row[6]
		}
		response.append(item)
	#Print formatted response
	for item in response:
		for key in item:
			if key == 'id':
				print(f"{item['id']}: {item['type'].upper()}")
			elif key != 'type':
				print(f'     {key.upper()}: {item[key]}')


if __name__ == '__main__':
	main()
