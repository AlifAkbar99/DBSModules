def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi")
        func() # @my_decorator bakalan kepanggil di func()
        print("Setelah fungsi dieksekusi")
    return wrapper

# Dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("Hello World")
    
# Memanggil fungsi yang sudah didekorasi
say_hello()