import collect
import collect
import analyze
import visualize
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
    for country in CONFIG['countries']:
            rf=collect.crawling_foreign_visitor(country, **CONFIG['common'] )#rf로 받음
            resultfiles['foreign_visitor'].append(rf)#rf를 resultfile에 추가

    # 1.analysis and visulize
    #result_analysis=analyze.analysis_correlation(resultfiles)
   # print(result_analysis)
    #print(result_analysis)

    #visualize
    #visualize.graph_scatter(result_analysis)

    #2.analysis and visualize, 장소별로 상관계수 구하끠
    result_analysis = analyze.analysis_correlation_by_tourspot(resultfiles)
    #graph_table = pd.DataFrame(result_analysis, columns=['tourspot','r_중국','r_일본','r_미국'])
    #graph_table = graph_table.set_index('tourspot')

    #graph_table.plot(kind='bar')
    #plt.show()
    #tourspot r_중국 r_일본 r_미국 중국_입국자수
    #경복궁     0.2    0.3    0.5
    #이런 값들을 넘겨줌니다.