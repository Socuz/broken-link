import subprocess
import csv

def check_broken_ext_links():
    headerList = ["urlname", "parentname", "base", "result", "warningstring", "infostring", "valid", "url", "line", "column","name", "dltime", "size", "checktime", "cached", "level", "modified"]

    subprocess.run(["linkchecker", "--check-extern", "-F", "csv", "-q", "https://docs.csc.fi"])

    # Clean csv linkchecker output
    with open("linkchecker-out.csv", "r") as csv_in, open("broken_links.csv", "w") as csv_out:
        csv_writer = csv.writer(csv_out)
        dw = csv.DictWriter(csv_out, delimiter=';', fieldnames=headerList)
        dw.writeheader()

        [csv_writer.writerow(row) for row in csv.reader(csv_in) if row[0].startswith("http")]

    # Read the new output file and get 404 errors
    with open("broken_links.csv", "r") as csv_in:
        csv_reader = csv.reader(csv_in, delimiter=';')
        line_count = 0

        print("Broken links:")
        for row in csv_reader:
            try:
                error = row[3].startswith("404")
                if error:
                    print(f"PARENT URL: {row[1]} has this broken link URL: {row[0]}")
                    line_count += 1
            except IndexError:
                pass
        
        print(f"Processed: {line_count}")

if __name__ == "__main__":
    check_broken_ext_links()