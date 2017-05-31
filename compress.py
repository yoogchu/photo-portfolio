import tinify
import os, os.path

tinify.key = "19UKhWk_BM2XBxQ1akPgWfrPB95fexFw"

DIR = "images/eugene/"
EXT = ".jpg"

def countFiles(path, extension):
	list_dir = []
	list_dir = os.listdir(path)
	count = 0
	for file in list_dir:
		if file.endswith(extension): # eg: '.txt'
			count += 1
	return count


# print countFiles(DIR, ".jpg")

for i in range (1, countFiles(DIR, EXT)+1):
	print 'compressing ' + str(i) + EXT
	source = tinify.from_file(DIR + str(i) + EXT)
	resized = source.resize(
	    method="scale",
	    width=350
	)
	resized.to_file(DIR + str(i) + "_thumb" + EXT)

print 'done'
