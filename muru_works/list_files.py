
import os
i =0 
def check_dot(name):
	index = name.index('.')
	if index:
		switch = 'yes'
	else:
		switch = 'no'

	return switch

def sep_dot(file_name):
	dot_index = file_name.index('.')
	length = len(file_name)
	act_name = file_name[0:int(dot_index)]
	ext_name = file_name[(1+int(dot_index)):length]
	return actual_name, ext_name






for filename in os.listdir('Resumes'):
	actual_name , extension_name = sep_dot(filename)	
	tag = check_dot(extension_name)
	if tag == 'yes':
		pass
	else:
		sep_dot



'''    if filename.endswith(".doc") or filename.endswith(".py"): 
        print filename
        i+=1
        # print(os.path.join(directory, filename))
        continue
    else:
        continue
print i
'''