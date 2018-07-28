# Genetic Algorithm

Genetic algorithm @ OCEV/UDESC

## Install

``` bash
> pip3 install numpy
> pip3 install matplotlib
> pip3 install scipy
> pip3 install opencv-contrib-python
> apt install python3-tk
```

## Run

``` bash
> python ga.py -h
```

## Problems
To solve other problems, you need to:
  
1. Create a fitness function at [fitness.py](fitness.py).
2. Create the problem's object at [problems.py](problems.py).
3. Then modify line 27 at [ga.py](ga.py) to use your problem.
