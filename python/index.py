#!/usr/bin/env python3
import pandas as pd
import json
import os

print("This is the example of pandas library")
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)