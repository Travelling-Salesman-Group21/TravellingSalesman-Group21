import copy
class DynamicProgrammingSearch:
    def __init__(self, problem:list[list[int]], start_location: int) -> None:
        self._cost_table:list[list[float]] = problem
        self._start_location:int = start_location
        self._best_route:list[int] = []
        self._best_cost:float = float('inf')

    def search(self) -> None:
        self._best_route, self._best_cost = self._dynamic_search([self._start_location], 0.0, self._start_location)

    def output_results(self) -> tuple[list[int], float]:
        return self._best_route, self._best_cost

    def print_results(self) -> None:
        print("Best route:", self._best_route)
        print("Best cost:", self._best_cost)

    def _dynamic_search(self, search_path:list[int], current_cost:float, curr_node:int) -> tuple[list[int], float]:
        # Tracked Values
        best_path:list[int] = []
        best_cost:float = float('inf')

        # Base Case
        if len(search_path) == len(self._cost_table):
            best_cost:float = self._cost_table[search_path[-1]][self._start_location] + current_cost
            best_path.append(self._start_location)
            return best_path, best_cost

        # Each Path
        for node in range(len(self._cost_table)):
            if node == curr_node or node in search_path:
                continue
            temp_path:list[int] = copy.deepcopy(search_path)
            next_cost:float = self._cost_table[temp_path[-1]][node] + current_cost
            temp_path.append(node)
            print(temp_path) # checking searches
            get_result:tuple[list[int], float] = self._dynamic_search(temp_path, next_cost, node)
            print(get_result) # checking tuple
            new_temp_path:list[int] = get_result[0]
            temp_cost:float = get_result[1]
            if temp_cost < best_cost and temp_path[-1] != self._start_location:
                best_path:list[int] = new_temp_path
                best_cost:float = temp_cost
                print(best_path)
        return best_path, best_cost

def main():
    dpn:DynamicProgrammingSearch = DynamicProgrammingSearch(cost, 0)
    dpn.search()
    dpn.print_results()

if __name__ == '__main__':
    cost = [
        [0, 3, 2, 5],
        [1, 0, 3, 2],
        [2, 3, 0, 4],
        [3, 4, 2, 0]
    ]
    main()
    del cost