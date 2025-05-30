import random
import math
import timeit
import matplotlib.pyplot
import seaborn
import greedy_search.dynamic_programming_search as dps
import k_opt_algorithm.k2_opt as ko

low_point:int = 10000
high_point:int = 10000
point_count:int = 10 # max 991
start:int = 0

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

def main(num:int) -> None:
    # Running Code
    point_map:list[list[float]] = generate_points(
            low=low_point,
            high=high_point,
            point_num=num
            )
    start_time: float = timeit.default_timer()
    dps.DynamicProgrammingSearch(
        problem=point_map,
        start_location=start
    )
    end_time: float = timeit.default_timer()
    times[each]: dict[int, float] = end_time - start_time
    print(f"iter: {num}, time: {times[num]}")

# Starting the run
times: dict[int, float] = {}
total_time_start:float = timeit.default_timer()
for each in range(1, point_count):
    main(each)
    # if total_time_start - timeit.default_timer() > 420:
    #     break

total_time_end: float = timeit.default_timer()
total_time:float = total_time_end - total_time_start

print(times)
print("Time Taken:", total_time, "Node Count", point_count)
seaborn.lineplot(data=times, color="blue", label="BnB")
# matplotlib.pyplot.xlabel("Node Count")
# matplotlib.pyplot.ylabel("Time (s)")
# matplotlib.pyplot.title("BnB Time Taken")
# matplotlib.pyplot.show()

times2: dict[int, float] = {}
total_time_start_2:float = timeit.default_timer()
def opting(opto):
    opt_point_map = generate_points(low_point, high_point, opto)
    initial_tour: list[int] = list(range(opto))
    timer_start = timeit.default_timer()
    optimized_tour: list[int] = ko.two_opt(initial_tour, opt_point_map)
    timer_end = timeit.default_timer()
    times2[opto]: float = timer_end - timer_start
    print(f"iter: {opto}, time: {times2[opto]}")

for point in range(2, point_count):
    opting(point)

total_time_end_2: float = timeit.default_timer()
total_time_2:float = total_time_end_2 - total_time_start_2
print(times2)
print("Time Taken:", total_time_2, "Node Count", point_count)
seaborn.lineplot(data=times2, color="red", label="2-Opt")
matplotlib.pyplot.xlabel("Node Count")
matplotlib.pyplot.ylabel("Time (s)")
# matplotlib.pyplot.title("2-opt Time Taken")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
