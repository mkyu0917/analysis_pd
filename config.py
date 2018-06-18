import os
#configuration
CONFIG={
    'district':'서울특별시',
    'countries':[('중국', 112), ('일본', 130), ('미국', 275)],
    'common': {
        'start_year':2017,
        'end_year':2017,
        'fetch':True,
        'result_directory': '__results__/crawling',
        'service_key': 'CltvcqjQZrEAZ%2BALT9RK1rIrikygd%2BKeHKuFqjc0N7Nf9EPcCxm3JvkMrD8AepS5BdKB6wc6prRZVSvU9DGmTg%3D%3D'
    }
}

if not os.path.exists(CONFIG['common']['result_directory']):
    os.makedirs(CONFIG['common']['result_directory'])



