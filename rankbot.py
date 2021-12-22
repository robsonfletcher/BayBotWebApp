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

    ranks_boy = result_boy[['year', 'year_rank']].copy()
    ranks_girl = result_girl[['year', 'year_rank']].copy()
    ranks_girl.reset_index(inplace=True)

    if not ranks_boy.empty:
        leastpop_boy_rank = ranks_boy['year_rank'].max()
        mostpop_boy_rank = ranks_boy['year_rank'].min()

        leastpop_boy_index = ranks_boy['year_rank'].idxmax()
        mostpop_boy_index = ranks_boy['year_rank'].idxmin()

        leastpop_boy_year = ranks_boy['year'].iloc[leastpop_boy_index]
        mostpop_boy_year = ranks_boy['year'].iloc[mostpop_boy_index]

    else:
        mostpop_boy_year = "N/A"
        mostpop_boy_rank = "N/A"
        leastpop_boy_year = "N/A"
        leastpop_boy_rank = "N/A"

    if not ranks_girl.empty:

        leastpop_girl_rank = ranks_girl['year_rank'].max()
        mostpop_girl_rank = ranks_girl['year_rank'].min()

        leastpop_girl_index = ranks_girl['year_rank'].idxmax()
        mostpop_girl_index = ranks_girl['year_rank'].idxmin()

        leastpop_girl_year = ranks_girl['year'].iloc[leastpop_girl_index]
        mostpop_girl_year = ranks_girl['year'].iloc[mostpop_girl_index]

    else:
        mostpop_girl_year = "N/A"
        mostpop_girl_rank = "N/A"
        leastpop_girl_year = "N/A"
        leastpop_girl_rank = "N/A"

    plt.gca().invert_yaxis()
    plt.plot(ranks_boy['year'], ranks_boy['year_rank'], color='blue', marker='.', label='Boys')
    plt.plot(ranks_girl['year'], result_girl['year_rank'], color='red', marker='.', label='Girls')
    plt.title(f'{name_in}')
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.legend()
    plt.savefig('./static/images/ranks.png')
    plt.clf()

    return[mostpop_boy_year, mostpop_boy_rank, leastpop_boy_year, leastpop_boy_rank,
           mostpop_girl_year, mostpop_girl_rank, leastpop_girl_year, leastpop_girl_rank]
