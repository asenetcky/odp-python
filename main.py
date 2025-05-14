import polars as pl
from sodapy import Socrata

def main():
   with Socrata("data.ct.gov", None) as client:
    results = client.get("qhtt-czu2", limit=10, offset=10)
    # results = client.get_all("qhtt-czu2")
    lf = pl.LazyFrame(results)
    print(lf.collect())


if __name__ == "__main__":
    main()