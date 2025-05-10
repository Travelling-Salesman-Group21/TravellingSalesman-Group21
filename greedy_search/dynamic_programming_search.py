""" To do a recursive Dynamic Programming solution to the Travelling Salesman Problem"""
import copy # to deep copy arrays

class DynamicProgrammingSearch:
    """ Class to solve the Travelling Salesman Problem using Dynamic Programming """
    def __init__(self, problem:list[list[int]], start_location: int) -> None:
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
    cost = [
        [0, 3, 2, 5],
        [1, 0, 3, 2],
        [2, 3, 0, 4],
        [3, 4, 2, 0]
    ]

    def main():
        dpn: DynamicProgrammingSearch = DynamicProgrammingSearch(cost, 0)
        dpn.print_results()
        print(dpn.output_results())
    main()

    del cost