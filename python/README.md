# Game Of Life - Python
This is the Conway's Game of Life written in Python.

Parameters that you can modify:
1. `Height`, `Width` - These are the dimensions of the Grid [default: `(200, 200)`]
2. `lowerBound`, `upperBound` - These are bounds for the evaluation metric as given by Conway [default: `(2, 3)`]
3. `ssc` - (Select Start Config) - Possible start configs: 1 - R-pentomino | 2 - Randomized [default: `1`]
4. `startLocations` - If `ssc` is 2 (Randomized), then `startLocations` are the number of points of spawn [default: `4000`]
5. `Window_Size` - Size of the window (display) [default: `(1000, 1000)`]
6. `speed_update` - Speed of updation of the Game of Life [default: `10`]
