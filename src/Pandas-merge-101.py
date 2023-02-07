# from the series https://stackoverflow.com/questions/53645882/pandas-merging-101
# Merging basics - basic types of joins (https://stackoverflow.com/questions/53645882/pandas-merging-101/53645883#53645883)

# 1. Initiate dataframes with a key and a value
# 
# %%
import pandas as pd
import numpy as np

np.random.seed(0)
left = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value': np.random.randn(4)})
right = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'value': np.random.randn(4)})
print('Left:')
print(left)
print('Right:')
print(right)

# %%
# 2. Inner join
#
# The inner join is the default join type in pandas. It returns only the rows that have matching keys in both dataframes.
#
print('Inner join:')
print(              left.merge(right, on='key', how='inner')  ) # or equivalently left.merge(right, on='key')

# %%
# 3. Left Outer join or Left Join
#
# The left outer join returns all rows from the left dataframe, and any matching rows from the right dataframe. If there is no match, the right dataframe will contain NaN values.
print('Left outer join:')
print(              left.merge(right, on='key', how='left')  ) # or equivalently left.merge(right, on='key', how='outer', indicator=True)
# %%
# 4. Right Outer join or Right Join
print('Right outer join:')
print(              left.merge(right, on='key', how='right')  ) # or equivalently right.merge(left, on='key', how='outer', indicator=True)
# %%
# 5. Full Outer join or Full Join
print('Full outer join:')
print(              left.merge(right, on='key', how='outer')  ) # or equivalently pd.merge(left, right, on='key', how='outer', indicator=True)

# %%
# 6. Left/Right Anti join or Left/Right Exclude join
#
# The left anti join returns only the rows from the left dataframe that do not have a match in the right dataframe.
print('Left anti join:')
print(              left.merge(right, on='key', how='left', indicator=True) .query('_merge == "left_only"') .drop('_merge', axis=1)  ) # or equivalently left.merge(right, on='key', how='outer', indicator=True).query('_merge == "left_only"').drop('_merge', axis=1)

# The right anti join returns only the rows from the right dataframe that do not have a match in the left dataframe.
print('Right anti join:')
print(              left.merge(right, on='key', how='right', indicator=True) .query('_merge == "right_only"') .drop('_merge', axis=1)  ) # or equivalently right.merge(left, on='key', how='outer', indicator=True).query('_merge == "right_only"').drop('_merge', axis=1)

# %%
# 7. Full Anti join or Full Exclude join
#
# The full anti join returns only the rows from both dataframes that do not have a match in the other dataframe.
print('Full anti join:')
print(              left.merge(right, on='key', how='outer', indicator=True) .query('_merge == "left_only" or _merge == "right_only"') .drop('_merge', axis=1)  ) # or equivalently pd.merge(left, right, on='key', how='outer', indicator=True).query('_merge == "left_only" or _merge == "right_only"').drop('_merge', axis=1)

# %%
# I. Semi joins (not in the original post)
#
#   Left semi join
#   The left semi join returns only the rows from the left dataframe that have a match in the right dataframe.
print('Left semi join:')
print(              left.merge(right, on='key', how='left', indicator=True) .query('_merge == "both"') .drop('_merge', axis=1)  ) # or equivalently left.merge(right, on='key', how='outer', indicator=True).query('_merge == "both"').drop('_merge', axis=1)

#   Cross Join
#   The cross join returns the cartesian product of the rows from the left and right dataframes. This is the same as an inner join, but without the matching condition.
print('Cross join:')
print(              left.merge(right, how='cross')  ) # or equivalently pd.merge(left, right, how='cross')
# %%
#   Self Join
#   A self join is a join between two copies of the same dataframe. This is useful for comparing values between rows.
print('Self join:')
print(              left.merge(left, on='key', suffixes=('_left', '_right'))  ) # or equivalently pd.merge(left, left, on='key', suffixes=('_left', '_right'))

# %%
# 8. Different names for key columns or Join on Index
#
# If the key columns have different names in the two dataframes, you can specify them separately.
left2 = left.rename({'key':'keyLeft'}, axis=1)
right2 = right.rename({'key':'keyRight'}, axis=1)
print('Different names for key columns:')
print(              left2.merge(right2, left_on='keyLeft', right_on='keyRight')  ) # or equivalently pd.merge(left2, right2, left_on='keyLeft', right_on='keyRight')
# %%
left3 = left2.concat('keyLeft', 'keyRight')