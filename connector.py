from node import node 
import copy 

class connector:
	def __init__(self,nodelist):
		self.nodelist=nodelist
		self.backup_nodelist=copy.deepcopy(nodelist)

	def __enter__(self):
		print("Enter")
		print(self.backup_nodelist[0].groups)
		print(self.nodelist[0].groups)
		return self.nodelist

	def __exit__(self,type,value,traceback):
		print("Exit")
		if type == Exception:
			#print(id(self.nodelist))
			#print(id(self.backup_nodelist))
			#print(self.nodelist[0].groups)
			#print(self.backup_nodelist[0].groups)
			self.nodelist=copy.deepcopy(self.backup_nodelist)

		print(str(value))
		return False

	def record_group(self,groupId):
		print("record")
		for node in self.nodelist:
			node.record_group(groupId)

	def delete_group(self,groupId):
		for node in self.nodelist:
			node.delete_group(groupId)
