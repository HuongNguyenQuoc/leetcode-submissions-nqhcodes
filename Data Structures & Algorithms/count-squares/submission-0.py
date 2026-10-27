class CountSquares:

    def __init__(self):
        self.points = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[x][y] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        res = 0
        '''
        points = {
            3: Counter({3: 1, 4: 1}),
            5: Counter({5: 1, 7: 1})
        }
        '''
        for y, freq in self.points[qx].items():
            if y == qy:
                continue

            d = y - qy

            for x in (qx + d, qx - d):
                res += (
                    freq *
                    self.points[x][qy] *
                    self.points[x][y]
                )
        
        return res

