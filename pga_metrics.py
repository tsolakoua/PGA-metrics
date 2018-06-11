import numpy as np
import pandas as pd
from collections import defaultdict
from collections import Counter
import sys
import argparse

def setup():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-d", "--dataset", required=True, help="Add the input dataset")
    parser.add_argument("-l", "--lang", required=False, help="Type the language searching for")
    return parser.parse_args()

def repos_no_license(data):
	count = 0
	no_license_repos = []
	for i in range(len(data)):
		row = data.iloc[i]
		if row.LICENSE is np.nan:
			count = count + 1
			no_license_repos.append(row.URL)
	print(count) # result 79117
	return no_license_repos
	 
def search_by_language(data, input_language):
	languages = []
	count = 0
	for i in range(len(data)):
		row = data.iloc[i]
		try:
			if "Perl" in row.LANGS:
				languages.append(row.URL)
				count = count + 1
		except TypeError:
			continue
	print(count)
	return languages

def count_organisations(data):
	urls = data.URL
	account_name = []
	for row in urls:
		token = row.split('/')[3]
		account_name.append(token)
	return Counter(account_name)

def main():
    args = setup()
    data = pd.read_csv(args.dataset)
    print(search_by_language(data, args.lang))
    print(count_organisations(data))
    print(repos_no_license(data))

if __name__ == "__main__":
    sys.exit(main())
