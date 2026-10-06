class MyClass:
    def __init__(self,value):
        self._value = value


    def show(self):
        print(f"value is : {self._value}")


    @property
    def ten_value(self):
        retur