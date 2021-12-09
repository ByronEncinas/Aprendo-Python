import matplotlib.pyplot as plt

x = [1,2,3]
y = [1,2,1]
yerrormin = [0.1,0.5,0.9]
yerrormax = [0.2,0.4,0.6]
xerror = 0.5

yerror = [yerrormin, yerrormax]

plt.plot(x,y,'o')
plt.errorbar(x,y,yerr=yerror, xerr=xerror, fmt='o', ecolor='black',elinewidth=2, capsize=5,capthick=2, barsabove=False, errorevery=1, lolims=False, uplims=False, xlolims=False,          xuplims=False, alpha=1, ms=10)

plt.show()

