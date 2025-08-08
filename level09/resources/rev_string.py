import sys

hash = sys.argv[1]
rev_string = ""
for i in range(0, len(hash)):
    rev_string = rev_string + chr(ord(hash[i]) - i)
print(rev_string)
