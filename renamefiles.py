import os

arr = os.listdir()
print(arr)


for filename in arr:
    os.rename(filename, filename.replace(".720p.BluRay.x264-SHORTBREHD", "").lower())
    print(filename)