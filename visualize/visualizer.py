import matplotlib.pyplot as plt


def graph_scatter(result_analysis):
    fig, subplots = plt.subplots(1,len(result_analysis), sharey=True) # x , y를 공유하겠다

    index=0

    for index, result in enumerate(result_analysis):
        subplots[index].set_xlabel('{0}인 입국자수'.format(result['country_name']))
        index==0 and subplots[index].set_ylabel('관광지 입장객 수') # index가 0이면 and 뒤에 실행
        subplots[index].set_title('r={:.5f}'.format(result['r']))
        subplots[index].scatter(
            result['x'],
            result['y'],
            c='black',
            s=8
        )
    plt.subplots_adjust(wspace=0)
    plt.show()
