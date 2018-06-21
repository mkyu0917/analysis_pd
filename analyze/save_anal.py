def analysis_correlation_by_tourspot(resultfiles):
    with open(resultfiles['tourspot_visitor'], 'r', encoding='utf-8') as initfile:  # 데이터열어서 확인
        json_data = json.loads(initfile.read())
        print(json_data)

        tourspot_table = pd.DataFrame(json_data, columns=['tourist_spot', 'count_foreigner','date'])  # DataFrame=table 을 생성하고 컬럼을 설정하고 값을 도출
        #print(tourist_spot)

        foreignvisitors = []
        for filename in resultfiles['foreign_visitor']:
            with open(filename, 'r', encoding='utf-8') as infile:
                json_data = json.loads(infile.read())
                #print(json_data)
            foreignvisitor_table = pd.DataFrame(json_data, columns=['country_name', 'date', 'visit_count'])
            foreignvisitor_table = pd.DataFrame(foreignvisitor_table.set_index('date'))
            tourist_spot = tourspot_table['tourist_spot'].unique()  # 모든 놀러가는 스팟
            temp_table = tourspot_table[tourspot_table['tourist_spot'] == '경복궁']  # 경복궁 값만 빼오기

            for spot in tourist_spot:
                tourist_spot = tourspot_table[tourspot_table['tourist_spot'] == spot]  # 경복궁 값만 빼오기
                tourist_spot = pd.DataFrame(tourist_spot.set_index('date'))


                for merge in foreignvisitor_table: #merge foreigner and spot
                    merge_table=pd.merge(
                        tourist_spot,foreignvisitor_table,right_index=True,left_index=True
                    )

                for data in merge_table:  # 데이터뽑아서 상관계수 함수에 전달

                    x = list(merge_table['visit_count'])
                    y = list(merge_table['count_foreigner'])
                    r = correlation_coefficient(x, y)
                print(r)