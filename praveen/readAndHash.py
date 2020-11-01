import hashlib
import os


L = ["Geeks\n", "for\n", "Geeks\n"] 

# Writing to a file 
#file1 = open('myfile.txt', 'w') 
#file1.writelines((L)) 
#file1.close() 

# Using readline() 
file1 = open('sample.txt', 'r') 
count = 0

while True: 
	count += 1

	# Get next line from file 
	line = file1.readline() 

	# if line is empty 
	# end of file is reached 
	if not line: 
		break
	#print("{}".format(line.strip())) 
	filename = line.strip()
	#print(filename )
	
	
	dir_name='C:/praveen/input_sample/'
	#filename = 'gethash.py'
	fileh = os.path.join(dir_name, filename)
	print(fileh)
	sha256_hash = hashlib.sha256()
	with open(fileh ,"rb") as f:
    		# Read and update hash string value in blocks of 4K
    		for byte_block in iter(lambda: f.read(4096),b""):
        		sha256_hash.update(byte_block)
    		print(sha256_hash.hexdigest())


file1.close() 
