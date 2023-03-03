# Tool for checking extern broken links
## Installation
After cloning this repo, you can create a virtual environment with Python:  
```py
python3 -m venv <env_name>
````
Enter the newly created virtual environment:  
```py
source <env_name>/bin/activate
```
And install the requirements:  
```py
pip3 install -r requirements.txt
````

## How to run
While you are into your virtual environment, you can run this command to run the tool:
```py
python3 brokenExtLinks.py
````
## Explanations
This script uses LinkChecker (https://github.com/linkchecker/linkchecker).
After LinkChecker is completed, it gets the results into a .txt file (linkchecker-out.txt). The next lines of the script will parse the text file and will look for lines that contain "Result     Error: 404 Not Found".  
It will report the Broken URL, Name and Parent URL. With those information, it's easy to locate the broken link.  
Here is an example of an output

```
BROKEN LINKS REPORT:

URL: `<some_url.com>'
Name: `<name_of_the_link>'
Parent URL: <url_where_is_located_the_broken_link>
Result     Error: 404 Not Found
...
Processed: xx
```