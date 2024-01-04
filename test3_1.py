import math
import pyecharts.options as opts
from pyecharts.charts import Line3D
data=[]
for I in range(0, 200):
    i = I/(2*math.pi)
    x = 5*math.cos(i)
    y = 5*math.sin(i)
    z = i
    data.append([x, y, z])
bar=Line3D()
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
        max_=35,
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
bar.render('test3_1_Line3D.html')