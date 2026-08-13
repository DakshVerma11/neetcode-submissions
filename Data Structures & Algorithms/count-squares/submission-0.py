class CountSquares:
    def __init__(self):
        # Map x -> Counter(y -> count)
        self.points_by_x = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points_by_x[x][y] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        total_squares = 0

        # For each point (x1, y2) that shares the same x-coordinate
        for y2, count_y2 in self.points_by_x[x1].items():
            side = y2 - y1
            if side == 0:
                continue   # same point, not a valid square

            # Two possible squares: one extends to the right (x1 + side),
            # the other to the left (x1 - side) of the vertical line.
            for x_other in (x1 + side, x1 - side):
                # The other two corners must be:
                # (x_other, y1) and (x_other, y2)
                count_x_other_y1 = self.points_by_x[x_other].get(y1, 0)
                count_x_other_y2 = self.points_by_x[x_other].get(y2, 0)

                # Add number of ways to form this square
                total_squares += count_y2 * count_x_other_y1 * count_x_other_y2

        return total_squares