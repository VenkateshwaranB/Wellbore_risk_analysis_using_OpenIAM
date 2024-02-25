'''
output: dis_log_dx
prediction score: 0.9475234002287183
Forward Pass
---------------------------------------------------------------
iter  parent  var  knot  mse       terms  gcv    rsq    grsq
---------------------------------------------------------------
0     -       -    -     5.688858  1      5.691  0.000  0.000
1     0       9    534   2.048397  3      2.053  0.640  0.639
2     0       10   3105  0.994461  5      0.999  0.825  0.825
3     1       10   1136  0.647187  7      0.651  0.886  0.886
4     1       9    4561  0.535051  9      0.539  0.906  0.905
5     0       2    -1    0.478516  10     0.483  0.916  0.915
6     1       3    -1    0.452857  11     0.457  0.920  0.920
7     4       9    2793  0.430384  13     0.435  0.924  0.924
8     0       8    -1    0.411403  14     0.417  0.928  0.927
9     4       10   4518  0.392549  16     0.398  0.931  0.930
10    9       0    -1    0.378552  17     0.384  0.933  0.932
11    0       4    -1    0.367805  18     0.374  0.935  0.934
12    17      10   3346  0.357808  20     0.364  0.937  0.936
13    1       10   4052  0.350800  22     0.358  0.938  0.937
14    9       10   4907  0.344265  24     0.352  0.939  0.938
15    3       3    -1    0.339926  25     0.348  0.940  0.939
---------------------------------------------------------------
Stopping Condition 2: Improvement below threshold

Pruning Pass
--------------------------------------------
iter  bf  terms  mse   gcv    rsq    grsq
--------------------------------------------
0     -   25     0.34  0.348  0.940  0.939
1     5   24     0.34  0.347  0.940  0.939
2     2   23     0.34  0.347  0.940  0.939
3     9   22     0.34  0.347  0.940  0.939
4     3   21     0.34  0.347  0.940  0.939
5     21  20     0.34  0.347  0.940  0.939
6     8   19     0.34  0.347  0.940  0.939
7     11  18     0.34  0.349  0.940  0.939
8     6   17     0.34  0.349  0.940  0.939
9     23  16     0.35  0.352  0.939  0.938
10    19  15     0.35  0.355  0.938  0.938
11    22  14     0.36  0.361  0.937  0.937
12    18  13     0.36  0.368  0.936  0.935
13    17  12     0.38  0.380  0.934  0.933
14    13  11     0.40  0.401  0.930  0.930
15    15  10     0.42  0.424  0.926  0.926
16    10  9      0.47  0.472  0.918  0.917
17    14  8      0.53  0.532  0.907  0.907
18    16  7      0.58  0.586  0.898  0.897
19    12  6      0.65  0.657  0.885  0.885
20    7   5      0.73  0.729  0.872  0.872
21    4   4      0.99  0.995  0.826  0.825
22    20  3      1.26  1.262  0.779  0.778
23    24  2      2.38  2.387  0.581  0.581
24    1   1      5.69  5.691  0.000  0.000
--------------------------------------------
Selected iteration: 4

Earth Model
--------------------------------------------------------------------------
Basis Function                                       Pruned  Coefficient
--------------------------------------------------------------------------
(Intercept)                                          No      4.41564
h(log_co2_mass-0.0821883)                            No      0.462761
h(0.0821883-log_co2_mass)                            Yes     None
h(log_brine_mass-15.5025)                            Yes     None
h(15.5025-log_brine_mass)                            No      -0.181386
h(log_brine_mass-14.6114)*h(log_co2_mass-0.0821883)  Yes     None
h(14.6114-log_brine_mass)*h(log_co2_mass-0.0821883)  No      -0.0303127
h(log_co2_mass-12.237)*h(log_co2_mass-0.0821883)     No      0.0102675
h(12.237-log_co2_mass)*h(log_co2_mass-0.0821883)     No      -0.00297148
por                                                  Yes     None
log_permh*h(log_co2_mass-0.0821883)                  No      0.0216382
h(log_co2_mass-1.31549)*h(15.5025-log_brine_mass)    No      0.0251399
h(1.31549-log_co2_mass)*h(15.5025-log_brine_mass)    No      -0.134561
time                                                 No      0.00678424
h(log_brine_mass-6.64239)*h(15.5025-log_brine_mass)  No      -0.035263
h(6.64239-log_brine_mass)*h(15.5025-log_brine_mass)  No      0.0116058
thick*por                                            No      -0.06328
log_aniso                                            No      -0.319837
h(log_brine_mass-14.5161)*log_aniso                  No      0.0547015
h(14.5161-log_brine_mass)*log_aniso                  No      0.0183501
h(log_brine_mass-10.8891)*h(log_co2_mass-0.0821883)  No      -0.0221905
h(10.8891-log_brine_mass)*h(log_co2_mass-0.0821883)  No      0.00482989
h(log_brine_mass-0.0352522)*por                      No      -0.129824
h(0.0352522-log_brine_mass)*por                      No      113.885
log_permh*h(log_brine_mass-15.5025)                  No      -0.0401091
--------------------------------------------------------------------------
MSE: 0.3403, GCV: 0.3468, RSQ: 0.9402, GRSQ: 0.9391
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
        lambda x: 4.415642851290571,
        lambda x: 0.4627609285779685 * max(0, x[9] - 0.08218833514948132),
        lambda x: -0.18138583632882113 * max(0, 15.502450949363372 - x[10]),
        lambda x: -0.03031265855174098 * max(0, 14.611416310861607 - x[10]) *\
            max(0, x[9] - 0.08218833514948132),
        lambda x: 0.010267543647911367 * max(0, x[9] - 12.236981288754603) *\
            max(0, x[9] - 0.08218833514948132),
        lambda x: -0.002971480642000382 * max(0, 12.236981288754603 - x[9]) *\
            max(0, x[9] - 0.08218833514948132),
        lambda x: 0.021638198849019796 * x[3] * max(0, x[9] - 0.08218833514948132),
        lambda x: 0.025139912048786517 * max(0, x[9] - 1.3154900858111318) *\
            max(0, 15.502450949363372 - x[10]),
        lambda x: -0.13456106153740263 * max(0, 1.3154900858111318 - x[9]) *\
            max(0, 15.502450949363372 - x[10]),
        lambda x: 0.006784244290090807 * x[8],
        lambda x: -0.03526301734510581 * max(0, x[10] - 6.642391444054431) *\
            max(0, 15.502450949363372 - x[10]),
        lambda x: 0.011605760166044206 * max(0, 6.642391444054431 - x[10]) *\
            max(0, 15.502450949363372 - x[10]),
        lambda x: -0.06327996381692566 * x[0] * x[2],
        lambda x: -0.31983724896423005 * x[4],
        lambda x: 0.054701501396305516 * max(0, x[10] - 14.516106176174521) * x[4],
        lambda x: 0.018350138757631307 * max(0, 14.516106176174521 - x[10]) * x[4],
        lambda x: -0.02219054896685023 * max(0, x[10] - 10.889124046903813) *\
            max(0, x[9] - 0.08218833514948132),
        lambda x: 0.004829891293377783 * max(0, 10.889124046903813 - x[10]) *\
            max(0, x[9] - 0.08218833514948132),
        lambda x: -0.12982423295354903 * max(0, x[10] - 0.03525219629883897) * x[2],
        lambda x: 113.88541476073533 * max(0, 0.03525219629883897 - x[10]) * x[2],
        lambda x: -0.04010907677771364 * x[3] * max(0, x[10] - 15.502450949363372)]
    for x in example_iterator:
        yield sum(accessor(x) for accessor in accessors)
