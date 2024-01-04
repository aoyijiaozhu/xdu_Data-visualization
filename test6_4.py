import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Geo,Timeline
from pyecharts.globals import ChartType
import os

folder_path='new_data'
# 获取文件夹内所有的 CSV 文件
csv_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.csv')])
# 创建时间轴
timeline = Timeline(init_opts=opts.InitOpts(width="1600px", height="900px"))
for file in csv_files:

    df = pd.read_csv(os.path.join(folder_path, file), encoding="GBK")


    geo = Geo()

    # 添加数据
    geo.add_schema(maptype="china")
    geo.add("PM2.5(微克每立方米)", zip(df['城市'], df['PM2.5(微克每立方米)']), type_=ChartType.HEATMAP)
    geo.add("PM10(微克每立方米)", zip(df['城市'], df[' PM10(微克每立方米)']), type_=ChartType.HEATMAP)
    geo.add("SO2(微克每立方米)", zip(df['城市'], df[' SO2(微克每立方米)']), type_=ChartType.HEATMAP)
    geo.add("NO2(微克每立方米)", zip(df['城市'], df[' NO2(微克每立方米)']), type_=ChartType.HEATMAP)
    geo.add("CO(毫克每立方米)", zip(df['城市'], df[' CO(毫克每立方米)']), type_=ChartType.HEATMAP)
    geo.add("O3(微克每立方米", zip(df['城市'], df[' O3(微克每立方米)']), type_=ChartType.HEATMAP)
    geo.add("U(m/s)", zip(df['城市'], df[' U(m/s)']), type_=ChartType.HEATMAP)
    geo.add("V(m/s)", zip(df['城市'], df[' V(m/s)']), type_=ChartType.HEATMAP)
    geo.add("TEMP(K)", zip(df['城市'], df[' TEMP(K)']), type_=ChartType.HEATMAP)
    geo.add("RH(%)", zip(df['城市'], df[' RH(%)']), type_=ChartType.HEATMAP)
    geo.add("PSFC(Pa)", zip(df['城市'], df[' PSFC(Pa)']), type_=ChartType.HEATMAP)


    geo.set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=300,
                                          pos_bottom="center",
                                          pos_right="10px"
                                          ),

        title_opts=opts.TitleOpts(title="中国城市污染数据"+ file[:-4]),
    )
    timeline.add(geo, file[:-4])


timeline.render('中国城市污染数据3.html')
