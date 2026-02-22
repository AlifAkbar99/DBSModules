def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info
print(cetak_info(nama='Muhammad Alif', usia='20', pekerjaan="AI Engineer"))