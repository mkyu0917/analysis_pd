import collect
import collect
import analyze
from config import CONFIG


if __name__ == '__main__':

    resultfiles=dict() #딕션만들고


    #collect
    resultfiles['tourspot_visitor']=collect.crawling_tourspot_visitor( #딕션에저장
        district=CONFIG['district'], #config에 있는 지역
        **CONFIG['common']) #커먼에 이쓴 속성을 불러옴,common= 공통적인 속성을 커먼이라는 딕셔너리로 묶음
        #start_year= CONFIG ['common']['start_year'],
        #end_year= CONFIG['common']['end_year'])

    resultfiles['foreign_visitor']=[]
    for country in CONFIG['conutries']:
            rf=collect.crawling_foreign_visitor(country, **CONFIG['common'] )#rf로 받음
            resultfiles['foreign_visitor'].append(rf)#rf를 resultfile에 추가
    #analysis
    analyze.analysis_correlation(resultfiles) #


    #visualize