class check_privilege_process():
	"""
	check_privilege_process:
    Do not grant to non Admin users.
	"""
	# References:
	# https://benchmarks.cisecurity.org/downloads/show-single/index.cfm?file=mysql.102

	TITLE    = 'PROCESS Privilege'
	CATEGORY = 'Privilege'
	TYPE     = 'sql'
	SQL      = "SELECT user, host FROM mysql.user WHERE Process_priv='Y'"
	
	verbose = False
	skip	= False
	result  = {}

	def do_check(self, *rows):
		if not self.skip:
			output               = ''
			self.result['level'] = 'GREEN'
			
			for row in rows:
				for r in row:					
					self.result['level'] = 'RED'
					output = output + r[0] + '\t' + r[1] + '\n'
			
			self.result['output'] = output
		
		return self.result
	
	def __init__(self, parent):
		print('Performing check: ' + self.TITLE)
