

import os
import topdf
i=1
obj = topdf.pdf()
def check_dot(name):
	
	if '.' in name: 
		switch = 'yes'
	else:
		switch = 'no'

	return switch

def sep_dot(file_name):
	dot_index = file_name.index('.')
	length = len(file_name)
	act_name = file_name[0:int(dot_index)]
	ext_name = file_name[(1+int(dot_index)):length]
	return act_name, ext_name

'''def doc2pdf(ori_name,new_name):
	p = subprocess.Popen(['unoconv', '--stdout', ori_name], stdout=subprocess.PIPE)
	with open(new_name, 'w') as output:
	   shutil.copyfileobj(p.stdout, output)
'''


for filename in os.listdir('Resumes'):
	actual_name , extension_name = sep_dot(filename)	
	tag = check_dot(extension_name)
	if tag == 'yes':
		actual_name2, extension_name = sep_dot(extension_name)
		actual_name = actual_name + actual_name2
		original_name  = actual_name+'_'+actual_name2
	else:
		original_name = actual_name

	
	original_name_pdf = original_name + '.pdf'
	ori_filename = 'Resumes'+'/'+filename
	dest_filename = 'resumes_pdf/'+original_name_pdf
	if extension_name == 'doc':
		print i
		i+=1
		#obj.doc2pdf(ori_filename,dest_filename)	
		#print "converted ", original_name
	


'''    if filename.endswith(".doc") or filename.endswith(".py"): 
        print filename
        i+=1
        # print(os.path.join(directory, filename))
        continue
    else:
        continue
print i
'''