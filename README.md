# Tool for checking extern broken links
## Installation
After cloning this repo, you can create a virtual environment with Python:  
```py
python3 -m venv <env_name>
````
Enter the newly created virtual environment:  
```py
source <env_name>/bon/activate
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
This script uses LinkChecker (https://github.com/linkchecker/linkchecker), get the results to a .csv file (linkchecker-out.csv).  
The initial output has three lines at the beginning that starts with '#'. Because of that, it's impossible to parse the information correctly, so there is another step that retrieves lines starting with 'http' and saves it to a new csv file (broken_links.csv).  
With this new file, it's easier to parse information and get the 404 status. The final output is in this format:  
```
Broken links:
PARENT URL: https://<some_url.com> has this broken link URL: https://<broken_link.com>
...
Processed: xx
```