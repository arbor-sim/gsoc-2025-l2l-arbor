# begin by importing Arbor and Units
import arbor as A
# we will also get support to plot things
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# do a quick 3d visualisaton
def plot_morphology(mrf, *, fg=None):
    tree = mrf.segment_tree
    colors = sns.color_palette('Set1')
    if not fg:
        fg = plt.figure(figsize=(10, 10))
    ax = fg.add_subplot(projection='3d')
    for seg in tree.segments:
        x0 = seg.prox.x
        x1 = seg.dist.x
        y0 = seg.prox.y
        y1 = seg.dist.y
        z0 = seg.prox.z
        z1 = seg.dist.z
        r0 = seg.prox.radius
        r1 = seg.dist.radius
        tag = seg.tag
        ax.plot(xs=[x0, x1], 
                ys=[y0, y1], 
                zs=[z0, z1], 
                color=colors[tag], 
                lw=(r0 + r1)) # average diameter from radius
    ax.set_xlabel(r'x $(\mu m)$')
    ax.set_ylabel(r'y $(\mu m)$')
    ax.set_zlabel(r'z $(\mu m)$')
    fg.tight_layout()
    return fg, ax