from typing import List

import plac
from pytrends.request import TrendReq


@plac.annotations(
    geo=("Country code", "option", "g", str, None, "NL"),
    keywords=("Comma separated list of keywords", "positional", None, lambda x: x.split(','), None))
def main(keywords: List[str],
         geo: str = "NL") -> None:
    """ Runner """
    pytrend = TrendReq()
    pytrend.build_payload(kw_list=keywords, geo=geo)
    # Interest Over Time

    interest_over_time_df = pytrend.interest_over_time()
    pprint(interest_over_time_df.tail())

    # Interest by Region
    interest_by_region_df = pytrend.interest_by_region()
    print(interest_by_region_df.head())

    # Related Queries, returns a dictionary of dataframes
    related_queries_dict = pytrend.related_queries()
    print(related_queries_dict)


if __name__ == "__main__":
    plac.call(main)
