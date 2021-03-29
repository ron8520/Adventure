from room import Room
from item import Item
from adventurer import Adventurer
from quest import Quest
import sys

def read_paths(source):
	paths = []
	source.seek(0)
	line = source.readline().strip("\n")

	while line != "":
		paths.append(line.split(" > "))
		line = source.readline().strip("\n")

	return paths
	source.close()

def create_rooms(paths):

	rooms = []
	i = 0
	while i < len(paths):
		rooms.append(Room(paths[i][0]))
		rooms.append(Room(paths[i][2]))
		i+=1
	return rooms


def generate_items(source):
	items = []
	line = source.readline().strip("\n")
	while line != '':
		items.append(Item(line.split(" | ")[0],line.split(" | ")[1],line.split(" | ")[2],line.split(" | ")[3]))
		line = source.readline().strip("\n")

	return items
	source.close()


def generate_quests(source, items, rooms):
	"""Returns a list of quests according to the specifications in a config file, (source).

	source contains quest specifications of the form:
	reward | action | quest description | before_text | after_text | quest requirements | failure message | success message | quest location
	"""

	ret = []
	line = source.readline().strip("\n")
	while line != '':
		ret.append(line.split(" | "))
		line = source.readline().strip("\n")

	return ret
	source.close()

# TODO: Retrieve info from CONFIG files. Use this information to make Adventurer, Item, Quest, and Room objects.
try:
	if len(sys.argv)< 4:
		print("Usage: python3 simulation.py <paths> <items> <quests>")
		sys.exit()

# Open three .txt documents and the mood is read only.
	path = open(sys.argv[1], "r")
	item = open(sys.argv[2], "r")
	quests = open(sys.argv[3], "r")

	file_content = path.readline()
	if file_content == "":
		print("No rooms exist! Exiting program...")
		sys.exit()

# When the file was not found
except FileNotFoundError:
	print("Please specify a valid configuration file.")
	sys.exit()



role = Adventurer()
# Make sure adventurer's abilities not be negative
if role.skill < 0 or role.will < 0:
	print("Advanturer's ability cannot lower than 0")
	role.skill = 0
	role.will = 0

# list of item object
items = generate_items(item)

# list of path string
paths = read_paths(path)

# list of room object
rooms = create_rooms(paths)


task = generate_quests(quests,1,2)

i = 0
while i < len(role.inventory):
	total_skill = role.skill + role.inventory[i].skill_bonus
	total_will = role.will + role.inventory[i].will_bonus
	i +=1


# TODO: Receive commands from standard input and act appropriately.
while True:
	command = input(">>> ")
	if command == "CHECK" or command == "check":
		c = input("Check what? ")

		i = 0
		while i < len(role.inventory):
			if c in role.inventory[i]:
				get_info(role.inventory[i])
			else:
				print("You don't have that.")
				print("")
			i+=1
		if c == "ME" or c == "me":
			print("")
			print("\nYou are an adventurer, with a SKILL {} and a WILL of {}".format(role.skill,role.will))
			print("You are carrying:\n")

			i = 0
			while i < len(role.inventory):
				get_info(role.inventory[i])
		# 	i = 0
		# 	if len (role.inventory) <1:
		# 		print("You are carrying \nnothing.")
		# 	while i < len(role.inventory):
		# 		print(role.inventory[i])
		# 		i+=1
		# 	# print("Grants a bouns of {} to SKILL.".format(item.skill_bonus))
		# 	# print("Grants a bouns of {} to WILL.".format(item.will_bonus))
		# 	print("")
		# 	print("With your items, you have a SKILL level of {} and a WILL power of {}.".format(total_skill,total_will))
		#
		# i = 0
		# while i < len(equiment):
		#
		# 	if c in equiment[i]:
		# 		Item(equiment[i][0],equiment[i][1],equiment[i][2],equiment[i][3]).get_info()
		# 	i+=1


	elif command == "HELP" or command == "help":
		print("HELP       - Shows some available commands.")
		print("LOOK or L  - Lets you see the map/room again.")
		print("QUESTS     - Lists all your active and completed quests.")
		print("INV        - Lists all the items in your inventory.")
		print("CHECK      - Lets you see an item (or yourself) in more detail.")
		print("NORTH or N - Moves you to the north.")
		print("SOUTH or S - Moves you to the south.")
		print("EAST or E  - Moves you to the east.")
		print("WEST or W  - Moves you to the west.")
		print("QUIT       - Ends the adventure.")
		print("")

	elif command == "QUIT" or command == "quit":
		print("Bye!")
		break

	elif command == "NORTH" or command == "N" or command == "n":
		print("You move to the north, arriving at the {}".format())
		print("")

	elif command == "SOUTH" or command == "S" or command == "s":
		print("You move to the south, arriving at the {}".format())
		print("")

	elif command == "EAST" or command == "E" or command == "e":
		print("You move to the east, arriving at the {}".format())
		print("")

	elif command == "WEST" or command == "W" or command == "w":
		print("You move to the west, arriving at the {}".format())
		print("")

	elif command == "INV":
		print("You are carrying:")
		if len(role.inventory) == 0:
			print("Nothing.")
			print("")
		i = 0
		while i < len(role.inventory):
			print("- A {}".format(role.inventory[i]))
			i+=1
	elif command == "QUESTS":
		print("#00: {}")

		if len(role.inventory) == 4:
			print("")
			print("=== All quests complete! Congratulations! ===")

	# elif command == "LOOK" or "L":
	# 	print("")


	else:
		print("You can't do that.")
		print("")
		continue
