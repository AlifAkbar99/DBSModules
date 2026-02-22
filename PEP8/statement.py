# 1. statement gabungan
foo = 20

# disarankan seperti ini
if foo == 'blah':
    do_blah_thing()
    do_one()
    do_two()
    do_three()
    
# 2. Trailing commas

# disaranakn seperti ini
FILES = 'setup.cfg',

def initialize(files, error=False):
    print(files, error)
    
# saran lainnya
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES, 
           error = True,
           )

# 3. Anotasi fungsi
def LuasPersegiPanjang(panjang: int = 2, lebar: int = None):
    luas = panjang*lebar
    return luas
luas_satu = LuasPersegiPanjang(lebar=2)
print(luas_satu)

