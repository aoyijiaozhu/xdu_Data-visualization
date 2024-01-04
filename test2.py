#x=day,,y=year,z=t;
from pyecharts.charts import Bar3D
import pyecharts.options as opts
import csv
data=[] #日期，年，数据
with open('daily-minimum-temperatures-in-me.csv','r') as file:
    csv_reader=csv.reader(file)
    header=next(csv_reader) #标题
    for row in csv_reader:
        if not row:
            break
        new_row=[str(row[0].split('-')[1])+'-'+str(row[0].split('-')[2]),row[0].split('-')[0],row[1]]
        data.append(new_row)
#    data=[[int(row[0].split('-')[0])],str(row[0].split('-')[1])+str(row[0].split('-')[2]),row[1]] for row in data]
bar=Bar3D()
bar.add(
        '',
        data=data,
        xaxis3d_opts=opts.Axis3DOpts(type_='category'),
        yaxis3d_opts=opts.Axis3DOpts(type_='category'),
        zaxis3d_opts=opts.Axis3DOpts(type_='value')
        )
bar.set_global_opts(
    visualmap_opts=opts.VisualMapOpts(
        max_=30,
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
bar.render('test2_bar3D.html')