class Hwang:
    def __init__(self, values=None):
        self.values = values

    def __len__(self):
        return len(self.values)
    
    def __getitem__(self, key):
        return self.values[key]
    
    def __setitem__(self, key, value):
        self.values[key] = value
    
    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)
    
    def __call__(self):
        print('calling')

Hwang()
h = Hwang({'age': 26, 'first_name': 'seoyeon'})

print(len(h)) # __len__ 호출 -> 출력값 : 2
print(h['age']) # __getitem__ 호출 -> 출력값 : 26
h['gender'] = 'women' # __setitem__ 호출
del h['gender'] # __delitem__ 호출
for x in h: # __iter__ 호출 -> 출력값 : age, first_name
    print(x)
