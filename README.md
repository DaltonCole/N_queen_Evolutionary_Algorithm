# N Queen problem

This is an evolutionary algorithm solution to the n queen problem.

## Run

```
python3 ec.py <board size> <random seed (optional)>
```

## Example

```
$ python3 ec.py 8 1504886928
Iteration: 	55
Random Seed:	1504886928
|   |   |   | Q |   |   |   |   |
---------------------------------
|   | Q |   |   |   |   |   |   |
---------------------------------
|   |   |   |   |   |   | Q |   |
---------------------------------
|   |   | Q |   |   |   |   |   |
---------------------------------
|   |   |   |   |   | Q |   |   |
---------------------------------
|   |   |   |   |   |   |   | Q |
---------------------------------
| Q |   |   |   |   |   |   |   |
---------------------------------
|   |   |   |   | Q |   |   |   |
---------------------------------

Valid queens: 	8
```

## Requirments
Tested on Python 3.5.2

## Notes
This is my first EA :)