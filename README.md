# Tool for checking extern broken links
## Installation
After cloning this repo, you need to install the requirements:
```py
pip3 install -r requirements.txt
````

## How to run
While you are into your virtual environment, you can run this command to run the tool:
```py
./broken_ext_links.py <opt_arg>
````
By default, if no argument is specified (_opt_arg_), it will run the test on **https://docs.csc.fi/**. It will last around 10 minutes.  
Otherwise, it will test the given website.
## Explanations
This script uses LinkChecker (https://github.com/linkchecker/linkchecker).
After LinkChecker is completed, it gets the results into a .txt file (linkchecker-out.txt). The next lines of the script will parse the text file and will look for lines that contain "Result     Error: 404 Not Found".  
It will report the Broken URL, Name and Parent URL. With those information, it's easy to locate the broken link.  
Here is an example of an output:

```
BROKEN LINKS REPORT:

URL: `<some_url.com>'
Name: `<name_of_the_link>'
Parent URL: <url_where_is_located_the_broken_link>
Result     Error: 404 Not Found
...
Processed: xx
```