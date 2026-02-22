class MyClass:
    def __init__(self):
        self._private_var = 42 # variabel non publik dengan awalan garis bawah
        self._secret_list = [1, 2, 3] # variabel non publik lainnya
    
    def _private_method(self):
        print("ini adalah method non publik")
    
    def public_method(self):
        print("ini adalah method publik")
        self._private_method()