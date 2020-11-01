# Python program to 
# demonstrate readline() 
import hashlib
#L = ["Geeks\n", "for\n", "Geeks\n"] 

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
	print("{}".format(line.strip())) 
	filename = input("Enter the input file name: ")
	sha256_hash = hashlib.sha256()
	with open(filename,"rb") as f:
    	    # Read and update hash string value in blocks of 4K
    	    for byte_block in iter(lambda: f.read(4096),b""):
                sha256_hash.update(byte_block)
    	    print(sha256_hash.hexdigest())


file1.close() 



# Python program to find SHA256 hash string of a file
#import hashlib
 
#sha256_hash = hashlib.sha256()
#with open(filename,"rb") as f:
    # Read and update hash string value in blocks of 4K
    #for byte_block in iter(lambda: f.read(4096),b""):
        #sha256_hash.update(byte_block)
    #print(sha256_hash.hexdigest())