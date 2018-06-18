import collect
import collect
from config import CONFIG


if __name__ == '__main__':
    #collect
    collect.crawling_tourspot_visitor(
        district=CONFIG['district'], #config에 있는 지역
        **CONFIG['common']) #커먼에 이쓴 속성을 불러옴,common= 공통적인 속성을 커먼이라는 딕셔너리로 묶음
        #start_year= CONFIG ['common']['start_year'],
        #end_year= CONFIG['common']['end_year'])

    for country in ['conutries']:
            collect.crawling_foreign_visitor(
                country,
                **CONFIG['common'] )

    #analysis

    #visualize