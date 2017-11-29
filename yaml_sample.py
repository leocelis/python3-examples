# Read yaml file
import pprint
import sys

import yaml

try:
    with open('yaml/yaml_sample.yaml', 'r') as f:
        sample = yaml.safe_load(f)
except OSError as e:
    sys.exit("File not found. Details: {e}".format(e=str(e)))

# pprint.pprint(type(sample))
pprint.pprint(sample)
# pprint.pprint(sample['this']['is']['a']['sample'])

for root in sample:
    print("Root:", root)

    for level1 in root:
        print("  Level 1:", level1)

        for level2 in level1:
            print("    Level 2:", level2)

order = sample['order']
print("Order: {o}. Type: {t}".format(o=order, t=str(type(order))))
