import subprocess

def check_broken_ext_links():
    subprocess.run(["linkchecker", "--check-extern", "-F", "text", "-q", "https://docs.csc.fi"])

    with open("linkchecker-out.txt", "r") as f_in:
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
    check_broken_ext_links()