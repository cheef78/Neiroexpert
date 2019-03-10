def Pass_Loko_Force (VSP_type, Condition, Radius, h, V, Sh_Kol, mu_fr,Show_or_return = "return"):


    '''VSP_type это VSP_type - тип всп (1 - б.п., 2 - з.п.)
    ' Condition это Condition - состояние пути (1 - отличное или хорошее, 2 - удовлетворительное)
    ' Radius это R_m - радиус кривизны учатска, радиус кривизны прямого участка принимается 10000 м
    ' h это h_mm - возвышение наружнего рельса, мм
    ' V это V_km/h - скорость движения экипажа, км/ч
    ' Sh_Kol это S_mm - значение ширины колеи, мм
    ' mu_fr это ftr - коэффициент трения

     outarray - это переменные выходных значиний (средние значения и СКО сил)
     mean_ - это среднее значение силы, кН
     RMS - это СКО силы, кН
     F_vertical_ - это вертикальная сил
     F_side_- это боковая сила
     1,2,3,4 - номер оси в экипаже (в экипаже принято две тележки по две оси в каждой)
     r,l - правое или левое колесо 
    
      VSP_type это VSP_type
      Condition это Main_type
    ' Radius это R_m
    ' h это h_mm
    ' V это V_km/h
    ' Sh_Kol это S_mm
    ' mu_fr это f_tr
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
    if VSP_type == 1:
        VSP = "бесст.путь"
    if VSP_type == 2:
        VSP = "звен.путь"

    MAINT = Condition
    if Condition == 1:
        MAINT = "'отл' или 'хор'"
    if VSP_type == 2:
        MAINT = "'удовл' или 'неуд'"

    Rad = Radius
    H=h
    v = V
    SHK=Sh_Kol
    FTR=mu_fr
    
    if (VSP_type<1):
        VSP_type = 1
    if (VSP_type>2):
        VSP_type = 2
    VSP_type = (VSP_type - 1)
     
    if (Condition<1):
        Condition = 1
    if (Condition>2):
        Condition = 2
    Condition = (Condition - 1)
     
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
     
    if (mu_fr<0.1):
        mu_fr = 0.1
    if (mu_fr>0.7):
        mu_fr = 0.7
    mu_fr = (mu_fr - 0.1) / 0.6
     
    netsum = -4.399824
    netsum = netsum + VSP_type * -8.421461E-03
    netsum = netsum + Condition * -6.003976E-02
    netsum = netsum + Radius * -36.58384
    netsum = netsum + h * 0.9841207
    netsum = netsum + V * 8.133942
    netsum = netsum + Sh_Kol * 5.968282E-03
    netsum = netsum + mu_fr * -0.2689933
    feature21 = 1 / (1 + math.exp(-netsum))
     
    netsum = 5.876644
    netsum = netsum + VSP_type * 2.387288E-02
    netsum = netsum + Condition * 0.1938307
    netsum = netsum + Radius * 15.44494
    netsum = netsum + h * -0.4923574
    netsum = netsum + V * -5.428844
    netsum = netsum + Sh_Kol * -2.144211E-03
    netsum = netsum + mu_fr * -0.8770627
    feature22 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.417705
    netsum = netsum + VSP_type * -2.639777E-03
    netsum = netsum + Condition * 8.066922E-02
    netsum = netsum + Radius * -28.10228
    netsum = netsum + h * -1.930238
    netsum = netsum + V * 11.57652
    netsum = netsum + Sh_Kol * -4.571524E-03
    netsum = netsum + mu_fr * -0.5829382
    feature23 = 1 / (1 + math.exp(-netsum))
     
    netsum = 4.255926
    netsum = netsum + VSP_type * 0
    netsum = netsum + Condition * 3.078234E-02
    netsum = netsum + Radius * 16.59376
    netsum = netsum + h * -0.2063686
    netsum = netsum + V * 1.075123
    netsum = netsum + Sh_Kol * 3.612623E-03
    netsum = netsum + mu_fr * -3.690425
    feature24 = 1 / (1 + math.exp(-netsum))
     
    netsum = -6.820318
    netsum = netsum + VSP_type * 1.000814E-02
    netsum = netsum + Condition * 0.1531859
    netsum = netsum + Radius * 3.379727
    netsum = netsum + h * -0.6368344
    netsum = netsum + V * 6.969996
    netsum = netsum + Sh_Kol * -1.644494E-02
    netsum = netsum + mu_fr * 4.268582
    feature25 = 1 / (1 + math.exp(-netsum))
     
    netsum = 2.748068
    netsum = netsum + VSP_type * -7.012059E-04
    netsum = netsum + Condition * 8.168188E-02
    netsum = netsum + Radius * 43.24664
    netsum = netsum + h * -0.302209
    netsum = netsum + V * -0.1240798
    netsum = netsum + Sh_Kol * -1.228043E-02
    netsum = netsum + mu_fr * -0.5155895
    feature26 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.982459
    netsum = netsum + VSP_type * 1.048727E-02
    netsum = netsum + Condition * 0.1928615
    netsum = netsum + Radius * -2.172644
    netsum = netsum + h * -2.984248
    netsum = netsum + V * 11.41353
    netsum = netsum + Sh_Kol * 1.795072E-02
    netsum = netsum + mu_fr * -0.6201311
    feature27 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.7244495
    netsum = netsum + VSP_type * 6.526529E-03
    netsum = netsum + Condition * 0
    netsum = netsum + Radius * -15.51307
    netsum = netsum + h * -1.329901
    netsum = netsum + V * 4.596648
    netsum = netsum + Sh_Kol * -9.675853E-03
    netsum = netsum + mu_fr * -0.2908433
    feature28 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.527272
    netsum = netsum + VSP_type * -1.14131E-03
    netsum = netsum + Condition * -1.586122E-02
    netsum = netsum + Radius * 5.553072
    netsum = netsum + h * -0.2290776
    netsum = netsum + V * 0.2278899
    netsum = netsum + Sh_Kol * -3.74193E-05
    netsum = netsum + mu_fr * 1.606444
    feature29 = 1 / (1 + math.exp(-netsum))
     
    netsum = 10.38668
    netsum = netsum + VSP_type * 6.642137E-03
    netsum = netsum + Condition * 5.201337E-02
    netsum = netsum + Radius * 29.68453
    netsum = netsum + h * 0.8591279
    netsum = netsum + V * -5.903466
    netsum = netsum + Sh_Kol * -6.535445E-04
    netsum = netsum + mu_fr * -9.480639
    feature210 = 1 / (1 + math.exp(-netsum))
     
    netsum = 4.564594
    netsum = netsum + VSP_type * 8.741715E-03
    netsum = netsum + Condition * -1.049779
    netsum = netsum + Radius * -5.683813
    netsum = netsum + h * -1.365708E-03
    netsum = netsum + V * -3.166965
    netsum = netsum + Sh_Kol * 1.140852E-02
    netsum = netsum + mu_fr * -0.2450223
    feature211 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.364288
    netsum = netsum + VSP_type * -6.385207E-03
    netsum = netsum + Condition * -4.456714E-02
    netsum = netsum + Radius * -20.02233
    netsum = netsum + h * 1.368904
    netsum = netsum + V * -5.728657
    netsum = netsum + Sh_Kol * 9.340457E-03
    netsum = netsum + mu_fr * -0.9676338
    feature212 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.809991
    netsum = netsum + VSP_type * -5.797992E-03
    netsum = netsum + Condition * 8.978966E-03
    netsum = netsum + Radius * -36.9858
    netsum = netsum + h * -1.787823
    netsum = netsum + V * 12.48318
    netsum = netsum + Sh_Kol * -3.81182E-03
    netsum = netsum + mu_fr * -0.7054645
    feature213 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.2255
    netsum = netsum + VSP_type * 3.953746E-03
    netsum = netsum + Condition * 0.1375608
    netsum = netsum + Radius * -12.98343
    netsum = netsum + h * -2.04301
    netsum = netsum + V * 9.958959
    netsum = netsum + Sh_Kol * -6.818861E-03
    netsum = netsum + mu_fr * -0.8002809
    feature214 = 1 / (1 + math.exp(-netsum))
     
    netsum = 8.79877
    netsum = netsum + VSP_type * -1.251171E-02
    netsum = netsum + Condition * -0.2655413
    netsum = netsum + Radius * -0.4400688
    netsum = netsum + h * 0.7294995
    netsum = netsum + V * -10.10298
    netsum = netsum + Sh_Kol * 3.085028E-02
    netsum = netsum + mu_fr * -5.049299
    feature215 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.7205589
    netsum = netsum + VSP_type * 6.255635E-03
    netsum = netsum + Condition * -0.1206014
    netsum = netsum + Radius * -28.08602
    netsum = netsum + h * -0.9911858
    netsum = netsum + V * 4.70498
    netsum = netsum + Sh_Kol * -1.983241E-02
    netsum = netsum + mu_fr * -0.6274369
    feature216 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.184468
    netsum = netsum + VSP_type * -5.104376E-04
    netsum = netsum + Condition * -6.035355E-02
    netsum = netsum + Radius * -99.33578
    netsum = netsum + h * -0.3456707
    netsum = netsum + V * 6.201008
    netsum = netsum + Sh_Kol * 2.127516E-02
    netsum = netsum + mu_fr * -0.458614
    feature217 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.472584
    netsum = netsum + VSP_type * -1.15634E-03
    netsum = netsum + Condition * -4.195265E-02
    netsum = netsum + Radius * 2.727163
    netsum = netsum + h * 3.403845
    netsum = netsum + V * -1.914657
    netsum = netsum + Sh_Kol * 5.256728E-03
    netsum = netsum + mu_fr * 0.4802766
    feature218 = 1 / (1 + math.exp(-netsum))
     
    netsum = 3.064563
    netsum = netsum + VSP_type * -8.922429E-02
    netsum = netsum + Condition * -0.2255795
    netsum = netsum + Radius * 17.96725
    netsum = netsum + h * 9.27595
    netsum = netsum + V * -6.94011
    netsum = netsum + Sh_Kol * 3.528452E-02
    netsum = netsum + mu_fr * 8.889433
    feature219 = 1 / (1 + math.exp(-netsum))
     
    netsum = -5.476974
    netsum = netsum + VSP_type * -7.296799E-03
    netsum = netsum + Condition * -5.574956E-02
    netsum = netsum + Radius * -4.494357
    netsum = netsum + h * -0.0395846
    netsum = netsum + V * -2.586158
    netsum = netsum + Sh_Kol * -2.870427E-02
    netsum = netsum + mu_fr * 5.303144
    feature220 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.214907
    netsum = netsum + feature21 * 0.9701632
    netsum = netsum + feature22 * 2.554868
    netsum = netsum + feature23 * -1.605413
    netsum = netsum + feature24 * -0.9026138
    netsum = netsum + feature25 * 0.6506291
    netsum = netsum + feature26 * 1.794979
    netsum = netsum + feature27 * -0.3953449
    netsum = netsum + feature28 * -0.7547052
    netsum = netsum + feature29 * 0.0223656
    netsum = netsum + feature210 * -2.219437
    netsum = netsum + feature211 * 4.853564E-02
    netsum = netsum + feature212 * 0.1065363
    netsum = netsum + feature213 * 1.077453
    netsum = netsum + feature214 * 1.314612
    netsum = netsum + feature215 * 0.3715702
    netsum = netsum + feature216 * 0.3284607
    netsum = netsum + feature217 * 6.627041
    netsum = netsum + feature218 * -0.4554062
    netsum = netsum + feature219 * -3.184206
    netsum = netsum + feature220 * -0.2466228
    outarray1 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.18229
    netsum = netsum + feature21 * 0.9857931
    netsum = netsum + feature22 * 2.302466
    netsum = netsum + feature23 * -0.8477859
    netsum = netsum + feature24 * -1.185763
    netsum = netsum + feature25 * 0.672235
    netsum = netsum + feature26 * 2.660967
    netsum = netsum + feature27 * -0.2042729
    netsum = netsum + feature28 * -0.5548757
    netsum = netsum + feature29 * 7.781296E-02
    netsum = netsum + feature210 * -1.695829
    netsum = netsum + feature211 * 6.566267E-02
    netsum = netsum + feature212 * -0.5038962
    netsum = netsum + feature213 * 0.6737776
    netsum = netsum + feature214 * 0.7334791
    netsum = netsum + feature215 * 0.4228235
    netsum = netsum + feature216 * 0.1952594
    netsum = netsum + feature217 * 5.035399
    netsum = netsum + feature218 * -0.4248815
    netsum = netsum + feature219 * -2.736088
    netsum = netsum + feature220 * -0.546147
    outarray2 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.889747
    netsum = netsum + feature21 * -0.789923
    netsum = netsum + feature22 * -2.087697
    netsum = netsum + feature23 * 1.838951
    netsum = netsum + feature24 * 1.554415
    netsum = netsum + feature25 * -2.363184E-02
    netsum = netsum + feature26 * -3.18158
    netsum = netsum + feature27 * 0.4400989
    netsum = netsum + feature28 * 0.182323
    netsum = netsum + feature29 * -0.4346136
    netsum = netsum + feature210 * 2.801889
    netsum = netsum + feature211 * -0.0450477
    netsum = netsum + feature212 * -1.140116
    netsum = netsum + feature213 * -1.07929
    netsum = netsum + feature214 * -1.489269
    netsum = netsum + feature215 * 9.383244E-03
    netsum = netsum + feature216 * -0.167304
    netsum = netsum + feature217 * -7.838731
    netsum = netsum + feature218 * 0.3847348
    netsum = netsum + feature219 * 3.389106
    netsum = netsum + feature220 * 0.9608193
    outarray3 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.1328585
    netsum = netsum + feature21 * -0.9566767
    netsum = netsum + feature22 * -2.795783
    netsum = netsum + feature23 * 2.159431
    netsum = netsum + feature24 * 3.007757
    netsum = netsum + feature25 * -4.853626E-02
    netsum = netsum + feature26 * -6.940655
    netsum = netsum + feature27 * 0.4430073
    netsum = netsum + feature28 * 0.5851393
    netsum = netsum + feature29 * -1.005916
    netsum = netsum + feature210 * 2.597586
    netsum = netsum + feature211 * -3.392866E-02
    netsum = netsum + feature212 * -1.90226
    netsum = netsum + feature213 * -1.306288
    netsum = netsum + feature214 * -1.709862
    netsum = netsum + feature215 * -0.0489491
    netsum = netsum + feature216 * -0.4336225
    netsum = netsum + feature217 * -10.05938
    netsum = netsum + feature218 * 0.3635313
    netsum = netsum + feature219 * 3.764516
    netsum = netsum + feature220 * 2.124238
    outarray4 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.64088
    netsum = netsum + feature21 * 0.9831491
    netsum = netsum + feature22 * 2.422321
    netsum = netsum + feature23 * -0.8869064
    netsum = netsum + feature24 * -0.3832487
    netsum = netsum + feature25 * 0.6786606
    netsum = netsum + feature26 * 0.1054543
    netsum = netsum + feature27 * -0.2550053
    netsum = netsum + feature28 * -0.3013716
    netsum = netsum + feature29 * -0.2930909
    netsum = netsum + feature210 * -1.917434
    netsum = netsum + feature211 * 6.807405E-02
    netsum = netsum + feature212 * -0.5507972
    netsum = netsum + feature213 * 0.6735364
    netsum = netsum + feature214 * 0.7466117
    netsum = netsum + feature215 * 0.3822145
    netsum = netsum + feature216 * 3.346252E-02
    netsum = netsum + feature217 * 3.942582
    netsum = netsum + feature218 * -0.4274316
    netsum = netsum + feature219 * -2.586155
    netsum = netsum + feature220 * 8.357861E-02
    outarray5 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.052832
    netsum = netsum + feature21 * 1.030469
    netsum = netsum + feature22 * 2.658787
    netsum = netsum + feature23 * -1.601664
    netsum = netsum + feature24 * -1.89358
    netsum = netsum + feature25 * 0.6480421
    netsum = netsum + feature26 * 4.596121
    netsum = netsum + feature27 * -0.3476208
    netsum = netsum + feature28 * -0.9610953
    netsum = netsum + feature29 * 0.4246893
    netsum = netsum + feature210 * -1.908165
    netsum = netsum + feature211 * 3.196063E-02
    netsum = netsum + feature212 * 0.3039394
    netsum = netsum + feature213 * 1.104664
    netsum = netsum + feature214 * 1.301544
    netsum = netsum + feature215 * 0.4145338
    netsum = netsum + feature216 * 0.4762146
    netsum = netsum + feature217 * 7.716951
    netsum = netsum + feature218 * -0.4303159
    netsum = netsum + feature219 * -3.264538
    netsum = netsum + feature220 * -1.049692
    outarray6 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.170806
    netsum = netsum + feature21 * -0.9113134
    netsum = netsum + feature22 * -2.717563
    netsum = netsum + feature23 * 2.30124
    netsum = netsum + feature24 * 2.038126
    netsum = netsum + feature25 * -5.342729E-02
    netsum = netsum + feature26 * -4.350987
    netsum = netsum + feature27 * 0.5206284
    netsum = netsum + feature28 * 0.3332818
    netsum = netsum + feature29 * -0.5293632
    netsum = netsum + feature210 * 3.133163
    netsum = netsum + feature211 * -3.563235E-02
    netsum = netsum + feature212 * -1.544229
    netsum = netsum + feature213 * -1.368929
    netsum = netsum + feature214 * -1.797953
    netsum = netsum + feature215 * 0
    netsum = netsum + feature216 * -0.2496859
    netsum = netsum + feature217 * -9.668394
    netsum = netsum + feature218 * 0.3774118
    netsum = netsum + feature219 * 3.676973
    netsum = netsum + feature220 * 1.233369
    outarray7 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.3747839
    netsum = netsum + feature21 * -0.8687637
    netsum = netsum + feature22 * -2.20308
    netsum = netsum + feature23 * 1.833363
    netsum = netsum + feature24 * 2.737065
    netsum = netsum + feature25 * -8.970472E-03
    netsum = netsum + feature26 * -6.179757
    netsum = netsum + feature27 * 0.3896833
    netsum = netsum + feature28 * 0.4338799
    netsum = netsum + feature29 * -0.9254011
    netsum = netsum + feature210 * 2.287826
    netsum = netsum + feature211 * -2.661863E-02
    netsum = netsum + feature212 * -1.593892
    netsum = netsum + feature213 * -1.097353
    netsum = netsum + feature214 * -1.487959
    netsum = netsum + feature215 * -2.871538E-02
    netsum = netsum + feature216 * -0.3550588
    netsum = netsum + feature217 * -8.726959
    netsum = netsum + feature218 * 0.3583307
    netsum = netsum + feature219 * 3.455828
    netsum = netsum + feature220 * 1.963173
    outarray8 = 1 / (1 + math.exp(-netsum))
     
    netsum = 2.131773
    netsum = netsum + feature21 * 0.1113874
    netsum = netsum + feature22 * -1.035907
    netsum = netsum + feature23 * 0.8487952
    netsum = netsum + feature24 * 0.0840218
    netsum = netsum + feature25 * -8.390561E-02
    netsum = netsum + feature26 * -1.201442
    netsum = netsum + feature27 * 0.5234043
    netsum = netsum + feature28 * 2.542347
    netsum = netsum + feature29 * -0.9761902
    netsum = netsum + feature210 * -1.519097
    netsum = netsum + feature211 * -1.132308
    netsum = netsum + feature212 * -0.7181947
    netsum = netsum + feature213 * -8.587395E-02
    netsum = netsum + feature214 * -1.392287
    netsum = netsum + feature215 * 0.1544502
    netsum = netsum + feature216 * -1.432032
    netsum = netsum + feature217 * 4.566871
    netsum = netsum + feature218 * 0.3314081
    netsum = netsum + feature219 * 0.5636055
    netsum = netsum + feature220 * 0.4310336
    outarray9 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.3242154
    netsum = netsum + feature21 * -0.430834
    netsum = netsum + feature22 * -0.8125665
    netsum = netsum + feature23 * 5.255017
    netsum = netsum + feature24 * -0.3353245
    netsum = netsum + feature25 * -2.360319
    netsum = netsum + feature26 * 0.8685439
    netsum = netsum + feature27 * 1.231603
    netsum = netsum + feature28 * 2.243823
    netsum = netsum + feature29 * 0.672294
    netsum = netsum + feature210 * -1.267209
    netsum = netsum + feature211 * -0.9878788
    netsum = netsum + feature212 * 2.679705
    netsum = netsum + feature213 * -3.471102
    netsum = netsum + feature214 * -3.140501
    netsum = netsum + feature215 * -1.472071
    netsum = netsum + feature216 * -0.5073316
    netsum = netsum + feature217 * 3.855181
    netsum = netsum + feature218 * 0.7349238
    netsum = netsum + feature219 * 1.170056
    netsum = netsum + feature220 * -0.9634658
    outarray10 = 1 / (1 + math.exp(-netsum))
     
    netsum = 3.220939
    netsum = netsum + feature21 * 0.1490366
    netsum = netsum + feature22 * -7.069509E-02
    netsum = netsum + feature23 * 0.6574219
    netsum = netsum + feature24 * -0.3909164
    netsum = netsum + feature25 * -0.4784757
    netsum = netsum + feature26 * -1.124184
    netsum = netsum + feature27 * 0.3287588
    netsum = netsum + feature28 * 3.33724
    netsum = netsum + feature29 * -1.041465
    netsum = netsum + feature210 * -1.724931
    netsum = netsum + feature211 * -1.355857
    netsum = netsum + feature212 * 0.3254792
    netsum = netsum + feature213 * -0.1091154
    netsum = netsum + feature214 * -1.207108
    netsum = netsum + feature215 * -0.235543
    netsum = netsum + feature216 * -1.821746
    netsum = netsum + feature217 * 2.849382
    netsum = netsum + feature218 * 0.3809979
    netsum = netsum + feature219 * -0.3169079
    netsum = netsum + feature220 * 0.1240838
    outarray11 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.0750581
    netsum = netsum + feature21 * -0.2074408
    netsum = netsum + feature22 * 0.8530763
    netsum = netsum + feature23 * 3.9914
    netsum = netsum + feature24 * -0.8760316
    netsum = netsum + feature25 * -2.238883
    netsum = netsum + feature26 * 2.002029
    netsum = netsum + feature27 * 1.002055
    netsum = netsum + feature28 * 2.040346
    netsum = netsum + feature29 * 0.3514432
    netsum = netsum + feature210 * -1.753898
    netsum = netsum + feature211 * -0.8969672
    netsum = netsum + feature212 * 2.549271
    netsum = netsum + feature213 * -2.685726
    netsum = netsum + feature214 * -2.325174
    netsum = netsum + feature215 * -1.587657
    netsum = netsum + feature216 * -0.5625331
    netsum = netsum + feature217 * 5.755742
    netsum = netsum + feature218 * 0.6452243
    netsum = netsum + feature219 * -5.195556E-02
    netsum = netsum + feature220 * -0.7038508
    outarray12 = 1 / (1 + math.exp(-netsum))
     
    netsum = 2.699453
    netsum = netsum + feature21 * -4.035787E-02
    netsum = netsum + feature22 * -1.553602
    netsum = netsum + feature23 * 2.344961
    netsum = netsum + feature24 * -7.755552E-02
    netsum = netsum + feature25 * -0.2069722
    netsum = netsum + feature26 * -2.325072
    netsum = netsum + feature27 * 0.8151368
    netsum = netsum + feature28 * 3.742217
    netsum = netsum + feature29 * -1.288833
    netsum = netsum + feature210 * -1.204214
    netsum = netsum + feature211 * -0.9897541
    netsum = netsum + feature212 * 0.8019289
    netsum = netsum + feature213 * -0.9032007
    netsum = netsum + feature214 * -2.543208
    netsum = netsum + feature215 * 0.1642724
    netsum = netsum + feature216 * -2.187467
    netsum = netsum + feature217 * 1.136329
    netsum = netsum + feature218 * 0.4724701
    netsum = netsum + feature219 * 1.324739
    netsum = netsum + feature220 * 4.219953E-02
    outarray13 = 1 / (1 + math.exp(-netsum))
     
    netsum = -5.174844E-02
    netsum = netsum + feature21 * -0.5971338
    netsum = netsum + feature22 * -0.8719507
    netsum = netsum + feature23 * 5.331323
    netsum = netsum + feature24 * -0.3907647
    netsum = netsum + feature25 * -2.531186
    netsum = netsum + feature26 * 2.583217
    netsum = netsum + feature27 * 1.253725
    netsum = netsum + feature28 * 1.953731
    netsum = netsum + feature29 * 0.9237798
    netsum = netsum + feature210 * -1.470369
    netsum = netsum + feature211 * -1.106762
    netsum = netsum + feature212 * 2.444174
    netsum = netsum + feature213 * -3.549794
    netsum = netsum + feature214 * -3.128538
    netsum = netsum + feature215 * -1.561182
    netsum = netsum + feature216 * -0.230767
    netsum = netsum + feature217 * 6.844418
    netsum = netsum + feature218 * 0.7761041
    netsum = netsum + feature219 * 0.2972487
    netsum = netsum + feature220 * -0.8988873
    outarray14 = 1 / (1 + math.exp(-netsum))
     
    netsum = 2.058028
    netsum = netsum + feature21 * 0.2184822
    netsum = netsum + feature22 * 1.234137
    netsum = netsum + feature23 * 1.423834
    netsum = netsum + feature24 * 0.2537328
    netsum = netsum + feature25 * -0.314253
    netsum = netsum + feature26 * -2.283062
    netsum = netsum + feature27 * 0.5854583
    netsum = netsum + feature28 * 3.562906
    netsum = netsum + feature29 * -1.272292
    netsum = netsum + feature210 * -2.158642
    netsum = netsum + feature211 * -1.016705
    netsum = netsum + feature212 * 0.1096286
    netsum = netsum + feature213 * -0.4710995
    netsum = netsum + feature214 * -1.775958
    netsum = netsum + feature215 * -0.1035952
    netsum = netsum + feature216 * -2.044654
    netsum = netsum + feature217 * 2.523726
    netsum = netsum + feature218 * 0.4620088
    netsum = netsum + feature219 * 5.486645E-02
    netsum = netsum + feature220 * 0.4835989
    outarray15 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.60348
    netsum = netsum + feature21 * -0.6717474
    netsum = netsum + feature22 * -0.1612618
    netsum = netsum + feature23 * 3.734934
    netsum = netsum + feature24 * -0.6048808
    netsum = netsum + feature25 * -2.733376
    netsum = netsum + feature26 * 2.101995
    netsum = netsum + feature27 * 0.7734269
    netsum = netsum + feature28 * 2.053403
    netsum = netsum + feature29 * 0.9281321
    netsum = netsum + feature210 * -2.147626
    netsum = netsum + feature211 * -1.076773
    netsum = netsum + feature212 * 2.598273
    netsum = netsum + feature213 * -2.816293
    netsum = netsum + feature214 * -1.77559
    netsum = netsum + feature215 * -1.857908
    netsum = netsum + feature216 * -0.3030864
    netsum = netsum + feature217 * 5.582402
    netsum = netsum + feature218 * 0.7969322
    netsum = netsum + feature219 * -0.4472463
    netsum = netsum + feature220 * -1.112702
    outarray16 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.713398
    netsum = netsum + feature21 * -0.3449662
    netsum = netsum + feature22 * -0.9386657
    netsum = netsum + feature23 * 4.385157E-03
    netsum = netsum + feature24 * 2.463789
    netsum = netsum + feature25 * -9.081337E-02
    netsum = netsum + feature26 * 1.364946
    netsum = netsum + feature27 * -1.436204E-02
    netsum = netsum + feature28 * -0.3473454
    netsum = netsum + feature29 * 0.7922854
    netsum = netsum + feature210 * 0.2394955
    netsum = netsum + feature211 * -3.358314E-02
    netsum = netsum + feature212 * 0.5646229
    netsum = netsum + feature213 * -0.0401766
    netsum = netsum + feature214 * 6.647743E-02
    netsum = netsum + feature215 * -1.953136E-02
    netsum = netsum + feature216 * 0.1571028
    netsum = netsum + feature217 * -0.8801696
    netsum = netsum + feature218 * 0.1093875
    netsum = netsum + feature219 * 0.3384621
    netsum = netsum + feature220 * 0.1515738
    outarray17 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.5280895
    netsum = netsum + feature21 * -0.2727568
    netsum = netsum + feature22 * -0.5198998
    netsum = netsum + feature23 * -0.1237645
    netsum = netsum + feature24 * 0.7626938
    netsum = netsum + feature25 * 0.3157772
    netsum = netsum + feature26 * -2.286403
    netsum = netsum + feature27 * -5.511641E-02
    netsum = netsum + feature28 * -8.500471E-02
    netsum = netsum + feature29 * -0.6982858
    netsum = netsum + feature210 * 0.6968975
    netsum = netsum + feature211 * 3.757744E-02
    netsum = netsum + feature212 * -1.106117
    netsum = netsum + feature213 * 0.1247723
    netsum = netsum + feature214 * -1.605147E-03
    netsum = netsum + feature215 * 0.149914
    netsum = netsum + feature216 * -0.1349418
    netsum = netsum + feature217 * -2.905812
    netsum = netsum + feature218 * 3.999193E-02
    netsum = netsum + feature219 * 0.7633122
    netsum = netsum + feature220 * 1.016439
    outarray18 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.881728
    netsum = netsum + feature21 * -0.1245932
    netsum = netsum + feature22 * -0.1490183
    netsum = netsum + feature23 * 0.1709654
    netsum = netsum + feature24 * -2.6916
    netsum = netsum + feature25 * -0.1374225
    netsum = netsum + feature26 * -9.371838E-02
    netsum = netsum + feature27 * 5.081445E-02
    netsum = netsum + feature28 * 0.2615183
    netsum = netsum + feature29 * -0.5697606
    netsum = netsum + feature210 * 0.7392634
    netsum = netsum + feature211 * 1.438955E-02
    netsum = netsum + feature212 * -8.862757E-02
    netsum = netsum + feature213 * -0.1331514
    netsum = netsum + feature214 * -0.1886609
    netsum = netsum + feature215 * -0.1109539
    netsum = netsum + feature216 * -0.1050948
    netsum = netsum + feature217 * -1.204216
    netsum = netsum + feature218 * 9.746586E-02
    netsum = netsum + feature219 * 0.6201037
    netsum = netsum + feature220 * -0.3283762
    outarray19 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.1717943
    netsum = netsum + feature21 * -0.206619
    netsum = netsum + feature22 * -0.3530101
    netsum = netsum + feature23 * -0.2024323
    netsum = netsum + feature24 * -7.474324E-02
    netsum = netsum + feature25 * -0.4959225
    netsum = netsum + feature26 * 0.4068283
    netsum = netsum + feature27 * -7.912831E-02
    netsum = netsum + feature28 * 0.177101
    netsum = netsum + feature29 * 0.3519543
    netsum = netsum + feature210 * -5.815904E-02
    netsum = netsum + feature211 * -6.001821E-02
    netsum = netsum + feature212 * 1.361021
    netsum = netsum + feature213 * -4.317081E-02
    netsum = netsum + feature214 * 0.2280004
    netsum = netsum + feature215 * -0.3296741
    netsum = netsum + feature216 * 4.724391E-02
    netsum = netsum + feature217 * 0.3407435
    netsum = netsum + feature218 * 0.1384533
    netsum = netsum + feature219 * 0.2059606
    netsum = netsum + feature220 * -0.3577614
    outarray20 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.124686
    netsum = netsum + feature21 * -0.3591851
    netsum = netsum + feature22 * -0.8254718
    netsum = netsum + feature23 * -0.4733379
    netsum = netsum + feature24 * 2.164232
    netsum = netsum + feature25 * -0.1393942
    netsum = netsum + feature26 * 2.403106
    netsum = netsum + feature27 * -0.1249425
    netsum = netsum + feature28 * -0.6160182
    netsum = netsum + feature29 * 1.009049
    netsum = netsum + feature210 * 6.105699E-02
    netsum = netsum + feature211 * -5.465844E-02
    netsum = netsum + feature212 * 1.010288
    netsum = netsum + feature213 * 0.2039109
    netsum = netsum + feature214 * 0.4683982
    netsum = netsum + feature215 * -5.484242E-02
    netsum = netsum + feature216 * 0.3470507
    netsum = netsum + feature217 * 0.6749989
    netsum = netsum + feature218 * 0.0957082
    netsum = netsum + feature219 * 9.481318E-02
    netsum = netsum + feature220 * -7.125432E-02
    outarray21 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.9230731
    netsum = netsum + feature21 * -0.2637001
    netsum = netsum + feature22 * -0.5740978
    netsum = netsum + feature23 * 0.1965144
    netsum = netsum + feature24 * 1.140229
    netsum = netsum + feature25 * 0.3791329
    netsum = netsum + feature26 * -3.315211
    netsum = netsum + feature27 * 1.270986E-02
    netsum = netsum + feature28 * 8.525315E-02
    netsum = netsum + feature29 * -0.8802038
    netsum = netsum + feature210 * 0.7755836
    netsum = netsum + feature211 * 5.543155E-02
    netsum = netsum + feature212 * -1.475451
    netsum = netsum + feature213 * -3.981964E-02
    netsum = netsum + feature214 * -0.2615797
    netsum = netsum + feature215 * 0.1896009
    netsum = netsum + feature216 * -0.2685308
    netsum = netsum + feature217 * -4.215075
    netsum = netsum + feature218 * 5.241763E-02
    netsum = netsum + feature219 * 0.9721654
    netsum = netsum + feature220 * 1.264728
    outarray22 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.899448
    netsum = netsum + feature21 * -0.1576641
    netsum = netsum + feature22 * -0.3491668
    netsum = netsum + feature23 * 0.2232863
    netsum = netsum + feature24 * -2.708677
    netsum = netsum + feature25 * -0.1714202
    netsum = netsum + feature26 * -0.1177996
    netsum = netsum + feature27 * 6.332735E-02
    netsum = netsum + feature28 * 0.2960454
    netsum = netsum + feature29 * -0.5495383
    netsum = netsum + feature210 * 0.8891937
    netsum = netsum + feature211 * 1.303738E-02
    netsum = netsum + feature212 * -7.168726E-02
    netsum = netsum + feature213 * -0.1722966
    netsum = netsum + feature214 * -0.2288811
    netsum = netsum + feature215 * -0.1278474
    netsum = netsum + feature216 * -0.1101377
    netsum = netsum + feature217 * -1.377501
    netsum = netsum + feature218 * 9.923632E-02
    netsum = netsum + feature219 * 0.7061671
    netsum = netsum + feature220 * -0.3308889
    outarray23 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.2727819
    netsum = netsum + feature21 * -0.2129447
    netsum = netsum + feature22 * -0.4198191
    netsum = netsum + feature23 * -0.1124256
    netsum = netsum + feature24 * -5.611598E-02
    netsum = netsum + feature25 * -0.4808321
    netsum = netsum + feature26 * 0.3482942
    netsum = netsum + feature27 * -4.874863E-02
    netsum = netsum + feature28 * 0.2265874
    netsum = netsum + feature29 * 0.2968339
    netsum = netsum + feature210 * -8.381478E-02
    netsum = netsum + feature211 * -5.442635E-02
    netsum = netsum + feature212 * 1.280435
    netsum = netsum + feature213 * -8.107089E-02
    netsum = netsum + feature214 * 0.1385736
    netsum = netsum + feature215 * -0.3140669
    netsum = netsum + feature216 * 4.833196E-03
    netsum = netsum + feature217 * 0.2398904
    netsum = netsum + feature218 * 0.144496
    netsum = netsum + feature219 * 0.2252898
    netsum = netsum + feature220 * -0.3280458
    outarray24 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.9561185
    netsum = netsum + feature21 * 5.643389E-02
    netsum = netsum + feature22 * 1.311424E-02
    netsum = netsum + feature23 * 0.1050141
    netsum = netsum + feature24 * -0.9383996
    netsum = netsum + feature25 * 1.557956E-02
    netsum = netsum + feature26 * 0.1084214
    netsum = netsum + feature27 * 2.551049E-02
    netsum = netsum + feature28 * 0.1207508
    netsum = netsum + feature29 * -4.228933E-02
    netsum = netsum + feature210 * 0.0598174
    netsum = netsum + feature211 * -0.1788934
    netsum = netsum + feature212 * -0.3051096
    netsum = netsum + feature213 * -5.819912E-02
    netsum = netsum + feature214 * -7.883332E-02
    netsum = netsum + feature215 * 4.639875E-02
    netsum = netsum + feature216 * -2.454935E-02
    netsum = netsum + feature217 * 0.221978
    netsum = netsum + feature218 * 2.124953E-04
    netsum = netsum + feature219 * -2.659701E-02
    netsum = netsum + feature220 * -0.2214358
    outarray25 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.2043008
    netsum = netsum + feature21 * 0.1548928
    netsum = netsum + feature22 * 1.087787
    netsum = netsum + feature23 * 0.2209619
    netsum = netsum + feature24 * 0.2009463
    netsum = netsum + feature25 * -0.2894838
    netsum = netsum + feature26 * 0.2034562
    netsum = netsum + feature27 * 2.239406E-02
    netsum = netsum + feature28 * 5.468767E-02
    netsum = netsum + feature29 * 9.380258E-02
    netsum = netsum + feature210 * -0.8539852
    netsum = netsum + feature211 * -0.1066345
    netsum = netsum + feature212 * -2.222476E-02
    netsum = netsum + feature213 * -0.2418805
    netsum = netsum + feature214 * 0.0332777
    netsum = netsum + feature215 * -0.2526767
    netsum = netsum + feature216 * 6.866442E-02
    netsum = netsum + feature217 * 0.6561565
    netsum = netsum + feature218 * 4.952797E-02
    netsum = netsum + feature219 * -0.118761
    netsum = netsum + feature220 * 0.1701344
    outarray26 = 1 / (1 + math.exp(-netsum))
     
    netsum = 2.975165E-03
    netsum = netsum + feature21 * -2.616548E-02
    netsum = netsum + feature22 * -2.678742E-02
    netsum = netsum + feature23 * -7.569569E-02
    netsum = netsum + feature24 * -1.16722
    netsum = netsum + feature25 * -0.1477974
    netsum = netsum + feature26 * 1.119462
    netsum = netsum + feature27 * -3.238937E-03
    netsum = netsum + feature28 * -9.188506E-03
    netsum = netsum + feature29 * 5.692618E-02
    netsum = netsum + feature210 * 0.2311727
    netsum = netsum + feature211 * -8.374769E-02
    netsum = netsum + feature212 * 0.2107114
    netsum = netsum + feature213 * 2.776761E-02
    netsum = netsum + feature214 * 3.371947E-02
    netsum = netsum + feature215 * -0.1172551
    netsum = netsum + feature216 * 4.149972E-02
    netsum = netsum + feature217 * 0.4391184
    netsum = netsum + feature218 * 2.156231E-02
    netsum = netsum + feature219 * 5.690441E-02
    netsum = netsum + feature220 * -0.2054468
    outarray27 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.1210271
    netsum = netsum + feature21 * -5.361257E-02
    netsum = netsum + feature22 * -0.1032785
    netsum = netsum + feature23 * 0.3310735
    netsum = netsum + feature24 * 0.147695
    netsum = netsum + feature25 * -2.313928E-02
    netsum = netsum + feature26 * -0.2320115
    netsum = netsum + feature27 * 6.470607E-02
    netsum = netsum + feature28 * 3.291428E-03
    netsum = netsum + feature29 * 2.205948E-02
    netsum = netsum + feature210 * 6.353044E-03
    netsum = netsum + feature211 * -7.682836E-02
    netsum = netsum + feature212 * 0.2660031
    netsum = netsum + feature213 * -0.2134088
    netsum = netsum + feature214 * -0.158905
    netsum = netsum + feature215 * -6.4864E-04
    netsum = netsum + feature216 * 2.700625E-02
    netsum = netsum + feature217 * -0.2260381
    netsum = netsum + feature218 * 4.049694E-02
    netsum = netsum + feature219 * 0.1203673
    netsum = netsum + feature220 * 2.024688E-02
    outarray28 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.8561659
    netsum = netsum + feature21 * 7.054358E-02
    netsum = netsum + feature22 * 1.625662E-02
    netsum = netsum + feature23 * 0.257961
    netsum = netsum + feature24 * -0.7945991
    netsum = netsum + feature25 * 6.607351E-02
    netsum = netsum + feature26 * -9.884433E-02
    netsum = netsum + feature27 * 0.0633121
    netsum = netsum + feature28 * 0.2104229
    netsum = netsum + feature29 * -0.1091533
    netsum = netsum + feature210 * 0.1129333
    netsum = netsum + feature211 * -0.1663424
    netsum = netsum + feature212 * -0.3858828
    netsum = netsum + feature213 * -0.1265117
    netsum = netsum + feature214 * -0.2259089
    netsum = netsum + feature215 * 8.820117E-02
    netsum = netsum + feature216 * -9.162002E-02
    netsum = netsum + feature217 * -0.3373766
    netsum = netsum + feature218 * 6.077099E-03
    netsum = netsum + feature219 * 3.719441E-02
    netsum = netsum + feature220 * -0.1373222
    outarray29 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.0182366
    netsum = netsum + feature21 * 0.1106367
    netsum = netsum + feature22 * 0.7161305
    netsum = netsum + feature23 * 0.1764939
    netsum = netsum + feature24 * 0.1770313
    netsum = netsum + feature25 * -0.2767954
    netsum = netsum + feature26 * 0.5438246
    netsum = netsum + feature27 * 1.869817E-02
    netsum = netsum + feature28 * -0.0267003
    netsum = netsum + feature29 * 0.1405011
    netsum = netsum + feature210 * -0.9160395
    netsum = netsum + feature211 * -0.1200034
    netsum = netsum + feature212 * 0.1344787
    netsum = netsum + feature213 * -0.2063428
    netsum = netsum + feature214 * 6.711944E-02
    netsum = netsum + feature215 * -0.217222
    netsum = netsum + feature216 * 0.1141628
    netsum = netsum + feature217 * 1.064439
    netsum = netsum + feature218 * 4.075497E-02
    netsum = netsum + feature219 * -0.2171953
    netsum = netsum + feature220 * 0.1603314
    outarray30 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.2526602
    netsum = netsum + feature21 * -2.557387E-02
    netsum = netsum + feature22 * 4.260203E-02
    netsum = netsum + feature23 * -1.831516E-03
    netsum = netsum + feature24 * -1.085573
    netsum = netsum + feature25 * -0.1458715
    netsum = netsum + feature26 * 1.171946
    netsum = netsum + feature27 * 1.073408E-02
    netsum = netsum + feature28 * -1.200739E-02
    netsum = netsum + feature29 * 7.265049E-02
    netsum = netsum + feature210 * 0.231932
    netsum = netsum + feature211 * -8.793658E-02
    netsum = netsum + feature212 * 0.1887155
    netsum = netsum + feature213 * -1.864098E-02
    netsum = netsum + feature214 * -7.724665E-03
    netsum = netsum + feature215 * -0.1148307
    netsum = netsum + feature216 * 5.258105E-02
    netsum = netsum + feature217 * 0.4907646
    netsum = netsum + feature218 * 2.339019E-02
    netsum = netsum + feature219 * 0.1038444
    netsum = netsum + feature220 * -0.1635011
    outarray31 = 1 / (1 + math.exp(-netsum))
     
    netsum = 6.811743E-02
    netsum = netsum + feature21 * -6.134878E-02
    netsum = netsum + feature22 * -0.1705747
    netsum = netsum + feature23 * 0.3289589
    netsum = netsum + feature24 * 0.1259168
    netsum = netsum + feature25 * -6.125182E-03
    netsum = netsum + feature26 * -0.164368
    netsum = netsum + feature27 * 7.051468E-02
    netsum = netsum + feature28 * 5.375671E-03
    netsum = netsum + feature29 * 1.476823E-02
    netsum = netsum + feature210 * 0.038884
    netsum = netsum + feature211 * -7.986647E-02
    netsum = netsum + feature212 * 0.2448045
    netsum = netsum + feature213 * -0.2038485
    netsum = netsum + feature214 * -0.1711724
    netsum = netsum + feature215 * 1.768962E-02
    netsum = netsum + feature216 * 2.235656E-02
    netsum = netsum + feature217 * -0.1698456
    netsum = netsum + feature218 * 3.997931E-02
    netsum = netsum + feature219 * 0.1480037
    netsum = netsum + feature220 * 1.178844E-02
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
    if (outarray32 < -200):
        outarray32 = -200
    if (outarray32 > 200):
        outarray32 = 200

     #'Осредняем силы по нитям и в общем

    #'Вертикальные силы

    #'средние значения
    Mean_F_vertical_L = round(((abs(outarray1)+abs(outarray2)+abs(outarray5)+abs(outarray6))/4),1)
    Mean_F_vertical_R = round(((abs(outarray3)+abs(outarray4)+abs(outarray7)+abs(outarray8))/4),1)
    Mean_Q = (Mean_F_vertical_L+Mean_F_vertical_R)/2

    #'СКО
    Rms_F_vertical_L = round((((abs(outarray9)**2+abs(outarray10)**2+abs(outarray13)**2+abs(outarray14)**2)/4)**0.5),1)
    Rms_F_vertical_R = round((((abs(outarray11)**2+abs(outarray12)**2+abs(outarray15)**2+abs(outarray16)**2)/4)**0.5),1)
    Rms_Q = round((((Rms_F_vertical_L**2+Rms_F_vertical_R**2)/2)**0.5),1)


    #'Боковые силы
    
    #'средние значения
    Mean_F_side_L = round(((abs(outarray17)+abs(outarray18)+abs(outarray21)+abs(outarray22))/4),1)
    Mean_F_side_R = round(((abs(outarray19)+abs(outarray20)+abs(outarray23)+abs(outarray24))/4),1)
    Mean_Y = (Mean_F_side_L+Mean_F_side_R)/2

    #'СКО
    Rms_F_side_L = round((((abs(outarray25)**2+abs(outarray26)**2+abs(outarray29)**2+abs(outarray30)**2)/4)**0.5),1)
    Rms_F_side_R = round((((abs(outarray27)**2+abs(outarray28)**2+abs(outarray31)**2+abs(outarray32)**2)/4)**0.5),1)
    Rms_Y = round((((Rms_F_side_L**2+Rms_F_side_R**2)/2)**0.5),1)

    outarray = [outarray1, outarray2, outarray3, outarray4, outarray5,outarray6, outarray7, outarray8,outarray9, outarray10, outarray11, outarray12, outarray13,outarray14, outarray15, outarray16,outarray17, outarray18, outarray19, outarray20, outarray21,outarray22, outarray23, outarray24,outarray25, outarray26, outarray27, outarray28, outarray29,outarray30, outarray31, outarray32]
    for el in range(0,len(outarray)):
        outarray[el]=abs(round(outarray[el], 1))

    #Эта ветка выводит в память список списков который состоит из значений для далььнейших расчетов (Сред.знач верт. силы, СКО вертикал силы, Сред.знач. боковой силы, ско боковой силы)
    #вывод идет как в целом по подвижному составу, так и отдельно по нитям
    #данный режим может быть использован для формирования массивов силовых факторов по вагонопотоку
        
    if Show_or_return == 'return':
        return [[Mean_Q, Rms_Q,Mean_Y, Rms_Y], [Mean_F_vertical_L, Rms_F_vertical_L, Mean_F_side_L, Rms_F_side_L], [Mean_F_vertical_R, Rms_F_vertical_R, Mean_F_side_R, Rms_F_side_R]]


    #эта ветка выводит на экран результаты расчетов, но в память их не загружает
    
    print ("Значения сил, действующие в системе 'колесо-рельс'\nпри движении пассажирского локомотива и следующих условиях:")
    print ("Тип В.С.П. - ",VSP, "\nСостояние пути - ", MAINT, "\nРадиус кривой, м -", Rad)
    print ("Возвышение наружнего рельса, мм - ", H, "\nСкорость движения, км/ч - ", v)
    print ("Ширина колеи, мм - ", SHK, "\nКоэффициент трения в системе 'колесо-рельс' -", FTR)
    print ()
    print ("Средние значения вертикальных сил по каждому колесу, кН:")
    print ('1_ось_лев_колесо= {};\n2_ось_лев_колесо= {};\n1_ось_прав_колесо= {};\n2_ось_прав_колесо= {};\n3_ось_лев_колесо= {};\n4_ось_лев_колесо= {};\n3_ось_прав_колесо= {};\n4_ось_прав_колесо= {}.'.format (outarray[0], outarray[1], outarray[2], outarray[3], outarray[4],outarray[5], outarray[6], outarray[7]))
    print ()
    print ("СКО вертикальных сил по каждому колесу, кН:")
    print ('1_ось_лев_колесо= {};\n2_ось_лев_колесо= {};\n1_ось_прав_колесо= {};\n2_ось_прав_колесо= {};\n3_ось_лев_колесо= {};\n4_ось_лев_колесо= {};\n3_ось_прав_колесо= {};\n4_ось_прав_колесо= {}.'.format (outarray[8], outarray[9], outarray[10], outarray[11], outarray[12],outarray[13], outarray[14], outarray[15]))
    print ()
    print ("Cредние значения боковых сил по каждому колесу, кН")
    print ('1_ось_лев_колесо= {};\n2_ось_лев_колесо= {};\n1_ось_прав_колесо= {};\n2_ось_прав_колесо= {};\n3_ось_лев_колесо= {};\n4_ось_лев_колесо= {};\n3_ось_прав_колесо= {};\n4_ось_прав_колесо= {}.'.format (outarray[16], outarray[17], outarray[18], outarray[19], outarray[20],outarray[21], outarray[22], outarray[23]))
    print ()
    print ("СКО боковых сил по каждому колесу, кН")
    print ('1_ось_лев_колесо= {};\n2_ось_лев_колесо= {};\n1_ось_прав_колесо= {};\n2_ось_прав_колесо= {};\n3_ось_лев_колесо= {};\n4_ось_лев_колесо= {};\n3_ось_прав_колесо= {};\n4_ось_прав_колесо= {}.'.format (outarray[24], outarray[25], outarray[26], outarray[27], outarray[28],outarray[29], outarray[30], outarray[31]))
    print ()
    print ()

    print ("ИТОГОВЫЕ ЗНАЧЕНИЯ ВОЗДЕЙСТВИЯ:")
    print ()
    print ("Средние значения вертикальных сил `колесо-рельс`, кН:")
    print ('по левой нити= {};\nпо правой нити = {};\nв среднем по экипажу= {};'.format (Mean_F_vertical_L, Mean_F_vertical_R, Mean_Q))
    print ()
    print ("СКО значений вертикальных сил `колесо-рельс, кН:")
    print ('по левой нити= {};\nпо правой нити = {};\nв среднем по экипажу= {};'.format(Rms_F_vertical_L, Rms_F_vertical_R, Rms_Q))
    print ()
    print ("Средние значения боковых сил `колесо-рельс`, кН:")
    print ('по левой нити= {};\nпо правой нити = {};\nв среднем по экипажу= {};'.format(Mean_F_side_L, Mean_F_side_R, Mean_Y))
    print ()
    print ("СКО значений боковых сил `колесо-рельс`:")
    print ('по левой нити= {};\nпо правой нити = {};\nв среднем по экипажу= {};'.format(Rms_F_side_L, Rms_F_side_R, Rms_Y))
    print ()
    
   
    
Pass_Loko_Force (1, 1, 250, 140, 80, 1520, 0.25, 'show')
print (Pass_Loko_Force (1, 1, 250, 140, 80, 1520, 0.25, 'return')) 
