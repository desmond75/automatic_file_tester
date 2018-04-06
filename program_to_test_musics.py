"""Python program to automatically test files on your computer
   Name: Fon Desmond Ade
   Email: adedesmond6@gmail.com
   This program can can be use to automatically test musics and
   photos on a computer by specifying the path where files are located """



import os
import time
from itertools import islice


def automatic_file_tester(full_path_to_file,number_of_files_to_test, test_time_in_seconds):
	""" # full_path_to_file is where your file is located eg if your file is located in D drive 
	    in musics your path will be D://musics/
	    # number_of_files_to_test is the amount of files you wish to test for example you may 
	    want to test the first 20 files it depends on you  
	    # test_time_in_seconds is the time you want a file to be tested,for example you may want 
	    each file to be tested for 5 seconds or more it depends on you

	    """
	try:
		if not os.path.exists(full_path_to_file):
			print('Your path is incorrect')
		else:
			for file in islice(os.listdir(full_path_to_file),number_of_files_to_test):#loops through all files in the directory

				path = os.path.join(full_path_to_file , file)# attach file with the full path provided
				time.sleep(test_time_in_seconds) #waiting time during each file testing
				os.startfile(path)#opens file using the default program on your computer
				print(f'I am now testing --> {file}')

	except BaseException as e:
		print('An error occured', e)


#To run the program uncomment the variables below and enter your own path to the 
#files you wish to test


# full_path_to_file = "D://aud/" #Enter your path
# number_of_files_to_test = 9 #You can set this to any number you want to
# test_time_in_seconds = 5 #You can change this to anything you want to make the test time much longer
# automatic_file_tester(full_path_to_file, number_of_files_to_test, test_time_in_seconds)