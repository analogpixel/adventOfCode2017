#!/usr/bin/env python


class node:

	def __init__(self, initdata, head=False, weight=0):
		self.data = initdata
		self.prev =  head
		self.next = []
		self.weight = weight

	def getWeight(self):
		return self.weight

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def getPrev(self):
		return self.prev

	def setData(self,d):
		self.data = d

	def setNext(self,n):
		self.next.append(n)

	def setPrev(self,p):
		self.prev = p

	def removeNext(self,n):
		self.next.remove( n )

## Find a Node on it's data
## head is where to start, and n is the data you are searching for
def findNode(head,n):
	if head.getData() ==  n:
		return head

	for node in head.getNext():
		tmp = findNode(node, n)
		if tmp:
			return tmp

	return False

def childWeights(head):
	
	if len(head.getNext()) == 0:
		return head.getWeight()

	s = head.getWeight()
	
	for child in head.getNext():
		s = s + childWeights(child)


	return s

def replaceHead(head,nodeToReplace, newParent):
	n1 = findNode(head,nodeToReplace)
	oldParent = n1.getPrev()
	n2 = findNode(head,newParent)

	if n1 == False or n2 == False:
		return False

	n1.setPrev(n2)
	oldParent.removeNext(n1)
	n2.setNext(n1)

	return True

def printTree(head):
	for n in head.getNext():
		print(n.getData())

head = node('head')
linkList = []

if __name__ == "__main__":

	# read in data and add all the nodes
	# but don't setup links yet (link all to head)
	for l in open("data2.txt").readlines():
		l = l.strip()

		if l.find(">") > 0:
			(nameWeight, links)  = l.split(">")
			ltmp=list(map(lambda x: x.strip(),links.split(",")))
		else:
			nameWeight = l
			ltmp = False

		(name,weight) = nameWeight.split("(")
		name = name.strip()
		weight = int(weight.split(")")[0])

		# if we have links then add them to be processed later
		if ltmp:
			linkList.append( {'parent':name, 'links': ltmp })

		head.setNext( node(name, head, weight) )

	# now that everything is connected to head, go back  and recconect
	# the links 
	for links in linkList:
		for link in links['links']:
			replaceHead(head, link, links['parent'])




# Answer for part 1
# print ( findNode(head,'head').getNext()[0].getData()	 )

# Answer for part 2
#
# mostly me manually going through parts of the tree looking for the node that was
# unbalanced and then find out by how much.
rootNode = findNode(head,'cumah')
for r in rootNode.getNext():
	print(r.getData(), childWeights(r) )
