from bs4 import BeautifulSoup

with open("linkchecker-out.html", "r") as htmlfile:
    contents = htmlfile.read()
    soup = BeautifulSoup(contents, 'html.parser')

    for name in soup:
        if soup.tag.name('URL'):
            print(name)
    #print(soup.get_text())

    # for tag in soup.find_all('td'):
    #     print(tag.name)