'''
output: pres_log_dy
prediction score: 0.9008707874459579
Forward Pass
-----------------------------------------------------------------
iter  parent  var  knot  mse        terms  gcv     rsq    grsq
-----------------------------------------------------------------
0     -       -    -     25.879084  1      25.889  0.000  0.000
1     0       10   3163  13.966399  3      13.997  0.460  0.459
2     0       9    3318  6.712333   5      6.740   0.741  0.740
3     3       10   446   4.612819   7      4.640   0.822  0.821
4     0       3    -1    3.820936   8      3.847   0.852  0.851
5     7       10   4454  3.514774   10     3.545   0.864  0.863
6     7       9    3289  3.287231   12     3.322   0.873  0.872
7     3       9    2702  3.051956   14     3.090   0.882  0.881
8     7       8    -1    2.859688   15     2.898   0.889  0.888
9     2       9    3535  2.690134   17     2.731   0.896  0.894
10    0       10   2094  2.599458   19     2.644   0.900  0.898
11    3       1    -1    2.547738   20     2.594   0.902  0.900
12    18      10   1499  2.508479   22     2.559   0.903  0.901
13    17      9    -1    2.473441   23     2.525   0.904  0.902
14    7       0    -1    2.439574   24     2.493   0.906  0.904
15    4       8    -1    2.407342   25     2.463   0.907  0.905
16    2       10   390   2.385534   27     2.445   0.908  0.906
-----------------------------------------------------------------
Stopping Condition 2: Improvement below threshold

Pruning Pass
------------------------------------------------
iter  bf  terms  mse    gcv     rsq     grsq
------------------------------------------------
0     -   27     2.39   2.445   0.908   0.906
1     17  26     2.39   2.442   0.908   0.906
2     25  25     2.40   2.454   0.907   0.905
3     26  24     2.41   2.460   0.907   0.905
4     21  23     2.41   2.463   0.907   0.905
5     16  22     2.44   2.490   0.906   0.904
6     22  21     2.48   2.525   0.904   0.902
7     20  20     2.51   2.558   0.903   0.901
8     23  19     2.56   2.600   0.901   0.900
9     19  18     2.60   2.647   0.899   0.898
10    24  17     2.66   2.698   0.897   0.896
11    6   16     2.74   2.776   0.894   0.893
12    15  15     2.79   2.824   0.892   0.891
13    2   14     2.86   2.900   0.889   0.888
14    18  13     2.90   2.935   0.888   0.887
15    3   12     2.97   2.998   0.885   0.884
16    9   11     3.04   3.064   0.883   0.882
17    10  10     3.18   3.203   0.877   0.876
18    12  9      3.18   3.201   0.877   0.876
19    13  8      3.32   3.343   0.872   0.871
20    14  7      3.45   3.468   0.867   0.866
21    8   6      3.72   3.736   0.856   0.856
22    5   5      5.31   5.334   0.795   0.794
23    7   4      8.05   8.077   0.689   0.688
24    4   3      9.59   9.606   0.630   0.629
25    11  2      14.06  14.076  0.457   0.456
26    1   1      25.88  25.889  -0.000  -0.000
------------------------------------------------
Selected iteration: 1

Earth Model
--------------------------------------------------------------------------
Basis Function                                       Pruned  Coefficient
--------------------------------------------------------------------------
(Intercept)                                          No      -84.5362
h(log_brine_mass-15.3164)                            No      11.2654
h(15.3164-log_brine_mass)                            No      -10.6976
h(log_co2_mass-13.5583)                              No      2.03795
h(13.5583-log_co2_mass)                              No      0.993975
h(log_brine_mass-9.09807)*h(log_co2_mass-13.5583)    No      -0.190556
h(9.09807-log_brine_mass)*h(log_co2_mass-13.5583)    No      0.154649
log_permh                                            No      -2.87876
h(log_brine_mass-21.4971)*log_permh                  No      0.945153
h(21.4971-log_brine_mass)*log_permh                  No      0.0602669
h(log_co2_mass-21.7055)*log_permh                    No      1.27242
h(21.7055-log_co2_mass)*log_permh                    No      0.0772156
h(log_co2_mass-21.6804)*h(log_co2_mass-13.5583)      No      1.49596
h(21.6804-log_co2_mass)*h(log_co2_mass-13.5583)      No      -0.102876
time*log_permh                                       No      0.00227906
h(log_co2_mass-13.8269)*h(15.3164-log_brine_mass)    No      -0.175545
h(13.8269-log_co2_mass)*h(15.3164-log_brine_mass)    No      -0.00833594
h(log_brine_mass-21.4426)                            Yes     None
h(21.4426-log_brine_mass)                            No      9.87342
depth*h(log_co2_mass-13.5583)                        No      0.000263775
h(log_brine_mass-20.0211)*h(21.4426-log_brine_mass)  No      2.23146
h(20.0211-log_brine_mass)*h(21.4426-log_brine_mass)  No      0.0798903
log_co2_mass*h(log_brine_mass-21.4426)               No      0.0777951
thick*log_permh                                      No      0.000821886
time*h(13.5583-log_co2_mass)                         No      0.00169501
h(log_brine_mass-6.56654)*h(15.3164-log_brine_mass)  No      0.0572939
h(6.56654-log_brine_mass)*h(15.3164-log_brine_mass)  No      -0.0761405
--------------------------------------------------------------------------
MSE: 2.3855, GCV: 2.4425, RSQ: 0.9078, GRSQ: 0.9057
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
        lambda x: -84.53618008371409,
        lambda x: 11.265436016307927 * max(0, x[10] - 15.316419960366586),
        lambda x: -10.69760674939224 * max(0, 15.316419960366586 - x[10]),
        lambda x: 2.0379537258087748 * max(0, x[9] - 13.558269712863583),
        lambda x: 0.9939753065507252 * max(0, 13.558269712863583 - x[9]),
        lambda x: -0.19055571450993172 * max(0, x[10] - 9.098066123227438) *\
            max(0, x[9] - 13.558269712863583),
        lambda x: 0.15464872340854927 * max(0, 9.098066123227438 - x[10]) *\
            max(0, x[9] - 13.558269712863583),
        lambda x: -2.878763928525285 * x[3],
        lambda x: 0.9451527058624112 * max(0, x[10] - 21.4970570785067) * x[3],
        lambda x: 0.06026686405620796 * max(0, 21.4970570785067 - x[10]) * x[3],
        lambda x: 1.272415680299609 * max(0, x[9] - 21.705510503788055) * x[3],
        lambda x: 0.07721560255897464 * max(0, 21.705510503788055 - x[9]) * x[3],
        lambda x: 1.4959602930863685 * max(0, x[9] - 21.680400670731164) *\
            max(0, x[9] - 13.558269712863583),
        lambda x: -0.10287641141634463 * max(0, 21.680400670731164 - x[9]) *\
            max(0, x[9] - 13.558269712863583),
        lambda x: 0.0022790606286120507 * x[8] * x[3],
        lambda x: -0.1755447584544894 * max(0, x[9] - 13.826939441664289) *\
            max(0, 15.316419960366586 - x[10]),
        lambda x: -0.008335936934595445 * max(0, 13.826939441664289 - x[9]) *\
            max(0, 15.316419960366586 - x[10]),
        lambda x: 9.873415210075782 * max(0, 21.4426102410005 - x[10]),
        lambda x: 0.0002637746867328872 * x[1] * max(0, x[9] - 13.558269712863583),
        lambda x: 2.231461861526763 * max(0, x[10] - 20.021084002381183) *\
            max(0, 21.4426102410005 - x[10]),
        lambda x: 0.079890261393602 * max(0, 20.021084002381183 - x[10]) *\
            max(0, 21.4426102410005 - x[10]),
        lambda x: 0.0777950885548423 * x[9] * max(0, x[10] - 21.4426102410005),
        lambda x: 0.0008218860267099615 * x[0] * x[3],
        lambda x: 0.0016950134868797262 * x[8] * max(0, 13.558269712863583 - x[9]),
        lambda x: 0.05729387607401898 * max(0, x[10] - 6.566538014312585) *\
            max(0, 15.316419960366586 - x[10]),
        lambda x: -0.07614052992722083 * max(0, 6.566538014312585 - x[10]) *\
            max(0, 15.316419960366586 - x[10])]
    for x in example_iterator:
        yield sum(accessor(x) for accessor in accessors)
