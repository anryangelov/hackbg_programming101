import os
import os.path
import sys


path = sys.argv[1]


files = []


def find_files(d):
    if os.path.isdir(d):
        for f in os.listdir(d):
            f = os.path.join(d, f)
            find_files(f)
    else:
        files.append(d)


find_files(path)


def get_size(fs):
    return sum([os.path.getsize(f) for f in fs])

size = get_size(files)/1000
print(size)
m = "KB"
d = 1

if 1000000 > size > 1000:
    m, d = "MB", 1000.0
elif size > 1000000:
    m, d = "G", 1000000.0

size = size/d

print("%s: %.2f%s" % (path, size, m))

