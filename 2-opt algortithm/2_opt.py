import math
import random

import matplotlib.pyplot as plt


def generate_points(low: int, high: int, point_num: int) -> tuple[list[tuple[float, float]], list[list[float]]]:
    """Generate a cost matrix for 2D Cartesian points."""
    random.seed(42)  # For reproducibility
    locations: list[tuple[float, float]] = [
        (random.randint(low, high), random.randint(low, high)) for _ in range(point_num)
    ]
    cost_list: list[list[float]] = []
    for location in locations:
        each_cost: list[float] = [
            math.sqrt((location[0] - dest[0]) ** 2 + (location[1] - dest[1]) ** 2) for dest in locations
        ]
        cost_list.append(each_cost)
    return locations, cost_list


def total_distance(tour: list[int], cost_matrix: list[list[float]]) -> float:
    """Calculate the total distance of the tour."""
    return sum(cost_matrix[tour[i]][tour[(i + 1) % len(tour)]] for i in range(len(tour)))


def two_opt(tour: list[int], cost_matrix: list[list[float]]) -> list[int]:
    """2-opt algorithm to improve the tour."""
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1:
                    continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                if total_distance(new_tour, cost_matrix) < total_distance(tour, cost_matrix):
                    tour = new_tour
                    improved = True
        if not improved:
            break
    return tour


def plot_tour(locations: list[tuple[float, float]], tour: list[int]):
    """Plot the tour."""
    x = [locations[i][0] for i in tour + [tour[0]]]
    y = [locations[i][1] for i in tour + [tour[0]]]
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, "o-")
    plt.title("2-opt TSP Tour")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()


# Main execution
if __name__ == "__main__":
    low_point: int = random.randint(-100, -1)
    high_point: int = random.randint(1, 100)
    point_num: int = random.randint(2, 15)
    locations, cost_matrix = generate_points(low_point, high_point, point_num)
    initial_tour: list[int] = list(range(point_num))
    random.shuffle(initial_tour)
    optimized_tour: list[int] = two_opt(initial_tour, cost_matrix)

    # Printing results
    print("Lowest Axis Coordinate: %i" % low_point)
    print("Highest Axis Coordinate: %i" % high_point)
    print("Number of points: %i" % point_num)
    print("Initial tour:", initial_tour)
    print("Initial distance:", total_distance(initial_tour, cost_matrix))
    print("Optimized distance:", total_distance(optimized_tour, cost_matrix))
    plot_tour(locations, optimized_tour)
