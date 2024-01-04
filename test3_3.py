import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Surface3D

data=[]
def ball(u, v):
    x = 5*np.sin(v) * np.cos(u)
    y = 5*np.sin(v) * np.sin(u)
    z = 5*np.cos(v)
    return [x, y, z]


u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
u, v = np.meshgrid(u, v)
x, y, z = ball(u, v)

for i in zip(x.flatten(), y.flatten(), z.flatten()):
    data.append(list(i))

bar=Surface3D()
bar.add(
    '',
    data=data,
    xaxis3d_opts=opts.Axis3DOpts(type_="value"),
    yaxis3d_opts=opts.Axis3DOpts(type_="value"),
    zaxis3d_opts=opts.Axis3DOpts(type_="value"),
    grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100)
)
bar.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(
        max_=5,
        min_=-5,
        range_color=[
                "#313695",
                "#4575b4",
                "#74add1",
                "#abd9e9",
                "#e0f3f8",
                "#ffffbf",
                "#fee090",
                "#fdae61",
                "#f46d43",
                "#d73027",
                "#a50026",
            ],
    )
)
bar.render('test3_3_Surface3D.html')