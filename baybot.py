import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def search_name(name_in):
    ab_names = pd.read_csv('abbabynames2020.csv', encoding='latin1')

    result = ab_names[ab_names['name'] == name_in.strip()]

    result = result.sort_values(by=['sex', 'year'])
    result.reset_index(drop=True, inplace=True)

    result_boy = result[result['sex'] == 'Boy']
    result_girl = result[result['sex'] == 'Girl']

    total_boy = result_boy['frequency'].sum()
    total_girl = result_girl['frequency'].sum()

    plt.plot(result_boy['year'], result_boy['frequency'], color='blue', marker='.', label='Boys')
    plt.plot(result_girl['year'], result_girl['frequency'], color='red', marker='.', label='Girls')
    plt.title(f'{name_in}')
    plt.xlabel('Year')
    plt.ylabel('Babies with that name')
    plt.legend()
    plt.savefig('./static/images/result.png')
    plt.clf()

    return [total_boy, total_girl]
