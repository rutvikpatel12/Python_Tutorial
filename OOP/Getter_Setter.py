# class MyClass:
#     def __init__(self, value):
#         self._value = value

#     def show(self):
#         print(f"Value is: {self._value}")

#     @property
#     def ten_value(self):
#         return 10* self._value

#     @ten_value.setter
#     def ten_value(self, new_value):
#         self._value = new_value/10

# obj = MyClass(10)
# obj.ten_value = 67
# print(obj.ten_value)
# obj.show()

# --- GETTER
# class Mobile:
#     def __init__(self):
#         self.model = 'Realme'
    
#     def get_model(self):
#         return self.model

# r3 = Mobile()
# m = r3.get_model()
# print(m)

# --- SETTER
class Mobile():
    def __init__(self):
        self.model = "Realme"
    
    def set_model(self):
        self.model = "SamSung"

realme = Mobile()
# Before Setting
print(realme.model)

# After Setting
realme.set_model()
print(realme.model)