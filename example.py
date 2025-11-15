import marimo

__generated_with = "0.17.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    return (np,)


@app.cell
def _(np):
    array = np.random.rand(3, 3)
    return (array,)


@app.cell
def _(array):
    print(array)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
