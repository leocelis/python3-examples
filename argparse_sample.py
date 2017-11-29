import argparse

# description
parser = argparse.ArgumentParser(description="calculate X to the power of Y")

# mutually exclusive arguments
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")

# regular arguments
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")

# parse arguments
args = parser.parse_args()

# perform operation
answer = args.x ** args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))
