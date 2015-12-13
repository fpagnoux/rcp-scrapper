import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("url", help="URL of the page with the polling data")
parser.add_argument("outputfile", nargs='?', help="CSV output file")
parser.add_argument("--noavg", help="Do not include the RCP Average row",
                    action="store_true")
args = parser.parse_args()

url = args.url
output = args.outputfile
if output is None:
    filename = url.split('/')[-1].split('.')[0]
    output = filename + ".csv"
    print("No output file specified : using " + output)
elif not output.endswith(".csv"):
    output += ".csv"
if os.path.isfile(output):
    os.remove(output)
noavg_opt = " -a noavg=1" if args.noavg else ""
os.system("scrapy crawl realclearpoliticsSpider -a url="+url+noavg_opt+" -o "+output)

