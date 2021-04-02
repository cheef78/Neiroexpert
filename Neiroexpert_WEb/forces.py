
def vagon_1 (input_val, Show_or_tell = "return"):
   
    VSP_type = input_val[0] 
    Condition = input_val[1] 
    Radius = input_val[2]
    h = input_val[3]
    V = input_val[4]
    axle_load = input_val[5]
    Sh_Kol = input_val[6] 
    mu_fr = input_val[7]

    #вычисление контактных напряжений
    from contact_pressure import contact_tension 
    input_val1 = [V,axle_load, mu_fr, Radius, h, Sh_Kol]
    
    cont_press = contact_tension(input_val1)
    
    MeanP1NarkPa = cont_press[0]
    RmsP1NarkPa = cont_press[1]
    MeanP1VnrkPa  = cont_press[2]
    RmsP1VnrkPa = cont_press[3]
    MeanP2NarkPa = cont_press[4]
    RmsP2NarkPa = cont_press[5]
    MeanP2VnrkPa = cont_press[6]
    RmsP2VnrkPa = cont_press[7]

     
    '''
    'Расчет сил для пассажирского вагона 
    'VSP_type это VSP_type - тип всп (1 - б.п., 2 - з.п.)
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

    VSP_type, Condition, Radius, h, V, Sh_Kol, mu_fr,


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

    #'Рамные силы
    
    #'средние значения
    Mean_Hp = abs(round((((outarray17)+(outarray18)+(outarray21)+(outarray22))/4),1) + round((((outarray19)+(outarray20)+(outarray23)+(outarray24))/4),1))
    
    #'СКО
    sigma_Hp = sigma_Y 
    




    outarray = [outarray1, outarray2, outarray3, outarray4, outarray5,outarray6, outarray7, outarray8,outarray9, outarray10, outarray11, outarray12, outarray13,outarray14, outarray15, outarray16,outarray17, outarray18, outarray19, outarray20, outarray21,outarray22, outarray23, outarray24,outarray25, outarray26, outarray27, outarray28, outarray29,outarray30, outarray31, outarray32]
    for el in range(0,len(outarray)):
        outarray[el]=abs(round(outarray[el], 1))

    
    
    #Эта ветка выводит в память список списков который состоит из значений для далььнейших расчетов (Сред.знач верт. силы, СКО вертикал силы, Сред.знач. боковой силы, ско боковой силы)
    #вывод идет как в целом по подвижному составу, так и отдельно по нитям
    #данный режим может быть использован для формирования массивов силовых факторов по вагонопотоку
        
    
    
    if Show_or_tell == 'return':
        return [Mean_F_vertR, Mean_F_vertL, Mean_Q, sigma_F_vertR, sigma_F_vertL, sigma_Q, Mean_F_sideR, Mean_F_sideL, Mean_Y, sigma_F_sideR, sigma_F_sideL, sigma_Y, Mean_Hp, sigma_Hp, MeanP1NarkPa, RmsP1NarkPa, MeanP1VnrkPa, RmsP1VnrkPa, MeanP2NarkPa, RmsP2NarkPa, MeanP2VnrkPa, RmsP2VnrkPa]

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
    


def vagon_3 (input_val, Show_or_return = "return"):

    VSP_type = input_val[0] 
    Condition = input_val[1] 
    Radius = input_val[2]
    h = input_val[3]
    V = input_val[4]
    axle_load = input_val[5]
    Sh_Kol = input_val[6] 
    mu_fr = input_val[7] 

    #вычисление контактных напряжений
    from contact_pressure import contact_tension
    input_val1 = [V,axle_load, mu_fr, Radius, h, Sh_Kol]
    
    cont_press = contact_tension(input_val1)
    
    MeanP1NarkPa = cont_press[0]
    RmsP1NarkPa = cont_press[1]
    MeanP1VnrkPa  = cont_press[2]
    RmsP1VnrkPa = cont_press[3]
    MeanP2NarkPa = cont_press[4]
    RmsP2NarkPa = cont_press[5]
    MeanP2VnrkPa = cont_press[6]
    RmsP2VnrkPa = cont_press[7]
    '''
    'Пассажирский локомотив
    'VSP_type это VSP_type - тип всп (1 - б.п., 2 - з.п.)
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


    #'Рамные силы
    
    #'средние значения
    Mean_Hp = abs(round((((outarray17)+(outarray18)+(outarray21)+(outarray22))/4),1) + round((((outarray19)+(outarray20)+(outarray23)+(outarray24))/4),1))
    
    #'СКО
    sigma_Hp = Rms_Y 




    outarray = [outarray1, outarray2, outarray3, outarray4, outarray5,outarray6, outarray7, outarray8,outarray9, outarray10, outarray11, outarray12, outarray13,outarray14, outarray15, outarray16,outarray17, outarray18, outarray19, outarray20, outarray21,outarray22, outarray23, outarray24,outarray25, outarray26, outarray27, outarray28, outarray29,outarray30, outarray31, outarray32]
    for el in range(0,len(outarray)):
        outarray[el]=abs(round(outarray[el], 1))

    #Эта ветка выводит в память список списков который состоит из значений для далььнейших расчетов (Сред.знач верт. силы, СКО вертикал силы, Сред.знач. боковой силы, ско боковой силы)
    #вывод идет как в целом по подвижному составу, так и отдельно по нитям
    #данный режим может быть использован для формирования массивов силовых факторов по вагонопотоку
        
    if Show_or_return == 'return':
        return [Mean_F_vertical_R, Mean_F_vertical_L, Mean_Q, Rms_F_vertical_R, Rms_F_vertical_L, Rms_Q, Mean_F_side_R,\
                Mean_F_side_L, Mean_Y, Rms_F_side_R, Rms_F_side_L, Rms_Y, Mean_Hp, sigma_Hp,\
                MeanP1NarkPa, RmsP1NarkPa, MeanP1VnrkPa, RmsP1VnrkPa, MeanP2NarkPa, RmsP2NarkPa, MeanP2VnrkPa, RmsP2VnrkPa]
                

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
    
   
    


def vagon_2 (input_val, Show_or_return = "return"):
    
    '''
    'Расчет сил для грузового вагона
    'VSP_type это VSP_type - тип всп (1 - б.п., 2 - з.п.)
    ' Condition это Condition - состояние пути (1 - отличное или хорошее, 2 - удовлетворительное)
    ' Radius это R_m - радиус кривизны учатска, радиус кривизны прямого участка принимается 10000 м
    ' h это h_mm - возвышение наружнего рельса, мм
    ' V это V_km/h - скорость движения экипажа, км/ч
    ' axle_load это axle_load_ts - это осевая нагрузка, тс 
    ' Sh_Kol это S_mm - значение ширины колеи, мм
    ' mu_fr это ftr - коэффициент трения

     outarray - это переменные выходных значиний (средние значения и СКО сил)
     mean_ - это среднее значение силы, кН
     sigma - это СКО силы, кН
     F_vert - это вертикальная сил
     F_side - это боковая сила
     H - это рамная сила
     1,2,3,4 - номер оси в экипаже (в экипаже принято две тележки по две оси в каждой)
     r,l - правое или левое колесо 

    ' outarray1 это mean_F_vert(V)_1l
    ' outarray2 это mean_F_vert(V)_2l
    ' outarray3 это mean_F_vert(V)_1r
    ' outarray4 это mean_F_vert(V)_2r
    ' outarray5 это mean_F_vert(V)_3l    
    ' outarray6 это mean_F_vert(V)_4l
    ' outarray7 это mean_F_vert(V)_3r
    ' outarray8 это mean_F_vert(V)_4r
    Mean_F_vertL = (abs(outarray1)+abs(outarray2)+abs(outarray5)+abs(outarray6))/4
    Mean_F_vertR = (abs(outarray3)+abs(outarray4)+abs(outarray7)+abs(outarray8))/4
    Mean_F_vert = (Mean_F_vertL+Mean_F_vertR)/2
    
    ' outarray9 это sigma_F_vert(V)_1l
    ' outarray10 это sigma_F_vert(V)_2l
    ' outarray11 это sigma_F_vert(V)_1r
    ' outarray12 это sigma_F_vert(V)_2r
    ' outarray13 это sigma_F_vert(V)_3l
    ' outarray14 это sigma_F_vert(V)_4l
    ' outarray15 это sigma_F_vert(V)_3r
    ' outarray16 это sigma_F_vert(V)_4r
    sigma_F_vertL = ((abs(outarray9)**2+abs(outarray10)**2+abs(outarray13)**2+abs(outarray14)**2)/4)**0.5
    sigma_F_vertR = ((abs(outarray11)**2+abs(outarray12)**2+abs(outarray15)**2+abs(outarray16)**2)/4)**0.5
    sigma_F_vert = ((Mean_F_vertL**2+Mean_F_vertR**2)/2)**0.5


    
    ' outarray17 это mean_F_side(L)_1l
    ' outarray18 это mean_F_side(L)_2l
    ' outarray19 это mean_F_side(L)_1r
    ' outarray20 это mean_F_side(L)_2r
    ' outarray21 это mean_F_side(L)_3l
    ' outarray22 это mean_F_side(L)_4l
    ' outarray23 это mean_F_side(L)_3r
    ' outarray24 это mean_F_side(L)_4r

    Mean_F_sideL = (abs(outarray17)+abs(outarray18)+abs(outarray21)+abs(outarray22))/4
    Mean_F_sideR = (abs(outarray19)+abs(outarray20)+abs(outarray23)+abs(outarray24))/4
    Mean_F_side = (Mean_F_sideL+Mean_F_sideR)/2



    ' outarray25 это sigma_F_side(L)_1l
    ' outarray26 это sigma_F_side(L)_2l
    ' outarray27 это sigma_F_side(L)_1r
    ' outarray28 это sigma_F_side(L)_2r
    ' outarray29 это sigma_F_side(L)_3l
    ' outarray30 это sigma_F_side(L)_4l
    ' outarray31 это sigma_F_side(L)_3r
    ' outarray32 это sigma_F_side(L)_4r

    sigma_F_sideL = ((abs(outarray25)**2+abs(outarray26)**2+abs(outarray29)**2+abs(outarray30)**2)/4)**0.5
    sigma_F_sideR = ((abs(outarray27)**2+abs(outarray28)**2+abs(outarray31)**2+abs(outarray32)**2)/4)**0.5
    sigma_F_side = ((sigma_F_sideL**2+sigma_F_sideR**2)/2)**0.5

    
    ' outarray33 это mean_H1
    ' outarray34 это mean_H2
    ' outarray35 это mean_H3
    ' outarray36 это mean_H4
    #'средние значения
    Mean_H = round(((abs(outarray33)+abs(outarray34)+abs(outarray35)+abs(outarray36))/4),1)
    
    #'СКО
    sigma_H = round((((abs(outarray37)**2+abs(outarray38)**2+abs(outarray39)**2+abs(outarray40)**2)/4)**0.5),1)
    



    ' outarray37 это sigma_H1
    ' outarray38 это sigma_H2
    ' outarray39 это sigma_H3
    ' outarray40 это sigma_H4'''
    
    VSP_type = input_val[0] 
    Condition = input_val[1] 
    Radius = input_val[2]
    h = input_val[3]
    V = input_val[4]
    axle_load = input_val[5]
    Sh_Kol = input_val[6] 
    mu_fr = input_val[7]

    #вычисление контактных напряжений
    
    from contact_pressure import contact_tension
    
    input_val1 = [V,axle_load, mu_fr, Radius, h, Sh_Kol]

    cont_press = contact_tension(input_val1)
    
    MeanP1NarkPa = cont_press[0]
    RmsP1NarkPa = cont_press[1]
    MeanP1VnrkPa  = cont_press[2]
    RmsP1VnrkPa = cont_press[3]
    MeanP2NarkPa = cont_press[4]
    RmsP2NarkPa = cont_press[5]
    MeanP2VnrkPa = cont_press[6]
    RmsP2VnrkPa = cont_press[7]

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
    Pos = axle_load
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
     
    if (Radius<200):
        Radius = 200
    if (Radius>10000):
        Radius = 10000
    Radius = (Radius - 200) / 9800
     
    if (h<0):
        h = 0
    if (h>160):
        h = 160
    h = h / 160
     
    if (V<5):
        V = 5
    if (V>110):
        V = 110
    V = (V - 5) / 105
     
    if (axle_load<5):
        axle_load = 5
    if (axle_load>30):
        axle_load = 30
    axle_load = (axle_load - 5) / 25
     
    if (Sh_Kol<1510):
        Sh_Kol = 1510
    if (Sh_Kol>1545):
        Sh_Kol = 1545
    Sh_Kol = (Sh_Kol - 1510) / 35
     
    if (mu_fr<0.1):
        mu_fr = 0.1
    if (mu_fr>0.75):
        mu_fr = 0.75
    mu_fr = (mu_fr - 0.1) / 0.65
     
    netsum = -0.8779284
    netsum = netsum + VSP_type * 0.0196113
    netsum = netsum + Condition * -1.628023E-02
    netsum = netsum + Radius * -0.3118623
    netsum = netsum + h * -0.6246858
    netsum = netsum + V * 3.431407
    netsum = netsum + axle_load * -0.5934311
    netsum = netsum + Sh_Kol * 1.635297E-02
    netsum = netsum + mu_fr * 6.492428E-02
    feature21 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.596228
    netsum = netsum + VSP_type * -9.683328E-03
    netsum = netsum + Condition * 0.4581077
    netsum = netsum + Radius * -0.1272031
    netsum = netsum + h * 2.014749E-02
    netsum = netsum + V * 0.7440364
    netsum = netsum + axle_load * 0.7920348
    netsum = netsum + Sh_Kol * 1.824367E-03
    netsum = netsum + mu_fr * 0.1039098
    feature22 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.637069
    netsum = netsum + VSP_type * 4.684691E-03
    netsum = netsum + Condition * 9.074254E-02
    netsum = netsum + Radius * 1.190828
    netsum = netsum + h * -0.649842
    netsum = netsum + V * 0.1637488
    netsum = netsum + axle_load * 3.08047
    netsum = netsum + Sh_Kol * -4.281888E-04
    netsum = netsum + mu_fr * 9.509201E-02
    feature23 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.3132215
    netsum = netsum + VSP_type * 3.73619E-03
    netsum = netsum + Condition * -0.4145217
    netsum = netsum + Radius * -0.8156928
    netsum = netsum + h * 0.2219606
    netsum = netsum + V * 4.334057E-02
    netsum = netsum + axle_load * 1.412599
    netsum = netsum + Sh_Kol * -2.731116E-03
    netsum = netsum + mu_fr * 0.6049104
    feature24 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.1855786
    netsum = netsum + VSP_type * 0.0195484
    netsum = netsum + Condition * -4.631246E-02
    netsum = netsum + Radius * -1.191343
    netsum = netsum + h * -0.6882868
    netsum = netsum + V * 3.358121
    netsum = netsum + axle_load * -0.2213472
    netsum = netsum + Sh_Kol * 0.0165094
    netsum = netsum + mu_fr * 0.1237197
    feature25 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.3112192
    netsum = netsum + VSP_type * -1.169685E-02
    netsum = netsum + Condition * -0.2254246
    netsum = netsum + Radius * 2.768906
    netsum = netsum + h * -0.4581332
    netsum = netsum + V * -0.3690927
    netsum = netsum + axle_load * 2.431689
    netsum = netsum + Sh_Kol * -1.615659E-03
    netsum = netsum + mu_fr * 1.612557E-03
    feature26 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.003194
    netsum = netsum + VSP_type * -0.0187494
    netsum = netsum + Condition * -0.3636706
    netsum = netsum + Radius * -15.39569
    netsum = netsum + h * 0.2740369
    netsum = netsum + V * -2.167522
    netsum = netsum + axle_load * 2.241904
    netsum = netsum + Sh_Kol * -1.543768E-03
    netsum = netsum + mu_fr * -2.651174
    feature27 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.252788
    netsum = netsum + VSP_type * -3.139062E-03
    netsum = netsum + Condition * -5.410749E-02
    netsum = netsum + Radius * -4.877655
    netsum = netsum + h * -0.526661
    netsum = netsum + V * 1.078479
    netsum = netsum + axle_load * 4.777053
    netsum = netsum + Sh_Kol * 2.01018E-03
    netsum = netsum + mu_fr * 0.114046
    feature28 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.3193696
    netsum = netsum + VSP_type * 1.261251E-03
    netsum = netsum + Condition * -0.2162307
    netsum = netsum + Radius * -0.9862177
    netsum = netsum + h * 0.1891039
    netsum = netsum + V * -0.1852484
    netsum = netsum + axle_load * -1.234742
    netsum = netsum + Sh_Kol * -1.570796E-03
    netsum = netsum + mu_fr * -4.251175E-02
    feature29 = 1 / (1 + math.exp(-netsum))
     
    netsum = 4.534059
    netsum = netsum + VSP_type * 1.788649E-03
    netsum = netsum + Condition * -0.1028314
    netsum = netsum + Radius * -3.500344
    netsum = netsum + h * -4.595692E-02
    netsum = netsum + V * 0.3912673
    netsum = netsum + axle_load * -0.5823087
    netsum = netsum + Sh_Kol * 1.610751E-03
    netsum = netsum + mu_fr * 0.1503751
    feature210 = 1 / (1 + math.exp(-netsum))
     
    netsum = 5.107103E-02
    netsum = netsum + VSP_type * -4.374513E-03
    netsum = netsum + Condition * -0.3509284
    netsum = netsum + Radius * -0.1275357
    netsum = netsum + h * -2.12247E-03
    netsum = netsum + V * 0.7795217
    netsum = netsum + axle_load * -0.409476
    netsum = netsum + Sh_Kol * 1.62673E-04
    netsum = netsum + mu_fr * 0.7189066
    feature211 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.833507
    netsum = netsum + VSP_type * 1.018576E-03
    netsum = netsum + Condition * -2.597385E-02
    netsum = netsum + Radius * -19.02908
    netsum = netsum + h * 0.0633862
    netsum = netsum + V * 1.627645
    netsum = netsum + axle_load * 3.308038
    netsum = netsum + Sh_Kol * -5.233867E-03
    netsum = netsum + mu_fr * 1.417578
    feature212 = 1 / (1 + math.exp(-netsum))
     
    netsum = -5.813908
    netsum = netsum + VSP_type * 1.001322E-03
    netsum = netsum + Condition * 2.190794E-02
    netsum = netsum + Radius * -50.41639
    netsum = netsum + h * -2.634212E-02
    netsum = netsum + V * 2.256421
    netsum = netsum + axle_load * 2.354749
    netsum = netsum + Sh_Kol * -8.436926E-04
    netsum = netsum + mu_fr * 0.1733611
    feature213 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.883401
    netsum = netsum + VSP_type * -8.898498E-05
    netsum = netsum + Condition * 2.826454E-02
    netsum = netsum + Radius * -1.060984
    netsum = netsum + h * 0.5535195
    netsum = netsum + V * 0.1165256
    netsum = netsum + axle_load * 4.197912
    netsum = netsum + Sh_Kol * 1.594416E-04
    netsum = netsum + mu_fr * 9.258552E-02
    feature214 = 1 / (1 + math.exp(-netsum))
     
    netsum = -6.936395
    netsum = netsum + VSP_type * 2.406313E-02
    netsum = netsum + Condition * -8.170411E-02
    netsum = netsum + Radius * -7.999993
    netsum = netsum + h * -0.1415604
    netsum = netsum + V * 2.002038
    netsum = netsum + axle_load * 1.907866
    netsum = netsum + Sh_Kol * -9.61585E-03
    netsum = netsum + mu_fr * 3.299991
    feature215 = 1 / (1 + math.exp(-netsum))
     
    netsum = 2.437062
    netsum = netsum + VSP_type * 0.0104815
    netsum = netsum + Condition * -3.266933E-02
    netsum = netsum + Radius * 6.633762
    netsum = netsum + h * -0.1551777
    netsum = netsum + V * -0.841204
    netsum = netsum + axle_load * 0.8992872
    netsum = netsum + Sh_Kol * -1.115624E-04
    netsum = netsum + mu_fr * -0.2477242
    feature216 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.578948
    netsum = netsum + VSP_type * -3.70922E-03
    netsum = netsum + Condition * -1.505512E-02
    netsum = netsum + Radius * -7.1371
    netsum = netsum + h * -0.434656
    netsum = netsum + V * 1.956263
    netsum = netsum + axle_load * 3.0549
    netsum = netsum + Sh_Kol * 0
    netsum = netsum + mu_fr * 0.1731671
    feature217 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.487802
    netsum = netsum + VSP_type * 2.375992E-02
    netsum = netsum + Condition * -2.062043E-02
    netsum = netsum + Radius * 0.471993
    netsum = netsum + h * -0.6646476
    netsum = netsum + V * 3.761829
    netsum = netsum + axle_load * -1.018315
    netsum = netsum + Sh_Kol * 2.035947E-02
    netsum = netsum + mu_fr * -0.1628135
    feature218 = 1 / (1 + math.exp(-netsum))
     
    netsum = -7.835839E-02
    netsum = netsum + VSP_type * 1.346537E-02
    netsum = netsum + Condition * 2.545992
    netsum = netsum + Radius * -3.239025
    netsum = netsum + h * -9.360485E-04
    netsum = netsum + V * 0.2478446
    netsum = netsum + axle_load * 0.1425488
    netsum = netsum + Sh_Kol * 1.394994E-03
    netsum = netsum + mu_fr * 6.538581E-02
    feature219 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.0851
    netsum = netsum + VSP_type * 1.46911E-03
    netsum = netsum + Condition * -2.505987E-02
    netsum = netsum + Radius * -0.3247593
    netsum = netsum + h * 0.2009234
    netsum = netsum + V * 1.330669
    netsum = netsum + axle_load * 0.6237336
    netsum = netsum + Sh_Kol * 4.473175E-03
    netsum = netsum + mu_fr * -2.964767E-02
    feature220 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.2814425
    netsum = netsum + VSP_type * 8.441789E-04
    netsum = netsum + Condition * -2.339525E-02
    netsum = netsum + Radius * -1.186471
    netsum = netsum + h * 0.1148786
    netsum = netsum + V * -0.1348869
    netsum = netsum + axle_load * 2.080524
    netsum = netsum + Sh_Kol * 1.38199E-04
    netsum = netsum + mu_fr * -0.154547
    feature221 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.546066
    netsum = netsum + VSP_type * -1.642044E-02
    netsum = netsum + Condition * -0.3496358
    netsum = netsum + Radius * -20.86767
    netsum = netsum + h * 0.2272356
    netsum = netsum + V * -1.518378
    netsum = netsum + axle_load * 2.167108
    netsum = netsum + Sh_Kol * -1.723164E-03
    netsum = netsum + mu_fr * -3.557379
    feature222 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.13996
    netsum = netsum + VSP_type * -1.379909E-03
    netsum = netsum + Condition * 5.425036E-02
    netsum = netsum + Radius * -33.27554
    netsum = netsum + h * 1.016273E-02
    netsum = netsum + V * 1.195987
    netsum = netsum + axle_load * 2.318208
    netsum = netsum + Sh_Kol * -2.223326E-03
    netsum = netsum + mu_fr * 0.3550184
    feature223 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.5040051
    netsum = netsum + VSP_type * 3.215188E-03
    netsum = netsum + Condition * 7.419364E-03
    netsum = netsum + Radius * 1.464642
    netsum = netsum + h * -0.4642037
    netsum = netsum + V * -0.5562761
    netsum = netsum + axle_load * -1.691309
    netsum = netsum + Sh_Kol * -2.340981E-03
    netsum = netsum + mu_fr * -0.1666984
    feature224 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.334876
    netsum = netsum + VSP_type * -1.773412E-03
    netsum = netsum + Condition * -4.815851E-03
    netsum = netsum + Radius * -12.42461
    netsum = netsum + h * -0.2524016
    netsum = netsum + V * 1.771035
    netsum = netsum + axle_load * 4.579422
    netsum = netsum + Sh_Kol * -3.722528E-03
    netsum = netsum + mu_fr * 0.167773
    feature225 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.5910046
    netsum = netsum + feature21 * 0.4676746
    netsum = netsum + feature22 * 0.153518
    netsum = netsum + feature23 * 0.7715832
    netsum = netsum + feature24 * 0.121013
    netsum = netsum + feature25 * -0.3551949
    netsum = netsum + feature26 * -0.3248742
    netsum = netsum + feature27 * 0.0880947
    netsum = netsum + feature28 * 0.8694144
    netsum = netsum + feature29 * -0.5628607
    netsum = netsum + feature210 * -0.1721558
    netsum = netsum + feature211 * 0.0740873
    netsum = netsum + feature212 * 0.1838181
    netsum = netsum + feature213 * 9.735654
    netsum = netsum + feature214 * -0.9197085
    netsum = netsum + feature215 * -0.3556137
    netsum = netsum + feature216 * -0.7286445
    netsum = netsum + feature217 * -0.9346861
    netsum = netsum + feature218 * -0.167161
    netsum = netsum + feature219 * -8.921844E-02
    netsum = netsum + feature220 * 0.2826763
    netsum = netsum + feature221 * 0.618141
    netsum = netsum + feature222 * -0.2581779
    netsum = netsum + feature223 * -3.224097
    netsum = netsum + feature224 * 0.5334088
    netsum = netsum + feature225 * 1.098175
    outarray1 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.6178949
    netsum = netsum + feature21 * 0.3974172
    netsum = netsum + feature22 * 0.1563303
    netsum = netsum + feature23 * 0.7654977
    netsum = netsum + feature24 * 0.3534194
    netsum = netsum + feature25 * -0.2804792
    netsum = netsum + feature26 * -0.2397466
    netsum = netsum + feature27 * 0.172621
    netsum = netsum + feature28 * 0.7269009
    netsum = netsum + feature29 * -0.5846642
    netsum = netsum + feature210 * -5.231767E-02
    netsum = netsum + feature211 * -0.1757264
    netsum = netsum + feature212 * 0.2023043
    netsum = netsum + feature213 * 9.978025
    netsum = netsum + feature214 * -1.004765
    netsum = netsum + feature215 * -0.2980122
    netsum = netsum + feature216 * -0.782156
    netsum = netsum + feature217 * -0.814315
    netsum = netsum + feature218 * -0.1202252
    netsum = netsum + feature219 * -7.649317E-02
    netsum = netsum + feature220 * 0.2310165
    netsum = netsum + feature221 * 0.4250831
    netsum = netsum + feature222 * -0.4374392
    netsum = netsum + feature223 * -3.458215
    netsum = netsum + feature224 * 0.4705696
    netsum = netsum + feature225 * 1.097835
    outarray2 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.3278839
    netsum = netsum + feature21 * -0.7784334
    netsum = netsum + feature22 * -0.2087741
    netsum = netsum + feature23 * -0.3633843
    netsum = netsum + feature24 * 9.388049E-02
    netsum = netsum + feature25 * 0.5140619
    netsum = netsum + feature26 * 0.5187399
    netsum = netsum + feature27 * 0.3941836
    netsum = netsum + feature28 * -0.8053547
    netsum = netsum + feature29 * -0.4140438
    netsum = netsum + feature210 * -0.5631438
    netsum = netsum + feature211 * 9.715674E-02
    netsum = netsum + feature212 * -0.2053899
    netsum = netsum + feature213 * -7.300817
    netsum = netsum + feature214 * 1.532844
    netsum = netsum + feature215 * 0.2563372
    netsum = netsum + feature216 * 0.8393056
    netsum = netsum + feature217 * 0.7444143
    netsum = netsum + feature218 * 0.3520651
    netsum = netsum + feature219 * 0.1103946
    netsum = netsum + feature220 * -0.3243998
    netsum = netsum + feature221 * 0.8525276
    netsum = netsum + feature222 * -0.3522995
    netsum = netsum + feature223 * 2.405329
    netsum = netsum + feature224 * -0.6956829
    netsum = netsum + feature225 * -0.8671932
    outarray3 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.164804
    netsum = netsum + feature21 * -0.8485013
    netsum = netsum + feature22 * -0.2071351
    netsum = netsum + feature23 * -0.324478
    netsum = netsum + feature24 * -2.560488E-02
    netsum = netsum + feature25 * 0.5517532
    netsum = netsum + feature26 * 0.5077131
    netsum = netsum + feature27 * 0.397075
    netsum = netsum + feature28 * -0.7956734
    netsum = netsum + feature29 * -0.5005944
    netsum = netsum + feature210 * -0.4811373
    netsum = netsum + feature211 * 0.1432692
    netsum = netsum + feature212 * -0.3039643
    netsum = netsum + feature213 * -6.725953
    netsum = netsum + feature214 * 1.486712
    netsum = netsum + feature215 * 0.4065414
    netsum = netsum + feature216 * 0.7426647
    netsum = netsum + feature217 * 0.7257034
    netsum = netsum + feature218 * 0.3755021
    netsum = netsum + feature219 * 0.0779283
    netsum = netsum + feature220 * -0.4253556
    netsum = netsum + feature221 * 0.8688537
    netsum = netsum + feature222 * -0.4544821
    netsum = netsum + feature223 * 2.155443
    netsum = netsum + feature224 * -0.7710276
    netsum = netsum + feature225 * -0.7761282
    outarray4 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.6479098
    netsum = netsum + feature21 * 0.4553233
    netsum = netsum + feature22 * 9.985083E-02
    netsum = netsum + feature23 * 0.788224
    netsum = netsum + feature24 * 0.2176718
    netsum = netsum + feature25 * -0.3254178
    netsum = netsum + feature26 * -0.2427426
    netsum = netsum + feature27 * 0.141133
    netsum = netsum + feature28 * 0.7869259
    netsum = netsum + feature29 * -0.5358567
    netsum = netsum + feature210 * -0.1102665
    netsum = netsum + feature211 * -5.515251E-02
    netsum = netsum + feature212 * 0.1492118
    netsum = netsum + feature213 * 9.970271
    netsum = netsum + feature214 * -0.9796157
    netsum = netsum + feature215 * -0.2320335
    netsum = netsum + feature216 * -0.7780719
    netsum = netsum + feature217 * -0.8688077
    netsum = netsum + feature218 * -0.1446787
    netsum = netsum + feature219 * -6.757702E-02
    netsum = netsum + feature220 * 0.2125923
    netsum = netsum + feature221 * 0.513426
    netsum = netsum + feature222 * -0.407477
    netsum = netsum + feature223 * -3.417006
    netsum = netsum + feature224 * 0.4513863
    netsum = netsum + feature225 * 1.134807
    outarray5 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.534664
    netsum = netsum + feature21 * 0.5657909
    netsum = netsum + feature22 * 0.1938858
    netsum = netsum + feature23 * 0.769861
    netsum = netsum + feature24 * 0.323707
    netsum = netsum + feature25 * -0.3927948
    netsum = netsum + feature26 * -0.3291752
    netsum = netsum + feature27 * 1.798386E-02
    netsum = netsum + feature28 * 0.8488866
    netsum = netsum + feature29 * -0.5760828
    netsum = netsum + feature210 * -0.1125463
    netsum = netsum + feature211 * -0.1149658
    netsum = netsum + feature212 * 0.2714466
    netsum = netsum + feature213 * 9.195269
    netsum = netsum + feature214 * -0.9361725
    netsum = netsum + feature215 * -0.4698191
    netsum = netsum + feature216 * -0.723328
    netsum = netsum + feature217 * -0.9135879
    netsum = netsum + feature218 * -0.2050285
    netsum = netsum + feature219 * -9.102254E-02
    netsum = netsum + feature220 * 0.3360762
    netsum = netsum + feature221 * 0.4908376
    netsum = netsum + feature222 * -0.1612042
    netsum = netsum + feature223 * -3.062356
    netsum = netsum + feature224 * 0.5903768
    netsum = netsum + feature225 * 1.034064
    outarray6 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.1974576
    netsum = netsum + feature21 * -0.9144153
    netsum = netsum + feature22 * -0.1828144
    netsum = netsum + feature23 * -0.3551986
    netsum = netsum + feature24 * 9.254902E-02
    netsum = netsum + feature25 * 0.5953339
    netsum = netsum + feature26 * 0.534924
    netsum = netsum + feature27 * 0.43466
    netsum = netsum + feature28 * -0.8682237
    netsum = netsum + feature29 * -0.5246946
    netsum = netsum + feature210 * -0.4414691
    netsum = netsum + feature211 * 5.067753E-02
    netsum = netsum + feature212 * -0.2920214
    netsum = netsum + feature213 * -6.579281
    netsum = netsum + feature214 * 1.44609
    netsum = netsum + feature215 * 0.40385
    netsum = netsum + feature216 * 0.7356561
    netsum = netsum + feature217 * 0.7755949
    netsum = netsum + feature218 * 0.4140566
    netsum = netsum + feature219 * 8.237474E-02
    netsum = netsum + feature220 * -0.4204783
    netsum = netsum + feature221 * 0.8081989
    netsum = netsum + feature222 * -0.4922127
    netsum = netsum + feature223 * 2.100229
    netsum = netsum + feature224 * -0.7691453
    netsum = netsum + feature225 * -0.7821053
    outarray7 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.2561117
    netsum = netsum + feature21 * -0.8565488
    netsum = netsum + feature22 * -0.2128047
    netsum = netsum + feature23 * -0.3576496
    netsum = netsum + feature24 * -9.518412E-02
    netsum = netsum + feature25 * 0.5424651
    netsum = netsum + feature26 * 0.5041564
    netsum = netsum + feature27 * 0.4547309
    netsum = netsum + feature28 * -0.7788351
    netsum = netsum + feature29 * -0.4341501
    netsum = netsum + feature210 * -0.587033
    netsum = netsum + feature211 * 0.2607703
    netsum = netsum + feature212 * -0.2553709
    netsum = netsum + feature213 * -6.980749
    netsum = netsum + feature214 * 1.561849
    netsum = netsum + feature215 * 0.3242879
    netsum = netsum + feature216 * 0.821121
    netsum = netsum + feature217 * 0.72686
    netsum = netsum + feature218 * 0.3734479
    netsum = netsum + feature219 * 9.618893E-02
    netsum = netsum + feature220 * -0.3733674
    netsum = netsum + feature221 * 0.9570783
    netsum = netsum + feature222 * -0.425447
    netsum = netsum + feature223 * 2.274691
    netsum = netsum + feature224 * -0.7418082
    netsum = netsum + feature225 * -0.8298314
    outarray8 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.285194E-02
    netsum = netsum + feature21 * -0.7076171
    netsum = netsum + feature22 * 0.2088495
    netsum = netsum + feature23 * 0.1005929
    netsum = netsum + feature24 * 0.1783138
    netsum = netsum + feature25 * 0.4314993
    netsum = netsum + feature26 * -9.738644E-02
    netsum = netsum + feature27 * -3.337545E-02
    netsum = netsum + feature28 * 1.942581E-02
    netsum = netsum + feature29 * -0.0836461
    netsum = netsum + feature210 * -0.0425932
    netsum = netsum + feature211 * -0.1404363
    netsum = netsum + feature212 * 0.1325815
    netsum = netsum + feature213 * 0.3715046
    netsum = netsum + feature214 * -0.1028009
    netsum = netsum + feature215 * -4.950707E-02
    netsum = netsum + feature216 * 9.279688E-02
    netsum = netsum + feature217 * 0.1527475
    netsum = netsum + feature218 * 0.2410512
    netsum = netsum + feature219 * -3.319473E-02
    netsum = netsum + feature220 * 0.2424095
    netsum = netsum + feature221 * -0.2059663
    netsum = netsum + feature222 * 0.1075844
    netsum = netsum + feature223 * -0.2649454
    netsum = netsum + feature224 * 0.1217912
    netsum = netsum + feature225 * -0.1243609
    outarray9 = 1 / (1 + math.exp(-netsum))
     
    netsum = -7.966814E-02
    netsum = netsum + feature21 * -0.6839097
    netsum = netsum + feature22 * 9.232419E-02
    netsum = netsum + feature23 * 0.1121814
    netsum = netsum + feature24 * 0.1335966
    netsum = netsum + feature25 * 0.3909144
    netsum = netsum + feature26 * -7.125718E-02
    netsum = netsum + feature27 * 0.1178851
    netsum = netsum + feature28 * 2.766999E-02
    netsum = netsum + feature29 * -0.103396
    netsum = netsum + feature210 * -2.695517E-02
    netsum = netsum + feature211 * -5.406244E-02
    netsum = netsum + feature212 * 8.103447E-02
    netsum = netsum + feature213 * 0.2879583
    netsum = netsum + feature214 * -0.1132597
    netsum = netsum + feature215 * -2.449199E-02
    netsum = netsum + feature216 * 0.0477157
    netsum = netsum + feature217 * 8.522675E-02
    netsum = netsum + feature218 * 0.2471665
    netsum = netsum + feature219 * -3.048959E-03
    netsum = netsum + feature220 * 0.3251563
    netsum = netsum + feature221 * -0.1320894
    netsum = netsum + feature222 * -0.1234804
    netsum = netsum + feature223 * -0.1844018
    netsum = netsum + feature224 * 0.1462408
    netsum = netsum + feature225 * -8.204897E-02
    outarray10 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.266763E-02
    netsum = netsum + feature21 * -0.6879297
    netsum = netsum + feature22 * 0.1247807
    netsum = netsum + feature23 * 9.906301E-02
    netsum = netsum + feature24 * 0.1541796
    netsum = netsum + feature25 * 0.4365071
    netsum = netsum + feature26 * -7.904745E-02
    netsum = netsum + feature27 * -5.670798E-02
    netsum = netsum + feature28 * 2.597244E-02
    netsum = netsum + feature29 * -4.181736E-02
    netsum = netsum + feature210 * -0.1104536
    netsum = netsum + feature211 * -0.1163966
    netsum = netsum + feature212 * 0.1103363
    netsum = netsum + feature213 * 0.1769232
    netsum = netsum + feature214 * -7.504701E-02
    netsum = netsum + feature215 * -4.300296E-02
    netsum = netsum + feature216 * 0.137261
    netsum = netsum + feature217 * 0.1398915
    netsum = netsum + feature218 * 0.2246181
    netsum = netsum + feature219 * -1.011241E-02
    netsum = netsum + feature220 * 0.276731
    netsum = netsum + feature221 * -0.1912415
    netsum = netsum + feature222 * 0.1287928
    netsum = netsum + feature223 * -0.1641963
    netsum = netsum + feature224 * 0.101349
    netsum = netsum + feature225 * -0.1297902
    outarray11 = 1 / (1 + math.exp(-netsum))
     
    netsum = -8.608222E-02
    netsum = netsum + feature21 * -0.6841068
    netsum = netsum + feature22 * 6.393795E-02
    netsum = netsum + feature23 * 0.1036721
    netsum = netsum + feature24 * 0.1156264
    netsum = netsum + feature25 * 0.3880677
    netsum = netsum + feature26 * -0.0679258
    netsum = netsum + feature27 * 9.622445E-02
    netsum = netsum + feature28 * 3.191493E-02
    netsum = netsum + feature29 * -8.425737E-02
    netsum = netsum + feature210 * -6.588635E-02
    netsum = netsum + feature211 * -2.743858E-02
    netsum = netsum + feature212 * 5.207845E-02
    netsum = netsum + feature213 * 0.2121047
    netsum = netsum + feature214 * -9.467597E-02
    netsum = netsum + feature215 * 1.443428E-02
    netsum = netsum + feature216 * 8.104354E-02
    netsum = netsum + feature217 * 7.168642E-02
    netsum = netsum + feature218 * 0.2507441
    netsum = netsum + feature219 * 7.332092E-03
    netsum = netsum + feature220 * 0.3197913
    netsum = netsum + feature221 * -0.1121016
    netsum = netsum + feature222 * -9.200578E-02
    netsum = netsum + feature223 * -0.153581
    netsum = netsum + feature224 * 0.1323175
    netsum = netsum + feature225 * -6.833058E-02
    outarray12 = 1 / (1 + math.exp(-netsum))
     
    netsum = 7.932802E-02
    netsum = netsum + feature21 * -0.862417
    netsum = netsum + feature22 * 0.2185032
    netsum = netsum + feature23 * 0.1016212
    netsum = netsum + feature24 * 0.1562566
    netsum = netsum + feature25 * 0.5312375
    netsum = netsum + feature26 * -0.1281282
    netsum = netsum + feature27 * -4.929374E-02
    netsum = netsum + feature28 * 2.431457E-02
    netsum = netsum + feature29 * -0.1392604
    netsum = netsum + feature210 * -7.610288E-02
    netsum = netsum + feature211 * -0.1350117
    netsum = netsum + feature212 * 0.1769107
    netsum = netsum + feature213 * 0.5162354
    netsum = netsum + feature214 * -0.1138052
    netsum = netsum + feature215 * -8.892351E-02
    netsum = netsum + feature216 * 9.698697E-02
    netsum = netsum + feature217 * 0.1687607
    netsum = netsum + feature218 * 0.2980546
    netsum = netsum + feature219 * -4.784997E-02
    netsum = netsum + feature220 * 0.1769145
    netsum = netsum + feature221 * -0.2273774
    netsum = netsum + feature222 * 0.1438989
    netsum = netsum + feature223 * -0.3883738
    netsum = netsum + feature224 * 8.527741E-02
    netsum = netsum + feature225 * -0.1315345
    outarray13 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.586405E-03
    netsum = netsum + feature21 * -0.6134783
    netsum = netsum + feature22 * 0.1398467
    netsum = netsum + feature23 * 8.685317E-02
    netsum = netsum + feature24 * 8.402548E-02
    netsum = netsum + feature25 * 0.3765116
    netsum = netsum + feature26 * -6.077626E-02
    netsum = netsum + feature27 * 4.896756E-02
    netsum = netsum + feature28 * 8.673498E-03
    netsum = netsum + feature29 * -0.1101577
    netsum = netsum + feature210 * 4.863643E-03
    netsum = netsum + feature211 * -0.0674628
    netsum = netsum + feature212 * 5.564898E-02
    netsum = netsum + feature213 * 0.1884878
    netsum = netsum + feature214 * -9.736215E-02
    netsum = netsum + feature215 * -4.421674E-03
    netsum = netsum + feature216 * 3.519465E-02
    netsum = netsum + feature217 * 8.305583E-02
    netsum = netsum + feature218 * 0.2015002
    netsum = netsum + feature219 * -2.648737E-02
    netsum = netsum + feature220 * 0.2145119
    netsum = netsum + feature221 * -0.1398563
    netsum = netsum + feature222 * -3.947678E-02
    netsum = netsum + feature223 * -0.1117221
    netsum = netsum + feature224 * 7.496893E-02
    netsum = netsum + feature225 * -6.642521E-02
    outarray14 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.0431067
    netsum = netsum + feature21 * -0.8951464
    netsum = netsum + feature22 * 7.646794E-02
    netsum = netsum + feature23 * 0.1026838
    netsum = netsum + feature24 * 0.1379751
    netsum = netsum + feature25 * 0.5598565
    netsum = netsum + feature26 * -7.301103E-02
    netsum = netsum + feature27 * -8.082351E-02
    netsum = netsum + feature28 * -7.414679E-04
    netsum = netsum + feature29 * -6.021904E-02
    netsum = netsum + feature210 * -0.152492
    netsum = netsum + feature211 * -0.1051785
    netsum = netsum + feature212 * 0.1137142
    netsum = netsum + feature213 * 0.2560272
    netsum = netsum + feature214 * -7.736931E-02
    netsum = netsum + feature215 * -1.868241E-02
    netsum = netsum + feature216 * 0.1745165
    netsum = netsum + feature217 * 0.1849758
    netsum = netsum + feature218 * 0.3177326
    netsum = netsum + feature219 * -2.717282E-03
    netsum = netsum + feature220 * 0.2153737
    netsum = netsum + feature221 * -0.2212202
    netsum = netsum + feature222 * 0.1725202
    netsum = netsum + feature223 * -0.2310837
    netsum = netsum + feature224 * 3.113598E-02
    netsum = netsum + feature225 * -0.1384838
    outarray15 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.601898E-02
    netsum = netsum + feature21 * -0.5606429
    netsum = netsum + feature22 * 3.791884E-02
    netsum = netsum + feature23 * 9.231119E-02
    netsum = netsum + feature24 * 5.084486E-02
    netsum = netsum + feature25 * 0.3565283
    netsum = netsum + feature26 * -1.864759E-02
    netsum = netsum + feature27 * 1.374653E-02
    netsum = netsum + feature28 * 3.420549E-03
    netsum = netsum + feature29 * -5.026943E-02
    netsum = netsum + feature210 * -4.186866E-02
    netsum = netsum + feature211 * -2.573906E-02
    netsum = netsum + feature212 * 4.537389E-02
    netsum = netsum + feature213 * 8.84438E-03
    netsum = netsum + feature214 * -7.203873E-02
    netsum = netsum + feature215 * -4.648749E-03
    netsum = netsum + feature216 * 7.587684E-02
    netsum = netsum + feature217 * 7.968081E-02
    netsum = netsum + feature218 * 0.1730068
    netsum = netsum + feature219 * 6.582209E-03
    netsum = netsum + feature220 * 0.2647083
    netsum = netsum + feature221 * -0.1154854
    netsum = netsum + feature222 * 1.943755E-02
    netsum = netsum + feature223 * -2.266277E-02
    netsum = netsum + feature224 * 5.153334E-02
    netsum = netsum + feature225 * -8.236165E-02
    outarray16 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.2004959
    netsum = netsum + feature21 * 1.064312E-02
    netsum = netsum + feature22 * 0.5470435
    netsum = netsum + feature23 * -0.1328462
    netsum = netsum + feature24 * 0.5892101
    netsum = netsum + feature25 * 2.692176E-02
    netsum = netsum + feature26 * -0.1398764
    netsum = netsum + feature27 * -2.235219
    netsum = netsum + feature28 * -0.2678176
    netsum = netsum + feature29 * -0.6304066
    netsum = netsum + feature210 * 0.8686233
    netsum = netsum + feature211 * -0.895759
    netsum = netsum + feature212 * 0.3399717
    netsum = netsum + feature213 * -0.1494467
    netsum = netsum + feature214 * 0.3271062
    netsum = netsum + feature215 * 0.7938711
    netsum = netsum + feature216 * 0
    netsum = netsum + feature217 * 0.225063
    netsum = netsum + feature218 * -9.450326E-03
    netsum = netsum + feature219 * -0.2457465
    netsum = netsum + feature220 * -0.3361732
    netsum = netsum + feature221 * -0.7375644
    netsum = netsum + feature222 * 4.272062
    netsum = netsum + feature223 * -1.811951
    netsum = netsum + feature224 * -0.2272466
    netsum = netsum + feature225 * -0.4039873
    outarray17 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.600235E-02
    netsum = netsum + feature21 * -0.1989832
    netsum = netsum + feature22 * -4.622339E-02
    netsum = netsum + feature23 * -2.638208E-02
    netsum = netsum + feature24 * 0.0958093
    netsum = netsum + feature25 * 0.245907
    netsum = netsum + feature26 * 9.158865E-02
    netsum = netsum + feature27 * 0.9882524
    netsum = netsum + feature28 * -0.4460606
    netsum = netsum + feature29 * -0.1352365
    netsum = netsum + feature210 * 0.1953002
    netsum = netsum + feature211 * -0.279787
    netsum = netsum + feature212 * 1.652651
    netsum = netsum + feature213 * -2.528264
    netsum = netsum + feature214 * 0.2320567
    netsum = netsum + feature215 * -1.860072
    netsum = netsum + feature216 * 0.4628718
    netsum = netsum + feature217 * 0.706215
    netsum = netsum + feature218 * -0.0378284
    netsum = netsum + feature219 * -2.381884E-02
    netsum = netsum + feature220 * -0.1044
    netsum = netsum + feature221 * -0.4397498
    netsum = netsum + feature222 * -1.594632
    netsum = netsum + feature223 * -1.371189
    netsum = netsum + feature224 * -0.4175567
    netsum = netsum + feature225 * -0.8517723
    outarray18 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.3975233
    netsum = netsum + feature21 * -0.2807255
    netsum = netsum + feature22 * -0.5648383
    netsum = netsum + feature23 * -0.1938709
    netsum = netsum + feature24 * -0.6557908
    netsum = netsum + feature25 * 0.1747649
    netsum = netsum + feature26 * 0.2068193
    netsum = netsum + feature27 * 2.562183
    netsum = netsum + feature28 * -0.0502165
    netsum = netsum + feature29 * 0.5206664
    netsum = netsum + feature210 * -0.9910026
    netsum = netsum + feature211 * 0.9297303
    netsum = netsum + feature212 * -0.6409851
    netsum = netsum + feature213 * -5.139451
    netsum = netsum + feature214 * 0.3717547
    netsum = netsum + feature215 * -0.3880104
    netsum = netsum + feature216 * 0.5581027
    netsum = netsum + feature217 * 8.50129E-03
    netsum = netsum + feature218 * 7.094616E-02
    netsum = netsum + feature219 * 0.2391349
    netsum = netsum + feature220 * 0.2557707
    netsum = netsum + feature221 * 0.7952533
    netsum = netsum + feature222 * -4.897451
    netsum = netsum + feature223 * 3.617627
    netsum = netsum + feature224 * -8.093408E-02
    netsum = netsum + feature225 * 4.628133E-02
    outarray19 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.4493698
    netsum = netsum + feature21 * -0.2158783
    netsum = netsum + feature22 * -0.1788772
    netsum = netsum + feature23 * -0.3178613
    netsum = netsum + feature24 * -0.1524076
    netsum = netsum + feature25 * 0.0468164
    netsum = netsum + feature26 * 0.1836744
    netsum = netsum + feature27 * -0.9141495
    netsum = netsum + feature28 * -1.512811E-02
    netsum = netsum + feature29 * 0.3919276
    netsum = netsum + feature210 * -0.5547231
    netsum = netsum + feature211 * 0.4142978
    netsum = netsum + feature212 * -1.834713
    netsum = netsum + feature213 * -2.35496
    netsum = netsum + feature214 * 0.4686331
    netsum = netsum + feature215 * 2.103957
    netsum = netsum + feature216 * 0.3281103
    netsum = netsum + feature217 * -0.2858336
    netsum = netsum + feature218 * 0.1960824
    netsum = netsum + feature219 * 0.1521183
    netsum = netsum + feature220 * -2.866123E-03
    netsum = netsum + feature221 * 0.5637525
    netsum = netsum + feature222 * 1.757553
    netsum = netsum + feature223 * 3.103899
    netsum = netsum + feature224 * 1.033181E-02
    netsum = netsum + feature225 * 0.3539754
    outarray20 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.329323E-02
    netsum = netsum + feature21 * -4.940293E-02
    netsum = netsum + feature22 * 0.4656545
    netsum = netsum + feature23 * -9.681116E-02
    netsum = netsum + feature24 * 0.473836
    netsum = netsum + feature25 * 1.985656E-02
    netsum = netsum + feature26 * -0.1739673
    netsum = netsum + feature27 * -2.191253
    netsum = netsum + feature28 * -0.2382315
    netsum = netsum + feature29 * -0.5303782
    netsum = netsum + feature210 * 0.7426797
    netsum = netsum + feature211 * -0.7418125
    netsum = netsum + feature212 * 0.1352199
    netsum = netsum + feature213 * -0.2197036
    netsum = netsum + feature214 * 0.3941032
    netsum = netsum + feature215 * 0.9580154
    netsum = netsum + feature216 * 0.2877409
    netsum = netsum + feature217 * 0.2255759
    netsum = netsum + feature218 * 5.280793E-02
    netsum = netsum + feature219 * -0.2201115
    netsum = netsum + feature220 * -0.330071
    netsum = netsum + feature221 * -0.6398184
    netsum = netsum + feature222 * 4.127397
    netsum = netsum + feature223 * -1.392447
    netsum = netsum + feature224 * -0.2423203
    netsum = netsum + feature225 * -0.4176259
    outarray21 = 1 / (1 + math.exp(-netsum))
     
    netsum = -7.079104E-02
    netsum = netsum + feature21 * 3.836608E-02
    netsum = netsum + feature22 * -0.2409236
    netsum = netsum + feature23 * -4.214456E-02
    netsum = netsum + feature24 * 0.0101113
    netsum = netsum + feature25 * 0.1229013
    netsum = netsum + feature26 * 0.2246649
    netsum = netsum + feature27 * 1.040253
    netsum = netsum + feature28 * -0.3956188
    netsum = netsum + feature29 * 0.1098201
    netsum = netsum + feature210 * -2.915872E-03
    netsum = netsum + feature211 * -0.1174589
    netsum = netsum + feature212 * 1.76592
    netsum = netsum + feature213 * -1.689116
    netsum = netsum + feature214 * 0.190192
    netsum = netsum + feature215 * -2.174724
    netsum = netsum + feature216 * 0.4194688
    netsum = netsum + feature217 * 0.5525334
    netsum = netsum + feature218 * -0.1114702
    netsum = netsum + feature219 * 7.485327E-02
    netsum = netsum + feature220 * -0.1188849
    netsum = netsum + feature221 * -0.2957865
    netsum = netsum + feature222 * -1.613025
    netsum = netsum + feature223 * -1.856167
    netsum = netsum + feature224 * -0.4557756
    netsum = netsum + feature225 * -0.7251074
    outarray22 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.1766084
    netsum = netsum + feature21 * -0.3840695
    netsum = netsum + feature22 * -0.5459561
    netsum = netsum + feature23 * -0.2273913
    netsum = netsum + feature24 * -0.4936724
    netsum = netsum + feature25 * 0.2567531
    netsum = netsum + feature26 * 0.1996366
    netsum = netsum + feature27 * 2.452877
    netsum = netsum + feature28 * -0.1040225
    netsum = netsum + feature29 * 0.329926
    netsum = netsum + feature210 * -0.8863566
    netsum = netsum + feature211 * 0.770371
    netsum = netsum + feature212 * -0.5147469
    netsum = netsum + feature213 * -4.618825
    netsum = netsum + feature214 * 0.3198798
    netsum = netsum + feature215 * -0.4069778
    netsum = netsum + feature216 * 0.372125
    netsum = netsum + feature217 * 0.0583452
    netsum = netsum + feature218 * 0.1033952
    netsum = netsum + feature219 * 0.2222385
    netsum = netsum + feature220 * 0.2142323
    netsum = netsum + feature221 * 0.6679732
    netsum = netsum + feature222 * -4.6637
    netsum = netsum + feature223 * 3.09447
    netsum = netsum + feature224 * -9.240476E-02
    netsum = netsum + feature225 * 5.634465E-02
    outarray23 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.4205609
    netsum = netsum + feature21 * -0.3574145
    netsum = netsum + feature22 * 5.627638E-02
    netsum = netsum + feature23 * -0.3093654
    netsum = netsum + feature24 * -0.1178279
    netsum = netsum + feature25 * 0.1287344
    netsum = netsum + feature26 * 0.0804376
    netsum = netsum + feature27 * -0.8969528
    netsum = netsum + feature28 * -0.0425215
    netsum = netsum + feature29 * 0.2578357
    netsum = netsum + feature210 * -0.4101266
    netsum = netsum + feature211 * 0.2908747
    netsum = netsum + feature212 * -1.898047
    netsum = netsum + feature213 * -3.402386
    netsum = netsum + feature214 * 0.5140675
    netsum = netsum + feature215 * 2.312259
    netsum = netsum + feature216 * 0.3540066
    netsum = netsum + feature217 * -0.1651463
    netsum = netsum + feature218 * 0.2184748
    netsum = netsum + feature219 * 5.698449E-02
    netsum = netsum + feature220 * -7.892144E-03
    netsum = netsum + feature221 * 0.4440458
    netsum = netsum + feature222 * 1.713681
    netsum = netsum + feature223 * 3.609373
    netsum = netsum + feature224 * 3.612475E-02
    netsum = netsum + feature225 * 0.2332484
    outarray24 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.287547
    netsum = netsum + feature21 * -0.4064873
    netsum = netsum + feature22 * 0.3129323
    netsum = netsum + feature23 * -0.0226568
    netsum = netsum + feature24 * 0.1858991
    netsum = netsum + feature25 * 0.2146034
    netsum = netsum + feature26 * -0.105403
    netsum = netsum + feature27 * -0.2090875
    netsum = netsum + feature28 * 6.753434E-02
    netsum = netsum + feature29 * -0.1894533
    netsum = netsum + feature210 * 6.189917E-02
    netsum = netsum + feature211 * -0.1526707
    netsum = netsum + feature212 * 0.313647
    netsum = netsum + feature213 * 0.5581246
    netsum = netsum + feature214 * -7.637074E-02
    netsum = netsum + feature215 * -0.3078103
    netsum = netsum + feature216 * -0.2320869
    netsum = netsum + feature217 * -2.492017E-02
    netsum = netsum + feature218 * 0.1968552
    netsum = netsum + feature219 * -0.0744594
    netsum = netsum + feature220 * -9.518302E-02
    netsum = netsum + feature221 * -0.1568473
    netsum = netsum + feature222 * 0.3293057
    netsum = netsum + feature223 * -0.7523289
    netsum = netsum + feature224 * 0.0609014
    netsum = netsum + feature225 * 2.049183E-02
    outarray25 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.675474E-02
    netsum = netsum + feature21 * -0.1184893
    netsum = netsum + feature22 * 0.1304565
    netsum = netsum + feature23 * 1.399891E-02
    netsum = netsum + feature24 * 3.763378E-02
    netsum = netsum + feature25 * 5.458301E-02
    netsum = netsum + feature26 * -1.369145E-02
    netsum = netsum + feature27 * 7.658686E-02
    netsum = netsum + feature28 * 4.371594E-03
    netsum = netsum + feature29 * -8.660305E-02
    netsum = netsum + feature210 * 0.1065252
    netsum = netsum + feature211 * -9.872559E-03
    netsum = netsum + feature212 * -0.110224
    netsum = netsum + feature213 * -0.4743085
    netsum = netsum + feature214 * -4.356546E-02
    netsum = netsum + feature215 * 9.346311E-02
    netsum = netsum + feature216 * -9.239668E-02
    netsum = netsum + feature217 * -1.539867E-02
    netsum = netsum + feature218 * 4.069473E-02
    netsum = netsum + feature219 * -2.060133E-02
    netsum = netsum + feature220 * 0.1133986
    netsum = netsum + feature221 * -3.068133E-02
    netsum = netsum + feature222 * -0.1166049
    netsum = netsum + feature223 * 0.4291836
    netsum = netsum + feature224 * 7.935212E-02
    netsum = netsum + feature225 * 7.416015E-04
    outarray26 = 1 / (1 + math.exp(-netsum))
     
    netsum = -6.007743E-03
    netsum = netsum + feature21 * -0.5171686
    netsum = netsum + feature22 * 3.190732E-02
    netsum = netsum + feature23 * -4.651923E-03
    netsum = netsum + feature24 * 0.1452246
    netsum = netsum + feature25 * 0.3110278
    netsum = netsum + feature26 * 7.026077E-02
    netsum = netsum + feature27 * -9.122505E-02
    netsum = netsum + feature28 * -3.444053E-02
    netsum = netsum + feature29 * 0.1091763
    netsum = netsum + feature210 * -0.1461589
    netsum = netsum + feature211 * -3.982874E-02
    netsum = netsum + feature212 * 0.2299097
    netsum = netsum + feature213 * 0.4585728
    netsum = netsum + feature214 * -9.967222E-03
    netsum = netsum + feature215 * -0.1552734
    netsum = netsum + feature216 * 4.857321E-02
    netsum = netsum + feature217 * 7.966736E-02
    netsum = netsum + feature218 * 0.2358864
    netsum = netsum + feature219 * 4.920834E-02
    netsum = netsum + feature220 * -1.506335E-02
    netsum = netsum + feature221 * -0.1182975
    netsum = netsum + feature222 * 0.1184809
    netsum = netsum + feature223 * -0.4880275
    netsum = netsum + feature224 * -3.492701E-02
    netsum = netsum + feature225 * -7.180636E-02
    outarray27 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.1022976
    netsum = netsum + feature21 * -0.1999748
    netsum = netsum + feature22 * 3.816332E-03
    netsum = netsum + feature23 * -2.437701E-02
    netsum = netsum + feature24 * 0.1008576
    netsum = netsum + feature25 * 0.1381694
    netsum = netsum + feature26 * 0.0252368
    netsum = netsum + feature27 * 0.2676923
    netsum = netsum + feature28 * -1.188881E-02
    netsum = netsum + feature29 * -1.069345E-02
    netsum = netsum + feature210 * -5.200301E-02
    netsum = netsum + feature211 * -1.635108E-02
    netsum = netsum + feature212 * -0.1108351
    netsum = netsum + feature213 * -0.2897478
    netsum = netsum + feature214 * -2.375951E-02
    netsum = netsum + feature215 * 0.1082142
    netsum = netsum + feature216 * 3.885437E-02
    netsum = netsum + feature217 * -3.380821E-02
    netsum = netsum + feature218 * 6.900962E-02
    netsum = netsum + feature219 * 3.007091E-02
    netsum = netsum + feature220 * 0.1474765
    netsum = netsum + feature221 * -3.554815E-02
    netsum = netsum + feature222 * -0.480933
    netsum = netsum + feature223 * 0.2595388
    netsum = netsum + feature224 * 5.851227E-02
    netsum = netsum + feature225 * 4.716478E-02
    outarray28 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.1834654
    netsum = netsum + feature21 * -0.2062431
    netsum = netsum + feature22 * 0.2697529
    netsum = netsum + feature23 * -1.286468E-03
    netsum = netsum + feature24 * 0.154379
    netsum = netsum + feature25 * 9.070759E-02
    netsum = netsum + feature26 * -3.532174E-02
    netsum = netsum + feature27 * -0.1802226
    netsum = netsum + feature28 * -5.631623E-03
    netsum = netsum + feature29 * -0.1737262
    netsum = netsum + feature210 * 0.2271055
    netsum = netsum + feature211 * -0.1813561
    netsum = netsum + feature212 * 0.3134227
    netsum = netsum + feature213 * 0.4087465
    netsum = netsum + feature214 * -6.459238E-02
    netsum = netsum + feature215 * -0.3287103
    netsum = netsum + feature216 * -0.2728
    netsum = netsum + feature217 * 6.461339E-02
    netsum = netsum + feature218 * 9.857619E-02
    netsum = netsum + feature219 * -7.020016E-02
    netsum = netsum + feature220 * -5.669348E-02
    netsum = netsum + feature221 * -0.1466825
    netsum = netsum + feature222 * 0.3167284
    netsum = netsum + feature223 * -0.5822093
    netsum = netsum + feature224 * 4.121005E-02
    netsum = netsum + feature225 * -6.709429E-02
    outarray29 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.555476E-02
    netsum = netsum + feature21 * -0.1034241
    netsum = netsum + feature22 * 0.1182307
    netsum = netsum + feature23 * 2.216047E-02
    netsum = netsum + feature24 * 1.182063E-02
    netsum = netsum + feature25 * 3.104968E-02
    netsum = netsum + feature26 * -1.482364E-03
    netsum = netsum + feature27 * 2.358994E-02
    netsum = netsum + feature28 * 1.067802E-03
    netsum = netsum + feature29 * -9.388089E-02
    netsum = netsum + feature210 * 0.157619
    netsum = netsum + feature211 * -7.926293E-03
    netsum = netsum + feature212 * -0.1660983
    netsum = netsum + feature213 * -0.5434625
    netsum = netsum + feature214 * -0.0452474
    netsum = netsum + feature215 * 0.1450205
    netsum = netsum + feature216 * -0.1926818
    netsum = netsum + feature217 * -2.119855E-02
    netsum = netsum + feature218 * 0.0261559
    netsum = netsum + feature219 * -0.0267729
    netsum = netsum + feature220 * 0.1516137
    netsum = netsum + feature221 * 5.017051E-03
    netsum = netsum + feature222 * -0.0776888
    netsum = netsum + feature223 * 0.5201233
    netsum = netsum + feature224 * 0.1079757
    netsum = netsum + feature225 * 2.698544E-02
    outarray30 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.373439E-02
    netsum = netsum + feature21 * -0.4744356
    netsum = netsum + feature22 * -0.0219764
    netsum = netsum + feature23 * -6.696534E-03
    netsum = netsum + feature24 * 0.1233853
    netsum = netsum + feature25 * 0.2886267
    netsum = netsum + feature26 * 7.442984E-02
    netsum = netsum + feature27 * -0.0550084
    netsum = netsum + feature28 * -7.515799E-02
    netsum = netsum + feature29 * 9.004208E-02
    netsum = netsum + feature210 * -0.1154302
    netsum = netsum + feature211 * -4.944462E-02
    netsum = netsum + feature212 * 0.1745976
    netsum = netsum + feature213 * 0.32843
    netsum = netsum + feature214 * 2.175576E-03
    netsum = netsum + feature215 * -0.1010809
    netsum = netsum + feature216 * 0.1111626
    netsum = netsum + feature217 * 0.1386023
    netsum = netsum + feature218 * 0.2175133
    netsum = netsum + feature219 * 5.165197E-02
    netsum = netsum + feature220 * -2.603708E-02
    netsum = netsum + feature221 * -0.1205535
    netsum = netsum + feature222 * 6.961054E-02
    netsum = netsum + feature223 * -0.332932
    netsum = netsum + feature224 * -7.866149E-02
    netsum = netsum + feature225 * -9.872774E-02
    outarray31 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.1380954
    netsum = netsum + feature21 * -7.122596E-02
    netsum = netsum + feature22 * 4.502888E-02
    netsum = netsum + feature23 * -0.0105364
    netsum = netsum + feature24 * 6.454158E-02
    netsum = netsum + feature25 * 5.715553E-02
    netsum = netsum + feature26 * 5.431092E-02
    netsum = netsum + feature27 * 0.1926934
    netsum = netsum + feature28 * -4.368871E-02
    netsum = netsum + feature29 * -4.698128E-03
    netsum = netsum + feature210 * 6.248261E-02
    netsum = netsum + feature211 * -2.202949E-02
    netsum = netsum + feature212 * -5.751355E-02
    netsum = netsum + feature213 * -0.4681675
    netsum = netsum + feature214 * -2.572915E-02
    netsum = netsum + feature215 * -2.626877E-02
    netsum = netsum + feature216 * -2.116663E-02
    netsum = netsum + feature217 * 0
    netsum = netsum + feature218 * 0.0021757
    netsum = netsum + feature219 * 1.270648E-02
    netsum = netsum + feature220 * 0.1452304
    netsum = netsum + feature221 * -1.951959E-02
    netsum = netsum + feature222 * -0.3562658
    netsum = netsum + feature223 * 0.3221529
    netsum = netsum + feature224 * 4.765598E-02
    netsum = netsum + feature225 * 7.49318E-03
    outarray32 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.1183078
    netsum = netsum + feature21 * -0.2889529
    netsum = netsum + feature22 * -9.554909E-03
    netsum = netsum + feature23 * -0.3096347
    netsum = netsum + feature24 * -0.0546734
    netsum = netsum + feature25 * 0.2078993
    netsum = netsum + feature26 * 0.1015305
    netsum = netsum + feature27 * 0.2956263
    netsum = netsum + feature28 * -0.3666882
    netsum = netsum + feature29 * -0.1506132
    netsum = netsum + feature210 * -2.433007E-02
    netsum = netsum + feature211 * -7.830003E-03
    netsum = netsum + feature212 * -0.227648
    netsum = netsum + feature213 * -4.922554
    netsum = netsum + feature214 * 0.6926962
    netsum = netsum + feature215 * 0.3283549
    netsum = netsum + feature216 * 0.4018129
    netsum = netsum + feature217 * 0.322463
    netsum = netsum + feature218 * 8.668222E-02
    netsum = netsum + feature219 * -1.590223E-02
    netsum = netsum + feature220 * -0.1315247
    netsum = netsum + feature221 * 4.510861E-02
    netsum = netsum + feature222 * -0.5621976
    netsum = netsum + feature223 * 1.665498
    netsum = netsum + feature224 * -0.3098621
    netsum = netsum + feature225 * -0.4244801
    outarray33 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.4069614
    netsum = netsum + feature21 * -0.4547772
    netsum = netsum + feature22 * -0.2021811
    netsum = netsum + feature23 * -0.3321226
    netsum = netsum + feature24 * -0.0490548
    netsum = netsum + feature25 * 0.3069231
    netsum = netsum + feature26 * 0.3092589
    netsum = netsum + feature27 * 5.293478E-02
    netsum = netsum + feature28 * -0.5080404
    netsum = netsum + feature29 * 0.2113589
    netsum = netsum + feature210 * -0.2611181
    netsum = netsum + feature211 * 0.1044965
    netsum = netsum + feature212 * -0.1128231
    netsum = netsum + feature213 * -4.490021
    netsum = netsum + feature214 * 0.6949203
    netsum = netsum + feature215 * 0.1420231
    netsum = netsum + feature216 * 0.611544
    netsum = netsum + feature217 * 0.5026024
    netsum = netsum + feature218 * 0.1931366
    netsum = netsum + feature219 * 0.1166495
    netsum = netsum + feature220 * -0.1625839
    netsum = netsum + feature221 * 0.1213914
    netsum = netsum + feature222 * 0.205451
    netsum = netsum + feature223 * 1.57286
    netsum = netsum + feature224 * -0.4011729
    netsum = netsum + feature225 * -0.5534166
    outarray34 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.1167191
    netsum = netsum + feature21 * -0.4346863
    netsum = netsum + feature22 * -6.573167E-02
    netsum = netsum + feature23 * -0.3084134
    netsum = netsum + feature24 * -1.338407E-02
    netsum = netsum + feature25 * 0.2713576
    netsum = netsum + feature26 * 6.642547E-02
    netsum = netsum + feature27 * 0.2264355
    netsum = netsum + feature28 * -0.3900345
    netsum = netsum + feature29 * -0.2457371
    netsum = netsum + feature210 * -2.722405E-02
    netsum = netsum + feature211 * -1.115668E-02
    netsum = netsum + feature212 * -0.3130637
    netsum = netsum + feature213 * -4.501023
    netsum = netsum + feature214 * 0.7059773
    netsum = netsum + feature215 * 0.4777404
    netsum = netsum + feature216 * 0.4744093
    netsum = netsum + feature217 * 0.3612096
    netsum = netsum + feature218 * 0.1720276
    netsum = netsum + feature219 * -9.369865E-03
    netsum = netsum + feature220 * -0.1614461
    netsum = netsum + feature221 * 0.0230598
    netsum = netsum + feature222 * -0.4707956
    netsum = netsum + feature223 * 1.57533
    netsum = netsum + feature224 * -0.3306912
    netsum = netsum + feature225 * -0.4189738
    outarray35 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.4037066
    netsum = netsum + feature21 * -0.3507708
    netsum = netsum + feature22 * -0.1616497
    netsum = netsum + feature23 * -0.3387644
    netsum = netsum + feature24 * -0.1006826
    netsum = netsum + feature25 * 0.2617168
    netsum = netsum + feature26 * 0.3396074
    netsum = netsum + feature27 * 0.1190105
    netsum = netsum + feature28 * -0.4846852
    netsum = netsum + feature29 * 0.321633
    netsum = netsum + feature210 * -0.3111618
    netsum = netsum + feature211 * 0.1420249
    netsum = netsum + feature212 * -5.990252E-02
    netsum = netsum + feature213 * -4.726746
    netsum = netsum + feature214 * 0.6983667
    netsum = netsum + feature215 * 3.293242E-02
    netsum = netsum + feature216 * 0.5924216
    netsum = netsum + feature217 * 0.4693687
    netsum = netsum + feature218 * 0.1374057
    netsum = netsum + feature219 * 0.1196791
    netsum = netsum + feature220 * -0.1800989
    netsum = netsum + feature221 * 0.1453259
    netsum = netsum + feature222 * 0.1487263
    netsum = netsum + feature223 * 1.6025
    netsum = netsum + feature224 * -0.4131266
    netsum = netsum + feature225 * -0.5500115
    outarray36 = 1 / (1 + math.exp(-netsum))
     
    netsum = 3.807949E-02
    netsum = netsum + feature21 * -0.15824
    netsum = netsum + feature22 * 0.2181091
    netsum = netsum + feature23 * -3.704252E-02
    netsum = netsum + feature24 * 6.229806E-02
    netsum = netsum + feature25 * 0.1044482
    netsum = netsum + feature26 * 0
    netsum = netsum + feature27 * 2.052095E-03
    netsum = netsum + feature28 * -5.293611E-02
    netsum = netsum + feature29 * -0.0882238
    netsum = netsum + feature210 * 9.098981E-02
    netsum = netsum + feature211 * -8.591522E-02
    netsum = netsum + feature212 * -2.245204E-05
    netsum = netsum + feature213 * 0.1358971
    netsum = netsum + feature214 * -0.0268836
    netsum = netsum + feature215 * -1.667229E-02
    netsum = netsum + feature216 * -0.1000836
    netsum = netsum + feature217 * 6.005905E-02
    netsum = netsum + feature218 * 4.914791E-02
    netsum = netsum + feature219 * -4.968102E-02
    netsum = netsum + feature220 * 1.195027E-03
    netsum = netsum + feature221 * -3.483957E-02
    netsum = netsum + feature222 * -2.353187E-02
    netsum = netsum + feature223 * -5.869979E-02
    netsum = netsum + feature224 * 2.819724E-02
    netsum = netsum + feature225 * 6.482068E-03
    outarray37 = 1 / (1 + math.exp(-netsum))
     
    netsum = -8.001687E-02
    netsum = netsum + feature21 * -0.2335714
    netsum = netsum + feature22 * 0.1394265
    netsum = netsum + feature23 * 1.491955E-02
    netsum = netsum + feature24 * 4.939032E-02
    netsum = netsum + feature25 * 0.1424357
    netsum = netsum + feature26 * 3.647018E-02
    netsum = netsum + feature27 * 0.173615
    netsum = netsum + feature28 * -5.190301E-02
    netsum = netsum + feature29 * -0.1020314
    netsum = netsum + feature210 * 0.1501091
    netsum = netsum + feature211 * -2.192736E-02
    netsum = netsum + feature212 * -8.404949E-02
    netsum = netsum + feature213 * -8.854298E-02
    netsum = netsum + feature214 * -4.543283E-02
    netsum = netsum + feature215 * 0.0976934
    netsum = netsum + feature216 * -0.1101972
    netsum = netsum + feature217 * 1.049425E-02
    netsum = netsum + feature218 * 6.671789E-02
    netsum = netsum + feature219 * -0.0194759
    netsum = netsum + feature220 * 0.1512435
    netsum = netsum + feature221 * -0.0406428
    netsum = netsum + feature222 * -0.250593
    netsum = netsum + feature223 * 0.1222182
    netsum = netsum + feature224 * 5.577745E-02
    netsum = netsum + feature225 * 1.437052E-02
    outarray38 = 1 / (1 + math.exp(-netsum))
     
    netsum = 2.415238E-02
    netsum = netsum + feature21 * -0.2301198
    netsum = netsum + feature22 * 0.2305605
    netsum = netsum + feature23 * -1.438899E-02
    netsum = netsum + feature24 * 5.146781E-02
    netsum = netsum + feature25 * 0.1321112
    netsum = netsum + feature26 * -2.223661E-02
    netsum = netsum + feature27 * 3.040958E-02
    netsum = netsum + feature28 * -2.403506E-02
    netsum = netsum + feature29 * -7.958664E-02
    netsum = netsum + feature210 * 7.331133E-02
    netsum = netsum + feature211 * -6.008292E-02
    netsum = netsum + feature212 * 7.528625E-03
    netsum = netsum + feature213 * 0.12398
    netsum = netsum + feature214 * -0.0387481
    netsum = netsum + feature215 * -2.271455E-02
    netsum = netsum + feature216 * -8.502299E-02
    netsum = netsum + feature217 * 4.761432E-02
    netsum = netsum + feature218 * 8.183844E-02
    netsum = netsum + feature219 * -5.026748E-02
    netsum = netsum + feature220 * 2.687267E-02
    netsum = netsum + feature221 * -3.455564E-02
    netsum = netsum + feature222 * -4.520472E-02
    netsum = netsum + feature223 * -0.0595547
    netsum = netsum + feature224 * 4.689292E-02
    netsum = netsum + feature225 * -3.491582E-03
    outarray39 = 1 / (1 + math.exp(-netsum))
     
    netsum = -9.215283E-02
    netsum = netsum + feature21 * -0.2078228
    netsum = netsum + feature22 * 0.1346722
    netsum = netsum + feature23 * 1.592144E-02
    netsum = netsum + feature24 * 2.157819E-02
    netsum = netsum + feature25 * 0.1250194
    netsum = netsum + feature26 * 0.0517159
    netsum = netsum + feature27 * 7.545946E-02
    netsum = netsum + feature28 * -5.908996E-02
    netsum = netsum + feature29 * -6.433312E-02
    netsum = netsum + feature210 * 0.1631168
    netsum = netsum + feature211 * -0.0297709
    netsum = netsum + feature212 * -8.870718E-02
    netsum = netsum + feature213 * -0.1648056
    netsum = netsum + feature214 * -4.355674E-02
    netsum = netsum + feature215 * 0.1288526
    netsum = netsum + feature216 * -0.1149588
    netsum = netsum + feature217 * 0.0196718
    netsum = netsum + feature218 * 5.288224E-02
    netsum = netsum + feature219 * -2.095088E-02
    netsum = netsum + feature220 * 0.1732745
    netsum = netsum + feature221 * -2.477687E-02
    netsum = netsum + feature222 * -0.11299
    netsum = netsum + feature223 * 0.1784782
    netsum = netsum + feature224 * 5.171063E-02
    netsum = netsum + feature225 * 9.380523E-03
    outarray40 = 1 / (1 + math.exp(-netsum))
     
     
    outarray1 = 600 *  (outarray1 - .1) / .8  + -300
    if (outarray1<-300):
        outarray1 = -300
    if (outarray1>300):
        outarray1 = 300
     
    outarray2 = 600 *  (outarray2 - .1) / .8  + -300
    if (outarray2<-300):
        outarray2 = -300
    if (outarray2>300):
        outarray2 = 300
     
    outarray3 = 600 *  (outarray3 - .1) / .8  + -300
    if (outarray3<-300):
        outarray3 = -300
    if (outarray3>300):
        outarray3 = 300
     
    outarray4 = 600 *  (outarray4 - .1) / .8  + -300
    if (outarray4<-300):
        outarray4 = -300
    if (outarray4>300):
        outarray4 = 300
     
    outarray5 = 600 *  (outarray5 - .1) / .8  + -300
    if (outarray5<-300):
        outarray5 = -300
    if (outarray5>300):
        outarray5 = 300
     
    outarray6 = 600 *  (outarray6 - .1) / .8  + -300
    if (outarray6<-300):
        outarray6 = -300
    if (outarray6>300):
        outarray6 = 300
     
    outarray7 = 600 *  (outarray7 - .1) / .8  + -300
    if (outarray7<-300):
        outarray7 = -300
    if (outarray7>300):
        outarray7 = 300
     
    outarray8 = 600 *  (outarray8 - .1) / .8  + -300
    if (outarray8<-300):
        outarray8 = -300
    if (outarray8>300):
        outarray8 = 300
     
    outarray9 = 600 *  (outarray9 - .1) / .8  + -300
    if (outarray9<-300):
        outarray9 = -300
    if (outarray9>300):
        outarray9 = 300
     
    outarray10 = 600 *  (outarray10 - .1) / .8  + -300
    if (outarray10<-300):
        outarray10 = -300
    if (outarray10>300):
        outarray10 = 300
     
    outarray11 = 600 *  (outarray11 - .1) / .8  + -300
    if (outarray11<-300):
        outarray11 = -300
    if (outarray11>300):
        outarray11 = 300
     
    outarray12 = 600 *  (outarray12 - .1) / .8  + -300
    if (outarray12<-300):
        outarray12 = -300
    if (outarray12>300):
        outarray12 = 300
     
    outarray13 = 600 *  (outarray13 - .1) / .8  + -300
    if (outarray13<-300):
        outarray13 = -300
    if (outarray13>300):
        outarray13 = 300
     
    outarray14 = 600 *  (outarray14 - .1) / .8  + -300
    if (outarray14<-300):
        outarray14 = -300
    if (outarray14>300):
        outarray14 = 300
     
    outarray15 = 600 *  (outarray15 - .1) / .8  + -300
    if (outarray15<-300):
        outarray15 = -300
    if (outarray15>300):
        outarray15 = 300
     
    outarray16 = 600 *  (outarray16 - .1) / .8  + -300
    if (outarray16<-300):
        outarray16 = -300
    if (outarray16>300):
        outarray16 = 300
     
    outarray17 = 600 *  (outarray17 - .1) / .8  + -300
    if (outarray17<-300):
        outarray17 = -300
    if (outarray17>300):
        outarray17 = 300
     
    outarray18 = 600 *  (outarray18 - .1) / .8  + -300
    if (outarray18<-300):
        outarray18 = -300
    if (outarray18>300):
        outarray18 = 300
     
    outarray19 = 600 *  (outarray19 - .1) / .8  + -300
    if (outarray19<-300):
        outarray19 = -300
    if (outarray19>300):
        outarray19 = 300
     
    outarray20 = 600 *  (outarray20 - .1) / .8  + -300
    if (outarray20<-300):
        outarray20 = -300
    if (outarray20>300):
        outarray20 = 300
     
    outarray21 = 600 *  (outarray21 - .1) / .8  + -300
    if (outarray21<-300):
        outarray21 = -300
    if (outarray21>300):
        outarray21 = 300
     
    outarray22 = 600 *  (outarray22 - .1) / .8  + -300
    if (outarray22<-300):
        outarray22 = -300
    if (outarray22>300):
        outarray22 = 300
     
    outarray23 = 600 *  (outarray23 - .1) / .8  + -300
    if (outarray23<-300):
        outarray23 = -300
    if (outarray23>300):
        outarray23 = 300
     
    outarray24 = 600 *  (outarray24 - .1) / .8  + -300
    if (outarray24<-300):
        outarray24 = -300
    if (outarray24>300):
        outarray24 = 300
     
    outarray25 = 600 *  (outarray25 - .1) / .8  + -300
    if (outarray25<-300):
        outarray25 = -300
    if (outarray25>300):
        outarray25 = 300
     
    outarray26 = 600 *  (outarray26 - .1) / .8  + -300
    if (outarray26<-300):
        outarray26 = -300
    if (outarray26>300):
        outarray26 = 300
     
    outarray27 = 600 *  (outarray27 - .1) / .8  + -300
    if (outarray27<-300):
        outarray27 = -300
    if (outarray27>300):
        outarray27 = 300
     
    outarray28 = 600 *  (outarray28 - .1) / .8  + -300
    if (outarray28<-300):
        outarray28 = -300
    if (outarray28>300):
        outarray28 = 300
     
    outarray29 = 600 *  (outarray29 - .1) / .8  + -300
    if (outarray29<-300):
        outarray29 = -300
    if (outarray29>300):
        outarray29 = 300
     
    outarray30 = 600 *  (outarray30 - .1) / .8  + -300
    if (outarray30<-300):
        outarray30 = -300
    if (outarray30>300):
        outarray30 = 300
     
    outarray31 = 600 *  (outarray31 - .1) / .8  + -300
    if (outarray31<-300):
        outarray31 = -300
    if (outarray31>300):
        outarray31 = 300
     
    outarray32 = 600 *  (outarray32 - .1) / .8  + -300
    if (outarray32<-300):
        outarray32 = -300
    if (outarray32>300):
        outarray32 = 300
     
    outarray33 = 600 *  (outarray33 - .1) / .8  + -300
    if (outarray33<-300):
        outarray33 = -300
    if (outarray33>300):
        outarray33 = 300
     
    outarray34 = 600 *  (outarray34 - .1) / .8  + -300
    if (outarray34<-300):
        outarray34 = -300
    if (outarray34>300):
        outarray34 = 300
     
    outarray35 = 600 *  (outarray35 - .1) / .8  + -300
    if (outarray35<-300):
        outarray35 = -300
    if (outarray35>300):
        outarray35 = 300
     
    outarray36 = 600 *  (outarray36 - .1) / .8  + -300
    if (outarray36<-300):
        outarray36 = -300
    if (outarray36>300):
        outarray36 = 300
     
    outarray37 = 600 *  (outarray37 - .1) / .8  + -300
    if (outarray37<-300):
        outarray37 = -300
    if (outarray37>300):
        outarray37 = 300
     
    outarray38 = 600 *  (outarray38 - .1) / .8  + -300
    if (outarray38<-300):
        outarray38 = -300
    if (outarray38>300):
        outarray38 = 300
     
    outarray39 = 600 *  (outarray39 - .1) / .8  + -300
    if (outarray39<-300):
        outarray39 = -300
    if (outarray39>300):
        outarray39 = 300
     
    outarray40 = 600 *  (outarray40 - .1) / .8  + -300
    if (outarray40<-300):
        outarray40 = -300
    if (outarray40>300):
        outarray40 = 300

    #'Осредняем силы по нитям и в общем

    #'Вертикальные силы

    #'средние значения
    Mean_F_vertL = round(((abs(outarray1)+abs(outarray2)+abs(outarray5)+abs(outarray6))/4),1)
    Mean_F_vertR = round(((abs(outarray3)+abs(outarray4)+abs(outarray7)+abs(outarray8))/4),1)
    Mean_F_vert = round(((Mean_F_vertL+Mean_F_vertR)/2),1)

    #'СКО
    sigma_F_vertL = round((((abs(outarray9)**2+abs(outarray10)**2+abs(outarray13)**2+abs(outarray14)**2)/4)**0.5),1)
    sigma_F_vertR = round((((abs(outarray11)**2+abs(outarray12)**2+abs(outarray15)**2+abs(outarray16)**2)/4)**0.5),1)
    sigma_F_vert = round((((sigma_F_vertL**2+sigma_F_vertR**2)/2)**0.5),1)


    #'Боковые силы
    
    #'средние значения
    Mean_F_sideL = round(((abs(outarray17)+abs(outarray18)+abs(outarray21)+abs(outarray22))/4),1)
    Mean_F_sideR = round(((abs(outarray19)+abs(outarray20)+abs(outarray23)+abs(outarray24))/4),1)
    Mean_F_side = round(((Mean_F_sideL+Mean_F_sideR)/2),1)

    #'СКО
    sigma_F_sideL = round((((abs(outarray25)**2+abs(outarray26)**2+abs(outarray29)**2+abs(outarray30)**2)/4)**0.5),1)
    sigma_F_sideR = round((((abs(outarray27)**2+abs(outarray28)**2+abs(outarray31)**2+abs(outarray32)**2)/4)**0.5),1)
    sigma_F_side = round((((sigma_F_sideL**2+sigma_F_sideR**2)/2)**0.5),1)

    #'Рамные силы

    #'средние значения
    Mean_H = round(((abs(outarray33)+abs(outarray34)+abs(outarray35)+abs(outarray36))/4),1)
    
    #'СКО
    sigma_H = round((((abs(outarray37)**2+abs(outarray38)**2+abs(outarray39)**2+abs(outarray40)**2)/4)**0.5),1)

    outarray = [outarray1, outarray2, outarray3, outarray4, outarray5,outarray6, outarray7, outarray8,outarray9, outarray10, outarray11, outarray12, outarray13,outarray14, outarray15, outarray16,outarray17, outarray18, outarray19, outarray20, outarray21,outarray22, outarray23, outarray24,outarray25, outarray26, outarray27, outarray28, outarray29,outarray30, outarray31, outarray32, outarray33, outarray34, outarray35, outarray36, outarray37, outarray38, outarray39, outarray40]
    for el in range(0,len(outarray)):
        outarray[el]=abs(round(outarray[el], 1))

    #Эта ветка выводит в память список списков который состоит из значений для далььнейших расчетов (Сред.знач верт. силы, СКО вертикал силы, Сред.знач. боковой силы, ско боковой силы)
    #вывод идет как в целом по подвижному составу, так и отдельно по нитям
    #данный режим может быть использован для формирования массивов силовых факторов по вагонопотоку
        
    if Show_or_return == 'return':
        return [Mean_F_vertR, Mean_F_vertL, Mean_F_vert, sigma_F_vertR, sigma_F_vertL, sigma_F_vert, Mean_F_sideR,\
                Mean_F_sideL, Mean_F_side, sigma_F_sideR, sigma_F_sideL, sigma_F_side, Mean_H, sigma_H,\
                MeanP1NarkPa, RmsP1NarkPa, MeanP1VnrkPa, RmsP1VnrkPa, MeanP2NarkPa, RmsP2NarkPa, MeanP2VnrkPa, RmsP2VnrkPa]
        
    #эта ветка выводит на экран результаты расчетов, но в память их не загружает
    
    print ("Значения сил, действующие в системе 'колесо-рельс'\nпри движении грузового вагона и следующих условиях:")
    print ("Тип В.С.П. - ",VSP, "\nСостояние пути - ", MAINT, "\nРадиус кривой, м -", Rad)
    print ("Возвышение наружнего рельса, мм - ", H, "\nСкорость движения, км/ч - ", v, "\nОсевая нагрузка, тс -", Pos)
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
    print ("Cредние значения рамных сил по каждой оси, кН")
    print ('1_ось= {};\n2_ось= {};\n3_ось= {};\n4_ось= {}.'.format (outarray[32], outarray[33], outarray[34], outarray[35]))
    print ()
    print ("СКО рамных сил по каждой оси, кН")
    print ('1_ось= {};\n2_ось= {};\n3_ось= {};\n4_ось= {}.'.format (outarray[36], outarray[37], outarray[38], outarray[39]))
    print ()
    print ()

    print ("ИТОГОВЫЕ ЗНАЧЕНИЯ ВОЗДЕЙСТВИЯ:")
    print ()
    print ("Средние значения вертикальных сил `колесо-рельс`, кН:")
    print ('по левой нити= {};\nпо правой нити = {};\nв среднем по экипажу= {};'.format (Mean_F_vertL, Mean_F_vertR, Mean_F_vert))
    print ()
    print ("СКО значений вертикальных сил `колесо-рельс, кН:")
    print ('по левой нити= {};\nпо правой нити = {};\nв среднем по экипажу= {};'.format(sigma_F_vertL, sigma_F_vertR, sigma_F_vert))
    print ()
    print ("Средние значения боковых сил `колесо-рельс`, кН:")
    print ('по левой нити= {};\nпо правой нити = {};\nв среднем по экипажу= {};'.format(Mean_F_sideL, Mean_F_sideR, Mean_F_side))
    print ()
    print ("СКО значений боковых сил `колесо-рельс`:")
    print ('по левой нити= {};\nпо правой нити = {};\nв среднем по экипажу= {};'.format(sigma_F_sideL, sigma_F_sideR, sigma_F_side))
    print ()
    print ("Средние значения рамных сил в среднем по экипажу кН: = ", Mean_H)
    print ()
    print ("СКО значений рамных сил в среднем по экипажу кН: =", sigma_H)


    

def vagon_4 (input_val, Show_or_return = "return"):

    VSP_type = input_val[0] 
    Condition = input_val[1] 
    Radius = input_val[2]
    h = input_val[3]
    V = input_val[4]
    axle_load = input_val[5]
    Sh_Kol = input_val[6] 
    mu_fr = input_val[7]


    #вычисление контактных напряжений

    from contact_pressure import contact_tension
    input_val1 = [V,axle_load, mu_fr, Radius, h, Sh_Kol]

    cont_press = contact_tension(input_val1)
    
    MeanP1NarkPa = cont_press[0]
    RmsP1NarkPa = cont_press[1]
    MeanP1VnrkPa  = cont_press[2]
    RmsP1VnrkPa = cont_press[3]
    MeanP2NarkPa = cont_press[4]
    RmsP2NarkPa = cont_press[5]
    MeanP2VnrkPa = cont_press[6]
    RmsP2VnrkPa = cont_press[7]

    '''
    'Грузовой локомотив
    'VSP_type это VSP_type - тип всп (1 - б.п., 2 - з.п.)
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
    

    ' outarray1 это mean_F_vertical_1l 
    ' outarray2 это mean_F_vertical_2l
    ' outarray3 это mean_F_vertical_1r
    ' outarray4 это mean_F_vertical_2r
    ' outarray5 это mean_F_vertical_3l
    ' outarray6 это mean_F_vertical_4l
    ' outarray7 это mean_F_vertical_3r
    ' outarray8 это mean_F_vertical_4r
    ' outarray9 это RMS_F_vertical_1l
    ' outarray10 это RMS_F_vertical_2l
    ' outarray11 это RMS_F_vertical_1r
    ' outarray12 это RMS_F_vertical_2r
    ' outarray13 это RMS_F_vertical_3l
    ' outarray14 это RMS_F_vertical_4l
    ' outarray15 это RMS_F_vertical_3r
    ' outarray16 это RMS_F_vertical_4r
    ' outarray17 это mean_F_side_1l
    ' outarray18 это mean_F_side_2l
    ' outarray19 это mean_F_side_1r
    ' outarray20 это mean_F_side_2r
    ' outarray21 это mean_F_side_3l
    ' outarray22 это mean_F_side_4l
    ' outarray23 это mean_F_side_3r
    ' outarray24 это mean_F_side_4r
    ' outarray25 это RMS_F_side_1l
    ' outarray26 это RMS_F_side_2l
    ' outarray27 это RMS_F_side_1r
    ' outarray28 это RMS_F_side_2r
    ' outarray29 это RMS_F_side_3l
    ' outarray30 это RMS_F_side_4l
    ' outarray31 это RMS_F_side_3r
    ' outarray32 это RMS_F_side_4r'''

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
     
    netsum = 2.585002
    netsum = netsum + VSP_type * 0
    netsum = netsum + Condition * 0
    netsum = netsum + Radius * -8.91273
    netsum = netsum + h * 0.8210604
    netsum = netsum + V * -3.471508
    netsum = netsum + Sh_Kol * 0
    netsum = netsum + mu_fr * -0.1360189
    feature21 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.377504
    netsum = netsum + VSP_type * 0
    netsum = netsum + Condition * -1.15781E-03
    netsum = netsum + Radius * -80.54958
    netsum = netsum + h * -7.702893E-02
    netsum = netsum + V * 5.772938
    netsum = netsum + Sh_Kol * -3.005799E-03
    netsum = netsum + mu_fr * 2.041161E-02
    feature22 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.933569
    netsum = netsum + VSP_type * -1.711932E-03
    netsum = netsum + Condition * 3.348329
    netsum = netsum + Radius * -9.856087
    netsum = netsum + h * 4.212798E-02
    netsum = netsum + V * -6.785546
    netsum = netsum + Sh_Kol * -2.193178E-02
    netsum = netsum + mu_fr * -0.115735
    feature23 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.203883
    netsum = netsum + VSP_type * 0
    netsum = netsum + Condition * -0.1876383
    netsum = netsum + Radius * -0.4741783
    netsum = netsum + h * -1.473345
    netsum = netsum + V * -27.2589
    netsum = netsum + Sh_Kol * 2.778484E-02
    netsum = netsum + mu_fr * -2.686149E-02
    feature24 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.1722996
    netsum = netsum + VSP_type * -4.179223E-02
    netsum = netsum + Condition * -3.111501
    netsum = netsum + Radius * -6.051737
    netsum = netsum + h * -1.546812
    netsum = netsum + V * 20.1687
    netsum = netsum + Sh_Kol * -6.053827E-02
    netsum = netsum + mu_fr * -0.27134
    feature25 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.066288
    netsum = netsum + VSP_type * 1.266568E-03
    netsum = netsum + Condition * 1.944989E-02
    netsum = netsum + Radius * 25.41498
    netsum = netsum + h * -1.981775E-03
    netsum = netsum + V * 1.603726
    netsum = netsum + Sh_Kol * -3.990319E-03
    netsum = netsum + mu_fr * -6.385222E-02
    feature26 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.120572
    netsum = netsum + VSP_type * -1.460704E-03
    netsum = netsum + Condition * -4.133869E-03
    netsum = netsum + Radius * 7.307359
    netsum = netsum + h * -2.142782
    netsum = netsum + V * 7.809622
    netsum = netsum + Sh_Kol * -3.511675E-03
    netsum = netsum + mu_fr * -0.2647697
    feature27 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.824843
    netsum = netsum + VSP_type * 0
    netsum = netsum + Condition * -0.1292598
    netsum = netsum + Radius * -0.9879975
    netsum = netsum + h * -1.204435
    netsum = netsum + V * -13.94144
    netsum = netsum + Sh_Kol * 1.130541E-02
    netsum = netsum + mu_fr * 2.213776E-04
    feature28 = 1 / (1 + math.exp(-netsum))
     
    netsum = 1.029858
    netsum = netsum + VSP_type * 1.767524E-03
    netsum = netsum + Condition * 0.9493096
    netsum = netsum + Radius * 29.43046
    netsum = netsum + h * 0.8889506
    netsum = netsum + V * -8.378217
    netsum = netsum + Sh_Kol * 4.480276E-03
    netsum = netsum + mu_fr * 0.1820433
    feature29 = 1 / (1 + math.exp(-netsum))
     
    netsum = 4.230172
    netsum = netsum + VSP_type * 0
    netsum = netsum + Condition * -4.297026E-02
    netsum = netsum + Radius * -8.079624
    netsum = netsum + h * 1.305674
    netsum = netsum + V * -5.790204
    netsum = netsum + Sh_Kol * 4.882933E-03
    netsum = netsum + mu_fr * -11.42556
    feature210 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.850837
    netsum = netsum + VSP_type * 0
    netsum = netsum + Condition * 2.729965E-02
    netsum = netsum + Radius * 24.26503
    netsum = netsum + h * -0.8527321
    netsum = netsum + V * 3.568127
    netsum = netsum + Sh_Kol * -7.076751E-04
    netsum = netsum + mu_fr * -1.893624
    feature211 = 1 / (1 + math.exp(-netsum))
     
    netsum = 5.964153
    netsum = netsum + VSP_type * 0.0101979
    netsum = netsum + Condition * 0.3099363
    netsum = netsum + Radius * -0.5788043
    netsum = netsum + h * 1.326795
    netsum = netsum + V * -16.57725
    netsum = netsum + Sh_Kol * 1.407271E-02
    netsum = netsum + mu_fr * 0.1802763
    feature212 = 1 / (1 + math.exp(-netsum))
     
    netsum = -7.644811E-02
    netsum = netsum + VSP_type * 0
    netsum = netsum + Condition * 0.3290109
    netsum = netsum + Radius * 23.57824
    netsum = netsum + h * -1.216775
    netsum = netsum + V * 6.496041
    netsum = netsum + Sh_Kol * 5.68667E-03
    netsum = netsum + mu_fr * 0.441742
    feature213 = 1 / (1 + math.exp(-netsum))
     
    netsum = 5.85291
    netsum = netsum + VSP_type * 4.121559E-03
    netsum = netsum + Condition * 5.228132E-02
    netsum = netsum + Radius * -5.183594
    netsum = netsum + h * -2.354057
    netsum = netsum + V * 1.04286
    netsum = netsum + Sh_Kol * 5.532813E-03
    netsum = netsum + mu_fr * -7.278997E-02
    feature214 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.3596448
    netsum = netsum + VSP_type * -0.0986152
    netsum = netsum + Condition * -6.176906
    netsum = netsum + Radius * 5.511677
    netsum = netsum + h * -5.737221
    netsum = netsum + V * -7.14607
    netsum = netsum + Sh_Kol * -0.1854707
    netsum = netsum + mu_fr * 0.2085879
    feature215 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.925175
    netsum = netsum + VSP_type * -2.069295E-02
    netsum = netsum + Condition * 1.198643
    netsum = netsum + Radius * 15.57942
    netsum = netsum + h * 4.30018
    netsum = netsum + V * -5.155819
    netsum = netsum + Sh_Kol * 7.023121E-02
    netsum = netsum + mu_fr * -0.3101979
    feature216 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.4316418
    netsum = netsum + VSP_type * -0.0115965
    netsum = netsum + Condition * -1.766893
    netsum = netsum + Radius * -19.04112
    netsum = netsum + h * -0.1739395
    netsum = netsum + V * 8.193781
    netsum = netsum + Sh_Kol * 0
    netsum = netsum + mu_fr * -8.844902E-02
    feature217 = 1 / (1 + math.exp(-netsum))
     
    netsum = 9.184696
    netsum = netsum + VSP_type * 2.459425E-02
    netsum = netsum + Condition * -5.261024
    netsum = netsum + Radius * 22.34481
    netsum = netsum + h * 5.298235
    netsum = netsum + V * -54.86484
    netsum = netsum + Sh_Kol * 0.2125103
    netsum = netsum + mu_fr * -0.5673731
    feature218 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.788542
    netsum = netsum + VSP_type * -0.017276
    netsum = netsum + Condition * 1.277058
    netsum = netsum + Radius * -9.111587
    netsum = netsum + h * 4.142786
    netsum = netsum + V * -5.90767
    netsum = netsum + Sh_Kol * 8.827934E-02
    netsum = netsum + mu_fr * -0.2551651
    feature219 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.5731257
    netsum = netsum + VSP_type * -2.299097E-02
    netsum = netsum + Condition * -2.863071
    netsum = netsum + Radius * -7.534512
    netsum = netsum + h * -1.145737
    netsum = netsum + V * 22.22261
    netsum = netsum + Sh_Kol * -4.156273E-02
    netsum = netsum + mu_fr * -0.3192002
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

    #'Рамные силы
    
    #'средние значения
    Mean_Hp = abs(round((((outarray17)+(outarray18)+(outarray21)+(outarray22))/4),1) + round((((outarray19)+(outarray20)+(outarray23)+(outarray24))/4),1))
    
    #'СКО
    sigma_Hp = Rms_Y 


    outarray = [outarray1, outarray2, outarray3, outarray4, outarray5,outarray6, outarray7, outarray8,outarray9, outarray10, outarray11, outarray12, outarray13,outarray14, outarray15, outarray16,outarray17, outarray18, outarray19, outarray20, outarray21,outarray22, outarray23, outarray24,outarray25, outarray26, outarray27, outarray28, outarray29,outarray30, outarray31, outarray32]
    for el in range(0,len(outarray)):
        outarray[el]=abs(round(outarray[el], 1))

    #Эта ветка выводит в память список списков который состоит из значений для далььнейших расчетов (Сред.знач верт. силы, СКО вертикал силы, Сред.знач. боковой силы, ско боковой силы)
    #вывод идет как в целом по подвижному составу, так и отдельно по нитям
    #данный режим может быть использован для формирования массивов силовых факторов по вагонопотоку
        
    if Show_or_return == 'return':
        return [Mean_F_vertical_R, Mean_F_vertical_L, Mean_Q, Rms_F_vertical_R, Rms_F_vertical_L, Rms_Q,\
                Mean_F_side_R, Mean_F_side_L, Mean_Y, Rms_F_side_R, Rms_F_side_L, Rms_Y, Mean_Hp, sigma_Hp,\
                MeanP1NarkPa, RmsP1NarkPa, MeanP1VnrkPa, RmsP1VnrkPa, MeanP2NarkPa, RmsP2NarkPa, MeanP2VnrkPa, RmsP2VnrkPa]
        
    #эта ветка выводит на экран результаты расчетов, но в память их не загружает
    
    print ("Значения сил, действующие в системе 'колесо-рельс'\nпри движении грузового локомотива и следующих условиях:")
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
    



    
 
