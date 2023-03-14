#!/usr/bin/python3
"""
Module for checking broken links (404)

Use https://docs.csc.fi/ as default URL for checking.
If you want to test another URL, you need to specify as argument

eg: ./broken_ext_links.py https://www.google.com
"""

import subprocess
import sys

def check_broken_ext_links(url):
    """
    Function for checking broken links (404).
    """
    subprocess.run(["linkchecker", "--check-extern", "-F", "text", "-q", url], check=False)

    with open("linkchecker-out.txt", "r", encoding="utf-8") as f_in:
        file = f_in.read()
        result = "Result     Error: 404 Not Found"
        counter = 0

        print("BROKEN LINKS REPORT: \n")
        for line in file.split('\n\n'):
            if result in line:
                url = line.split('\n')[0].split('        ')[-1]
                name = line.split('\n')[1].split('       ')[-1]
                parent_url = line.split('\n')[2].split(' ')[-5].strip(',')
                counter += 1
                print(f"URL: {url}\nName: {name}\nParent URL: {parent_url}\n{result}\n")
        print(f"Processed: {counter}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        URL = "https://docs.csc.fi/"
        print(f"No URL specified, testing: {URL}")
    else:
        URL = sys.argv[1]
        print(f"Testing {URL}")

    check_broken_ext_links(URL)
