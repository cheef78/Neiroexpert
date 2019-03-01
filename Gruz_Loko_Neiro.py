def GR_Loko_Force (VSP_type, Main_type, Radius, h, V, Sh_Kol, f_tr):


    '''VSP_type это VSP_type - тип всп (1 - б.п., 2 - з.п.)
    ' Main_type это Main_type - состояние пути (1 - отличное или хорошее, 2 - удовлетворительное)
    ' Radius это R_m - радиус кривизны учатска, радиус кривизны прямого участка принимается 10000 м
    ' h это h_mm - возвышение наружнего рельса, мм
    ' V это V_km/h - скорость движения экипажа, км/ч
    ' Sh_Kol это S_mm - значение ширины колеи, мм
    ' f_tr это ftr - коэффициент трения

     outarray - это переменные выходных значиний (средние значения и СКО сил)
     mean_ - это среднее значение силы, кН
     RMS - это СКО силы, кН
     Q_ - это вертикальная сил
     Y_ - это боковая сила
     1,2,3,4 - номер оси в экипаже (в экипаже принято две тележки по две оси в каждой)
     r,l - правое или левое колесо 
    

    ' outarray1 это mean_Q_1l 
    ' outarray2 это mean_Q_2l
    ' outarray3 это mean_Q_1r
    ' outarray4 это mean_Q_2r
    ' outarray5 это mean_Q_3l
    ' outarray6 это mean_Q_4l
    ' outarray7 это mean_Q_3r
    ' outarray8 это mean_Q_4r
    ' outarray9 это RMS_Q_1l
    ' outarray10 это RMS_Q_2l
    ' outarray11 это RMS_Q_1r
    ' outarray12 это RMS_Q_2r
    ' outarray13 это RMS_Q_3l
    ' outarray14 это RMS_Q_4l
    ' outarray15 это RMS_Q_3r
    ' outarray16 это RMS_Q_4r
    ' outarray17 это mean_Y_1l
    ' outarray18 это mean_Y_2l
    ' outarray19 это mean_Y_1r
    ' outarray20 это mean_Y_2r
    ' outarray21 это mean_Y_3l
    ' outarray22 это mean_Y_4l
    ' outarray23 это mean_Y_3r
    ' outarray24 это mean_Y_4r
    ' outarray25 это RMS_Y_1l
    ' outarray26 это RMS_Y_2l
    ' outarray27 это RMS_Y_1r
    ' outarray28 это RMS_Y_2r
    ' outarray29 это RMS_Y_3l
    ' outarray30 это RMS_Y_4l
    ' outarray31 это RMS_Y_3r
    ' outarray32 это RMS_Y_4r'''

    import math

    VSP = VSP_type
    MAINT = Main_type
    Rad = Radius
    H=h
    v = V
    SHK=Sh_Kol
    FTR=f_tr
     


    if (VSP_type<1):
        VSP_type = 1
    if (VSP_type>2):
        VSP_type = 2
    VSP_type = (VSP_type - 1)
     
    if (Main_type<1):
        Main_type = 1
    if (Main_type>2):
        Main_type = 2
    Main_type = (Main_type - 1)
     
    if (Radius<150):
        Radius = 150
    if (Radius>10000):
        Radius = 10000
    Radius = (Radius - 150) / 9850
     
    if (h<0):
        h = 0
    if (h>200):
        h = 200
    h = h / 200
     
    if (V<5):
        V = 5
    if (V>200):
        V = 200
    V = (V - 5) / 195
     
    if (Sh_Kol<1510):
        Sh_Kol = 1510
    if (Sh_Kol>1560):
        Sh_Kol = 1560
    Sh_Kol = (Sh_Kol - 1510) / 50
     
    if (f_tr<0.1):
        f_tr = 0.1
    if (f_tr>0.7):
        f_tr = 0.7
    f_tr = (f_tr - 0.1) / 0.6
     
    netsum = 2.585002
    netsum = netsum + VSP_type * 0
    netsum = netsum + Main_type * 0
    netsum = netsum + Radius * -8.91273
    netsum = netsum + h * 0.8210604
    netsum = netsum + V * -3.471508
    netsum = netsum + Sh_Kol * 0
    netsum = netsum + f_tr * -0.1360189
    feature21 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.377504
    netsum = netsum + VSP_type * 0
    netsum = netsum + Main_type * -1.15781E-03
    netsum = netsum + Radius * -80.54958
    netsum = netsum + h * -7.702893E-02
    netsum = netsum + V * 5.772938
    netsum = netsum + Sh_Kol * -3.005799E-03
    netsum = netsum + f_tr * 2.041161E-02
    feature22 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.933569
    netsum = netsum + VSP_type * -1.711932E-03
    netsum = netsum + Main_type * 3.348329
    netsum = netsum + Radius * -9.856087
    netsum = netsum + h * 4.212798E-02
    netsum = netsum + V * -6.785546
    netsum = netsum + Sh_Kol * -2.193178E-02
    netsum = netsum + f_tr * -0.115735
    feature23 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.203883
    netsum = netsum + VSP_type * 0
    netsum = netsum + Main_type * -0.1876383
    netsum = netsum + Radius * -0.4741783
    netsum = netsum + h * -1.473345
    netsum = netsum + V * -27.2589
    netsum = netsum + Sh_Kol * 2.778484E-02
    netsum = netsum + f_tr * -2.686149E-02
    feature24 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.1722996
    netsum = netsum + VSP_type * -4.179223E-02
    netsum = netsum + Main_type * -3.111501
    netsum = netsum + Radius * -6.051737
    netsum = netsum + h * -1.546812
    netsum = netsum + V * 20.1687
    netsum = netsum + Sh_Kol * -6.053827E-02
    netsum = netsum + f_tr * -0.27134
    feature25 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.066288
    netsum = netsum + VSP_type * 1.266568E-03
    netsum = netsum + Main_type * 1.944989E-02
    netsum = netsum + Radius * 25.41498
    netsum = netsum + h * -1.981775E-03
    netsum = netsum + V * 1.603726
    netsum = netsum + Sh_Kol * -3.990319E-03
    netsum = netsum + f_tr * -6.385222E-02
    feature26 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.120572
    netsum = netsum + VSP_type * -1.460704E-03
    netsum = netsum + Main_type * -4.133869E-03
    netsum = netsum + Radius * 7.307359
    netsum = netsum + h * -2.142782
    netsum = netsum + V * 7.809622
    netsum = netsum + Sh_Kol * -3.511675E-03
    netsum = netsum + f_tr * -0.2647697
    feature27 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.824843
    netsum = netsum + VSP_type * 0
    netsum = netsum + Main_type * -0.1292598
    netsum = netsum + Radius * -0.9879975
    netsum = netsum + h * -1.204435
    netsum = netsum + V * -13.94144
    netsum = netsum + Sh_Kol * 1.130541E-02
    netsum = netsum + f_tr * 2.213776E-04
    feature28 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.029858
    netsum = netsum + VSP_type * 1.767524E-03
    netsum = netsum + Main_type * 0.9493096
    netsum = netsum + Radius * 29.43046
    netsum = netsum + h * 0.8889506
    netsum = netsum + V * -8.378217
    netsum = netsum + Sh_Kol * 4.480276E-03
    netsum = netsum + f_tr * 0.1820433
    feature29 = 1 / (1 + math.exp(-netsum))
     
    netsum = 4.230172
    netsum = netsum + VSP_type * 0
    netsum = netsum + Main_type * -4.297026E-02
    netsum = netsum + Radius * -8.079624
    netsum = netsum + h * 1.305674
    netsum = netsum + V * -5.790204
    netsum = netsum + Sh_Kol * 4.882933E-03
    netsum = netsum + f_tr * -11.42556
    feature210 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.850837
    netsum = netsum + VSP_type * 0
    netsum = netsum + Main_type * 2.729965E-02
    netsum = netsum + Radius * 24.26503
    netsum = netsum + h * -0.8527321
    netsum = netsum + V * 3.568127
    netsum = netsum + Sh_Kol * -7.076751E-04
    netsum = netsum + f_tr * -1.893624
    feature211 = 1 / (1 + math.exp(-netsum))
     
    netsum = 5.964153
    netsum = netsum + VSP_type * 0.0101979
    netsum = netsum + Main_type * 0.3099363
    netsum = netsum + Radius * -0.5788043
    netsum = netsum + h * 1.326795
    netsum = netsum + V * -16.57725
    netsum = netsum + Sh_Kol * 1.407271E-02
    netsum = netsum + f_tr * 0.1802763
    feature212 = 1 / (1 + math.exp(-netsum))
     
    netsum = -7.644811E-02
    netsum = netsum + VSP_type * 0
    netsum = netsum + Main_type * 0.3290109
    netsum = netsum + Radius * 23.57824
    netsum = netsum + h * -1.216775
    netsum = netsum + V * 6.496041
    netsum = netsum + Sh_Kol * 5.68667E-03
    netsum = netsum + f_tr * 0.441742
    feature213 = 1 / (1 + math.exp(-netsum))
     
    netsum = 5.85291
    netsum = netsum + VSP_type * 4.121559E-03
    netsum = netsum + Main_type * 5.228132E-02
    netsum = netsum + Radius * -5.183594
    netsum = netsum + h * -2.354057
    netsum = netsum + V * 1.04286
    netsum = netsum + Sh_Kol * 5.532813E-03
    netsum = netsum + f_tr * -7.278997E-02
    feature214 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.3596448
    netsum = netsum + VSP_type * -0.0986152
    netsum = netsum + Main_type * -6.176906
    netsum = netsum + Radius * 5.511677
    netsum = netsum + h * -5.737221
    netsum = netsum + V * -7.14607
    netsum = netsum + Sh_Kol * -0.1854707
    netsum = netsum + f_tr * 0.2085879
    feature215 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.925175
    netsum = netsum + VSP_type * -2.069295E-02
    netsum = netsum + Main_type * 1.198643
    netsum = netsum + Radius * 15.57942
    netsum = netsum + h * 4.30018
    netsum = netsum + V * -5.155819
    netsum = netsum + Sh_Kol * 7.023121E-02
    netsum = netsum + f_tr * -0.3101979
    feature216 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.4316418
    netsum = netsum + VSP_type * -0.0115965
    netsum = netsum + Main_type * -1.766893
    netsum = netsum + Radius * -19.04112
    netsum = netsum + h * -0.1739395
    netsum = netsum + V * 8.193781
    netsum = netsum + Sh_Kol * 0
    netsum = netsum + f_tr * -8.844902E-02
    feature217 = 1 / (1 + math.exp(-netsum))
     
    netsum = 9.184696
    netsum = netsum + VSP_type * 2.459425E-02
    netsum = netsum + Main_type * -5.261024
    netsum = netsum + Radius * 22.34481
    netsum = netsum + h * 5.298235
    netsum = netsum + V * -54.86484
    netsum = netsum + Sh_Kol * 0.2125103
    netsum = netsum + f_tr * -0.5673731
    feature218 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.788542
    netsum = netsum + VSP_type * -0.017276
    netsum = netsum + Main_type * 1.277058
    netsum = netsum + Radius * -9.111587
    netsum = netsum + h * 4.142786
    netsum = netsum + V * -5.90767
    netsum = netsum + Sh_Kol * 8.827934E-02
    netsum = netsum + f_tr * -0.2551651
    feature219 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.5731257
    netsum = netsum + VSP_type * -2.299097E-02
    netsum = netsum + Main_type * -2.863071
    netsum = netsum + Radius * -7.534512
    netsum = netsum + h * -1.145737
    netsum = netsum + V * 22.22261
    netsum = netsum + Sh_Kol * -4.156273E-02
    netsum = netsum + f_tr * -0.3192002
    feature220 = 1 / (1 + math.exp(-netsum))
     
    netsum = 3.353116E-02
    netsum = netsum + feature21 * -1.098593
    netsum = netsum + feature22 * 5.549904
    netsum = netsum + feature23 * -0.5538056
    netsum = netsum + feature24 * -0.4779334
    netsum = netsum + feature25 * 0.1769448
    netsum = netsum + feature26 * -0.780533
    netsum = netsum + feature27 * 0.2913962
    netsum = netsum + feature28 * 0.6850054
    netsum = netsum + feature29 * -0.3726028
    netsum = netsum + feature210 * 0.2664965
    netsum = netsum + feature211 * -0.9582636
    netsum = netsum + feature212 * -7.820591E-03
    netsum = netsum + feature213 * 1.179895
    netsum = netsum + feature214 * 0.6720694
    netsum = netsum + feature215 * 5.076898E-03
    netsum = netsum + feature216 * -0.2022146
    netsum = netsum + feature217 * -0.2928072
    netsum = netsum + feature218 * -2.080953E-02
    netsum = netsum + feature219 * 6.183216E-02
    netsum = netsum + feature220 * -0.1839077
    outarray1 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.3498494
    netsum = netsum + feature21 * -1.834111
    netsum = netsum + feature22 * 5.791573
    netsum = netsum + feature23 * -0.2514298
    netsum = netsum + feature24 * -0.2978224
    netsum = netsum + feature25 * 0.1322535
    netsum = netsum + feature26 * -1.295514
    netsum = netsum + feature27 * -0.3528982
    netsum = netsum + feature28 * 0.4777231
    netsum = netsum + feature29 * -0.3576145
    netsum = netsum + feature210 * -0.2962484
    netsum = netsum + feature211 * 1.311984
    netsum = netsum + feature212 * 4.333354E-03
    netsum = netsum + feature213 * -0.1591013
    netsum = netsum + feature214 * 0.6897363
    netsum = netsum + feature215 * 4.615961E-03
    netsum = netsum + feature216 * -0.3132345
    netsum = netsum + feature217 * -0.2696128
    netsum = netsum + feature218 * -1.271417E-02
    netsum = netsum + feature219 * 0.2794035
    netsum = netsum + feature220 * -0.1356083
    outarray2 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.3942647
    netsum = netsum + feature21 * 1.095245
    netsum = netsum + feature22 * -6.823901
    netsum = netsum + feature23 * 0.2044797
    netsum = netsum + feature24 * 0.3647338
    netsum = netsum + feature25 * -4.462903E-02
    netsum = netsum + feature26 * 1.377934
    netsum = netsum + feature27 * -0.4888797
    netsum = netsum + feature28 * -0.5601993
    netsum = netsum + feature29 * 5.470579E-02
    netsum = netsum + feature210 * -0.1733635
    netsum = netsum + feature211 * 0.5966043
    netsum = netsum + feature212 * -6.280725E-03
    netsum = netsum + feature213 * -0.8801793
    netsum = netsum + feature214 * -0.619571
    netsum = netsum + feature215 * -7.863672E-03
    netsum = netsum + feature216 * -0.1205514
    netsum = netsum + feature217 * 6.181026E-02
    netsum = netsum + feature218 * 2.211483E-03
    netsum = netsum + feature219 * 0.2025758
    netsum = netsum + feature220 * 4.565382E-02
    outarray3 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.9175387
    netsum = netsum + feature21 * 1.952492
    netsum = netsum + feature22 * -6.569154
    netsum = netsum + feature23 * -6.019495E-02
    netsum = netsum + feature24 * 0.1443978
    netsum = netsum + feature25 * -1.092275E-02
    netsum = netsum + feature26 * 1.813446
    netsum = netsum + feature27 * 0.260812
    netsum = netsum + feature28 * -0.3017134
    netsum = netsum + feature29 * 9.961278E-02
    netsum = netsum + feature210 * 0.4097358
    netsum = netsum + feature211 * -1.77512
    netsum = netsum + feature212 * -1.885083E-02
    netsum = netsum + feature213 * 0.5683448
    netsum = netsum + feature214 * -0.6428273
    netsum = netsum + feature215 * -7.75435E-03
    netsum = netsum + feature216 * 0.1038436
    netsum = netsum + feature217 * 7.456393E-02
    netsum = netsum + feature218 * -4.547582E-03
    netsum = netsum + feature219 * -0.1345036
    netsum = netsum + feature220 * 9.239615E-03
    outarray4 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.502343E-02
    netsum = netsum + feature21 * -1.090052
    netsum = netsum + feature22 * 6.86203
    netsum = netsum + feature23 * -0.457256
    netsum = netsum + feature24 * -0.4349099
    netsum = netsum + feature25 * 0.1451138
    netsum = netsum + feature26 * -1.048277
    netsum = netsum + feature27 * 0.3949459
    netsum = netsum + feature28 * 0.6379126
    netsum = netsum + feature29 * -0.2376748
    netsum = netsum + feature210 * 0.209325
    netsum = netsum + feature211 * -0.7538633
    netsum = netsum + feature212 * -1.181277E-02
    netsum = netsum + feature213 * 0.9511968
    netsum = netsum + feature214 * 0.6535029
    netsum = netsum + feature215 * 4.697547E-03
    netsum = netsum + feature216 * -8.267083E-02
    netsum = netsum + feature217 * -0.2052777
    netsum = netsum + feature218 * -1.990907E-02
    netsum = netsum + feature219 * 7.190094E-04
    netsum = netsum + feature220 * -0.1584994
    outarray5 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.268903
    netsum = netsum + feature21 * -1.732059
    netsum = netsum + feature22 * 8.395462
    netsum = netsum + feature23 * -4.07727E-03
    netsum = netsum + feature24 * -0.2408742
    netsum = netsum + feature25 * 8.008063E-02
    netsum = netsum + feature26 * -1.498133
    netsum = netsum + feature27 * -0.1847566
    netsum = netsum + feature28 * 0.3912296
    netsum = netsum + feature29 * -0.1704496
    netsum = netsum + feature210 * -0.3434489
    netsum = netsum + feature211 * 1.486558
    netsum = netsum + feature212 * 2.178594E-02
    netsum = netsum + feature213 * -0.531067
    netsum = netsum + feature214 * 0.6804692
    netsum = netsum + feature215 * 4.394625E-03
    netsum = netsum + feature216 * -0.185082
    netsum = netsum + feature217 * -0.1380431
    netsum = netsum + feature218 * -1.576273E-02
    netsum = netsum + feature219 * 0.1864778
    netsum = netsum + feature220 * -0.0748531
    outarray6 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.3959927
    netsum = netsum + feature21 * 1.15371
    netsum = netsum + feature22 * -8.460967
    netsum = netsum + feature23 * 5.011388E-02
    netsum = netsum + feature24 * 0.2945628
    netsum = netsum + feature25 * 2.030455E-03
    netsum = netsum + feature26 * 1.638292
    netsum = netsum + feature27 * -0.5413416
    netsum = netsum + feature28 * -0.4782964
    netsum = netsum + feature29 * -9.451984E-02
    netsum = netsum + feature210 * -7.911574E-02
    netsum = netsum + feature211 * 0.2558129
    netsum = netsum + feature212 * -9.202598E-03
    netsum = netsum + feature213 * -0.5275772
    netsum = netsum + feature214 * -0.6061891
    netsum = netsum + feature215 * -8.579658E-03
    netsum = netsum + feature216 * -0.1992158
    netsum = netsum + feature217 * -4.765136E-02
    netsum = netsum + feature218 * 3.966052E-05
    netsum = netsum + feature219 * 0.2145361
    netsum = netsum + feature220 * 1.086839E-03
    outarray7 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.6656377
    netsum = netsum + feature21 * 1.864682
    netsum = netsum + feature22 * -10.15182
    netsum = netsum + feature23 * -0.480636
    netsum = netsum + feature24 * 0.1227503
    netsum = netsum + feature25 * 8.661247E-02
    netsum = netsum + feature26 * 2.208038
    netsum = netsum + feature27 * 4.929926E-02
    netsum = netsum + feature28 * -0.2525318
    netsum = netsum + feature29 * -0.2039512
    netsum = netsum + feature210 * 0.508822
    netsum = netsum + feature211 * -2.146807
    netsum = netsum + feature212 * -4.379946E-02
    netsum = netsum + feature213 * 1.055437
    netsum = netsum + feature214 * -0.6360419
    netsum = netsum + feature215 * -8.813688E-03
    netsum = netsum + feature216 * -0.133117
    netsum = netsum + feature217 * -0.1497762
    netsum = netsum + feature218 * -3.591663E-03
    netsum = netsum + feature219 * 0.0646526
    netsum = netsum + feature220 * -0.1034148
    outarray8 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.1773429
    netsum = netsum + feature21 * -0.9226599
    netsum = netsum + feature22 * 5.383438
    netsum = netsum + feature23 * -3.264552
    netsum = netsum + feature24 * 2.304427
    netsum = netsum + feature25 * 1.694919
    netsum = netsum + feature26 * -2.992868
    netsum = netsum + feature27 * 0.6541744
    netsum = netsum + feature28 * -0.7387958
    netsum = netsum + feature29 * 1.780018
    netsum = netsum + feature210 * 0.8809488
    netsum = netsum + feature211 * -3.256931
    netsum = netsum + feature212 * -0.9032668
    netsum = netsum + feature213 * 2.758149
    netsum = netsum + feature214 * -0.3700259
    netsum = netsum + feature215 * -0.1873785
    netsum = netsum + feature216 * 0.8754309
    netsum = netsum + feature217 * 9.738607E-02
    netsum = netsum + feature218 * -0.5431947
    netsum = netsum + feature219 * -0.9182767
    netsum = netsum + feature220 * -2.225594
    outarray9 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.6292897
    netsum = netsum + feature21 * -2.15927
    netsum = netsum + feature22 * 7.663716
    netsum = netsum + feature23 * -1.285421
    netsum = netsum + feature24 * 5.21628
    netsum = netsum + feature25 * 1.001565
    netsum = netsum + feature26 * -5.030556
    netsum = netsum + feature27 * 0.1797435
    netsum = netsum + feature28 * -3.766723
    netsum = netsum + feature29 * 2.996246
    netsum = netsum + feature210 * -0.2305049
    netsum = netsum + feature211 * 1.152343
    netsum = netsum + feature212 * -0.7809108
    netsum = netsum + feature213 * -1.19842
    netsum = netsum + feature214 * -0.4975233
    netsum = netsum + feature215 * -0.1336476
    netsum = netsum + feature216 * 1.061205
    netsum = netsum + feature217 * 0.9869141
    netsum = netsum + feature218 * -0.3316541
    netsum = netsum + feature219 * -0.8945517
    netsum = netsum + feature220 * -1.519637
    outarray10 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.783026E-02
    netsum = netsum + feature21 * -1.026898
    netsum = netsum + feature22 * 4.941339
    netsum = netsum + feature23 * -3.343899
    netsum = netsum + feature24 * 2.321918
    netsum = netsum + feature25 * 1.733271
    netsum = netsum + feature26 * -3.496337
    netsum = netsum + feature27 * 0.935725
    netsum = netsum + feature28 * -0.6916156
    netsum = netsum + feature29 * 2.201578
    netsum = netsum + feature210 * 1.013789
    netsum = netsum + feature211 * -3.780458
    netsum = netsum + feature212 * -0.9760148
    netsum = netsum + feature213 * 3.196086
    netsum = netsum + feature214 * -0.3828191
    netsum = netsum + feature215 * -0.1800996
    netsum = netsum + feature216 * 1.058963
    netsum = netsum + feature217 * 0.3344175
    netsum = netsum + feature218 * -0.5538318
    netsum = netsum + feature219 * -1.057324
    netsum = netsum + feature220 * -2.297487
    outarray11 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.5202509
    netsum = netsum + feature21 * -2.34315
    netsum = netsum + feature22 * 7.167701
    netsum = netsum + feature23 * -1.339984
    netsum = netsum + feature24 * 5.131456
    netsum = netsum + feature25 * 1.016612
    netsum = netsum + feature26 * -5.36483
    netsum = netsum + feature27 * 0.3302812
    netsum = netsum + feature28 * -3.687559
    netsum = netsum + feature29 * 3.267813
    netsum = netsum + feature210 * -8.462605E-02
    netsum = netsum + feature211 * 0.609605
    netsum = netsum + feature212 * -0.7954996
    netsum = netsum + feature213 * -0.7434843
    netsum = netsum + feature214 * -0.4722541
    netsum = netsum + feature215 * -0.1344143
    netsum = netsum + feature216 * 1.187592
    netsum = netsum + feature217 * 1.155195
    netsum = netsum + feature218 * -0.3500069
    netsum = netsum + feature219 * -1.024901
    netsum = netsum + feature220 * -1.553456
    outarray12 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.141217
    netsum = netsum + feature21 * 0.4276485
    netsum = netsum + feature22 * 6.214697
    netsum = netsum + feature23 * -2.789092
    netsum = netsum + feature24 * 2.290824
    netsum = netsum + feature25 * 1.354501
    netsum = netsum + feature26 * -2.448692
    netsum = netsum + feature27 * 1.200069
    netsum = netsum + feature28 * -0.6827573
    netsum = netsum + feature29 * 1.643703
    netsum = netsum + feature210 * 0.8824716
    netsum = netsum + feature211 * -3.422272
    netsum = netsum + feature212 * -0.899049
    netsum = netsum + feature213 * 2.83456
    netsum = netsum + feature214 * -0.5144021
    netsum = netsum + feature215 * -0.1619347
    netsum = netsum + feature216 * 1.230502
    netsum = netsum + feature217 * 0.1640199
    netsum = netsum + feature218 * -0.4216803
    netsum = netsum + feature219 * -1.223111
    netsum = netsum + feature220 * -1.858874
    outarray13 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.04075
    netsum = netsum + feature21 * 0.170699
    netsum = netsum + feature22 * 10.02113
    netsum = netsum + feature23 * -1.28634
    netsum = netsum + feature24 * 3.47871
    netsum = netsum + feature25 * 0.4785491
    netsum = netsum + feature26 * -3.706671
    netsum = netsum + feature27 * 1.160403
    netsum = netsum + feature28 * -2.456724
    netsum = netsum + feature29 * 2.803556
    netsum = netsum + feature210 * 0.1007762
    netsum = netsum + feature211 * -0.3428284
    netsum = netsum + feature212 * -0.7835656
    netsum = netsum + feature213 * 0.3055489
    netsum = netsum + feature214 * -0.6331436
    netsum = netsum + feature215 * -0.1058753
    netsum = netsum + feature216 * 1.516424
    netsum = netsum + feature217 * 1.027973
    netsum = netsum + feature218 * -0.1890224
    netsum = netsum + feature219 * -1.345499
    netsum = netsum + feature220 * -0.9667585
    outarray14 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.068232
    netsum = netsum + feature21 * 2.381257E-03
    netsum = netsum + feature22 * 5.712757
    netsum = netsum + feature23 * -2.996465
    netsum = netsum + feature24 * 2.373052
    netsum = netsum + feature25 * 1.448243
    netsum = netsum + feature26 * -2.992934
    netsum = netsum + feature27 * 1.342702
    netsum = netsum + feature28 * -0.7016318
    netsum = netsum + feature29 * 2.007418
    netsum = netsum + feature210 * 1.002051
    netsum = netsum + feature211 * -3.86185
    netsum = netsum + feature212 * -0.9562348
    netsum = netsum + feature213 * 3.283995
    netsum = netsum + feature214 * -0.505074
    netsum = netsum + feature215 * -0.1634573
    netsum = netsum + feature216 * 1.24502
    netsum = netsum + feature217 * 0.3066483
    netsum = netsum + feature218 * -0.4362727
    netsum = netsum + feature219 * -1.199779
    netsum = netsum + feature220 * -1.966204
    outarray15 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.088283
    netsum = netsum + feature21 * -0.1611582
    netsum = netsum + feature22 * 9.265305
    netsum = netsum + feature23 * -1.30646
    netsum = netsum + feature24 * 3.66775
    netsum = netsum + feature25 * 0.4446989
    netsum = netsum + feature26 * -4.271426
    netsum = netsum + feature27 * 1.364162
    netsum = netsum + feature28 * -2.580253
    netsum = netsum + feature29 * 3.089345
    netsum = netsum + feature210 * 0.2409219
    netsum = netsum + feature211 * -0.8575228
    netsum = netsum + feature212 * -0.7696498
    netsum = netsum + feature213 * 0.7406545
    netsum = netsum + feature214 * -0.5968755
    netsum = netsum + feature215 * -0.1154349
    netsum = netsum + feature216 * 1.680009
    netsum = netsum + feature217 * 1.197013
    netsum = netsum + feature218 * -0.1799574
    netsum = netsum + feature219 * -1.44905
    netsum = netsum + feature220 * -0.9253221
    outarray16 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.3421165
    netsum = netsum + feature21 * -0.2089277
    netsum = netsum + feature22 * -1.590221
    netsum = netsum + feature23 * 0.4181143
    netsum = netsum + feature24 * 0.1781095
    netsum = netsum + feature25 * -5.811331E-02
    netsum = netsum + feature26 * 0.2720192
    netsum = netsum + feature27 * -0.4396541
    netsum = netsum + feature28 * -0.2596879
    netsum = netsum + feature29 * 8.489856E-02
    netsum = netsum + feature210 * -0.2428683
    netsum = netsum + feature211 * 1.815587
    netsum = netsum + feature212 * 3.122752E-02
    netsum = netsum + feature213 * -1.278744
    netsum = netsum + feature214 * -0.1052151
    netsum = netsum + feature215 * 1.998434E-03
    netsum = netsum + feature216 * -9.191313E-02
    netsum = netsum + feature217 * 8.641152E-02
    netsum = netsum + feature218 * -2.19506E-04
    netsum = netsum + feature219 * 0.1665398
    netsum = netsum + feature220 * 7.711826E-02
    outarray17 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.4564251
    netsum = netsum + feature21 * 1.043108
    netsum = netsum + feature22 * -3.449038
    netsum = netsum + feature23 * -0.4309924
    netsum = netsum + feature24 * -0.1647706
    netsum = netsum + feature25 * 0.0975165
    netsum = netsum + feature26 * 1.068513
    netsum = netsum + feature27 * 0.3024451
    netsum = netsum + feature28 * 0.1506853
    netsum = netsum + feature29 * -0.2005913
    netsum = netsum + feature210 * 0.4461666
    netsum = netsum + feature211 * -1.852689
    netsum = netsum + feature212 * -1.646452E-02
    netsum = netsum + feature213 * 1.204371
    netsum = netsum + feature214 * -0.1637983
    netsum = netsum + feature215 * -5.249042E-03
    netsum = netsum + feature216 * 1.697159E-02
    netsum = netsum + feature217 * -0.1530266
    netsum = netsum + feature218 * -8.369832E-03
    netsum = netsum + feature219 * -9.366111E-02
    netsum = netsum + feature220 * -0.1018416
    outarray18 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.4613237
    netsum = netsum + feature21 * 0.3115571
    netsum = netsum + feature22 * -1.317435
    netsum = netsum + feature23 * 0.1026621
    netsum = netsum + feature24 * 0.1548386
    netsum = netsum + feature25 * -5.736619E-02
    netsum = netsum + feature26 * -7.647621E-02
    netsum = netsum + feature27 * -0.1501828
    netsum = netsum + feature28 * -0.2081005
    netsum = netsum + feature29 * 8.314418E-02
    netsum = netsum + feature210 * -0.2550678
    netsum = netsum + feature211 * 7.783496E-02
    netsum = netsum + feature212 * -8.596314E-03
    netsum = netsum + feature213 * -0.2554932
    netsum = netsum + feature214 * -0.19974
    netsum = netsum + feature215 * -2.831288E-03
    netsum = netsum + feature216 * 6.209408E-02
    netsum = netsum + feature217 * 6.765909E-02
    netsum = netsum + feature218 * 1.185837E-02
    netsum = netsum + feature219 * -1.975279E-02
    netsum = netsum + feature220 * 5.296303E-02
    outarray19 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.1235382
    netsum = netsum + feature21 * 0.4752302
    netsum = netsum + feature22 * -0.2415218
    netsum = netsum + feature23 * 0.1921248
    netsum = netsum + feature24 * 0.1827796
    netsum = netsum + feature25 * -8.520814E-02
    netsum = netsum + feature26 * 0.1046492
    netsum = netsum + feature27 * 0.2390811
    netsum = netsum + feature28 * -0.2309878
    netsum = netsum + feature29 * 0.2720473
    netsum = netsum + feature210 * 8.973013E-02
    netsum = netsum + feature211 * -0.3533387
    netsum = netsum + feature212 * -9.271041E-03
    netsum = netsum + feature213 * -0.1024219
    netsum = netsum + feature214 * -0.2268568
    netsum = netsum + feature215 * -6.961597E-04
    netsum = netsum + feature216 * 0.1696071
    netsum = netsum + feature217 * 0.1890293
    netsum = netsum + feature218 * 6.624366E-03
    netsum = netsum + feature219 * -0.1377756
    netsum = netsum + feature220 * 7.928956E-02
    outarray20 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.3360249
    netsum = netsum + feature21 * -8.111735E-02
    netsum = netsum + feature22 * -2.566041
    netsum = netsum + feature23 * 0.2515105
    netsum = netsum + feature24 * 7.028193E-02
    netsum = netsum + feature25 * 5.976525E-03
    netsum = netsum + feature26 * 0.5620199
    netsum = netsum + feature27 * -0.4033906
    netsum = netsum + feature28 * -0.1559567
    netsum = netsum + feature29 * 2.212418E-02
    netsum = netsum + feature210 * -0.1079135
    netsum = netsum + feature211 * 1.258038
    netsum = netsum + feature212 * 2.488076E-02
    netsum = netsum + feature213 * -0.882225
    netsum = netsum + feature214 * -0.1104123
    netsum = netsum + feature215 * -2.060996E-03
    netsum = netsum + feature216 * -0.177692
    netsum = netsum + feature217 * 2.572446E-02
    netsum = netsum + feature218 * -1.420416E-02
    netsum = netsum + feature219 * 0.2012963
    netsum = netsum + feature220 * 1.250283E-02
    outarray21 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.961892E-02
    netsum = netsum + feature21 * 0.8398662
    netsum = netsum + feature22 * -6.374781
    netsum = netsum + feature23 * -0.6359119
    netsum = netsum + feature24 * -0.1591452
    netsum = netsum + feature25 * 0.1733185
    netsum = netsum + feature26 * 1.381419
    netsum = netsum + feature27 * 5.255827E-02
    netsum = netsum + feature28 * 0.1339978
    netsum = netsum + feature29 * -0.4184866
    netsum = netsum + feature210 * 0.4626694
    netsum = netsum + feature211 * -1.887709
    netsum = netsum + feature212 * -0.0254734
    netsum = netsum + feature213 * 1.245483
    netsum = netsum + feature214 * -0.1705417
    netsum = netsum + feature215 * -7.037055E-03
    netsum = netsum + feature216 * -0.2494927
    netsum = netsum + feature217 * -0.3053909
    netsum = netsum + feature218 * -0.0195224
    netsum = netsum + feature219 * 0.1408274
    netsum = netsum + feature220 * -0.1820123
    outarray22 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.5106606
    netsum = netsum + feature21 * 0.2680255
    netsum = netsum + feature22 * -1.539242
    netsum = netsum + feature23 * 0.1186015
    netsum = netsum + feature24 * 0.1490008
    netsum = netsum + feature25 * -5.356299E-02
    netsum = netsum + feature26 * -5.205155E-02
    netsum = netsum + feature27 * -0.1997186
    netsum = netsum + feature28 * -0.2058557
    netsum = netsum + feature29 * 4.752015E-02
    netsum = netsum + feature210 * -0.2542466
    netsum = netsum + feature211 * 0.1190819
    netsum = netsum + feature212 * -3.902274E-03
    netsum = netsum + feature213 * -0.2652279
    netsum = netsum + feature214 * -0.2009
    netsum = netsum + feature215 * -3.17901E-03
    netsum = netsum + feature216 * 3.953297E-02
    netsum = netsum + feature217 * 4.783199E-02
    netsum = netsum + feature218 * 1.083519E-02
    netsum = netsum + feature219 * -1.703934E-02
    netsum = netsum + feature220 * 5.401357E-02
    outarray23 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.21219
    netsum = netsum + feature21 * 0.3348127
    netsum = netsum + feature22 * -0.1060788
    netsum = netsum + feature23 * 0.2139757
    netsum = netsum + feature24 * 0.1598769
    netsum = netsum + feature25 * -9.847008E-02
    netsum = netsum + feature26 * -0.0530447
    netsum = netsum + feature27 * 0.1356257
    netsum = netsum + feature28 * -0.2008115
    netsum = netsum + feature29 * 0.3245636
    netsum = netsum + feature210 * 1.369337E-02
    netsum = netsum + feature211 * -4.424707E-02
    netsum = netsum + feature212 * -1.525341E-02
    netsum = netsum + feature213 * -0.1434229
    netsum = netsum + feature214 * -0.2277205
    netsum = netsum + feature215 * 4.642502E-04
    netsum = netsum + feature216 * 0.1997487
    netsum = netsum + feature217 * 0.2274629
    netsum = netsum + feature218 * 9.874996E-03
    netsum = netsum + feature219 * -0.154218
    netsum = netsum + feature220 * 0.0897963
    outarray24 = 1 / (1 + math.exp(-netsum))
     
    netsum = 7.964132E-02
    netsum = netsum + feature21 * 0.1229193
    netsum = netsum + feature22 * 0.2055507
    netsum = netsum + feature23 * -0.4156206
    netsum = netsum + feature24 * -4.025633E-02
    netsum = netsum + feature25 * 0.1110056
    netsum = netsum + feature26 * -7.158862E-02
    netsum = netsum + feature27 * 0.1515599
    netsum = netsum + feature28 * 8.000591E-02
    netsum = netsum + feature29 * 4.851295E-02
    netsum = netsum + feature210 * 7.531486E-02
    netsum = netsum + feature211 * -0.5649268
    netsum = netsum + feature212 * -7.200994E-02
    netsum = netsum + feature213 * 0.5013899
    netsum = netsum + feature214 * -1.502891E-02
    netsum = netsum + feature215 * -1.327877E-02
    netsum = netsum + feature216 * -2.695415E-02
    netsum = netsum + feature217 * -5.812597E-02
    netsum = netsum + feature218 * -1.755004E-02
    netsum = netsum + feature219 * 2.453618E-02
    netsum = netsum + feature220 * -0.1503086
    outarray25 = 1 / (1 + math.exp(-netsum))
     
    netsum = 7.381488E-02
    netsum = netsum + feature21 * -0.1896643
    netsum = netsum + feature22 * 1.139046
    netsum = netsum + feature23 * -0.1679181
    netsum = netsum + feature24 * 0.1472248
    netsum = netsum + feature25 * 5.021053E-02
    netsum = netsum + feature26 * -0.40334
    netsum = netsum + feature27 * 6.380035E-02
    netsum = netsum + feature28 * -0.1144476
    netsum = netsum + feature29 * 0.2406472
    netsum = netsum + feature210 * -2.048679E-02
    netsum = netsum + feature211 * 8.447149E-02
    netsum = netsum + feature212 * -6.084381E-02
    netsum = netsum + feature213 * 3.673738E-03
    netsum = netsum + feature214 * -1.165766E-02
    netsum = netsum + feature215 * -6.838651E-03
    netsum = netsum + feature216 * 3.085905E-02
    netsum = netsum + feature217 * 7.368595E-02
    netsum = netsum + feature218 * -5.536998E-03
    netsum = netsum + feature219 * 5.521997E-03
    netsum = netsum + feature220 * -8.661441E-02
    outarray26 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.2186999
    netsum = netsum + feature21 * -0.1735915
    netsum = netsum + feature22 * 0.2196825
    netsum = netsum + feature23 * -3.351988E-02
    netsum = netsum + feature24 * 0.1259665
    netsum = netsum + feature25 * 2.386554E-02
    netsum = netsum + feature26 * -0.3742577
    netsum = netsum + feature27 * -0.1190041
    netsum = netsum + feature28 * -0.1311142
    netsum = netsum + feature29 * 0.2378967
    netsum = netsum + feature210 * -0.134159
    netsum = netsum + feature211 * 0.2794299
    netsum = netsum + feature212 * -6.242372E-02
    netsum = netsum + feature213 * -0.1792494
    netsum = netsum + feature214 * -4.739735E-02
    netsum = netsum + feature215 * -1.027228E-02
    netsum = netsum + feature216 * 6.931562E-02
    netsum = netsum + feature217 * 0.1035848
    netsum = netsum + feature218 * -1.291817E-02
    netsum = netsum + feature219 * -5.032325E-02
    netsum = netsum + feature220 * -5.656576E-02
    outarray27 = 1 / (1 + math.exp(-netsum))
     
    netsum = 7.764826E-02
    netsum = netsum + feature21 * 0.1093686
    netsum = netsum + feature22 * -0.3142678
    netsum = netsum + feature23 * -0.2236696
    netsum = netsum + feature24 * 0.1940019
    netsum = netsum + feature25 * 7.218265E-02
    netsum = netsum + feature26 * -5.904306E-02
    netsum = netsum + feature27 * 0.1261876
    netsum = netsum + feature28 * -0.1709496
    netsum = netsum + feature29 * 0.1729055
    netsum = netsum + feature210 * 0.1025779
    netsum = netsum + feature211 * -0.4121553
    netsum = netsum + feature212 * -7.452177E-02
    netsum = netsum + feature213 * 0.2114551
    netsum = netsum + feature214 * -6.377601E-02
    netsum = netsum + feature215 * -1.102662E-02
    netsum = netsum + feature216 * 3.759936E-02
    netsum = netsum + feature217 * 3.957795E-02
    netsum = netsum + feature218 * -1.822769E-02
    netsum = netsum + feature219 * -4.030802E-02
    netsum = netsum + feature220 * -0.114265
    outarray28 = 1 / (1 + math.exp(-netsum))
     
    netsum = 9.725799E-02
    netsum = netsum + feature21 * 7.757957E-02
    netsum = netsum + feature22 * 0.4571629
    netsum = netsum + feature23 * -0.3580945
    netsum = netsum + feature24 * 3.938904E-03
    netsum = netsum + feature25 * 8.634206E-02
    netsum = netsum + feature26 * -0.1302019
    netsum = netsum + feature27 * 0.1021544
    netsum = netsum + feature28 * 1.842203E-02
    netsum = netsum + feature29 * 3.725807E-02
    netsum = netsum + feature210 * 9.366755E-03
    netsum = netsum + feature211 * -0.2824594
    netsum = netsum + feature212 * -0.0670981
    netsum = netsum + feature213 * 0.3060683
    netsum = netsum + feature214 * -1.417599E-02
    netsum = netsum + feature215 * -8.951175E-03
    netsum = netsum + feature216 * -2.768059E-02
    netsum = netsum + feature217 * -6.313896E-02
    netsum = netsum + feature218 * -1.018785E-02
    netsum = netsum + feature219 * 3.972781E-02
    netsum = netsum + feature220 * -0.1242885
    outarray29 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.1516648
    netsum = netsum + feature21 * -8.909733E-02
    netsum = netsum + feature22 * 2.266368
    netsum = netsum + feature23 * -4.900719E-02
    netsum = netsum + feature24 * 0.1632882
    netsum = netsum + feature25 * 9.671763E-05
    netsum = netsum + feature26 * -0.4831223
    netsum = netsum + feature27 * 0.1418322
    netsum = netsum + feature28 * -0.1298564
    netsum = netsum + feature29 * 0.3292342
    netsum = netsum + feature210 * -5.728577E-02
    netsum = netsum + feature211 * 0.2211122
    netsum = netsum + feature212 * -6.064167E-02
    netsum = netsum + feature213 * -9.633538E-02
    netsum = netsum + feature214 * -5.607917E-03
    netsum = netsum + feature215 * -4.852026E-03
    netsum = netsum + feature216 * 0.1231913
    netsum = netsum + feature217 * 0.1461556
    netsum = netsum + feature218 * 9.603768E-05
    netsum = netsum + feature219 * -0.0745758
    netsum = netsum + feature220 * -3.632028E-02
    outarray30 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.15735
    netsum = netsum + feature21 * -0.1435484
    netsum = netsum + feature22 * 0.36606
    netsum = netsum + feature23 * -8.066627E-03
    netsum = netsum + feature24 * 0.1055407
    netsum = netsum + feature25 * 1.822122E-02
    netsum = netsum + feature26 * -0.3476865
    netsum = netsum + feature27 * -0.1084576
    netsum = netsum + feature28 * -0.1150629
    netsum = netsum + feature29 * 0.2361375
    netsum = netsum + feature210 * -0.1392767
    netsum = netsum + feature211 * 0.3230533
    netsum = netsum + feature212 * -6.027653E-02
    netsum = netsum + feature213 * -0.2001586
    netsum = netsum + feature214 * -0.0451511
    netsum = netsum + feature215 * -1.026765E-02
    netsum = netsum + feature216 * 6.419748E-02
    netsum = netsum + feature217 * 0.101221
    netsum = netsum + feature218 * -1.080079E-02
    netsum = netsum + feature219 * -4.717461E-02
    netsum = netsum + feature220 * -4.851091E-02
    outarray31 = 1 / (1 + math.exp(-netsum))
     
    netsum = 2.875041E-02
    netsum = netsum + feature21 * 0.1245188
    netsum = netsum + feature22 * -0.1816397
    netsum = netsum + feature23 * -0.1973075
    netsum = netsum + feature24 * 0.1375433
    netsum = netsum + feature25 * 5.061831E-02
    netsum = netsum + feature26 * -1.727108E-02
    netsum = netsum + feature27 * 0.077958
    netsum = netsum + feature28 * -0.1307696
    netsum = netsum + feature29 * 0.1166659
    netsum = netsum + feature210 * 6.703661E-02
    netsum = netsum + feature211 * -0.2718073
    netsum = netsum + feature212 * -7.070681E-02
    netsum = netsum + feature213 * 0.1740384
    netsum = netsum + feature214 * -5.652602E-02
    netsum = netsum + feature215 * -1.135072E-02
    netsum = netsum + feature216 * 3.169836E-02
    netsum = netsum + feature217 * 1.270081E-02
    netsum = netsum + feature218 * -1.224594E-02
    netsum = netsum + feature219 * -4.085485E-02
    netsum = netsum + feature220 * -8.657492E-02
    outarray32 = 1 / (1 + math.exp(-netsum))
     
     
    outarray1 = 300 *  (outarray1 - .1) / .8 
    if (outarray1<0):
        outarray1 = 0
    if (outarray1>300):
        outarray1 = 300
     
    outarray2 = 300 *  (outarray2 - .1) / .8 
    if (outarray2<0):
        outarray2 = 0
    if (outarray2>300):
        outarray2 = 300
     
    outarray3 = 300 *  (outarray3 - .1) / .8 
    if (outarray3<0):
        outarray3 = 0
    if (outarray3>300):
        outarray3 = 300
     
    outarray4 = 300 *  (outarray4 - .1) / .8 
    if (outarray4<0):
        outarray4 = 0
    if (outarray4>300):
        outarray4 = 300
     
    outarray5 = 300 *  (outarray5 - .1) / .8 
    if (outarray5<0):
        outarray5 = 0
    if (outarray5>300):
        outarray5 = 300
     
    outarray6 = 300 *  (outarray6 - .1) / .8 
    if (outarray6<0):
        outarray6 = 0
    if (outarray6>300):
        outarray6 = 300
     
    outarray7 = 300 *  (outarray7 - .1) / .8 
    if (outarray7<0):
        outarray7 = 0
    if (outarray7>300):
        outarray7 = 300
     
    outarray8 = 300 *  (outarray8 - .1) / .8 
    if (outarray8<0):
        outarray8 = 0
    if (outarray8>300):
        outarray8 = 300
     
    outarray9 = 100 *  (outarray9 - .1) / .8 
    if (outarray9<0):
        outarray9 = 0
    if (outarray9>100):
        outarray9 = 100
     
    outarray10 = 100 *  (outarray10 - .1) / .8 
    if (outarray10<0):
        outarray10 = 0
    if (outarray10>100):
        outarray10 = 100
     
    outarray11 = 100 *  (outarray11 - .1) / .8 
    if (outarray11<0):
        outarray11 = 0
    if (outarray11>100):
        outarray11 = 100
     
    outarray12 = 100 *  (outarray12 - .1) / .8 
    if (outarray12<0):
        outarray12 = 0
    if (outarray12>100):
        outarray12 = 100
     
    outarray13 = 100 *  (outarray13 - .1) / .8 
    if (outarray13<0):
        outarray13 = 0
    if (outarray13>100):
        outarray13 = 100
     
    outarray14 = 100 *  (outarray14 - .1) / .8 
    if (outarray14<0):
        outarray14 = 0
    if (outarray14>100):
        outarray14 = 100
     
    outarray15 = 100 *  (outarray15 - .1) / .8 
    if (outarray15<0):
        outarray15 = 0
    if (outarray15>100):
        outarray15 = 100
     
    outarray16 = 100 *  (outarray16 - .1) / .8 
    if (outarray16<0):
        outarray16 = 0
    if (outarray16>100):
        outarray16 = 100
     
    outarray17 = 400 *  (outarray17 - .1) / .8  + -200
    if (outarray17<-200):
        outarray17 = -200
    if (outarray17>200):
        outarray17 = 200
     
    outarray18 = 400 *  (outarray18 - .1) / .8  + -200
    if (outarray18<-200):
        outarray18 = -200
    if (outarray18>200):
        outarray18 = 200
     
    outarray19 = 400 *  (outarray19 - .1) / .8  + -200
    if (outarray19<-200):
        outarray19 = -200
    if (outarray19>200):
        outarray19 = 200
     
    outarray20 = 400 *  (outarray20 - .1) / .8  + -200
    if (outarray20<-200):
        outarray20 = -200
    if (outarray20>200):
        outarray20 = 200
     
    outarray21 = 400 *  (outarray21 - .1) / .8  + -200
    if (outarray21<-200):
        outarray21 = -200
    if (outarray21>200):
        outarray21 = 200
     
    outarray22 = 400 *  (outarray22 - .1) / .8  + -200
    if (outarray22<-200):
        outarray22 = -200
    if (outarray22>200):
        outarray22 = 200
     
    outarray23 = 400 *  (outarray23 - .1) / .8  + -200
    if (outarray23<-200):
        outarray23 = -200
    if (outarray23>200):
        outarray23 = 200
     
    outarray24 = 400 *  (outarray24 - .1) / .8  + -200
    if (outarray24<-200):
        outarray24 = -200
    if (outarray24>200):
        outarray24 = 200
     
    outarray25 = 400 *  (outarray25 - .1) / .8  + -200
    if (outarray25<-200):
        outarray25 = -200
    if (outarray25>200):
        outarray25 = 200
     
    outarray26 = 400 *  (outarray26 - .1) / .8  + -200
    if (outarray26<-200):
        outarray26 = -200
    if (outarray26>200):
        outarray26 = 200
     
    outarray27 = 400 *  (outarray27 - .1) / .8  + -200
    if (outarray27<-200):
        outarray27 = -200
    if (outarray27>200):
        outarray27 = 200
     
    outarray28 = 400 *  (outarray28 - .1) / .8  + -200
    if (outarray28<-200):
        outarray28 = -200
    if (outarray28>200):
        outarray28 = 200
     
    outarray29 = 400 *  (outarray29 - .1) / .8  + -200
    if (outarray29<-200):
        outarray29 = -200
    if (outarray29>200):
        outarray29 = 200
     
    outarray30 = 400 *  (outarray30 - .1) / .8  + -200
    if (outarray30<-200):
        outarray30 = -200
    if (outarray30>200):
        outarray30 = 200
     
    outarray31 = 400 *  (outarray31 - .1) / .8  + -200
    if (outarray31<-200):
        outarray31 = -200
    if (outarray31>200):
        outarray31 = 200
     
    outarray32 = 400 *  (outarray32 - .1) / .8  + -200
    if (outarray32<-200):
        outarray32 = -200
    if (outarray32>200):
        outarray32 = 200


    #'Осредняем силы по нитям и в общем

    #'Вертикальные силы

    #'средние значения
    Mean_Q_L = round(((abs(outarray1)+abs(outarray2)+abs(outarray5)+abs(outarray6))/4),1)
    Mean_Q_R = round(((abs(outarray3)+abs(outarray4)+abs(outarray7)+abs(outarray8))/4),1)
    Mean_Q = (Mean_Q_L+Mean_Q_R)/2

    #'СКО
    Rms_Q_L = round((((abs(outarray9)**2+abs(outarray10)**2+abs(outarray13)**2+abs(outarray14)**2)/4)**0.5),1)
    Rms_Q_R = round((((abs(outarray11)**2+abs(outarray12)**2+abs(outarray15)**2+abs(outarray16)**2)/4)**0.5),1)
    Rms_Q = round((((Rms_Q_L**2+Rms_Q_R**2)/2)**0.5),1)


    #'Боковые силы
    
    #'средние значения
    Mean_Y_L = round(((abs(outarray17)+abs(outarray18)+abs(outarray21)+abs(outarray22))/4),1)
    Mean_Y_R = round(((abs(outarray19)+abs(outarray20)+abs(outarray23)+abs(outarray24))/4),1)
    Mean_Y = (Mean_Y_L+Mean_Y_R)/2

    #'СКО
    Rms_Y_L = round((((abs(outarray25)**2+abs(outarray26)**2+abs(outarray29)**2+abs(outarray30)**2)/4)**0.5),1)
    Rms_Y_R = round((((abs(outarray27)**2+abs(outarray28)**2+abs(outarray31)**2+abs(outarray32)**2)/4)**0.5),1)
    Rms_Y = round((((Rms_Y_L**2+Rms_Y_R**2)/2)**0.5),1)

    print ("Значения сил, действующие в системе 'колесо-рельс'\nпри движении грузового локомотива и следующих условиях:")
    print ("Тип В.С.П. - ",VSP, "\nСостояние пути - ", MAINT, "\nРадиус кривой, м -", Rad)
    print ("Возвышение наружнего рельса, мм - ", H, "\nСкорость движения, км/ч - ", v)
    print ("Ширина колеи, мм - ", SHK, "\nКоэффициент трения в системе 'колесо-рельс' -", FTR)
    print ()
    print ("Средние значения вертикальных сил, кН:")
    print (outarray1, outarray2, outarray3, outarray4, outarray5,outarray6, outarray7, outarray8)
    print ()
    print ("СКО вертикальных сил, кН:")
    print (outarray9, outarray10, outarray11, outarray12, outarray13,outarray14, outarray15, outarray16)
    print ()
    print ("Cредние значения боковых сил, кН")
    print (outarray17, outarray18, outarray19, outarray20, outarray21,outarray22, outarray23, outarray24)
    print ()
    print ("СКО боковых сил, кН")
    print (outarray25, outarray26, outarray27, outarray28, outarray29,outarray30, outarray31, outarray32)
    print ()
    print ()

    print ("ИТОГОВЫЕ ЗНАЧЕНИЯ ВОЗДЕЙСТВИЯ:")
    print ()
    print ("Средние значения вертикальных сил `колесо-рельс` по левой нити, по правой нити, в среднем по экипажу кН:")
    print (Mean_Q_L, Mean_Q_R, Mean_Q)
    print ()
    print ("СКО значений вертикальных сил `колесо-рельс`по левой нити, по правой нити, в среднем по экипажу кН:")
    print (Rms_Q_L, Rms_Q_R, Rms_Q)
    print ()
    print ("Средние значения боковых сил `колесо-рельс` по левой нити, по правой нити, в среднем по экипажу кН:")
    print (Mean_Y_L, Mean_Y_R, Mean_Y)
    print ()
    print ("СКО значений боковых сил `колесо-рельс` по левой нити, по правой нити, в среднем по экипажу кН:")
    print (Rms_Y_L, Rms_Y_R, Rms_Y)
    print ()



    
    
print (GR_Loko_Force (1, 1, 250, 140, 80, 1520, 0.25))
 

