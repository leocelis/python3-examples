# validate timestamps
vl = ["495084958856", "1508599259"]

for v in vl:
    try:
        int(v)
    except ValueError:
        print("Not a valid timestamp")

    vlen = len(str(v))

    if vlen != 10 and vlen != 13:
        print("Not a valid timestamp: {}".format(v))
    else:
        print("Valid timestamp: {}".format(v))
