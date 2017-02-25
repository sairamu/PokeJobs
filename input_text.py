#!/usr/bin/python
'''This file parse all the resumes in the file named resume and convert into the feature vector and return them'''


import os
import numpy
import glob

class text_parse:
	def read_file(self, filename):
		self.file_name = filename
		#direc = '/' + self.file_name
		os.chdir(self.file_name)
		for file in glob.glob('.doc'):
			print file





if __name__=='__main__':
	text_parse_obj = text_parse()
	text_parse_obj.read_file(filename='Resumes')