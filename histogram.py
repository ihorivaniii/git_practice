
from matplotlib import pyplot as plt


past_years_averages = [82, 84, 83, 86, 74, 84, 90]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006]
error = [1.5, 2.1, 1.2, 3.2, 2.3, 1.7, 2.4]

# Make your chart here
plt.figure(figsize=(10,8))
plt.bar(range(len(past_years_averages)), past_years_averages, yerr=error, capsize=5)
plt.axis([-0.5, 6.5, 70, 95])
ax = plt.subplot()
ax.set_xticks(range(len(years)))
ax.set_xticklabels(years)
plt.title('Final Exam Averages')
plt.xlabel('Year')
plt.ylabel('Test average')
plt.savefig('my_bar_chart.png')
plt.show()

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
school_a_x = [0.8, 2.8, 4.8, 6.8, 8.8]
school_b_x = [1.6, 3.6, 5.6, 7.6, 9.6]
# Make your chart here
t=2
w=0.8
n=1
d=5
x_values = create_x(t, w, n, d)
x_values1 = create_x(t, w, n+1, d)
plt.bar(x_values, school_a_x)
plt.bar(x_values1, school_b_x)
plt.figure(figsize=(10, 8))
ax = plt.subplot()
plt.bar(x_values, middle_school_a, label = "Middle School A")
plt.bar(x_values1, middle_school_b, label = "Middle School B")
middle_x = [(a+b) / 2.0 for a, b in zip(school_a_x, school_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)
plt.legend()
plt.title("Test Averages on Different Units")
plt.xlabel("Unit")
plt.ylabel("Test Average")
plt.show()
plt.savefig("my_side_by_side.png")
from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs)
#create d_bottom and f_bottom here
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)
plt.figure(figsize=(10,8))
plt.bar(range(len(As)),As)
plt.bar(range(len(Bs)), Bs, bottom = As)
plt.bar(range(len(Cs)), Cs, bottom = c_bottom)
plt.bar(range(len(Ds)), Ds, bottom = d_bottom)
plt.bar(range(len(Fs)), Fs, bottom = f_bottom)
ax = plt.subplot()
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)
plt.title("Grade distribution")
plt.ylabel('Number of Students')
plt.xlabel('Unit')
#create your plot here
plt.savefig("my_stacked_bar.png")
plt.show()
