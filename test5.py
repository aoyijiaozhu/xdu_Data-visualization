import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
import csv

# 读取 CSV 文件
df = pd.read_csv('CN-Reanalysis-daily-2018120100.csv')
data = [(row[' lon'], row[' lat'], row['PM2.5']) for _, row in df.iterrows()]
print(df.columns)

# 创建 Geo 图表
geo = Geo(init_opts=opts.InitOpts(width="1000px", height="600px"))

# 添加地理坐标系
geo.add_schema(maptype="china")

# 添加数据
geo.add('PM2.5', data, type_=ChartType.HEATMAP)

# 设置全局配置项
geo.set_global_opts(
    title_opts=opts.TitleOpts(title="污染地图"),
    visualmap_opts=opts.VisualMapOpts(max_=100)  # 根据你的数据调整最大值
)

# 渲染图表
geo.render('test5.html')

