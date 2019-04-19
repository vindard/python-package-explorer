import indy
import re, json

class IndyMethods():

	def __init__(self):
		self.methods_ = {j: i for i in dir(indy) for j in dir(getattr(indy, i))}

	def find(self, regex):
		results = {}
		for m in self.methods_:
			match = re.search(regex, m)
			if match:
				results[m] = self.methods_[m]
		#print(json.dumps(results, indent=2))
		return results

	def __docstring(self, k, v):
		return getattr(getattr(indy, v), k).__doc__

	def __find_w_docstring(self, regex):
		results = self.find(regex)
		descriptions = {}
		for m in results:
			descriptions[m] = {
				'module': results[m],
				'docstring': self.__docstring(m, results[m])
				}
		return descriptions

	def print_docstrings(self, regex):
		b, _b = '\033[1m', '\033[0m'
		docstrings_dict = self.__find_w_docstring(regex)
		for m in docstrings_dict:
			print(f"{b}Call with: indy.{docstrings_dict[m]['module']}.{m}{_b}")
			print(docstrings_dict[m]['docstring'])
			print('-----\n')

