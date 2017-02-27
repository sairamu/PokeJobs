import subprocess
import shutil



class pdf:
	def doc2pdf(self,ori_name,new_name):
		p = subprocess.Popen(['unoconv', '--stdout', ori_name], stdout=subprocess.PIPE)
		with open(new_name, 'w') as output:
		   shutil.copyfileobj(p.stdout, output)


'''

p = subprocess.Popen(['unoconv', '--stdout', input_filename], stdout=subprocess.PIPE)
with open(output_filename, 'w') as output:
   shutil.copyfileobj(p.stdout, output)
   '''