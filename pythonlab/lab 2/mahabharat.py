# . If the given string S1= “Maha Bharat”, generate the following strings
# by manipulating S1.
# a. “mAHA bHARAT”
# b. “Bharat”
# c. “BharatBharatBharat”
# d. “Mera Bharat”
# e. “Mera Bharat Mahan”

s="Maha Bharat"
a = s[5:]
print(a)
h=a*3
print(h)
c=s.replace("a","e",1)
c=c.replace("h","r",1)
print(c)
s1 = s[0:4] + "n"
c = c+" "+s1
print(c)
print(s.swapcase())