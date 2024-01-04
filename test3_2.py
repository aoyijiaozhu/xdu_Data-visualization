import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Surface3D
data=[]

x_lst = np.linspace(-3, 3, 100)
y_lst= np.linspace(-3, 3, 100)

x, y = np.meshgrid(x_lst, y_lst)

z = np.exp(-(x ** 2 + y ** 2))


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
        max_=1,
        min_=0,
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
bar.render('test3_2_Surface3D.html')