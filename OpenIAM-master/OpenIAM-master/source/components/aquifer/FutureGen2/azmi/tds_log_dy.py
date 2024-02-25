'''
output: tds_log_dy
prediction score: 0.8612169151644194
Forward Pass
---------------------------------------------------------------
iter  parent  var  knot  mse       terms  gcv    rsq    grsq
---------------------------------------------------------------
0     -       -    -     7.152737  1      7.155  0.000  0.000
1     0       10   1081  3.966688  3      3.975  0.445  0.444
2     1       1    -1    1.770493  4      1.776  0.752  0.752
3     0       9    905   1.519941  6      1.528  0.788  0.787
4     1       9    696   1.264986  8      1.274  0.823  0.822
5     4       2    240   1.227035  10     1.238  0.828  0.827
6     1       3    -1    1.214973  11     1.227  0.830  0.829
7     4       9    4748  1.203788  13     1.218  0.832  0.830
8     1       4    -1    1.193852  14     1.209  0.833  0.831
9     0       1    404   1.186555  16     1.204  0.834  0.832
10    15      1    -1    1.022972  17     1.039  0.857  0.855
11    15      10   830   1.015302  19     1.033  0.858  0.856
12    1       10   2991  1.006289  21     1.026  0.859  0.857
13    1       2    -1    0.999216  22     1.019  0.860  0.858
---------------------------------------------------------------
Stopping Condition 2: Improvement below threshold

Pruning Pass
--------------------------------------------
iter  bf  terms  mse   gcv    rsq    grsq
--------------------------------------------
0     -   22     1.00  1.019  0.860  0.858
1     18  21     1.00  1.018  0.860  0.858
2     8   20     1.00  1.017  0.860  0.858
3     14  19     1.00  1.017  0.860  0.858
4     5   18     1.00  1.016  0.860  0.858
5     7   17     1.00  1.016  0.860  0.858
6     2   16     1.00  1.016  0.860  0.858
7     13  15     1.01  1.021  0.859  0.857
8     21  14     1.01  1.026  0.858  0.857
9     12  13     1.02  1.033  0.857  0.856
10    19  12     1.03  1.041  0.856  0.855
11    20  11     1.04  1.047  0.855  0.854
12    17  10     1.04  1.048  0.855  0.854
13    11  9      1.05  1.057  0.853  0.852
14    10  8      1.06  1.069  0.852  0.851
15    9   7      1.10  1.103  0.847  0.846
16    15  6      1.25  1.256  0.825  0.824
17    16  5      1.27  1.274  0.823  0.822
18    6   4      1.53  1.536  0.786  0.785
19    4   3      1.79  1.793  0.750  0.749
20    3   2      3.98  3.985  0.444  0.443
21    1   1      7.15  7.155  0.000  0.000
--------------------------------------------
Selected iteration: 5

Earth Model
--------------------------------------------------------------------------
Basis Function                                       Pruned  Coefficient
--------------------------------------------------------------------------
(Intercept)                                          No      -0.778677
h(log_brine_mass-7.74307)                            No      1.92418
h(7.74307-log_brine_mass)                            No      -0.0201219
depth*h(log_brine_mass-7.74307)                      No      0.00126686
h(log_co2_mass-14.6976)                              No      0.291631
h(14.6976-log_co2_mass)                              Yes     None
h(log_co2_mass-13.8754)*h(log_brine_mass-7.74307)    No      -0.0334765
h(13.8754-log_co2_mass)*h(log_brine_mass-7.74307)    Yes     None
h(por-0.199557)*h(log_co2_mass-14.6976)              Yes     None
h(0.199557-por)*h(log_co2_mass-14.6976)              No      1.01841
log_permh*h(log_brine_mass-7.74307)                  No      0.020855
h(log_co2_mass-22.2325)*h(log_co2_mass-14.6976)      No      0.0776859
h(22.2325-log_co2_mass)*h(log_co2_mass-14.6976)      No      0.0235682
log_aniso*h(log_brine_mass-7.74307)                  No      -0.0109503
h(depth+702.833)                                     Yes     None
h(-702.833-depth)                                    No      0.0112197
depth*h(-702.833-depth)                              No      6.98062e-06
h(log_brine_mass-10.59)*h(-702.833-depth)            No      0.000641752
h(10.59-log_brine_mass)*h(-702.833-depth)            Yes     None
h(log_brine_mass-14.8312)*h(log_brine_mass-7.74307)  No      -0.00663513
h(14.8312-log_brine_mass)*h(log_brine_mass-7.74307)  No      0.0346708
por*h(log_brine_mass-7.74307)                        No      -0.25673
--------------------------------------------------------------------------
MSE: 1.0008, GCV: 1.0161, RSQ: 0.8601, GRSQ: 0.8580
parameters:
X[ 0 ] =  thick
X[ 1 ] =  depth
X[ 2 ] =  por
X[ 3 ] =  log_permh
X[ 4 ] =  log_aniso
X[ 5 ] =  rel_vol_frac_calcite
X[ 6 ] =  log_co2_rate
X[ 7 ] =  log_brine_rate
X[ 8 ] =  time
X[ 9 ] =  log_co2_mass
X[ 10 ] =  log_brine_mass
'''
def model(example_iterator):
    accessors = [
        lambda x: -0.7786765341855256,
        lambda x: 1.9241831041487594 * max(0, x[10] - 7.743066687074416),
        lambda x: -0.020121890380055987 * max(0, 7.743066687074416 - x[10]),
        lambda x: 0.0012668621433319961 * x[1] * max(0, x[10] - 7.743066687074416),
        lambda x: 0.29163093768174475 * max(0, x[9] - 14.69757777262863),
        lambda x: -0.03347647831261553 * max(0, x[9] - 13.875406671187159) *\
            max(0, x[10] - 7.743066687074416),
        lambda x: 1.0184113658204832 * max(0, 0.1995572603199634 - x[2]) *\
            max(0, x[9] - 14.69757777262863),
        lambda x: 0.02085498356759217 * x[3] * max(0, x[10] - 7.743066687074416),
        lambda x: 0.07768592393438968 * max(0, x[9] - 22.232482825856238) *\
            max(0, x[9] - 14.69757777262863),
        lambda x: 0.02356822422492821 * max(0, 22.232482825856238 - x[9]) *\
            max(0, x[9] - 14.69757777262863),
        lambda x: -0.010950278091013982 * x[4] * max(0, x[10] - 7.743066687074416),
        lambda x: 0.011219650542743279 * max(0, -702.8333268275682 - x[1]),
        lambda x: 6.980624761565579e-06 * x[1] * max(0, -702.8333268275682 - x[1]),
        lambda x: 0.0006417515025129317 * max(0, x[10] - 10.589959868429036) *\
            max(0, -702.8333268275682 - x[1]),
        lambda x: -0.006635128626744999 * max(0, x[10] - 14.831156080201502) *\
            max(0, x[10] - 7.743066687074416),
        lambda x: 0.034670835293705266 * max(0, 14.831156080201502 - x[10]) *\
            max(0, x[10] - 7.743066687074416),
        lambda x: -0.2567297926166889 * x[2] * max(0, x[10] - 7.743066687074416)]
    for x in example_iterator:
        yield sum(accessor(x) for accessor in accessors)
