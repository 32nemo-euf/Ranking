"""
Example to show the intended usage of the implemented GamesDataset and BlockRankingAlgorithm classes.
"""

from ranking_classes import GamesDataset, BlockRankingAlgorithm

# ------------------------------

division = 'Open'

# Prepare dataset
dataset_name = 'EUF_2019_{}'.format(division)
dataset_path = 'data/games_euf_2019_clean_{}.csv'.format(division.lower())

#
euf_dataset = GamesDataset(dataset_path, dataset_name)

# Apply Windmill Algo
windmill_algo = BlockRankingAlgorithm(algo_name='Windmill', rank_diff_func='score_diff',
                                      game_weight_func='uniform', rank_fit_func='regression',
                                      rank_fit_params={'n_round': 2})
euf_dataset.get_ratings(windmill_algo, block_algo=True)
euf_dataset.get_weekly_ratings(windmill_algo, verbose=True)

# Apply USAU Block Algo without date weights
usau_algo = BlockRankingAlgorithm(algo_name='USAU', rank_diff_func='usau', game_weight_func='usau_no_date',
                                  rank_fit_func='iteration', game_ignore_func='blowout',
                                  rank_fit_params={'rating_start': 1000, 'n_round': 2, 'n_iter': 1000})
euf_dataset.get_ratings(usau_algo, block_algo=True)
euf_dataset.get_weekly_ratings(usau_algo, verbose=True)  # this takes some time

# Export Results
euf_dataset.export_to_excel()
euf_dataset.export_to_excel(include_weekly=True)
#
c_plot_list = ['Rating_USAU', 'Rating_Windmill', 'Games',
               'W_Ratio', 'Opponent_W_Ratio', 'Avg_Point_Diff']
euf_dataset.plot_bar_race_fig(c_plot_list)
euf_dataset.plot_bar_race_fig(c_plot_list, include_weekly=True)
