import requests
import json

"""source: https://github.com/allenai/s2-folks/blob/main/examples/python/search_bulk/get_dataset.py"""
query = "python type annotations"
fields = "title,year,citationCount,fieldsOfStudy"

url = f"http://api.semanticscholar.org/graph/v1/paper/search/bulk?query={query}&fields={fields}&year=2007-"
r = requests.get(url).json()
try:
    print(f"Will retrieve an estimated {r['total']} documents")
except KeyError:
    print(r)
retrieved = 0

with open(f"papers.jsonl", "a") as file:
    while True:
        if "data" in r:
            retrieved += len(r["data"])
            print(f"Retrieved {retrieved} papers...")
            for paper in r["data"]:
                print(json.dumps(paper), file=file)
        if "token" not in r:
            break
        r = requests.get(f"{url}&token={r['token']}").json()

print(f"Done! Retrieved {retrieved} papers total")
