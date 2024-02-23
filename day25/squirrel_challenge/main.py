import pandas

csv = pandas.read_csv("squirrel_data.csv")

# get all different values in the column
raw_values_fur = csv["Primary Fur Color"].unique()
# get rid of the nan values
values_fur = [x for x in raw_values_fur if x == x]
# list of counts for each value in values_fur
values_count = []

for value in values_fur:
    value_count = len(csv[csv["Primary Fur Color"] == value])
    values_count.append(value_count)

#converts the 2 list in 1 list of pairs
list_of_tuples = list(zip(values_fur, values_count))

df = pandas.DataFrame(list_of_tuples, columns=['Fur Color', 'Count'])

df.to_csv("squirrel_count.csv")