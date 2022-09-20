class node:
	def __init__(self,name):
		self.name=name
		self.groups=[]

	def __repr__(self):
		return '<Name %s, Groups: %s>' % (self.name, self.groups)

	def record_group(self,groupId):
		if groupId in self.groups:
			raise Exception
		else:
			self.groups.append(groupId)
			print(str(self.groups))

	def delete_group(self,groupId):
		self.groups.remove[groupId]

	def get_all_groups(self):
		return self.groups