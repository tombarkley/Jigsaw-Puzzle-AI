# import functions from jigsaw-functions.py
from jigsaw_functions import showpic, showlist, load_from_processed, load_raw_file, thread_match
import time
import os
import numpy as np
run_matching = True

# prep files
# load_raw_file('d.png', 'd', 13, 'landscape')
# exit()



if __name__ == '__main__' and run_matching:
    abs_start_time = time.time()
    tiles, tile_centers, canvas_tiles, comp_results = load_from_processed()
    print('tiles: ' + str(len(tiles)))
    print('tile_centers: ' + str(len(tile_centers)))
    print('canvas_tiles: ' + str(len(canvas_tiles)))
    matches = []
    exp_comp = 0
    match_list = []
    all_match_list = []
    print('calculate all possible matches')
    # calculate number of expected comparisons
    exp_comp = 0
    for a in range(len(tiles)-1):
        for b in range(a+1,len(tiles)):
            exp_comp += 1
            match_list.append((a,b))
            # if str(a) + '-' + str(b) not in comp_results:
            #     match_list.append((a,b))
    print('expected comparisons: ' + str(exp_comp))
    print(comp_results)
    matches = thread_match(match_list[:10], tiles, canvas_tiles, comp_results)
    # print('flip and sort')
    # for n in range(len(matches)):
    #     pair, ij, pointa, pointb, angle, fmatch, cmatch, fit, lock = matches[n]
    #     matches.extend([[(pair[1],pair[0]), ij, pointb, pointa, -angle, fmatch, cmatch, fit, lock]])
    #     matches.sort(key=lambda m: (m[0], m[-2]))

    # print(len(matches))
    print('total time: ' + str(round(time.time()-abs_start_time,2)) + ' seconds')
    # print(matches)