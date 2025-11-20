import sys
from stats import report
if len(sys.argv) > 1:
    report(sys.argv[1])
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)