import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType

# 读取 CSV 文件
df = pd.read_csv('城市文件.csv',encoding="GBK")

# 提取经纬度和 PM2.5 数据
data = [(row['城市'], row['PM2.5']) for _,row in df.iterrows()]

# 创建 Geo 图表
geo = Geo(init_opts=opts.InitOpts(width="1000px", height="600px"))

# 添加地理坐标系
geo.add_schema(maptype="china")

# 添加数据
geo.add("PM2.5", data, type_=ChartType.HEATMAP)

# 设置全局配置项
geo.set_global_opts(
    title_opts=opts.TitleOpts(title="PM2.5 污染地图"),
    visualmap_opts=opts.VisualMapOpts(max_=500)  # 根据你的数据调整最大值
)

# 渲染图表
geo.render('test6.html')
