import json
import pandas as pd #판다스 임포트
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import math

def analysis_correlation(resultfiles):
    with open(resultfiles['tourspot_visitor'],'r',encoding='utf-8') as initfile: #데이터열어서 확인
        json_data =json.loads(initfile.read())
        print(json_data)

    tourspotvisitor_table  = pd.DataFrame(json_data, columns=['count_foreigner','date','tourist_spot']) # DataFrame=table 을 생성하고 컬럼을 설정하고 값을 도출
    temp_tourspotvisitor_table= pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum()) #날짜에 대한 외국인들 합산값 데이트별로 도출

    results=[]
    results = []
    for filename in resultfiles['foreign_visitor']:
        with open(filename, 'r', encoding='utf-8') as infile:
            json_data = json.loads(infile.read())
            print(json_data)
        foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
        print(foreignvisitor_table)
        foreignvisitor_table = foreignvisitor_table.set_index('date')
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
        print(json_data)

        tourspot_table = pd.DataFrame(json_data, columns=['tourist_spot', 'count_foreigner','date'])  # DataFrame=table 을 생성하고 컬럼을 설정하고 값을 도출
        temp_table = tourspot_table[tourspot_table['tourist_spot'] == '경복궁']  # 경복궁 값만 빼오기
        tourist_spot = tourspot_table['tourist_spot'].unique() #모든 놀러가는 스팟
        print(tourist_spot)

        results = []
        for filename in resultfiles['foreign_visitor']:
            with open(filename, 'r', encoding='utf-8') as infile:
                json_data = json.loads(infile.read())
                print(json_data)
            foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
            print(foreignvisitor_table)



   #경복궁빼내기
#----------------


         #중복되는 리스트 제거
        tourist_spot = tourspot_table['tourist_spot'].unique()
        print(tourist_spot)

        temp_table = tourspot_table[tourspot_table['tourist_spot'] == '경복궁']  # 경복궁 값만 빼오기
        print(temp_table)

        for spot in len(tourist_spot):
           spot['tourist_spot']
           print(tourist_spot)

#-----------------



        merge_table = pd.merge(
             temp_table,
             foreignvisitor_table,
             )
        print(merge_table)
        merge_table=pd.DataFrame(merge_table,columns=['date','count_foreigner','visit_count'])
        print(merge_table)
