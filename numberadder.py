n = int(input("Enter a Whole Number "))
o = int("%s" % n)
p = int("%s%s" % (n, n))
q = int("%s%s%s" % (n, n, n))
print(o + p + q)