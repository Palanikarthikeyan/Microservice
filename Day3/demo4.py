import pstats

stats = pstats.Stats("profile_results.pdf")
stats.sort_stats("cumtime")
stats.print_stats()