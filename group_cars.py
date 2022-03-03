import json
from pypareto import Comparison, by_none, MaxMinList, MaxMin, by_value, GroupNones, Domination


def read_data(filename:str) -> list:
    with open(filename, 'r') as f:
        data = json.load(f)
        yield from construct_rows(data)



def construct_rows(data):
    """
    rows are going to be [[year, km, price, id]*]
        year: maximize
        km: minimize
        price: minimize
        id: has to be unique and not None
    """
    names = ["year", "km", "price", "id"]

    for entry in data.get('cars', []):
        yield ( entry.get("year", None), entry.get("km", None), entry.get("price", None), entry.get("id") )


sorter_chain = GroupNones(
    MaxMinList(
        MaxMin.MIN, # no year means old
        MaxMin.MAX, # no km means lots of drive
        MaxMin.MAX) # no prize means expensive
        ).and_then(
    Comparison(by_value, MaxMinList(
        MaxMin.MAX,   # Maximize year
        MaxMin.MIN,   # Minimize km
        MaxMin.MIN,   # Minimize prize
        ))) # Minimize stock prize / markets


def get_groups(filename:str) -> list:
    rows = read_data(filename)
    pareto_sets = sorter_chain.split_by_pareto(rows)
    pareto_sets = map(lambda aset: sorted(list(aset), key=lambda item: item[3]), pareto_sets) # sort to alphabetic order
    return pareto_sets

