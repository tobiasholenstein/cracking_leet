class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        nrows = len(grid)
        ncols = len(grid[0])
        islands = []

        def new_island():
            islands.append(len(islands))
            return islands[-1]
        def find_island(island):
            if islands[island] == island:
                return island
            else:
                return find_island(islands[island])

        belongs = [[None for _ in range(ncols)] for _ in range(nrows)]
        for row in range(nrows):
            for col in range(ncols):
                if grid[row][col] == "1":
                    if row == 0:
                        if col == 0:  # row==0 col==0
                            belongs[row][col] = new_island()

                        else:  # row == 0 col !=0
                            if grid[row][col-1] == "1":  # left
                                belongs[row][col] = belongs[row][col-1]
                            else:
                                belongs[row][col] = new_island()
                    elif col == 0:  # row !=0 col == 0
                        if grid[row-1][col] == "1":
                            belongs[row][col] = belongs[row-1][col]
                        else:
                            belongs[row][col] = new_island()
                    else:
                        if grid[row-1][col] == "1":
                            if grid[row][col-1] == "1":  # both
                                top_island = find_island(belongs[row-1][col])
                                left_island = find_island(belongs[row][col-1])
                                if top_island == left_island:
                                    belongs[row][col] = top_island
                                else:
                                    (min_island, max_island) = (
                                        top_island, left_island) if top_island < left_island else (left_island, top_island)
                                    islands[max_island] = min_island
                                    belongs[row][col] = min_island
                            else:  # only top
                                belongs[row][col] = belongs[row-1][col]
                        else:
                            if grid[row][col-1] == "1":  # only left
                                belongs[row][col] = belongs[row][col-1]
                            else:  # none -> new island
                                belongs[row][col] = new_island()

                    # look at left and top if one of them is 1 then current belongs to same island
                    # if both are 0 then create a new island
                    # if both are 1:
                    #    if they are on the same island:
                    #        current belongs to the island
                    #    else:
                    #        unify the islands (in islands array point larger to smaller)
                
 

        return sum([1 for idx, isl in enumerate(islands) if isl == idx])

def test_many():
    grid = [["1","0","1","1","0","0","1","0","1","1","1","1","0","1","0","1","1","1","1","0"],["0","1","0","0","1","0","1","0","1","1","1","1","1","1","0","1","1","0","1","1"],["1","0","0","1","0","1","0","1","0","1","1","0","1","1","1","0","0","1","1","0"],["0","1","1","0","0","1","1","0","1","1","1","1","0","0","1","0","0","0","1","1"],["1","1","0","1","0","0","1","0","0","0","1","0","1","0","1","1","1","0","1","1"],["0","0","0","0","1","0","1","1","0","0","1","0","0","1","0","1","1","1","1","0"],["1","0","1","1","1","1","0","1","1","0","1","1","0","1","1","1","0","0","1","0"],["0","1","1","0","0","0","1","0","0","1","0","1","1","1","0","0","1","1","0","1"],["0","0","0","0","1","1","0","1","0","0","1","1","0","1","0","0","1","0","1","0"],["0","0","1","1","1","0","1","0","1","0","1","1","1","0","1","1","1","1","1","0"],["1","0","1","0","1","1","1","0","1","1","1","0","1","0","1","0","1","0","1","1"],["0","0","1","1","1","1","0","1","1","1","0","1","0","0","0","1","1","1","0","1"],["1","1","1","0","0","0","0","0","1","1","0","1","1","1","0","1","1","1","1","0"],["0","0","1","1","1","0","0","1","0","0","1","1","1","1","1","1","0","1","1","0"],["0","0","0","1","1","0","0","0","0","1","1","0","1","0","0","1","1","1","1","1"],["0","1","1","1","0","1","0","0","1","1","1","1","1","0","1","1","1","0","0","1"],["0","0","0","0","1","1","1","1","0","0","0","0","1","0","0","0","0","1","1","0"],["1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1","1","1"],["0","1","0","0","1","0","0","1","1","1","1","1","1","0","1","0","1","1","1","1"],["0","0","1","1","1","1","1","0","0","0","1","1","1","1","1","1","0","1","1","0"]]
    sol = Solution()
    assert sol.numIslands(grid) == 23

def test_four():
    grid = [["1", "1", "1", "1", "1", "0", "1", "1", "1", "1"],
            ["1", "0", "1", "0", "1", "1", "1", "1", "1", "1"],
            ["0", "1", "1", "1", "0", "1", "1", "1", "1", "1"],
            ["1", "1", "0", "1", "1", "0", "0", "0", "0", "1"],
            ["1", "0", "1", "0", "1", "0", "0", "1", "0", "1"],
            ["1", "0", "0", "1", "1", "1", "0", "1", "0", "0"],
            ["0", "0", "1", "0", "0", "1", "1", "1", "1", "0"],
            ["1", "0", "1", "1", "1", "0", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "0", "1"],
            ["1", "0", "1", "1", "1", "1", "1", "1", "1", "0"]]
    sol = Solution()
    assert sol.numIslands(grid) == 2


def test_simple():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    sol = Solution()
    assert sol.numIslands(grid) == 1


def test_two():
    grid = [
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    sol = Solution()
    assert sol.numIslands(grid) == 2


def test_five():
    grid = [
        ["1", "1", "0", "1", "0"],
        ["0", "0", "0", "1", "0"],
        ["1", "1", "0", "0", "1"],
        ["0", "0", "1", "1", "0"]
    ]
    sol = Solution()
    assert sol.numIslands(grid) == 5


def test_three():
    grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
    sol = Solution()
    assert sol.numIslands(grid) == 1


# look at left and top if one of them is 1 then current belongs to same island
# if both are 0 then create a new island
# if both are 1:
#    if they are on the same island:
#        current belongs to the island
#    else:
#        unify the islands (in islands array point larger to smaller)
