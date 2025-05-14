"""
Travelling Salesman Problem
To do a recursive Dynamic Programming solution
Branch & Prune Method

WARNING: Number of points Above about 10 may turn computer into Heater for quite a while
This algorithm has The Worst Case Time Complexity: O(N!)
YOu have been WARNED

- Searches all nodes connected to the current node to get cost
    - if the next node is not a leaf node
        - the cost cannot be determined
        - if the cost to reach a child node is greater than the upper bound
            - that node is skipped
        - the child nodes need to be queried and the total cost to get to them needs to be calculated
        - the process repeats until it reaches a leaf node
    - if the next node is a leaf node
        - the total cost to get to that node is calculated
        - the total cost is returned back up the tree.
        - when receiving a total cost from a child node
            - the total cost is lower than the previous upper bound
"""

import copy # to deep copy arrays
import math


class DynamicProgrammingSearch:
    """ Class to solve the Travelling Salesman Problem using Dynamic Programming """
    def __init__(self, problem:list[list[float]], start_location: int) -> None:
        """ Initializing Class with the required fields"""
        # Constant Fields
        self._cost_table:list[list[float]] = problem
        self._start_location:int = start_location

        # Results Field
        self._best_route:list[int] = []
        self._best_cost:float = float('inf')

        # Starting Search
        self._search()

    def output_results(self) -> tuple[list[int], float]:
        """ Method to output usable values for _best_route and _best_cost"""
        return self._best_route, self._best_cost

    def print_results(self) -> None:
        """ Method to output the results to terminal """
        print("Best route:", self._best_route)
        print("Best cost:", self._best_cost)

    def _search(self) -> None:
        """ method to start searching"""
        self._best_route, self._best_cost = self._dynamic_search([self._start_location], 0.0, self._start_location)

    def _dynamic_search(self, search_path:list[int], current_cost:float, curr_node:int) -> tuple[list[int], float]:
        """ Recursive function to dynamically search graph for travelling salesman problem"""

        # Tracked Values
        best_path:list[int] = []
        best_cost:float = float('inf')

        # Base Case
        if len(search_path) == len(self._cost_table):
            """ For when all nodes have been searched to return to the origin """
            best_cost:float = self._cost_table[search_path[-1]][self._start_location] + current_cost
            best_path:list[int] = copy.deepcopy(search_path)
            best_path.append(self._start_location)
            # leaf returning result of going back to origin back down the stack
            return best_path, best_cost

        # Each Path
        for node in range(len(self._cost_table)):
            """ to search the cost of each node then the cost of their children till all paths are searched """
            if node == curr_node or node in search_path: # skipping this loop if attempting to find the cost of node going to it's self
                continue
            # copying due to each time the method is called needing a separate array otherwise they all over write each other
            temp_path:list[int] = copy.deepcopy(search_path)
            next_cost:float = self._cost_table[temp_path[-1]][node] + current_cost
            temp_path.append(node)
            get_result:tuple[list[int], float] = self._dynamic_search(temp_path, next_cost, node) # point of recursion
            if get_result[1] < best_cost and temp_path[-1] != self._start_location:
                best_path:list[int] = get_result[0]
                best_cost: float = get_result[1]
        # returning the result to the next down in the stack
        return best_path, best_cost

if __name__ == '__main__':
    import random

    low_point:int = random.randint(-100, -1)
    high_point:int = random.randint(1, 100)
    point_count:int = random.randint(2, 15)

    def generate_points(low:int, high:int, point_num:int) -> list[list[float]]:
        """ Generating list of 2D Cartesian points """
        locations:list[tuple[float, float]] = [
            (random.randint(low, high),
             random.randint(low, high)
             ) for _ in range(point_num)
        ]

        cost_list:list[list[float]] = []
        for location in locations:
            each_cost:list[float] = []
            each_cost.extend(
                math.sqrt(
                    (location[0]-destination[0])**2
                    +(location[1]-destination[1])**2
                ) for destination in locations
            )
            cost_list.append(each_cost)
        return cost_list

    def main():
        # Running Code
        dpn: DynamicProgrammingSearch = DynamicProgrammingSearch(
                                            problem=generate_points(
                                                            low=low_point,
                                                            high=high_point,
                                                            point_num=point_count
                                                            ),
                                            start_location=0
        )

        # Printing Things
        # Attributes of the problem
        print("Lowest Axis Coordinate: %i" % low_point)
        print("Highest Axis Coordinate: %i" % high_point)
        print("Number of points: %i" % point_count)
        # Results
        dpn.print_results()
        # Results of return value
        print(f"Tuple Format\n%s" % str(dpn.output_results()))

    # Starting the run
    main()

    # JUST PARANOIA
    # making sure all the references are deleted from the environment so they don't pollute memory
    del low_point, high_point, point_count # variables
    del main, DynamicProgrammingSearch # methods, classes
    del random, copy, math # imports