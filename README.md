# Game of Life

This repository is an implementation of [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) following the video called [Conway's Game of Life in Python](https://www.youtube.com/watch?v=cRWg2SWuXtM) of [NeuralNine](https://www.youtube.com/c/NeuralNine).

## Conda

To create a conda environment, you have to use the command:

```sh
conda env create -f environment.yml
```

To activate the environment, use the following command:

```sh
conda activate game-of-life
```

Finally, to add kernel to Jupyter, you have to use `ipykernel` as follow:

```sh
python -m ipykernel install --user --name game-of-life --display-name "Python (game-of-life)"
```

## Pylint

Tu run `pylint`, please use the following command:

```sh
# pylint <path>
pylint src/
```
