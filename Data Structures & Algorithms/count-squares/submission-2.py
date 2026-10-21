class CountSquares:
    def __init__(self):
        self.pointsCount = {}

    def add(self, point: List[int]) -> None:
        # Add it to dict if it doesnt already exist
        if tuple(point) not in self.pointsCount:
            self.pointsCount[tuple(point)] = 0

        # Increase the count by one
        self.pointsCount[tuple(point)] = self.pointsCount[tuple(point)] + 1

    def count(self, point: List[int]) -> int:
        # First find all points that can form a diagonal with this point
        res = 0
        pointX, pointY = point
        for key in self.pointsCount:
            # Check if current point is a diagonal:
            if abs((key[0] - pointX)) == abs((key[1] - pointY)) and key[0] != pointX:
                # Since it's a diagonal, see if we can find other two points in hashmap.
                if ((pointX, key[1]) in self.pointsCount) and (
                    (key[0], pointY) in self.pointsCount
                ):
                    res = res + self.pointsCount[key] * self.pointsCount[(pointX, key[1])] * self.pointsCount[(key[0], pointY)]
        return res
