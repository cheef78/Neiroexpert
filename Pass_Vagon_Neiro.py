def Pass_Vagon_Force (VSP_type, Condition, Radius, h, V, Sh_Kol, mu_fr, Show_or_tell = "return"):


    '''VSP_type это VSP_type - тип всп (1 - б.п., 2 - з.п.)
    ' Condition это Condition - состояние пути (1 - отличное или хорошее, 2 - удовлетворительное)
    ' Radius это R_m - радиус кривизны учатска, радиус кривизны прямого участка принимается 10000 м
    ' h это h_mm - возвышение наружнего рельса, мм
    ' V это V_km/h - скорость движения экипажа, км/ч
    ' Sh_Kol это S_mm - значение ширины колеи, мм
    ' mu_fr это ftr - коэффициент трения

     outarray - это переменные выходных значиний (средние значения и СКО сил)
     mean_ - это среднее значение силы, кН
     sigma - это СКО силы, кН
     F_vert - это вертикальная сил
     F_side - это боковая сила
     1,2,3,4 - номер оси в экипаже (в экипаже принято две тележки по две оси в каждой)
     r,l - правое или левое колесо 

    ' VSP_type это VSP_type
    ' Condition это Condition
    ' Radius это R_m
    ' h это h_mm
    ' V это V_km/h
    ' Sh_Kol это S_mm
    ' mu_fr это ftr
    ' outarray1 это mean_F_vert1l
    ' outarray2 это mean_F_vert2l
    ' outarray3 это mean_F_vert1r
    ' outarray4 это mean_F_vert2r
    ' outarray5 это mean_F_vert3l
    ' outarray6 это mean_F_vert4l
    ' outarray7 это mean_F_vert3r
    ' outarray8 это mean_F_vert4r
    ' outarray9 это sigma_F_vert1l
    ' outarray10 это sigma_F_vert2l
    ' outarray11 это sigma_F_vert1r
    ' outarray12 это sigma_F_vert2r
    ' outarray13 это sigma_F_vert3l
    ' outarray14 это sigma_F_vert4l
    ' outarray15 это sigma_F_vert3r
    ' outarray16 это sigma_F_vert4r
    ' outarray17 это mean_F_side1l
    ' outarray18 это mean_F_side2l
    ' outarray19 это mean_F_side1r
    ' outarray20 это mean_F_side2r
    ' outarray21 это mean_F_side3l
    ' outarray22 это mean_F_side4l
    ' outarray23 это mean_F_side3r
    ' outarray24 это mean_F_side4r
    ' outarray25 это sigma_F_side1l
    ' outarray26 это sigma_F_side2l
    ' outarray27 это sigma_F_side1r
    ' outarray28 это sigma_F_side2r
    ' outarray29 это sigma_F_side3l
    ' outarray30 это sigma_F_side4l
    ' outarray31 это sigma_F_side3r
    ' outarray32 это sigma_F_side4r'''

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

    
     
    netsum = -2.056844
    netsum = netsum + VSP_type * -1.674277E-02
    netsum = netsum + Condition * -7.744499E-02
    netsum = netsum + Radius * -24.53757
    netsum = netsum + h * 0.5196798
    netsum = netsum + V * 4.369862
    netsum = netsum + Sh_Kol * -1.241707E-02
    netsum = netsum + mu_fr * 8.976191E-02
    feature21 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.572905
    netsum = netsum + VSP_type * 2.277066E-02
    netsum = netsum + Condition * -2.153906
    netsum = netsum + Radius * -4.313865
    netsum = netsum + h * -1.547812E-03
    netsum = netsum + V * 2.655373
    netsum = netsum + Sh_Kol * 7.831133E-02
    netsum = netsum + mu_fr * 2.517023E-02
    feature22 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.730006
    netsum = netsum + VSP_type * -8.496147E-02
    netsum = netsum + Condition * -7.114672
    netsum = netsum + Radius * -21.81108
    netsum = netsum + h * -2.077752
    netsum = netsum + V * 7.700017
    netsum = netsum + Sh_Kol * 8.650757E-02
    netsum = netsum + mu_fr * 0.2583438
    feature23 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.6056789
    netsum = netsum + VSP_type * 2.220191E-03
    netsum = netsum + Condition * -1.324854E-02
    netsum = netsum + Radius * -4.054384
    netsum = netsum + h * -1.784244
    netsum = netsum + V * 1.271507
    netsum = netsum + Sh_Kol * 1.697616E-02
    netsum = netsum + mu_fr * -0.1380494
    feature24 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.080014
    netsum = netsum + VSP_type * 2.135393E-02
    netsum = netsum + Condition * -0.2916321
    netsum = netsum + Radius * -1.572667
    netsum = netsum + h * 0.6810031
    netsum = netsum + V * 7.015578
    netsum = netsum + Sh_Kol * 7.589923E-03
    netsum = netsum + mu_fr * -0.2228371
    feature25 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.891042
    netsum = netsum + VSP_type * -0.0947731
    netsum = netsum + Condition * -1.51869
    netsum = netsum + Radius * -24.4087
    netsum = netsum + h * -2.197192
    netsum = netsum + V * 8.666063
    netsum = netsum + Sh_Kol * 0.0716885
    netsum = netsum + mu_fr * 0.291816
    feature26 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.204415
    netsum = netsum + VSP_type * -1.957693E-03
    netsum = netsum + Condition * -1.566624E-02
    netsum = netsum + Radius * -8.242467
    netsum = netsum + h * 7.341398E-02
    netsum = netsum + V * -0.4306396
    netsum = netsum + Sh_Kol * 3.640902E-03
    netsum = netsum + mu_fr * 2.723164
    feature27 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.5528809
    netsum = netsum + VSP_type * 6.956611E-03
    netsum = netsum + Condition * 1.996848E-02
    netsum = netsum + Radius * -19.76722
    netsum = netsum + h * -1.670439E-02
    netsum = netsum + V * 0.61563
    netsum = netsum + Sh_Kol * -1.051568E-03
    netsum = netsum + mu_fr * -5.931755E-02
    feature28 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.921773
    netsum = netsum + VSP_type * -8.301372E-03
    netsum = netsum + Condition * 1.171315E-02
    netsum = netsum + Radius * 7.456222
    netsum = netsum + h * -0.239795
    netsum = netsum + V * 1.584885
    netsum = netsum + Sh_Kol * -1.162313E-02
    netsum = netsum + mu_fr * 0.6419078
    feature29 = 1 / (1 + math.exp(-netsum))
     
    netsum = 3.0353
    netsum = netsum + VSP_type * -8.727208E-03
    netsum = netsum + Condition * 3.803679
    netsum = netsum + Radius * 8.828891
    netsum = netsum + h * 0.2100716
    netsum = netsum + V * -2.89821
    netsum = netsum + Sh_Kol * -0.1080203
    netsum = netsum + mu_fr * -5.490991E-02
    feature210 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.530256E-02
    netsum = netsum + VSP_type * 3.109104E-03
    netsum = netsum + Condition * 2.916718E-02
    netsum = netsum + Radius * 5.28324
    netsum = netsum + h * -0.4140067
    netsum = netsum + V * 1.025839
    netsum = netsum + Sh_Kol * -1.260998E-03
    netsum = netsum + mu_fr * 0.4561448
    feature211 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.286902
    netsum = netsum + VSP_type * -6.047982E-02
    netsum = netsum + Condition * 0.3657906
    netsum = netsum + Radius * -1.0361
    netsum = netsum + h * -3.537917
    netsum = netsum + V * 3.570548
    netsum = netsum + Sh_Kol * 0.2292967
    netsum = netsum + mu_fr * -0.1268787
    feature212 = 1 / (1 + math.exp(-netsum))
     
    netsum = 2.025668
    netsum = netsum + VSP_type * 1.409652E-03
    netsum = netsum + Condition * 8.670598E-02
    netsum = netsum + Radius * 12.38302
    netsum = netsum + h * -2.010853
    netsum = netsum + V * 15.15542
    netsum = netsum + Sh_Kol * -2.926049E-03
    netsum = netsum + mu_fr * 0.4367821
    feature213 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.197032
    netsum = netsum + VSP_type * -2.785344E-03
    netsum = netsum + Condition * -4.529055E-03
    netsum = netsum + Radius * -4.70599
    netsum = netsum + h * 6.917594E-02
    netsum = netsum + V * -0.2862649
    netsum = netsum + Sh_Kol * -2.504497E-04
    netsum = netsum + mu_fr * -4.965199
    feature214 = 1 / (1 + math.exp(-netsum))
     
    netsum = 4.105983
    netsum = netsum + VSP_type * 5.445226E-02
    netsum = netsum + Condition * 7.508694E-02
    netsum = netsum + Radius * 30.23627
    netsum = netsum + h * 1.363742
    netsum = netsum + V * -8.651688
    netsum = netsum + Sh_Kol * 1.294826E-02
    netsum = netsum + mu_fr * -0.2415695
    feature215 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.822506
    netsum = netsum + VSP_type * -0.0102597
    netsum = netsum + Condition * -0.10539
    netsum = netsum + Radius * -20.01071
    netsum = netsum + h * 1.617531
    netsum = netsum + V * -9.293655
    netsum = netsum + Sh_Kol * 6.591396E-03
    netsum = netsum + mu_fr * -0.5702147
    feature216 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.301498
    netsum = netsum + VSP_type * 0
    netsum = netsum + Condition * 1.040568E-02
    netsum = netsum + Radius * -67.89986
    netsum = netsum + h * 1.307989E-03
    netsum = netsum + V * 4.151078
    netsum = netsum + Sh_Kol * -4.656155E-03
    netsum = netsum + mu_fr * 4.637571E-02
    feature217 = 1 / (1 + math.exp(-netsum))
     
    netsum = 23.29279
    netsum = netsum + VSP_type * -0.4505285
    netsum = netsum + Condition * -1.835948
    netsum = netsum + Radius * 25.00619
    netsum = netsum + h * -11.31998
    netsum = netsum + V * -15.44753
    netsum = netsum + Sh_Kol * 1.123955
    netsum = netsum + mu_fr * -0.8934864
    feature218 = 1 / (1 + math.exp(-netsum))
     
    netsum = 2.077933
    netsum = netsum + VSP_type * 0
    netsum = netsum + Condition * -3.330237E-03
    netsum = netsum + Radius * 32.00002
    netsum = netsum + h * -0.1448482
    netsum = netsum + V * -0.5430921
    netsum = netsum + Sh_Kol * 5.337259E-03
    netsum = netsum + mu_fr * -0.136044
    feature219 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.786319
    netsum = netsum + VSP_type * 3.810539E-02
    netsum = netsum + Condition * 0.1004213
    netsum = netsum + Radius * -4.310048
    netsum = netsum + h * -2.951375
    netsum = netsum + V * 6.668316
    netsum = netsum + Sh_Kol * 4.389524E-02
    netsum = netsum + mu_fr * 0.3857325
    feature220 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.785868
    netsum = netsum + feature21 * 1.125506
    netsum = netsum + feature22 * 0.1733193
    netsum = netsum + feature23 * -1.329099
    netsum = netsum + feature24 * 1.035502
    netsum = netsum + feature25 * 3.956766E-02
    netsum = netsum + feature26 * 1.44613
    netsum = netsum + feature27 * -6.117656E-02
    netsum = netsum + feature28 * -0.2107152
    netsum = netsum + feature29 * -2.132922
    netsum = netsum + feature210 * 0.2516105
    netsum = netsum + feature211 * 1.053341
    netsum = netsum + feature212 * -0.6044647
    netsum = netsum + feature213 * -2.112262
    netsum = netsum + feature214 * 1.100148E-02
    netsum = netsum + feature215 * 0.6540566
    netsum = netsum + feature216 * -2.18968
    netsum = netsum + feature217 * 6.823247
    netsum = netsum + feature218 * -0.8922272
    netsum = netsum + feature219 * 0.5672547
    netsum = netsum + feature220 * -0.1428435
    outarray1 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.202289
    netsum = netsum + feature21 * 1.1068
    netsum = netsum + feature22 * -0.1977015
    netsum = netsum + feature23 * -0.8129511
    netsum = netsum + feature24 * 1.001406
    netsum = netsum + feature25 * 0.1070663
    netsum = netsum + feature26 * 0.9468349
    netsum = netsum + feature27 * -0.4400211
    netsum = netsum + feature28 * 0.231933
    netsum = netsum + feature29 * -0.789242
    netsum = netsum + feature210 * -4.390785E-02
    netsum = netsum + feature211 * 0.2826367
    netsum = netsum + feature212 * -0.1043596
    netsum = netsum + feature213 * -1.923762
    netsum = netsum + feature214 * -0.6774552
    netsum = netsum + feature215 * 0.5832939
    netsum = netsum + feature216 * -1.860217
    netsum = netsum + feature217 * 8.33335
    netsum = netsum + feature218 * -0.1494767
    netsum = netsum + feature219 * 2.335967
    netsum = netsum + feature220 * -7.494315E-02
    outarray2 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.2424218
    netsum = netsum + feature21 * -0.73632
    netsum = netsum + feature22 * -9.554798E-02
    netsum = netsum + feature23 * 2.526849
    netsum = netsum + feature24 * -1.031905
    netsum = netsum + feature25 * -4.536095E-02
    netsum = netsum + feature26 * -2.700801
    netsum = netsum + feature27 * 0.1127101
    netsum = netsum + feature28 * -0.9061959
    netsum = netsum + feature29 * 0.2669712
    netsum = netsum + feature210 * -3.649996E-03
    netsum = netsum + feature211 * -1.157335
    netsum = netsum + feature212 * 0.7794117
    netsum = netsum + feature213 * 1.782813
    netsum = netsum + feature214 * -2.416229E-02
    netsum = netsum + feature215 * -0.6983551
    netsum = netsum + feature216 * 1.467978
    netsum = netsum + feature217 * -11.33339
    netsum = netsum + feature218 * 1.897115
    netsum = netsum + feature219 * -2.899775
    netsum = netsum + feature220 * 0.2315149
    outarray3 = 1 / (1 + math.exp(-netsum))
     
    netsum = 3.580196
    netsum = netsum + feature21 * -0.8361706
    netsum = netsum + feature22 * 0.2312457
    netsum = netsum + feature23 * 2.281318
    netsum = netsum + feature24 * -1.042019
    netsum = netsum + feature25 * -0.1166836
    netsum = netsum + feature26 * -2.540937
    netsum = netsum + feature27 * 0.7375132
    netsum = netsum + feature28 * -1.350236
    netsum = netsum + feature29 * -0.8642877
    netsum = netsum + feature210 * 0.1683357
    netsum = netsum + feature211 * -0.0281276
    netsum = netsum + feature212 * 0.2670156
    netsum = netsum + feature213 * 0.9010475
    netsum = netsum + feature214 * 1.084543
    netsum = netsum + feature215 * -0.7250697
    netsum = netsum + feature216 * 0.2928824
    netsum = netsum + feature217 * -12.8802
    netsum = netsum + feature218 * 1.449433
    netsum = netsum + feature219 * -4.94558
    netsum = netsum + feature220 * 0.1525067
    outarray4 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.148323
    netsum = netsum + feature21 * 1.082046
    netsum = netsum + feature22 * -0.3008403
    netsum = netsum + feature23 * -1.043741
    netsum = netsum + feature24 * 0.9038571
    netsum = netsum + feature25 * 0.1063656
    netsum = netsum + feature26 * 1.164185
    netsum = netsum + feature27 * -9.370567E-02
    netsum = netsum + feature28 * 6.800798E-02
    netsum = netsum + feature29 * -2.18153
    netsum = netsum + feature210 * -0.1952266
    netsum = netsum + feature211 * 0.9733641
    netsum = netsum + feature212 * -0.2719284
    netsum = netsum + feature213 * -1.873661
    netsum = netsum + feature214 * -8.841527E-02
    netsum = netsum + feature215 * 0.5948551
    netsum = netsum + feature216 * -2.028385
    netsum = netsum + feature217 * 7.649231
    netsum = netsum + feature218 * -0.536645
    netsum = netsum + feature219 * 1.226759
    netsum = netsum + feature220 * -9.800868E-02
    outarray5 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.197279
    netsum = netsum + feature21 * 1.110954
    netsum = netsum + feature22 * 0.1225212
    netsum = netsum + feature23 * -0.849079
    netsum = netsum + feature24 * 0.9465693
    netsum = netsum + feature25 * 7.434957E-02
    netsum = netsum + feature26 * 0.9494805
    netsum = netsum + feature27 * -0.2246459
    netsum = netsum + feature28 * 4.543704E-02
    netsum = netsum + feature29 * -0.4265902
    netsum = netsum + feature210 * 0.2116805
    netsum = netsum + feature211 * 0.40861
    netsum = netsum + feature212 * -0.2064068
    netsum = netsum + feature213 * -2.119173
    netsum = netsum + feature214 * -0.312288
    netsum = netsum + feature215 * 0.5750673
    netsum = netsum + feature216 * -1.975197
    netsum = netsum + feature217 * 7.853
    netsum = netsum + feature218 * -0.3092841
    netsum = netsum + feature219 * 1.989273
    netsum = netsum + feature220 * -0.0942919
    outarray6 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.279917
    netsum = netsum + feature21 * -0.7721077
    netsum = netsum + feature22 * 0.3480102
    netsum = netsum + feature23 * 2.483006
    netsum = netsum + feature24 * -0.9246333
    netsum = netsum + feature25 * -0.1185848
    netsum = netsum + feature26 * -2.691574
    netsum = netsum + feature27 * 0.2885928
    netsum = netsum + feature28 * -1.191796
    netsum = netsum + feature29 * 0.4909846
    netsum = netsum + feature210 * 0.3475774
    netsum = netsum + feature211 * -0.8790801
    netsum = netsum + feature212 * 0.4695702
    netsum = netsum + feature213 * 1.235564
    netsum = netsum + feature214 * 0.3170881
    netsum = netsum + feature215 * -0.7178416
    netsum = netsum + feature216 * 0.9401435
    netsum = netsum + feature217 * -12.5682
    netsum = netsum + feature218 * 1.477958
    netsum = netsum + feature219 * -3.7707
    netsum = netsum + feature220 * 0.1811391
    outarray7 = 1 / (1 + math.exp(-netsum))
     
    netsum = 3.32767
    netsum = netsum + feature21 * -0.7955967
    netsum = netsum + feature22 * -2.594878E-02
    netsum = netsum + feature23 * 2.22609
    netsum = netsum + feature24 * -1.00739
    netsum = netsum + feature25 * -9.418875E-02
    netsum = netsum + feature26 * -2.382029
    netsum = netsum + feature27 * 0.5299413
    netsum = netsum + feature28 * -1.214384
    netsum = netsum + feature29 * -1.105661
    netsum = netsum + feature210 * 4.885524E-02
    netsum = netsum + feature211 * -0.1985287
    netsum = netsum + feature212 * 0.4271136
    netsum = netsum + feature213 * 1.247384
    netsum = netsum + feature214 * 0.7257112
    netsum = netsum + feature215 * -0.6436878
    netsum = netsum + feature216 * 0.6425165
    netsum = netsum + feature217 * -12.59982
    netsum = netsum + feature218 * 1.518115
    netsum = netsum + feature219 * -4.699186
    netsum = netsum + feature220 * 0.1762328
    outarray8 = 1 / (1 + math.exp(-netsum))
     
    netsum = 4.571124
    netsum = netsum + feature21 * 0.1358973
    netsum = netsum + feature22 * -1.734179
    netsum = netsum + feature23 * 1.776384
    netsum = netsum + feature24 * 0.135829
    netsum = netsum + feature25 * 0.3932915
    netsum = netsum + feature26 * -2.189184
    netsum = netsum + feature27 * 0.3879926
    netsum = netsum + feature28 * -0.4440541
    netsum = netsum + feature29 * -0.9845995
    netsum = netsum + feature210 * -2.031663
    netsum = netsum + feature211 * 0.6294667
    netsum = netsum + feature212 * 0.5092759
    netsum = netsum + feature213 * -1.837671
    netsum = netsum + feature214 * 0.5919555
    netsum = netsum + feature215 * -0.7124115
    netsum = netsum + feature216 * -2.19593
    netsum = netsum + feature217 * 3.691803
    netsum = netsum + feature218 * -0.3485064
    netsum = netsum + feature219 * -0.8906702
    netsum = netsum + feature220 * -0.1553635
    outarray9 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.417557
    netsum = netsum + feature21 * -0.3619252
    netsum = netsum + feature22 * -1.478799
    netsum = netsum + feature23 * 2.003422
    netsum = netsum + feature24 * 0.1487709
    netsum = netsum + feature25 * 0.4557309
    netsum = netsum + feature26 * -2.277721
    netsum = netsum + feature27 * -0.9530517
    netsum = netsum + feature28 * 0.8992682
    netsum = netsum + feature29 * -1.013972
    netsum = netsum + feature210 * -1.292415
    netsum = netsum + feature211 * -1.349738
    netsum = netsum + feature212 * 0.7177424
    netsum = netsum + feature213 * 3.21609
    netsum = netsum + feature214 * -1.690021
    netsum = netsum + feature215 * -1.035162
    netsum = netsum + feature216 * 3.910199
    netsum = netsum + feature217 * 7.080857
    netsum = netsum + feature218 * -0.5551711
    netsum = netsum + feature219 * 3.740892
    netsum = netsum + feature220 * -9.912337E-02
    outarray10 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.245878
    netsum = netsum + feature21 * -0.1557933
    netsum = netsum + feature22 * -1.755904
    netsum = netsum + feature23 * 4.37112
    netsum = netsum + feature24 * -4.996385E-02
    netsum = netsum + feature25 * 0.3938292
    netsum = netsum + feature26 * -4.955411
    netsum = netsum + feature27 * 0.6180847
    netsum = netsum + feature28 * -0.7606342
    netsum = netsum + feature29 * -1.272214
    netsum = netsum + feature210 * -1.896258
    netsum = netsum + feature211 * 0.6989514
    netsum = netsum + feature212 * 1.076216
    netsum = netsum + feature213 * -1.741121
    netsum = netsum + feature214 * 0.9083576
    netsum = netsum + feature215 * -1.511273
    netsum = netsum + feature216 * -2.280057
    netsum = netsum + feature217 * 1.937295
    netsum = netsum + feature218 * 4.694289
    netsum = netsum + feature219 * -1.850401
    netsum = netsum + feature220 * -7.861116E-02
    outarray11 = 1 / (1 + math.exp(-netsum))
     
    netsum = -6.173999
    netsum = netsum + feature21 * -0.5332672
    netsum = netsum + feature22 * -1.244749
    netsum = netsum + feature23 * 4.797469
    netsum = netsum + feature24 * 5.133425E-02
    netsum = netsum + feature25 * 0.4508138
    netsum = netsum + feature26 * -5.2386
    netsum = netsum + feature27 * -0.9743421
    netsum = netsum + feature28 * 0.4691221
    netsum = netsum + feature29 * -2.372114
    netsum = netsum + feature210 * -0.8410765
    netsum = netsum + feature211 * -1.545464
    netsum = netsum + feature212 * 1.297496
    netsum = netsum + feature213 * 3.813648
    netsum = netsum + feature214 * -1.792708
    netsum = netsum + feature215 * -1.851807
    netsum = netsum + feature216 * 3.953895
    netsum = netsum + feature217 * 5.354822
    netsum = netsum + feature218 * 4.403447
    netsum = netsum + feature219 * 2.798894
    netsum = netsum + feature220 * -4.035388E-02
    outarray12 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.7156953
    netsum = netsum + feature21 * -0.6269372
    netsum = netsum + feature22 * -1.607676
    netsum = netsum + feature23 * 2.414669
    netsum = netsum + feature24 * -2.429831E-02
    netsum = netsum + feature25 * 0.4280955
    netsum = netsum + feature26 * -2.840868
    netsum = netsum + feature27 * -0.5583541
    netsum = netsum + feature28 * 0.9419342
    netsum = netsum + feature29 * 0.0100731
    netsum = netsum + feature210 * -1.666344
    netsum = netsum + feature211 * -0.976676
    netsum = netsum + feature212 * 0.9274795
    netsum = netsum + feature213 * 1.584129
    netsum = netsum + feature214 * -1.034493
    netsum = netsum + feature215 * -1.21754
    netsum = netsum + feature216 * 1.876329
    netsum = netsum + feature217 * 6.542487
    netsum = netsum + feature218 * -3.07471
    netsum = netsum + feature219 * 3.021846
    netsum = netsum + feature220 * -0.1495802
    outarray13 = 1 / (1 + math.exp(-netsum))
     
    netsum = -6.467258E-02
    netsum = netsum + feature21 * -0.6080172
    netsum = netsum + feature22 * -1.364473
    netsum = netsum + feature23 * 2.947749
    netsum = netsum + feature24 * -9.645301E-02
    netsum = netsum + feature25 * 0.3792456
    netsum = netsum + feature26 * -3.239512
    netsum = netsum + feature27 * 0.2724067
    netsum = netsum + feature28 * 0.5243781
    netsum = netsum + feature29 * 1.506846
    netsum = netsum + feature210 * -1.341139
    netsum = netsum + feature211 * 0.2215318
    netsum = netsum + feature212 * 1.063667
    netsum = netsum + feature213 * -4.818081E-02
    netsum = netsum + feature214 * 0.4391525
    netsum = netsum + feature215 * -1.262765
    netsum = netsum + feature216 * 6.214781E-02
    netsum = netsum + feature217 * 4.501929
    netsum = netsum + feature218 * -1.41464
    netsum = netsum + feature219 * 0.8614317
    netsum = netsum + feature220 * -0.1617428
    outarray14 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.307773
    netsum = netsum + feature21 * -0.7453241
    netsum = netsum + feature22 * -1.534536
    netsum = netsum + feature23 * 5.023742
    netsum = netsum + feature24 * -0.1543842
    netsum = netsum + feature25 * 0.437259
    netsum = netsum + feature26 * -5.529728
    netsum = netsum + feature27 * -0.6622664
    netsum = netsum + feature28 * 0.5483186
    netsum = netsum + feature29 * -1.593421
    netsum = netsum + feature210 * -1.393351
    netsum = netsum + feature211 * -1.215323
    netsum = netsum + feature212 * 1.361717
    netsum = netsum + feature213 * 1.740003
    netsum = netsum + feature214 * -1.262835
    netsum = netsum + feature215 * -1.966532
    netsum = netsum + feature216 * 1.675963
    netsum = netsum + feature217 * 4.810294
    netsum = netsum + feature218 * 4.870515
    netsum = netsum + feature219 * 2.192886
    netsum = netsum + feature220 * -3.862309E-02
    outarray15 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.761717
    netsum = netsum + feature21 * -0.8044406
    netsum = netsum + feature22 * -1.217384
    netsum = netsum + feature23 * 5.068672
    netsum = netsum + feature24 * -0.1965134
    netsum = netsum + feature25 * 0.3738902
    netsum = netsum + feature26 * -5.504719
    netsum = netsum + feature27 * 0.4057567
    netsum = netsum + feature28 * 0.1841062
    netsum = netsum + feature29 * 0.7206596
    netsum = netsum + feature210 * -1.103962
    netsum = netsum + feature211 * 0.2534447
    netsum = netsum + feature212 * 1.450735
    netsum = netsum + feature213 * 0.5302182
    netsum = netsum + feature214 * 0.5867805
    netsum = netsum + feature215 * -1.877508
    netsum = netsum + feature216 * 0.283076
    netsum = netsum + feature217 * 3.012236
    netsum = netsum + feature218 * 3.625452
    netsum = netsum + feature219 * 3.951157E-02
    netsum = netsum + feature220 * -0.115868
    outarray16 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.08155
    netsum = netsum + feature21 * 1.038121E-02
    netsum = netsum + feature22 * -8.542268E-02
    netsum = netsum + feature23 * 0.4191774
    netsum = netsum + feature24 * -0.334367
    netsum = netsum + feature25 * -3.602937E-02
    netsum = netsum + feature26 * -0.3840888
    netsum = netsum + feature27 * 0.8656741
    netsum = netsum + feature28 * -0.5796348
    netsum = netsum + feature29 * -1.101411
    netsum = netsum + feature210 * -1.384153E-02
    netsum = netsum + feature211 * 1.404642
    netsum = netsum + feature212 * 0.2323336
    netsum = netsum + feature213 * 0.2460751
    netsum = netsum + feature214 * 1.327608
    netsum = netsum + feature215 * 3.799919E-02
    netsum = netsum + feature216 * 0.1428605
    netsum = netsum + feature217 * -0.9658258
    netsum = netsum + feature218 * 0.3257971
    netsum = netsum + feature219 * 0.3363021
    netsum = netsum + feature220 * -1.766033E-02
    outarray17 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.918964
    netsum = netsum + feature21 * -0.0315922
    netsum = netsum + feature22 * 0.2026693
    netsum = netsum + feature23 * 0.1274721
    netsum = netsum + feature24 * -0.2086412
    netsum = netsum + feature25 * -4.434973E-02
    netsum = netsum + feature26 * -9.538755E-02
    netsum = netsum + feature27 * 0.801203
    netsum = netsum + feature28 * -0.8729526
    netsum = netsum + feature29 * -0.314322
    netsum = netsum + feature210 * 0.2344269
    netsum = netsum + feature211 * 0.8671019
    netsum = netsum + feature212 * -0.1060188
    netsum = netsum + feature213 * -0.392655
    netsum = netsum + feature214 * 1.262237
    netsum = netsum + feature215 * 7.322495E-02
    netsum = netsum + feature216 * -0.5799488
    netsum = netsum + feature217 * -3.674599
    netsum = netsum + feature218 * -0.1882325
    netsum = netsum + feature219 * -2.149889
    netsum = netsum + feature220 * -2.251602E-02
    outarray18 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.3724271
    netsum = netsum + feature21 * -0.2494194
    netsum = netsum + feature22 * -9.181143E-02
    netsum = netsum + feature23 * 4.863477E-02
    netsum = netsum + feature24 * 8.502606E-02
    netsum = netsum + feature25 * 5.154249E-02
    netsum = netsum + feature26 * -4.517824E-02
    netsum = netsum + feature27 * -1.020475
    netsum = netsum + feature28 * 0.6675621
    netsum = netsum + feature29 * 2.228612
    netsum = netsum + feature210 * -7.392637E-02
    netsum = netsum + feature211 * -2.092999
    netsum = netsum + feature212 * 5.807842E-02
    netsum = netsum + feature213 * 0.4628156
    netsum = netsum + feature214 * -1.657578
    netsum = netsum + feature215 * -9.122687E-02
    netsum = netsum + feature216 * 0.6296142
    netsum = netsum + feature217 * -1.574796
    netsum = netsum + feature218 * 1.375246E-02
    netsum = netsum + feature219 * -0.2262131
    netsum = netsum + feature220 * 7.649389E-02
    outarray19 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.5017936
    netsum = netsum + feature21 * -0.2170953
    netsum = netsum + feature22 * -6.922447E-03
    netsum = netsum + feature23 * -0.5270804
    netsum = netsum + feature24 * -6.438468E-02
    netsum = netsum + feature25 * -3.112137E-03
    netsum = netsum + feature26 * 0.4441553
    netsum = netsum + feature27 * -0.421872
    netsum = netsum + feature28 * 0.518665
    netsum = netsum + feature29 * -6.017657E-02
    netsum = netsum + feature210 * -0.1861524
    netsum = netsum + feature211 * -0.4690161
    netsum = netsum + feature212 * -0.2270621
    netsum = netsum + feature213 * 0.4348253
    netsum = netsum + feature214 * -0.616725
    netsum = netsum + feature215 * -1.781456E-02
    netsum = netsum + feature216 * 0.427351
    netsum = netsum + feature217 * -0.5859799
    netsum = netsum + feature218 * -0.4105581
    netsum = netsum + feature219 * 0.2822433
    netsum = netsum + feature220 * 0
    outarray20 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.31304
    netsum = netsum + feature21 * 3.975924E-02
    netsum = netsum + feature22 * 0.3255771
    netsum = netsum + feature23 * 5.883366E-02
    netsum = netsum + feature24 * -0.250234
    netsum = netsum + feature25 * -7.149534E-02
    netsum = netsum + feature26 * 8.381304E-03
    netsum = netsum + feature27 * 1.112547
    netsum = netsum + feature28 * -0.9754968
    netsum = netsum + feature29 * -0.1458866
    netsum = netsum + feature210 * 0.3841395
    netsum = netsum + feature211 * 1.33192
    netsum = netsum + feature212 * -7.187739E-03
    netsum = netsum + feature213 * 2.021478E-02
    netsum = netsum + feature214 * 1.73402
    netsum = netsum + feature215 * 0.1382156
    netsum = netsum + feature216 * 5.016276E-02
    netsum = netsum + feature217 * -1.39364
    netsum = netsum + feature218 * -0.2164804
    netsum = netsum + feature219 * -9.008802E-02
    netsum = netsum + feature220 * -4.509138E-02
    outarray21 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.89792
    netsum = netsum + feature21 * -5.195401E-02
    netsum = netsum + feature22 * -6.553362E-02
    netsum = netsum + feature23 * 6.573726E-02
    netsum = netsum + feature24 * -0.1864161
    netsum = netsum + feature25 * -8.711408E-03
    netsum = netsum + feature26 * -0.118029
    netsum = netsum + feature27 * 0.3268128
    netsum = netsum + feature28 * -0.4452805
    netsum = netsum + feature29 * -0.542514
    netsum = netsum + feature210 * -9.083617E-02
    netsum = netsum + feature211 * 0.3350286
    netsum = netsum + feature212 * -1.570706E-03
    netsum = netsum + feature213 * -4.039016E-02
    netsum = netsum + feature214 * 0.4890881
    netsum = netsum + feature215 * 7.674664E-02
    netsum = netsum + feature216 * -0.3137443
    netsum = netsum + feature217 * -3.765858
    netsum = netsum + feature218 * -6.880286E-02
    netsum = netsum + feature219 * -1.55009
    netsum = netsum + feature220 * 0.0102404
    outarray22 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.6418824
    netsum = netsum + feature21 * -0.2693253
    netsum = netsum + feature22 * -0.1321889
    netsum = netsum + feature23 * 4.700382E-02
    netsum = netsum + feature24 * 3.738032E-02
    netsum = netsum + feature25 * 3.649674E-02
    netsum = netsum + feature26 * -8.010613E-02
    netsum = netsum + feature27 * -1.023189
    netsum = netsum + feature28 * 0.7722459
    netsum = netsum + feature29 * 1.628305
    netsum = netsum + feature210 * -0.1944233
    netsum = netsum + feature211 * -1.771025
    netsum = netsum + feature212 * 1.495997E-02
    netsum = netsum + feature213 * 0.2584344
    netsum = netsum + feature214 * -1.633716
    netsum = netsum + feature215 * -0.1196539
    netsum = netsum + feature216 * 0.3888123
    netsum = netsum + feature217 * -1.957377
    netsum = netsum + feature218 * -4.075601E-02
    netsum = netsum + feature219 * -0.4700816
    netsum = netsum + feature220 * 6.523748E-02
    outarray23 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.1267087
    netsum = netsum + feature21 * -0.2099214
    netsum = netsum + feature22 * -0.1343425
    netsum = netsum + feature23 * -0.1957432
    netsum = netsum + feature24 * -0.1359159
    netsum = netsum + feature25 * 0.0139167
    netsum = netsum + feature26 * 0.228073
    netsum = netsum + feature27 * -0.1807471
    netsum = netsum + feature28 * 0.3521537
    netsum = netsum + feature29 * 1.044598E-03
    netsum = netsum + feature210 * -0.1626039
    netsum = netsum + feature211 * -0.2054112
    netsum = netsum + feature212 * -2.806306E-02
    netsum = netsum + feature213 * 0.5092325
    netsum = netsum + feature214 * -0.2548383
    netsum = netsum + feature215 * -4.820158E-02
    netsum = netsum + feature216 * 0.5279593
    netsum = netsum + feature217 * 4.293848E-02
    netsum = netsum + feature218 * -0.1105653
    netsum = netsum + feature219 * 0.2157057
    netsum = netsum + feature220 * 9.487538E-03
    outarray24 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.060552
    netsum = netsum + feature21 * -5.590516E-02
    netsum = netsum + feature22 * -0.2594931
    netsum = netsum + feature23 * 0.6718954
    netsum = netsum + feature24 * 6.807075E-02
    netsum = netsum + feature25 * 4.614263E-02
    netsum = netsum + feature26 * -0.8460076
    netsum = netsum + feature27 * -0.3680552
    netsum = netsum + feature28 * 3.166395E-02
    netsum = netsum + feature29 * 0.4177012
    netsum = netsum + feature210 * -0.3659469
    netsum = netsum + feature211 * -0.8083573
    netsum = netsum + feature212 * 0.233106
    netsum = netsum + feature213 * 0.1539692
    netsum = netsum + feature214 * -0.6015865
    netsum = netsum + feature215 * -0.3757489
    netsum = netsum + feature216 * 7.686427E-02
    netsum = netsum + feature217 * -0.6038808
    netsum = netsum + feature218 * 0.3289219
    netsum = netsum + feature219 * -0.4948363
    netsum = netsum + feature220 * 4.490872E-02
    outarray25 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.653121
    netsum = netsum + feature21 * -0.0410608
    netsum = netsum + feature22 * -3.424145E-02
    netsum = netsum + feature23 * 0.8407567
    netsum = netsum + feature24 * -2.665068E-02
    netsum = netsum + feature25 * 2.876358E-02
    netsum = netsum + feature26 * -0.9707005
    netsum = netsum + feature27 * -0.3213267
    netsum = netsum + feature28 * -0.0446106
    netsum = netsum + feature29 * -0.9409361
    netsum = netsum + feature210 * 6.239333E-02
    netsum = netsum + feature211 * -0.5440413
    netsum = netsum + feature212 * 0.3754928
    netsum = netsum + feature213 * 0.7291335
    netsum = netsum + feature214 * -0.5729116
    netsum = netsum + feature215 * -0.486437
    netsum = netsum + feature216 * 0.5993913
    netsum = netsum + feature217 * 0.4262047
    netsum = netsum + feature218 * 0.203049
    netsum = netsum + feature219 * 0.2677971
    netsum = netsum + feature220 * 5.108519E-02
    outarray26 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.5667483
    netsum = netsum + feature21 * -7.393005E-02
    netsum = netsum + feature22 * -0.1539082
    netsum = netsum + feature23 * 0.1993837
    netsum = netsum + feature24 * 5.357502E-02
    netsum = netsum + feature25 * 0.0392919
    netsum = netsum + feature26 * -0.2226233
    netsum = netsum + feature27 * -0.2975293
    netsum = netsum + feature28 * 0.1189574
    netsum = netsum + feature29 * 0.8999006
    netsum = netsum + feature210 * -0.1403761
    netsum = netsum + feature211 * -0.7270341
    netsum = netsum + feature212 * 0.0841027
    netsum = netsum + feature213 * 0.343686
    netsum = netsum + feature214 * -0.5251154
    netsum = netsum + feature215 * -8.153324E-02
    netsum = netsum + feature216 * 0.426272
    netsum = netsum + feature217 * -4.098329E-02
    netsum = netsum + feature218 * 0.1629081
    netsum = netsum + feature219 * 4.914165E-02
    netsum = netsum + feature220 * 2.124031E-02
    outarray27 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.4922689
    netsum = netsum + feature21 * -0.0465962
    netsum = netsum + feature22 * -0.1215129
    netsum = netsum + feature23 * -1.580215E-02
    netsum = netsum + feature24 * 0
    netsum = netsum + feature25 * 2.279883E-02
    netsum = netsum + feature26 * -4.278897E-02
    netsum = netsum + feature27 * -0.1835937
    netsum = netsum + feature28 * 0.192954
    netsum = netsum + feature29 * -0.1838886
    netsum = netsum + feature210 * -0.2029118
    netsum = netsum + feature211 * -0.2314366
    netsum = netsum + feature212 * 5.994388E-02
    netsum = netsum + feature213 * 0.1265928
    netsum = netsum + feature214 * -0.2987311
    netsum = netsum + feature215 * -3.247429E-02
    netsum = netsum + feature216 * 0.1073686
    netsum = netsum + feature217 * -0.4213115
    netsum = netsum + feature218 * -2.304118E-02
    netsum = netsum + feature219 * 6.621788E-02
    netsum = netsum + feature220 * 4.760051E-04
    outarray28 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.5295808
    netsum = netsum + feature21 * -2.172546E-02
    netsum = netsum + feature22 * -0.2355379
    netsum = netsum + feature23 * 0.7058599
    netsum = netsum + feature24 * -1.693489E-02
    netsum = netsum + feature25 * 3.834485E-02
    netsum = netsum + feature26 * -0.8283792
    netsum = netsum + feature27 * -0.099432
    netsum = netsum + feature28 * -0.111461
    netsum = netsum + feature29 * 2.914068E-02
    netsum = netsum + feature210 * -0.2148281
    netsum = netsum + feature211 * -0.4318093
    netsum = netsum + feature212 * 0.2801415
    netsum = netsum + feature213 * 0.2174189
    netsum = netsum + feature214 * -0.220482
    netsum = netsum + feature215 * -0.3579643
    netsum = netsum + feature216 * 0.1829587
    netsum = netsum + feature217 * -0.1473778
    netsum = netsum + feature218 * 0.2306515
    netsum = netsum + feature219 * -0.0670507
    netsum = netsum + feature220 * 4.440991E-02
    outarray29 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.206721
    netsum = netsum + feature21 * -1.790362E-02
    netsum = netsum + feature22 * -3.260501E-02
    netsum = netsum + feature23 * 1.171075
    netsum = netsum + feature24 * -2.319251E-02
    netsum = netsum + feature25 * 1.610833E-02
    netsum = netsum + feature26 * -1.285904
    netsum = netsum + feature27 * -0.2643319
    netsum = netsum + feature28 * -9.104663E-02
    netsum = netsum + feature29 * -0.5913308
    netsum = netsum + feature210 * 5.374086E-02
    netsum = netsum + feature211 * -0.4589422
    netsum = netsum + feature212 * 0.416329
    netsum = netsum + feature213 * 5.803988E-02
    netsum = netsum + feature214 * -0.4536895
    netsum = netsum + feature215 * -0.5362931
    netsum = netsum + feature216 * -3.790326E-03
    netsum = netsum + feature217 * 0.2187628
    netsum = netsum + feature218 * 0.2583776
    netsum = netsum + feature219 * -4.973809E-02
    netsum = netsum + feature220 * 6.200325E-02
    outarray30 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.9039834
    netsum = netsum + feature21 * -8.946004E-02
    netsum = netsum + feature22 * -0.2177419
    netsum = netsum + feature23 * 0.2378419
    netsum = netsum + feature24 * 3.808164E-02
    netsum = netsum + feature25 * 4.775133E-02
    netsum = netsum + feature26 * -0.2662458
    netsum = netsum + feature27 * -0.2924001
    netsum = netsum + feature28 * 0.2649332
    netsum = netsum + feature29 * 0.8357953
    netsum = netsum + feature210 * -0.2342594
    netsum = netsum + feature211 * -0.6832726
    netsum = netsum + feature212 * 0.1162777
    netsum = netsum + feature213 * 0.4055955
    netsum = netsum + feature214 * -0.5283988
    netsum = netsum + feature215 * -8.358163E-02
    netsum = netsum + feature216 * 0.4770353
    netsum = netsum + feature217 * 0.1473191
    netsum = netsum + feature218 * 0.189322
    netsum = netsum + feature219 * 0.4209955
    netsum = netsum + feature220 * 1.621097E-02
    outarray31 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.806869
    netsum = netsum + feature21 * 0.0191614
    netsum = netsum + feature22 * -0.1254466
    netsum = netsum + feature23 * 8.346197E-02
    netsum = netsum + feature24 * -6.714058E-03
    netsum = netsum + feature25 * 1.907871E-02
    netsum = netsum + feature26 * -0.1151328
    netsum = netsum + feature27 * 0.1268808
    netsum = netsum + feature28 * -0.1011124
    netsum = netsum + feature29 * -0.1629249
    netsum = netsum + feature210 * -0.1833452
    netsum = netsum + feature211 * 0.1936489
    netsum = netsum + feature212 * 4.431617E-02
    netsum = netsum + feature213 * -0.2119399
    netsum = netsum + feature214 * 0.1992556
    netsum = netsum + feature215 * 1.063894E-04
    netsum = netsum + feature216 * -0.2869335
    netsum = netsum + feature217 * -0.4985775
    netsum = netsum + feature218 * 3.437439E-02
    netsum = netsum + feature219 * -0.4534729
    netsum = netsum + feature220 * -9.441807E-03
    outarray32 = 1 / (1 + math.exp(-netsum))
     
     
    outarray1 = 200 *  (outarray1 - .1) / .8 
    if (outarray1<0):
        outarray1 = 0
    if (outarray1>200):
        outarray1 = 200
     
    outarray2 = 200 *  (outarray2 - .1) / .8 
    if (outarray2<0):
        outarray2 = 0
    if (outarray2>200):
        outarray2 = 200
     
    outarray3 = 200 *  (outarray3 - .1) / .8 
    if (outarray3<0):
        outarray3 = 0
    if (outarray3>200):
        outarray3 = 200
     
    outarray4 = 200 *  (outarray4 - .1) / .8 
    if (outarray4<0):
        outarray4 = 0
    if (outarray4>200):
        outarray4 = 200
     
    outarray5 = 200 *  (outarray5 - .1) / .8 
    if (outarray5<0):
        outarray5 = 0
    if (outarray5>200):
        outarray5 = 200
     
    outarray6 = 200 *  (outarray6 - .1) / .8 
    if (outarray6<0):
        outarray6 = 0
    if (outarray6>200):
        outarray6 = 200
     
    outarray7 = 200 *  (outarray7 - .1) / .8 
    if (outarray7<0):
        outarray7 = 0
    if (outarray7>200):
        outarray7 = 200
     
    outarray8 = 200 *  (outarray8 - .1) / .8 
    if (outarray8<0):
        outarray8 = 0
    if (outarray8>200):
        outarray8 = 200
     
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
    Mean_F_vertL = round(((abs(outarray1)+abs(outarray2)+abs(outarray5)+abs(outarray6))/4),1)
    Mean_F_vertR = round(((abs(outarray3)+abs(outarray4)+abs(outarray7)+abs(outarray8))/4),1)
    Mean_Q = (Mean_F_vertL+Mean_F_vertR)/2

    #'СКО
    sigma_F_vertL = round((((abs(outarray9)**2+abs(outarray10)**2+abs(outarray13)**2+abs(outarray14)**2)/4)**0.5),1)
    sigma_F_vertR = round((((abs(outarray11)**2+abs(outarray12)**2+abs(outarray15)**2+abs(outarray16)**2)/4)**0.5),1)
    sigma_Q = round((((sigma_F_vertL**2+sigma_F_vertR**2)/2)**0.5),1)


    #'Боковые силы
    
    #'средние значения
    Mean_F_sideL = round(((abs(outarray17)+abs(outarray18)+abs(outarray21)+abs(outarray22))/4),1)
    Mean_F_sideR = round(((abs(outarray19)+abs(outarray20)+abs(outarray23)+abs(outarray24))/4),1)
    Mean_Y = (Mean_F_sideL+Mean_F_sideR)/2

    #'СКО
    sigma_F_sideL = round((((abs(outarray25)**2+abs(outarray26)**2+abs(outarray29)**2+abs(outarray30)**2)/4)**0.5),1)
    sigma_F_sideR = round((((abs(outarray27)**2+abs(outarray28)**2+abs(outarray31)**2+abs(outarray32)**2)/4)**0.5),1)
    sigma_Y = round((((sigma_F_sideL**2+sigma_F_sideR**2)/2)**0.5),1)

    outarray = [outarray1, outarray2, outarray3, outarray4, outarray5,outarray6, outarray7, outarray8,outarray9, outarray10, outarray11, outarray12, outarray13,outarray14, outarray15, outarray16,outarray17, outarray18, outarray19, outarray20, outarray21,outarray22, outarray23, outarray24,outarray25, outarray26, outarray27, outarray28, outarray29,outarray30, outarray31, outarray32]
    for el in range(0,len(outarray)):
        outarray[el]=abs(round(outarray[el], 1))

    #Эта ветка выводит в память список списков который состоит из значений для далььнейших расчетов (Сред.знач верт. силы, СКО вертикал силы, Сред.знач. боковой силы, ско боковой силы)
    #вывод идет как в целом по подвижному составу, так и отдельно по нитям
    #данный режим может быть использован для формирования массивов силовых факторов по вагонопотоку
        
    if Show_or_tell == 'return':
        return [[Mean_Q, sigma_Q,Mean_Y, sigma_Y], [Mean_F_vertL, sigma_F_vertL, Mean_F_sideL, sigma_F_sideL], [Mean_F_vertR, sigma_F_vertR, Mean_F_sideR, sigma_F_sideR]]

    #эта ветка выводит на экран результаты расчетов, но в память их не загружает
        
    print ("Значения сил, действующие в системе 'колесо-рельс'\nпри движении пассажирского вагона и следующих условиях:")
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
    print ('по левой нити= {};\nпо правой нити = {};\nв среднем по экипажу= {};'.format (Mean_F_vertL, Mean_F_vertR, Mean_Q))
    print ()
    print ("СКО значений вертикальных сил `колесо-рельс, кН:")
    print ('по левой нити= {};\nпо правой нити = {};\nв среднем по экипажу= {};'.format(sigma_F_vertL, sigma_F_vertR, sigma_Q))
    print ()
    print ("Средние значения боковых сил `колесо-рельс`, кН:")
    print ('по левой нити= {};\nпо правой нити = {};\nв среднем по экипажу= {};'.format(Mean_F_sideL, Mean_F_sideR, Mean_Y))
    print ()
    print ("СКО значений боковых сил `колесо-рельс`:")
    print ('по левой нити= {};\nпо правой нити = {};\nв среднем по экипажу= {};'.format(sigma_F_sideL, sigma_F_sideR, sigma_Y))
    print ()
    



    
    
Pass_Vagon_Force (1, 1, 250, 140, 80, 1520, 0.25, "show")
print (Pass_Vagon_Force (1, 1, 250, 140, 80, 1520, 0.25, "return"))
 
