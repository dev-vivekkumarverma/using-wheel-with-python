import pandas as pd

import numpy as np

import matplotlib.pyplot as plt


def main():

    # Example: Fetch data and analyze

    data={"timestamp":[1,2,3,4,5]}
    

    df = pd.DataFrame(data)

    df["values"] = np.random.rand(len(df))

    

    df.plot(x="timestamp", y="values")

    plt.savefig("output.png")

    print("Analysis complete! Saved to output.png.")

if __name__ == "__main__":

    main()