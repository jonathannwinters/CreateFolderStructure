#!//usr/bin/python



__author__ = "Jonathan N. Winters"
__copyright__ = "Copyright Feb, 4 2021"
__credits__ = [""]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Jonathan N. Winters"
__email__ = "jnw25@cornell.edu"
__status__ = ""


# Usage:
# create a single column text file with all of the desired relative paths, ie:
#  folder1/subfolder1
#  folder2/subfolder2
#  folder3/subfolder3
# and so on...

# save the file as input.txt

# execut the following:
#  $ CreateFolderStructure.py input.txt /destination/path

import sys, os

input_file = sys.argv[1]


with open(input_file) as file:
    for count,line in enumerate(file):
        relative_path = line.strip()
        full_path = sys.argv[2] + relative_path
        os.makedirs(full_path)




