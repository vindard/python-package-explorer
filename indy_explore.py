import indy, json

class IndyMethods():

	def __init__(self):
		self.methods_ = [{j: i} for i in dir(indy) for j in dir(getattr(indy, i))]

	def find(self, search):
		results = []
		for m in self.methods_:
			for v in m.keys():
				if search in v:
					results.append(m)
		#print(json.dumps(results, indent=2))
		return results

	def __docstring(self, method_dict):
		k, v = list(method_dict.items())[0]
		return getattr(getattr(indy, v), k).__doc__

	def __find_w_docstring(self, search):
		results = self.find(search)
		descriptions = []
		for d in results:
			descriptions.append((d, self.__docstring(d)))
		return descriptions

	def print_docstrings(self, search):
		docstrings_tuples = self.__find_w_docstring(search)
		for method in docstrings_tuples:
			print(method[0])
			k = list(method[0].keys())[0]
			print(f"Call with: indy.{method[0][k]}.{k}")
			print(method[1])
			print('-----\n')

