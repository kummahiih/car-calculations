
import sys
from pprint import pprint
from .group_cars import get_groups



if __name__ == "__main__":
    pareto_sets = get_groups(sys.argv[1])

    for i, pareto_set in enumerate(pareto_sets):
        print("===Pareto set {} ===".format(i))
        print("#: {}".format(len(pareto_set)))
        pprint(pareto_set)