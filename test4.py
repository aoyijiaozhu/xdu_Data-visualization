
import pandas
import re
from pyecharts import options as opts
from pyecharts.charts import Map,Timeline


def SumSheet():     #生成各省统计表
    dataframe = pandas.read_excel('CityData.xlsx')
    dataframe.drop(columns=['city_suspectedCount','city_curedCount','city_deadCount'],inplace=True)
    result=dataframe.groupby(['countryName', 'provinceName','updateTime'],as_index=False)['city_confirmedCount'].sum()
    result['updateTime']=result['updateTime'].dt.strftime('%Y-%m-%d')
    result.to_excel('test4_new_data.xlsx', index=False)

def func1(dataframe):   #4月1日数据图
    new_dataframe = dataframe.loc[dataframe['updateTime'] == '2020-04-01']
#    max_cfm = new_dataframe['city_confirmedCount']   #最大确诊数
    new_datalst=new_dataframe.values.tolist()
    new_data=[[d[1],d[3]] for d in new_datalst]

    map = Map(init_opts=opts.InitOpts(width="1600px", height="900px"))
    map.add(
        '累计确诊',
        data_pair=new_data,
        maptype='china',
    )
    map.set_global_opts(
        title_opts=opts.TitleOpts(title="2020-04-01中国各省新冠确诊病例"),

        visualmap_opts=opts.VisualMapOpts(
            max_=500,
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
            pos_bottom="center",
            pos_right="10px"
        )
    )

    map.render('test4_1.html')

def func2(dataframe):   #时间线
    new_datalst=dataframe.values.tolist()
    new_data=[[d[1],d[2],d[3]] for d in new_datalst]
    tl=Timeline()
    tl.add_schema(play_interval=1000)
    tl = Timeline(init_opts=opts.InitOpts(width="1600px", height="900px"))
    data_dict={}
    for province, date, value in new_data:
        if date not in data_dict:
            data_dict[date] = [[province, value]]
        else:
            data_dict[date].append([province, value])
    for date in sorted(data_dict.keys()):
        map=Map()
        map.add(
            '累计确诊',
            data_pair=data_dict[date],
            maptype='china',
        )
        map.set_global_opts(
            title_opts=opts.TitleOpts(title=f"{date}中国各省新冠确诊病例"),

            visualmap_opts=opts.VisualMapOpts(
                max_=500,
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
                pos_bottom="center",
                pos_right="10px"
            ),
        )
        tl.add(map, date)
    tl.render('test4_2.html')

if __name__ == '__main__':
    SumSheet()
    dataframe=pandas.read_excel('test4_new_data.xlsx')
    func1(dataframe=dataframe)
    func2(dataframe=dataframe)








