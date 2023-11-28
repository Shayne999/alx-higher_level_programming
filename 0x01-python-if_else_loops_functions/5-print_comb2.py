#!/usr/bin/python3
for i in range(100):
    if i == 100:
        print("{}".format(i))
    else:
        print("{:02}".format(i), end=", ")
