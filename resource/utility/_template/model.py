if __name__ == "__main__":
    import os

    if not hasattr(os, "_chdir"):
        os.chdir("..")
        os.chdir("..")
        os._chdir = True

    print(os.getcwd())

import numpy as np

print("Converted model.ipynb to model.py")



