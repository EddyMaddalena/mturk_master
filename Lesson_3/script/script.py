import os
import csv

# Specifying the path of the images folder
DIR_PATH = '../images/'

# Creating a list of names of the files with *.jpg format present in the folder
images = [ f for f in os.listdir(DIR_PATH) if f.endswith('.jpg')]

# Printing out such file names
print( f'{ len(images) } images found in "{ DIR_PATH }" folder' )
for i, f in enumerate(images):
	print( f'  {i+1} - {f}')

# Prepending the img_url string to the list. It will be the column name in the header
images.insert(0, 'image_url')

# I use the list as the first column of a CSV and they I write it out in the file system
with open('data.csv', 'w') as f:
	writer = csv.writer(f)
	for val in images:
		writer.writerow([val])
print('Done.')




# https://raw.githubusercontent.com/EddyMaddalena/mturk_master/a0981449d99e80b78d50b33796fb0869f2264710/maksim-zhashkevych-x-zJ8i-HWRM-unsplash.jpg