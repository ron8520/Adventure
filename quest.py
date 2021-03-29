class Quest:
	def __init__(self, reward, action, desc, before, after, req, fail_msg, pass_msg, room):
		self.reward = reward
		self.action = action
		self.desc = desc
		self.before = before
		self.after = after
		self.req = req
		self.fail_msg = fail_msg
		self.pass_msg = pass_msg
		self.room = room

	def get_info(self):

		return self.desc

	def is_complete(self):
		"""TODO: Returns whether or not the quest is complete."""
		...

	def get_action(self):
		"""TODO: Returns a command that the user can input to attempt the quest."""
		if command == self.action:

			return command
	def get_room_desc(self):
		"""TODO: Returns a description for the room that the quest is currently in. Note that this is different depending on whether or not the quest has been completed."""
		...

	def attempt(self, player):
		"""TODO: Allows the player to attempt this quest.

		Check the cumulative skill or will power of the player and all their items. If this value is larger than the required skill or will threshold for this quest's completion, they succeed and are rewarded with an item (the room's description will also change because of this).

		Otherwise, nothing happens."""
		if total_skill > self.req or total_will > self.req:
			role.take(self.reward)
			print(self.pass_msg)
		else:
			print(self.fail_msg)
			print("")
			pass
