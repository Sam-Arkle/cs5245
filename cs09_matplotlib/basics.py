import numpy as np
import matplotlib.pyplot as plt

# creating the dataset
data = {'C': 20, 'C++': 15, 'Java': 30,
        'Python': 35}
data2 = {'Haskell': 4, 'C#': 25, 'JavaScript': 50,
         'r': 32}
courses = list(data.keys())
values = list(data.values())
courses2 = list(data2.keys())
values2 = list(data2.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
# plt.bar(courses, values, color='maroon',
#         width=0.4)
# plt.bar(courses2, values2, color='pink',
#         width=0.4)

# plt.show()

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=False, gridspec_kw={'hspace': 0})
ax1.bar(courses, values)
ax2.bar(courses2, values2)
ax1.set_ylabel('Want this')

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
fig.set_tight_layout(True)
plt.show()


