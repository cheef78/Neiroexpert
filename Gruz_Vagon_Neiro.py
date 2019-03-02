def GR_VagoN_Force (VSP_type, Main_type, Radius, h, V, Pst, Sh_Kol, f_tr):
    
    '''
    'VSP_type это VSP_type - тип всп (1 - б.п., 2 - з.п.)
    ' Main_type это Main_type - состояние пути (1 - отличное или хорошее, 2 - удовлетворительное)
    ' Radius это R_m - радиус кривизны учатска, радиус кривизны прямого участка принимается 10000 м
    ' h это h_mm - возвышение наружнего рельса, мм
    ' V это V_km/h - скорость движения экипажа, км/ч
    ' Pst это PST_ts - это осевая нагрузка, тс 
    ' Sh_Kol это S_mm - значение ширины колеи, мм
    ' f_tr это ftr - коэффициент трения

     outarray - это переменные выходных значиний (средние значения и СКО сил)
     mean_ - это среднее значение силы, кН
     RMS - это СКО силы, кН
     Q_ - это вертикальная сил
     Y_ - это боковая сила
     H - это рамная сила
     1,2,3,4 - номер оси в экипаже (в экипаже принято две тележки по две оси в каждой)
     r,l - правое или левое колесо 

    ' outarray1 это mean_Q(V)_1l
    ' outarray2 это mean_Q(V)_2l
    ' outarray3 это mean_Q(V)_1r
    ' outarray4 это mean_Q(V)_2r
    ' outarray5 это mean_Q(V)_3l
    ' outarray6 это mean_Q(V)_4l
    ' outarray7 это mean_Q(V)_3r
    ' outarray8 это mean_Q(V)_4r
    Mean_Q_L = (abs(outarray1)+abs(outarray2)+abs(outarray5)+abs(outarray6))/4
    Mean_Q_R = (abs(outarray3)+abs(outarray4)+abs(outarray7)+abs(outarray8))/4
    Mean_Q = (Mean_Q_L+Mean_Q_R)/2
    
    ' outarray9 это RMS_Q(V)_1l
    ' outarray10 это RMS_Q(V)_2l
    ' outarray11 это RMS_Q(V)_1r
    ' outarray12 это RMS_Q(V)_2r
    ' outarray13 это RMS_Q(V)_3l
    ' outarray14 это RMS_Q(V)_4l
    ' outarray15 это RMS_Q(V)_3r
    ' outarray16 это RMS_Q(V)_4r
    Rms_Q_L = ((abs(outarray9)**2+abs(outarray10)**2+abs(outarray13)**2+abs(outarray14)**2)/4)**0.5
    Rms_Q_R = ((abs(outarray11)**2+abs(outarray12)**2+abs(outarray15)**2+abs(outarray16)**2)/4)**0.5
    Rms_Q = ((Mean_Q_L**2+Mean_Q_R**2)/2)**0.5


    
    ' outarray17 это mean_Y(L)_1l
    ' outarray18 это mean_Y(L)_2l
    ' outarray19 это mean_Y(L)_1r
    ' outarray20 это mean_Y(L)_2r
    ' outarray21 это mean_Y(L)_3l
    ' outarray22 это mean_Y(L)_4l
    ' outarray23 это mean_Y(L)_3r
    ' outarray24 это mean_Y(L)_4r

    Mean_Y_L = (abs(outarray17)+abs(outarray18)+abs(outarray21)+abs(outarray22))/4
    Mean_Y_R = (abs(outarray19)+abs(outarray20)+abs(outarray23)+abs(outarray24))/4
    Mean_Y = (Mean_Y_L+Mean_Y_R)/2



    ' outarray25 это RMS_Y(L)_1l
    ' outarray26 это RMS_Y(L)_2l
    ' outarray27 это RMS_Y(L)_1r
    ' outarray28 это RMS_Y(L)_2r
    ' outarray29 это RMS_Y(L)_3l
    ' outarray30 это RMS_Y(L)_4l
    ' outarray31 это RMS_Y(L)_3r
    ' outarray32 это RMS_Y(L)_4r

    Rms_Y_L = ((abs(outarray25)**2+abs(outarray26)**2+abs(outarray29)**2+abs(outarray30)**2)/4)**0.5
    Rms_Y_R = ((abs(outarray27)**2+abs(outarray28)**2+abs(outarray31)**2+abs(outarray32)**2)/4)**0.5
    Rms_Y = ((Rms_Y_L**2+Rms_Y_R**2)/2)**0.5

    
    ' outarray33 это mean_H1
    ' outarray34 это mean_H2
    ' outarray35 это mean_H3
    ' outarray36 это mean_H4
    #'средние значения
    Mean_H = round(((abs(outarray33)+abs(outarray34)+abs(outarray35)+abs(outarray36))/4),1)
    
    #'СКО
    Rms_H = round((((abs(outarray37)**2+abs(outarray38)**2+abs(outarray39)**2+abs(outarray40)**2)/4)**0.5),1)
    



    ' outarray37 это RMS_H1
    ' outarray38 это RMS_H2
    ' outarray39 это RMS_H3
    ' outarray40 это RMS_H4'''
    import math
    VSP = VSP_type
    if VSP_type == 1:
        VSP = "бесст.путь"
    if VSP_type == 2:
        VSP = "звен.путь"

    MAINT = Main_type
    if Main_type == 1:
        MAINT = "'отл' или 'хор'"
    if VSP_type == 2:
        MAINT = "'удовл' или 'неуд'"
        
    Rad = Radius
    H=h
    v = V
    Pos = Pst
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
     
    if (Pst<5):
        Pst = 5
    if (Pst>30):
        Pst = 30
    Pst = (Pst - 5) / 25
     
    if (Sh_Kol<1510):
        Sh_Kol = 1510
    if (Sh_Kol>1545):
        Sh_Kol = 1545
    Sh_Kol = (Sh_Kol - 1510) / 35
     
    if (f_tr<0.1):
        f_tr = 0.1
    if (f_tr>0.75):
        f_tr = 0.75
    f_tr = (f_tr - 0.1) / 0.65
     
    netsum = -0.8779284
    netsum = netsum + VSP_type * 0.0196113
    netsum = netsum + Main_type * -1.628023E-02
    netsum = netsum + Radius * -0.3118623
    netsum = netsum + h * -0.6246858
    netsum = netsum + V * 3.431407
    netsum = netsum + Pst * -0.5934311
    netsum = netsum + Sh_Kol * 1.635297E-02
    netsum = netsum + f_tr * 6.492428E-02
    feature21 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.596228
    netsum = netsum + VSP_type * -9.683328E-03
    netsum = netsum + Main_type * 0.4581077
    netsum = netsum + Radius * -0.1272031
    netsum = netsum + h * 2.014749E-02
    netsum = netsum + V * 0.7440364
    netsum = netsum + Pst * 0.7920348
    netsum = netsum + Sh_Kol * 1.824367E-03
    netsum = netsum + f_tr * 0.1039098
    feature22 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.637069
    netsum = netsum + VSP_type * 4.684691E-03
    netsum = netsum + Main_type * 9.074254E-02
    netsum = netsum + Radius * 1.190828
    netsum = netsum + h * -0.649842
    netsum = netsum + V * 0.1637488
    netsum = netsum + Pst * 3.08047
    netsum = netsum + Sh_Kol * -4.281888E-04
    netsum = netsum + f_tr * 9.509201E-02
    feature23 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.3132215
    netsum = netsum + VSP_type * 3.73619E-03
    netsum = netsum + Main_type * -0.4145217
    netsum = netsum + Radius * -0.8156928
    netsum = netsum + h * 0.2219606
    netsum = netsum + V * 4.334057E-02
    netsum = netsum + Pst * 1.412599
    netsum = netsum + Sh_Kol * -2.731116E-03
    netsum = netsum + f_tr * 0.6049104
    feature24 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.1855786
    netsum = netsum + VSP_type * 0.0195484
    netsum = netsum + Main_type * -4.631246E-02
    netsum = netsum + Radius * -1.191343
    netsum = netsum + h * -0.6882868
    netsum = netsum + V * 3.358121
    netsum = netsum + Pst * -0.2213472
    netsum = netsum + Sh_Kol * 0.0165094
    netsum = netsum + f_tr * 0.1237197
    feature25 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.3112192
    netsum = netsum + VSP_type * -1.169685E-02
    netsum = netsum + Main_type * -0.2254246
    netsum = netsum + Radius * 2.768906
    netsum = netsum + h * -0.4581332
    netsum = netsum + V * -0.3690927
    netsum = netsum + Pst * 2.431689
    netsum = netsum + Sh_Kol * -1.615659E-03
    netsum = netsum + f_tr * 1.612557E-03
    feature26 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.003194
    netsum = netsum + VSP_type * -0.0187494
    netsum = netsum + Main_type * -0.3636706
    netsum = netsum + Radius * -15.39569
    netsum = netsum + h * 0.2740369
    netsum = netsum + V * -2.167522
    netsum = netsum + Pst * 2.241904
    netsum = netsum + Sh_Kol * -1.543768E-03
    netsum = netsum + f_tr * -2.651174
    feature27 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.252788
    netsum = netsum + VSP_type * -3.139062E-03
    netsum = netsum + Main_type * -5.410749E-02
    netsum = netsum + Radius * -4.877655
    netsum = netsum + h * -0.526661
    netsum = netsum + V * 1.078479
    netsum = netsum + Pst * 4.777053
    netsum = netsum + Sh_Kol * 2.01018E-03
    netsum = netsum + f_tr * 0.114046
    feature28 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.3193696
    netsum = netsum + VSP_type * 1.261251E-03
    netsum = netsum + Main_type * -0.2162307
    netsum = netsum + Radius * -0.9862177
    netsum = netsum + h * 0.1891039
    netsum = netsum + V * -0.1852484
    netsum = netsum + Pst * -1.234742
    netsum = netsum + Sh_Kol * -1.570796E-03
    netsum = netsum + f_tr * -4.251175E-02
    feature29 = 1 / (1 + math.exp(-netsum))
     
    netsum = 4.534059
    netsum = netsum + VSP_type * 1.788649E-03
    netsum = netsum + Main_type * -0.1028314
    netsum = netsum + Radius * -3.500344
    netsum = netsum + h * -4.595692E-02
    netsum = netsum + V * 0.3912673
    netsum = netsum + Pst * -0.5823087
    netsum = netsum + Sh_Kol * 1.610751E-03
    netsum = netsum + f_tr * 0.1503751
    feature210 = 1 / (1 + math.exp(-netsum))
     
    netsum = 5.107103E-02
    netsum = netsum + VSP_type * -4.374513E-03
    netsum = netsum + Main_type * -0.3509284
    netsum = netsum + Radius * -0.1275357
    netsum = netsum + h * -2.12247E-03
    netsum = netsum + V * 0.7795217
    netsum = netsum + Pst * -0.409476
    netsum = netsum + Sh_Kol * 1.62673E-04
    netsum = netsum + f_tr * 0.7189066
    feature211 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.833507
    netsum = netsum + VSP_type * 1.018576E-03
    netsum = netsum + Main_type * -2.597385E-02
    netsum = netsum + Radius * -19.02908
    netsum = netsum + h * 0.0633862
    netsum = netsum + V * 1.627645
    netsum = netsum + Pst * 3.308038
    netsum = netsum + Sh_Kol * -5.233867E-03
    netsum = netsum + f_tr * 1.417578
    feature212 = 1 / (1 + math.exp(-netsum))
     
    netsum = -5.813908
    netsum = netsum + VSP_type * 1.001322E-03
    netsum = netsum + Main_type * 2.190794E-02
    netsum = netsum + Radius * -50.41639
    netsum = netsum + h * -2.634212E-02
    netsum = netsum + V * 2.256421
    netsum = netsum + Pst * 2.354749
    netsum = netsum + Sh_Kol * -8.436926E-04
    netsum = netsum + f_tr * 0.1733611
    feature213 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.883401
    netsum = netsum + VSP_type * -8.898498E-05
    netsum = netsum + Main_type * 2.826454E-02
    netsum = netsum + Radius * -1.060984
    netsum = netsum + h * 0.5535195
    netsum = netsum + V * 0.1165256
    netsum = netsum + Pst * 4.197912
    netsum = netsum + Sh_Kol * 1.594416E-04
    netsum = netsum + f_tr * 9.258552E-02
    feature214 = 1 / (1 + math.exp(-netsum))
     
    netsum = -6.936395
    netsum = netsum + VSP_type * 2.406313E-02
    netsum = netsum + Main_type * -8.170411E-02
    netsum = netsum + Radius * -7.999993
    netsum = netsum + h * -0.1415604
    netsum = netsum + V * 2.002038
    netsum = netsum + Pst * 1.907866
    netsum = netsum + Sh_Kol * -9.61585E-03
    netsum = netsum + f_tr * 3.299991
    feature215 = 1 / (1 + math.exp(-netsum))
     
    netsum = 2.437062
    netsum = netsum + VSP_type * 0.0104815
    netsum = netsum + Main_type * -3.266933E-02
    netsum = netsum + Radius * 6.633762
    netsum = netsum + h * -0.1551777
    netsum = netsum + V * -0.841204
    netsum = netsum + Pst * 0.8992872
    netsum = netsum + Sh_Kol * -1.115624E-04
    netsum = netsum + f_tr * -0.2477242
    feature216 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.578948
    netsum = netsum + VSP_type * -3.70922E-03
    netsum = netsum + Main_type * -1.505512E-02
    netsum = netsum + Radius * -7.1371
    netsum = netsum + h * -0.434656
    netsum = netsum + V * 1.956263
    netsum = netsum + Pst * 3.0549
    netsum = netsum + Sh_Kol * 0
    netsum = netsum + f_tr * 0.1731671
    feature217 = 1 / (1 + math.exp(-netsum))
     
    netsum = -1.487802
    netsum = netsum + VSP_type * 2.375992E-02
    netsum = netsum + Main_type * -2.062043E-02
    netsum = netsum + Radius * 0.471993
    netsum = netsum + h * -0.6646476
    netsum = netsum + V * 3.761829
    netsum = netsum + Pst * -1.018315
    netsum = netsum + Sh_Kol * 2.035947E-02
    netsum = netsum + f_tr * -0.1628135
    feature218 = 1 / (1 + math.exp(-netsum))
     
    netsum = -7.835839E-02
    netsum = netsum + VSP_type * 1.346537E-02
    netsum = netsum + Main_type * 2.545992
    netsum = netsum + Radius * -3.239025
    netsum = netsum + h * -9.360485E-04
    netsum = netsum + V * 0.2478446
    netsum = netsum + Pst * 0.1425488
    netsum = netsum + Sh_Kol * 1.394994E-03
    netsum = netsum + f_tr * 6.538581E-02
    feature219 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.0851
    netsum = netsum + VSP_type * 1.46911E-03
    netsum = netsum + Main_type * -2.505987E-02
    netsum = netsum + Radius * -0.3247593
    netsum = netsum + h * 0.2009234
    netsum = netsum + V * 1.330669
    netsum = netsum + Pst * 0.6237336
    netsum = netsum + Sh_Kol * 4.473175E-03
    netsum = netsum + f_tr * -2.964767E-02
    feature220 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.2814425
    netsum = netsum + VSP_type * 8.441789E-04
    netsum = netsum + Main_type * -2.339525E-02
    netsum = netsum + Radius * -1.186471
    netsum = netsum + h * 0.1148786
    netsum = netsum + V * -0.1348869
    netsum = netsum + Pst * 2.080524
    netsum = netsum + Sh_Kol * 1.38199E-04
    netsum = netsum + f_tr * -0.154547
    feature221 = 1 / (1 + math.exp(-netsum))
     
    netsum = -2.546066
    netsum = netsum + VSP_type * -1.642044E-02
    netsum = netsum + Main_type * -0.3496358
    netsum = netsum + Radius * -20.86767
    netsum = netsum + h * 0.2272356
    netsum = netsum + V * -1.518378
    netsum = netsum + Pst * 2.167108
    netsum = netsum + Sh_Kol * -1.723164E-03
    netsum = netsum + f_tr * -3.557379
    feature222 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.13996
    netsum = netsum + VSP_type * -1.379909E-03
    netsum = netsum + Main_type * 5.425036E-02
    netsum = netsum + Radius * -33.27554
    netsum = netsum + h * 1.016273E-02
    netsum = netsum + V * 1.195987
    netsum = netsum + Pst * 2.318208
    netsum = netsum + Sh_Kol * -2.223326E-03
    netsum = netsum + f_tr * 0.3550184
    feature223 = 1 / (1 + math.exp(-netsum))
     
    netsum = 0.5040051
    netsum = netsum + VSP_type * 3.215188E-03
    netsum = netsum + Main_type * 7.419364E-03
    netsum = netsum + Radius * 1.464642
    netsum = netsum + h * -0.4642037
    netsum = netsum + V * -0.5562761
    netsum = netsum + Pst * -1.691309
    netsum = netsum + Sh_Kol * -2.340981E-03
    netsum = netsum + f_tr * -0.1666984
    feature224 = 1 / (1 + math.exp(-netsum))
     
    netsum = -4.334876
    netsum = netsum + VSP_type * -1.773412E-03
    netsum = netsum + Main_type * -4.815851E-03
    netsum = netsum + Radius * -12.42461
    netsum = netsum + h * -0.2524016
    netsum = netsum + V * 1.771035
    netsum = netsum + Pst * 4.579422
    netsum = netsum + Sh_Kol * -3.722528E-03
    netsum = netsum + f_tr * 0.167773
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

    #'Рамные силы

    #'средние значения
    Mean_H = round(((abs(outarray33)+abs(outarray34)+abs(outarray35)+abs(outarray36))/4),1)
    
    #'СКО
    Rms_H = round((((abs(outarray37)**2+abs(outarray38)**2+abs(outarray39)**2+abs(outarray40)**2)/4)**0.5),1)

    outarray = [outarray1, outarray2, outarray3, outarray4, outarray5,outarray6, outarray7, outarray8,outarray9, outarray10, outarray11, outarray12, outarray13,outarray14, outarray15, outarray16,outarray17, outarray18, outarray19, outarray20, outarray21,outarray22, outarray23, outarray24,outarray25, outarray26, outarray27, outarray28, outarray29,outarray30, outarray31, outarray32, outarray33, outarray34, outarray35, outarray36, outarray37, outarray38, outarray39, outarray40]
    for el in range(0,len(outarray)):
        outarray[el]=abs(round(outarray[el], 1))





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
    print ('по левой нити= {};\nпо правой нити = {};\nв среднем по экипажу= {};'.format (Mean_Q_L, Mean_Q_R, Mean_Q))
    print ()
    print ("СКО значений вертикальных сил `колесо-рельс, кН:")
    print ('по левой нити= {};\nпо правой нити = {};\nв среднем по экипажу= {};'.format(Rms_Q_L, Rms_Q_R, Rms_Q))
    print ()
    print ("Средние значения боковых сил `колесо-рельс`, кН:")
    print ('по левой нити= {};\nпо правой нити = {};\nв среднем по экипажу= {};'.format(Mean_Y_L, Mean_Y_R, Mean_Y))
    print ()
    print ("СКО значений боковых сил `колесо-рельс`:")
    print ('по левой нити= {};\nпо правой нити = {};\nв среднем по экипажу= {};'.format(Rms_Y_L, Rms_Y_R, Rms_Y))
    print ()
    print ("Средние значения рамных сил в среднем по экипажу кН: = ", Mean_H)
    print ()
    print ("СКО значений рамных сил в среднем по экипажу кН: =", Rms_H)


    

print (GR_VagoN_Force (2, 2, 250, 140, 80, 27.5, 1520, 0.25))
 

