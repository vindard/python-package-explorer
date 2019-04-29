import re, json

class Explore():

	def __init__(self, package):
		self.package = package
		self.methods_ = {j: i for i in dir(self.package) for j in dir(getattr(self.package, i))}

	def find(self, regex):
		results = {}
		for m in self.methods_:
			match = re.search(regex, m)
			if match:
				results[m] = self.methods_[m]
		#print(json.dumps(results, indent=2))
		return results

	def __docstring(self, k, v):
		return getattr(getattr(self.package, v), k).__doc__

	def __find_w_docstring(self, regex):
		results = self.find(regex)
		descriptions = {}
		for m in results:
			descriptions[m] = {
				'module': results[m],
				'docstring': self.__docstring(m, results[m])
				}
		return descriptions

	def get_docstrings(self, regex):
		b, _b = '\033[1m', '\033[0m'
		docstrings_dict = self.__find_w_docstring(regex)
		result = ''
		for m in docstrings_dict:
			line1 = f"\n{b}Call with: {self.package.__name__}.{docstrings_dict[m]['module']}.{m}{_b}\n"
			line2 = docstrings_dict[m]['docstring']
			linesep = f"\n\n-----\n"
			result += f"{linesep}{line1}{line2}"
		result = result[len(linesep):]   # trim last linesep

		return result

	def describe(self, regex):
		print(self.get_docstrings(regex))

