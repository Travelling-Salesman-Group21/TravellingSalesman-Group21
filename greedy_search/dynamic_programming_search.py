import copy
class DynamicProgrammingSearch:
    def __init__(self, problem, start_location):
        self.cost_table:list[list[float]] = problem
        self.start_location:int = start_location

    def dynamic_search(self, search_path:list[int], current_cost:float, curr_node:int) -> tuple[list[int], float]:
        # Tracked Values
        best_path:list[int] = []
        best_cost:float = float('inf')

        # Base Case
        if len(search_path) == len(self.cost_table):
            best_cost:float = self.cost_table[search_path[-1]][self.start_location] + current_cost
            best_path.append(self.start_location)
            return best_path, best_cost

        # Each Path
        for node in range(len(self.cost_table)):
            if node == curr_node or node in search_path:
                continue
            temp_path:list[int] = copy.deepcopy(search_path)
            temp_path.append(node)
            next_cost:float = self.cost_table[temp_path[-1]][node] + current_cost
            get_result:tuple[list[int], float] = self.dynamic_search(temp_path, next_cost, node)
            temp_path:list[int] = get_result[0]
            temp_cost:float = get_result[1]
            if temp_cost < best_cost:
                best_path:list[int] = temp_path
                best_cost:float = temp_cost
        return best_path, best_cost

def main():
    dpn:DynamicProgrammingSearch = DynamicProgrammingSearch(cost, 0)
    dpn.dynamic_search([0], 0.0, 0)

if __name__ == '__main__':
    cost = [
        [0, 3, 2, 5],
        [1, 0, 3, 2],
        [2, 3, 0, 4],
        [3, 4, 2, 0]
    ]
    main()
    del cost