# #!/usr/bin/python3
for i in range(1, 90):
    if i == 89:
        print("{}".format(i))
    elif (i == 10) | (i == 11) | (i == 20) | (i == 21) | (i == 22) | (i == 30) | (i == 31) | (i == 32) | (i == 33) | (i == 30):
        continue
    else:
        print("{:02}".format(i), end=", ")
