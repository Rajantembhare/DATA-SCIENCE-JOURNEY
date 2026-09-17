import pandas as pd
score = pd.Series([210,326,548,999],index=["shruti","rajan","divya","rohan"])
print(score["shruti"])
print(score["rajan"])
print(score["divya"])
print(score["rohan"])
print(score)
