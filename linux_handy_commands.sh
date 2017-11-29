# list of the files types
find . -type f -name "*.*" | awk -F. '{print $NF}' | sort -u

# search for different strings including/excluding files
grep -E "CAAA|CAAC|AAAC|CAAH" -r ./ --include \*.py --include \*.yml --include \*.yaml --exclude-dir="\site-packages"