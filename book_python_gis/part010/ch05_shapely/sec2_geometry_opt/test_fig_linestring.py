'''
From shapely respo.
'''

from matplotlib import pyplot
from shapely.geometry import LineString

from matplotlib.font_manager import FontProperties

font_song = FontProperties(fname="/usr/share/fonts/xpfonts/simfang.ttf")

from figures import SIZE, set_limits, plot_coords, plot_bounds, plot_line_issimple

COLOR = {
    True: '#6699cc',
    False: '#ffcc33'
}


def v_color(ob):
    return COLOR[ob.is_simple]


def plot_coords(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, 'o', color='#999999', zorder=1)


def plot_bounds(ax, ob):
    x, y = zip(*list((p.x, p.y) for p in ob.boundary))
    ax.plot(x, y, 'o', color='#000000', zorder=1)


def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color=v_color(ob), alpha=0.7, linewidth=3, solid_capstyle='round', zorder=2)


fig = pyplot.figure(1, figsize=SIZE, dpi=90)

# 1: simple line
ax = fig.add_subplot(121)
line = LineString([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])

plot_coords(ax, line)
plot_bounds(ax, line)
plot_line_issimple(ax, line, alpha=0.7)

ax.set_title('a) 简单线', fontproperties=font_song)

set_limits(ax, -1, 4, -1, 3)

# 2: complex line
ax = fig.add_subplot(122)
line2 = LineString([(0, 0), (1, 1), (0, 2), (2, 2), (-1, 1), (1, 0)])

plot_coords(ax, line2)
plot_bounds(ax, line2)
plot_line_issimple(ax, line2, alpha=0.7)

ax.set_title('b) 复杂线', fontproperties=font_song)

set_limits(ax, -2, 3, -1, 3)

# pyplot.show()

import os

plt = pyplot
plt.savefig(os.path.join(
    os.path.split(os.path.realpath(__file__))[0],
    'xx{bname}.pdf'.format(
        bname=os.path.splitext(os.path.basename(__file__))[0][4:]
    )), bbox_inches='tight')

plt.savefig(os.path.join(
    os.path.split(os.path.realpath(__file__))[0],
    'xx{bname}.png'.format(
        bname=os.path.splitext(os.path.basename(__file__))[0][4:]
    )), bbox_inches='tight')
pyplot.clf()
