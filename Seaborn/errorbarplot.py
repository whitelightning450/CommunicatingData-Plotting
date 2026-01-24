import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import io
from IPython.display import SVG
from IPython.display import display

sns.set_theme(style="darkgrid")


f = mpl.figure.Figure(figsize=(8, 5))
axs = f.subplots(2, 2, sharex=True, sharey=True,)

plt.setp(axs, xlim=(-1, 1), ylim=(-1, 1), xticks=[], yticks=[])
for ax, color in zip(axs.flat, ["C0", "C2", "C3", "C1"]):
    ax.set_facecolor(mpl.colors.to_rgba(color, .25))

kws = dict(x=0, y=.2, ha="center", va="center", size=18)
axs[0, 0].text(s="Standard deviation", **kws)
axs[0, 1].text(s="Standard error", **kws)
axs[1, 0].text(s="Percentile interval", **kws)
axs[1, 1].text(s="Confidence interval", **kws)

kws = dict(x=0, y=-.2, ha="center", va="center", size=18)
axs[0, 0].text(s='errorbar=("sd", scale)', **kws)
axs[0, 1].text(s='errorbar=("se", scale)', **kws)
axs[1, 0].text(s='errorbar=("pi", width)', **kws)
axs[1, 1].text(s='errorbar=("ci", width)', **kws)

kws = dict(size=18)
axs[0, 0].set_title("Spread", **kws)
axs[0, 1].set_title("Uncertainty", **kws)
axs[0, 0].set_ylabel("Parametric", **kws)
axs[1, 0].set_ylabel("Nonparametric", **kws)

f.tight_layout()
f.subplots_adjust(hspace=.05, wspace=.05 * (4 / 6))
f.savefig(svg:=io.StringIO(), format="svg")
SVG(svg.getvalue())
display(f)