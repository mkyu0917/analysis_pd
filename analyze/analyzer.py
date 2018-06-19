import json
import pandas as pd #판다스 임포트

def analysis_correlation(resultfiles):
    with open(resultfiles['tourspot_visitor'],'r',encoding='utf-8') as initfile: #데이터열어서 확인
        json_data =json.loads(initfile.read())
        #print(json_data)

    tourspotvisitor_table  = pd.DataFrame(json_data, columns=['count_foreigner','date','tourist_spot']) # DataFrame=table 을 생성하고 컬럼을 설정하고 값을 도출
    temp_tourspotvisitor_table= pd.DataFrame(tourspotvisitor_table.groupby('date')['count_foreigner'].sum()) #날짜에 대한 외국인들 합산값 데이트별로 도출


    for filename in resultfiles['foreign_visitor']:
       with open(filename,'r',encoding='utf-8') as infile:
           json_data=json.loads(infile.read())

       foreignvisitor_table = pd.DataFrame(json_data, columns=['country_foreigner'])