# FastAPI experiments
Quick experiments with FastAPI to help with problem solving in a simple environment

## Installation

Make sure you have the [Poetry package manager](https://python-poetry.org/) installed on your computer.

In the project directory:

1. activate the project environment
    - `poetry shell`
2. install the project dependencies
    - `poetry install`

## Run

Once you have installed the project and activated the environment, run the following command to start the project server.

```sh
uvicorn main:app --reload
```

The above command will reload the server when local files change.
