import json
import pandas as pd #판다스 임포트
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import math

def analysis_correlation(resultfiles):
    with open(resultfiles['tourspot_visitor'],'r',encoding='utf-8') as initfile: #데이터열어서 확인
        json_data =json.loads(initfile.read())
        #print(json_data)

    tourspotvisitor_table  = pd.DataFrame(json_data, columns=['count_foreigner','date','tourist_spot']) # DataFrame=table 을 생성하고 컬럼을 설정하고 값을 도출
    temp_tourspotvisitor_table= pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum()) #날짜에 대한 외국인들 합산값 데이트별로 도출

    results=[]
    # results = []
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())
            #print(json_data)
        foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])

        #print(foreignvisitor_table)
        foreignvisitor_table = foreignvisitor_table.set_index('date')
        print(foreignvisitor_table)
        # merge_table = pd.merge(
        #     temp_tourspotvisitor_table,
        #     foreignvisitor_table,
        #     left_index=True, right_index=True)

        # x = list(merge_table['visit_count'])
        # y = list(merge_table['count_foreigner'])
        # country_name = foreignvisitor_table['country_name'].unique().item(0)
        # r = ss.pearsonr(x, y)[0]
        # # r = np.corrcoef(x, y)[0]
        # results.append({'x': x, 'y': y, 'country_name': country_name, 'r': r})
        #
        # merge_table['visit_count'].plot(kind='bar')
        # plt.show()

    return results


def analysis_correlation_by_tourspot(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as initfile:  # 데이터열어서 확인
        json_data = json.loads(initfile.read())

        tourspot_table = pd.DataFrame(json_data, columns=['tourist_spot', 'count_foreigner','date'])  # DataFrame=table 을 생성하고 컬럼을 설정하고 값을 도출
        #print(tourist_spot)
        tourist_spot = tourspot_table['tourist_spot'].unique()

        result_analysis=[]
        for spot in tourist_spot:
            tourist_spot = tourspot_table[tourspot_table['tourist_spot'] == spot]  # 경복궁 값만 빼오기
            tourist_spot = pd.DataFrame(tourist_spot.set_index('date'))

            z = []
            for filename in resultfiles['foreign_visitor']:
                with open(filename, 'r', encoding='utf-8') as infile:
                    json_data = json.loads(infile.read())
                    #print(json_data)
                foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
                foreignvisitor_table = pd.DataFrame(foreignvisitor_table.set_index('date'))
                temp_table = tourspot_table[tourspot_table['tourist_spot'] == '경복궁']  # 경복궁 값만 빼오기

                merge_table=pd.merge(
                        tourist_spot,foreignvisitor_table,right_index=True,left_index=True
                    )


                x = list(merge_table['visit_count'])
                y = list(merge_table['count_foreigner'])

                a = tourist_spot['tourist_spot'].unique().item(0)
                r = correlation_coefficient(x, y)
                z.append(r)
            result_analysis.append({'tourspot': a, 'r_중국':z[0], 'r_일본':z[1], 'r_미국':z[2]})
    graph_table = pd.DataFrame(result_analysis, columns=['tourspot', 'r_중국', 'r_일본', 'r_미국'])
    graph_table = graph_table.set_index('tourspot')
    graph_table.plot(kind='bar')


    plt.show()

def correlation_coefficient(x, y):
    n = len(x)
    vals = range(n)

    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0

    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]), 2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)

    try:
        r = ((n * mul_xy_sum) - (x_sum * y_sum)) / \
            math.sqrt(((n * x_sum_pow) - pow(x_sum, 2)) * ((n * y_sum_pow) - pow(y_sum, 2)))
    except Exception as e:
        r = 0.0

    return r

        # merge_table = pd.merge(
        #      temp_table,
        #      foreignvisitor_table,
        #      )
        # print(merge_table)
        # merge_table=pd.DataFrame(merge_table,columns=['date','count_foreigner','visit_count'])
        # print(merge_table)
