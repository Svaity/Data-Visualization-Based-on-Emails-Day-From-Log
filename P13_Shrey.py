"""
Created on Sat Dec 1 2018
@author: shrey vaity
Title: Plot graph of number of emails per day by scraping a text file

"""
import matplotlib.pyplot as plt


def file_name():
	"""Get file name from the user"""
	file_name = input("Enter the file name:")
	return file_name


def remove_values(filename):
	"""Reading file and returning value"""
	file_name = filename
	try:
		fp = open(file_name, "r")
	except FileNotFoundError:
		print("File Doesnt exist")
		exit()
	else:
		with fp:
			for line in fp:
				line = line.strip("\n")
				offset = line.find("From")
				offset1 = line.find("@")
				line = line[-24:]
				offset3 = line.find("@")
				if offset == 0 and offset1>0 and offset3==-1:
					line = line[:-21]
					yield line


def main():
	name = file_name()
	dd = {'Sun':0, 'Mon':0, 'Tue':0, 'Wed':0, 'Thu':0, 'Fri':0, 'Sat':0}
	a = remove_values(name)
	cnt = 0
	for i in a:
		if i in dd:
			dd[i] += 1
		cnt += len(i)
	val= dd.values()
	keys = dd.keys()
	zp = zip(dd.keys(), dd.values())
	for i in val:
		i = val
		j = keys
		plt.bar(j, i, align='center', alpha=0.5)

	plt.ylabel('Number of messages')
	plt.title('Emails per day')
	plt.show()


if __name__ == '__main__':
	main()