# import functions from jigsaw-functions.py
from jigsaw_functions import showpic, showlist, load_from_processed, load_raw_file, thread_match
import time
run_matching = False

# prep files
# load_raw_file('j1a.png', 'j', 36)

tiles, tile_centers, canvas_tiles = load_from_processed()
print('tiles: ' + str(len(tiles)))
print('tile_centers: ' + str(len(tile_centers)))
print('canvas_tiles: ' + str(len(canvas_tiles)))

if __name__ == '__main__' and run_matching:
  abs_start_time = time.time()
  tiles, tile_centers, canvas_tiles = load_from_processed()
  matches = []
  exp_comp = 0
  match_list = []
  print('calculate all possible matches')
  # calculate number of expected comparisons
  exp_comp = 0
  for a in range(len(tiles)-1):
    for b in range(a+1,len(tiles)):
      exp_comp += 1
      match_list.append((a,b))
  print('expected comparisons: ' + str(exp_comp))
  matches = thread_match(match_list, tiles, tile_centers, canvas_tiles)
  print('flip and sort')
  for n in range(len(matches)):
    pair, ij, pointa, pointb, angle, fmatch, cmatch, fit, lock = matches[n]
    matches.extend([[(pair[1],pair[0]), ij, pointb, pointa, -angle, fmatch, cmatch, fit, lock]])
  matches.sort(key=lambda m: (m[0], m[-2]))

  print(len(matches))
  print('total time: ' + str(round(time.time()-abs_start_time,2)) + ' seconds')
  # print(matches)