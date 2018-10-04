import csv

class Attribute:
	def __init__(self, name, element_list):
		self.name = name;
		self.element_list = element_list



class Dataset:
	def __init__(self):
		self.attlist = [] #lista de "Attribute"
		self.attnum = 0
		self.datasize = 0


	

def callexit():
    print('')
    exit()



def readdataset(datapath):
    
	with open(datapath, 'rb') as csvfile:
    	
		dataset = Dataset()

		csvline = csv.reader(csvfile, delimiter=';')

		i = 0

		for row in csvline:
			
			if(i==0): # primeira linha
				
				dataset.attnum = len(row)

				print("ue")

				for j in range(dataset.attnum):
					dataset.attlist.append(Attribute(row[j], [])) # instancia cada atributo

				i+=1

				

			else:
				for j in range(dataset.attnum):
					dataset.attlist[j].element_list.append(row[j]) # enche a lista de atributos
			
	#for i in range(dataset.attnum):
	#		print(dataset.attlist[i].element_list)  # pra debug

	return dataset


