import matplotlib.pyplot as plt
import seaborn as sb
from pydataset import data

df = data('iris')

f1 = df['Species'] == 'setosa'
f2 = df['Species'] == 'versicolor'
f3 = df['Species'] == 'virginica'

s = df[f1]
vc = df[f2]
vg = df[f3]

fig, (ax1, ax2) = plt.subplots(2)
fig.tight_layout()

petal_line = sb.regplot(x=df['Petal.Length'], y=df['Petal.Width'],
                        fit_reg=True, ax=ax1, scatter=False,
                        line_kws={'color': '#444444'})

s_scatter = sb.regplot(x=s['Petal.Length'], y=s['Petal.Width'],
                       fit_reg=False, ax=ax1,
                       scatter_kws={'color': 'r', 's': 10}, label='Setosa')

vc_scatter = sb.regplot(x=vc['Petal.Length'], y=vc['Petal.Width'],
                        fit_reg=False, ax=ax1,
                        scatter_kws={'color': 'b', 's': 10}, label='Versicolor')

vg_scatter = sb.regplot(x=vg['Petal.Length'], y=vg['Petal.Width'],
                        fit_reg=False, ax=ax1,
                        scatter_kws={'color': 'g', 's': 10}, label='Virginica')

sepal_line = sb.regplot(x=df['Sepal.Length'], y=df['Sepal.Width'],
                        fit_reg=True, ax=ax2, scatter=False,
                        line_kws={'color': '#444444'})

s_scatter2 = sb.regplot(x=s['Sepal.Length'], y=s['Sepal.Width'],
                        fit_reg=False, ax=ax2,
                        scatter_kws={'color': 'r', 's': 10})

vc_scatter2 = sb.regplot(x=vc['Sepal.Length'], y=vc['Sepal.Width'],
                         fit_reg=False, ax=ax2,
                         scatter_kws={'color': 'b', 's': 10})

vg_scatter2 = sb.regplot(x=vg['Sepal.Length'], y=vg['Sepal.Width'],
                         fit_reg=False, ax=ax2,
                         scatter_kws={'color': 'g', 's': 10})

fig.suptitle('Flower Sizes')
ax1.set(xlabel='Petal Length', ylabel='Petal Width', ylim=(0, 3))
ax2.set(xlabel='Sepal Length', ylabel='Sepal Width', ylim=(0, 5))

fig.subplots_adjust(left=0.11, top=0.933, hspace=0.27, bottom=0.114)
legend = ax1.legend(shadow=True, title="Species", fancybox=True)
legend.get_title().set_color('#444444')
plt.show()
