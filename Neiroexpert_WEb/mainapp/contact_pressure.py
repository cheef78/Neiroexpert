
def contact_tension(input_val):

    '''
    opredelenie srednix znachenii
    napryagenii v tochke kontakta
    koleso-rels gruzovogo vagona
    Vxodnie dannie
    /* inarray[0] - это Vkmh */ skorost dvigeniya,
    /* inarray[1] - это Pts */ osevyaya nagruzka
    /* inarray[2] - это ftr */ koef treniya koleso-rels
    /* inarray[3] - это Rm */ radius krivoi
    /* inarray[4] - это Hmm */ vozvishenie krivoi
    /* inarray[5] - это ShKolmm * shirina kolei
    Vixodnie dannie
    /* outarray[0] - это MeanP1NarkPa */narygnii rels tochka 1
    /* outarray[1] - это MeanP1VnrkPa *
    vnutrenii rels tochka 1
    /* outarray[2] - это MeanP2NarkPa *
    narugnii rels tochka 2
    /* outarray[3] - это MeanP2VnrkPa *
    vnutrenii rels tochka 2
    tochka 1 - golovka relsa
    tochka 2 - bokovaya gran relsa
   
     '''

    from math import exp
    from random import gauss
    inarray = [0]*6
    outarray = [0]*4
    
    inarray[0] = input_val[0] 
    inarray[1] = input_val[1]
    inarray[2] = input_val[2]
    inarray[3] = input_val[3]
    inarray[4] = input_val[4]
    inarray[5] = input_val[5]

    feature2 = [0]*34
    feature3 = [0]*34
    
    if (inarray[0]<0):
         inarray[0] = 0
    if (inarray[0]>117.0887):
         inarray[0] = 117.0887
    inarray[0] =  2 * inarray[0] / 117.0887 -1
     
    if (inarray[1]<4):
         inarray[1] = 4
    if (inarray[1]>34.96661):
         inarray[1] = 34.96661
    inarray[1] =  2 * (inarray[1] - 4) / 30.96661 -1
     
    if (inarray[2]<0):
         inarray[2] = 0
    if (inarray[2]>0.6968256):
         inarray[2] = 0.6968256
    inarray[2] =  2 * inarray[2] / 0.6968256 -1
     
    if (inarray[3]<150):
         inarray[3] = 150
    if (inarray[3]>10000):
         inarray[3] = 10000
    inarray[3] =  2 * (inarray[3] - 150) / 9850 -1
     
    if (inarray[4]<0):
         inarray[4] = 0
    if (inarray[4]>160):
         inarray[4] = 160
    inarray[4] =  2 * inarray[4] / 160 -1
     
    if (inarray[5]<1487.456):
         inarray[5] = 1487.456
    if (inarray[5]>1565.044):
         inarray[5] = 1565.044
    inarray[5] =  2 * (inarray[5] - 1487.456) / 77.58789 -1
     
    netsum = 2.870922
    netsum += inarray[0] * -0.1709344
    netsum += inarray[1] * 0.2966346
    netsum += inarray[2] * 0.5379155
    netsum += inarray[3] * 6.366183
    netsum += inarray[4] * 0.2240459
    netsum += inarray[5] * 2.847323
    feature2[0] = exp(-netsum * netsum)
     
    netsum = 0.6385031
    netsum += inarray[0] * -0.2585038
    netsum += inarray[1] * 0.7043483
    netsum += inarray[2] * 0.936078
    netsum += inarray[3] * 1.257857
    netsum += inarray[4] * 0.6221642
    netsum += inarray[5] * 1.058738
    feature2[1] = exp(-netsum * netsum)
     
    netsum = 1.143515
    netsum += inarray[0] * -1.498042E-02
    netsum += inarray[1] * -1.192439E-02
    netsum += inarray[2] * -0.1524242
    netsum += inarray[3] * 0.220244
    netsum += inarray[4] * -3.687662E-02
    netsum += inarray[5] * -1.854256
    feature2[2] = exp(-netsum * netsum)
     
    netsum = 3.489393
    netsum += inarray[0] * 1.867759
    netsum += inarray[1] * 0.6215432
    netsum += inarray[2] * 1.378547
    netsum += inarray[3] * 0.9280712
    netsum += inarray[4] * -1.643068
    netsum += inarray[5] * 0.2586319
    feature2[3] = exp(-netsum * netsum)
     
    netsum = 9.120878E-02
    netsum += inarray[0] * -2.254164E-02
    netsum += inarray[1] * -9.891802E-02
    netsum += inarray[2] * -8.093496E-02
    netsum += inarray[3] * 0.1540929
    netsum += inarray[4] * -3.221845E-02
    netsum += inarray[5] * -2.987869E-02
    feature2[4] = exp(-netsum * netsum)
     
    netsum = -1.394357
    netsum += inarray[0] * -0.1088995
    netsum += inarray[1] * 0.3797587
    netsum += inarray[2] * 2.283877E-02
    netsum += inarray[3] * -0.5375136
    netsum += inarray[4] * 1.683216E-02
    netsum += inarray[5] * 3.214459
    feature2[5] = exp(-netsum * netsum)
     
    netsum = 1.60595
    netsum += inarray[0] * -0.2646919
    netsum += inarray[1] * 0.4588814
    netsum += inarray[2] * 0.6927755
    netsum += inarray[3] * 3.92536
    netsum += inarray[4] * 0.3667009
    netsum += inarray[5] * -6.527613E-03
    feature2[6] = exp(-netsum * netsum)
     
    netsum = -8.283701E-02
    netsum += inarray[0] * 0.9051446
    netsum += inarray[1] * 0.5037767
    netsum += inarray[2] * 0.2185411
    netsum += inarray[3] * -0.368861
    netsum += inarray[4] * 9.610359E-02
    netsum += inarray[5] * -1.407426E-02
    feature2[7] = exp(-netsum * netsum)
     
    netsum = -1.527804
    netsum += inarray[0] * -0.9558788
    netsum += inarray[1] * -0.1375043
    netsum += inarray[2] * -0.7563996
    netsum += inarray[3] * -0.7947075
    netsum += inarray[4] * 0.884544
    netsum += inarray[5] * 1.867297E-02
    feature2[8] = exp(-netsum * netsum)
     
    netsum = 0.1582844
    netsum += inarray[0] * 0.1690769
    netsum += inarray[1] * 0.5600514
    netsum += inarray[2] * -0.0390348
    netsum += inarray[3] * 0.3507375
    netsum += inarray[4] * 0.255347
    netsum += inarray[5] * 0.1432398
    feature2[9] = exp(-netsum * netsum)
     
    netsum = 1.643441
    netsum += inarray[0] * -0.1746619
    netsum += inarray[1] * -0.2160221
    netsum += inarray[2] * 9.116123E-02
    netsum += inarray[3] * 1.931185
    netsum += inarray[4] * -0.1059715
    netsum += inarray[5] * -0.7765722
    feature2[10] = exp(-netsum * netsum)
     
    netsum = 0.3126492
    netsum += inarray[0] * -4.494799E-02
    netsum += inarray[1] * -0.1285336
    netsum += inarray[2] * -6.436901E-02
    netsum += inarray[3] * -1.350925
    netsum += inarray[4] * -8.649003E-02
    netsum += inarray[5] * 4.134218
    feature2[11] = exp(-netsum * netsum)
     
    netsum = 0.3190714
    netsum += inarray[0] * 0.0218656
    netsum += inarray[1] * -0.3951759
    netsum += inarray[2] * -0.7990462
    netsum += inarray[3] * -0.5682194
    netsum += inarray[4] * -0.2612948
    netsum += inarray[5] * -1.945229
    feature2[12] = exp(-netsum * netsum)
     
    netsum = 0.5099972
    netsum += inarray[0] * 3.624618E-02
    netsum += inarray[1] * -0.175646
    netsum += inarray[2] * -0.432832
    netsum += inarray[3] * 0.7951019
    netsum += inarray[4] * 0.2369255
    netsum += inarray[5] * -0.1351196
    feature2[13] = exp(-netsum * netsum)
     
    netsum = 0.3600342
    netsum += inarray[0] * 1.045972
    netsum += inarray[1] * 0.9383097
    netsum += inarray[2] * 0.3548829
    netsum += inarray[3] * 0.5709983
    netsum += inarray[4] * 0.1239592
    netsum += inarray[5] * -0.5031498
    feature2[14] = exp(-netsum * netsum)
     
    netsum = -2.982012
    netsum += inarray[0] * -1.555809
    netsum += inarray[1] * -0.6247139
    netsum += inarray[2] * -1.248557
    netsum += inarray[3] * 0.3812528
    netsum += inarray[4] * 1.27212
    netsum += inarray[5] * 1.485257
    feature2[15] = exp(-netsum * netsum)
     
    netsum = 0.6761945
    netsum += inarray[0] * -0.2009013
    netsum += inarray[1] * 6.522259E-02
    netsum += inarray[2] * -5.303423E-02
    netsum += inarray[3] * 1.977283
    netsum += inarray[4] * -3.191051E-03
    netsum += inarray[5] * 1.382444
    feature2[16] = exp(-netsum * netsum)
     
    netsum = 3.781912
    netsum += inarray[0] * 2.28973
    netsum += inarray[1] * 0.9581401
    netsum += inarray[2] * 1.854602
    netsum += inarray[3] * -0.560687
    netsum += inarray[4] * -1.890435
    netsum += inarray[5] * -1.951481
    feature2[17] = exp(-netsum * netsum)
     
    netsum = 0.4838525
    netsum += inarray[0] * -0.5031015
    netsum += inarray[1] * -0.3665758
    netsum += inarray[2] * -7.188109E-02
    netsum += inarray[3] * 1.147216
    netsum += inarray[4] * 0.3112251
    netsum += inarray[5] * 0.5641898
    feature2[18] = exp(-netsum * netsum)
     
    netsum = 0.8326344
    netsum += inarray[0] * 0.1944844
    netsum += inarray[1] * -0.7988504
    netsum += inarray[2] * 0.5067988
    netsum += inarray[3] * 0.469945
    netsum += inarray[4] * -8.322838E-03
    netsum += inarray[5] * -0.2411868
    feature2[19] = exp(-netsum * netsum)
     
    netsum = 0.9234133
    netsum += inarray[0] * 1.117016
    netsum += inarray[1] * 0.3103575
    netsum += inarray[2] * 0.578948
    netsum += inarray[3] * -0.7250456
    netsum += inarray[4] * -0.7487242
    netsum += inarray[5] * -1.131261
    feature2[20] = exp(-netsum * netsum)
     
    netsum = 0.1731308
    netsum += inarray[0] * -0.3104963
    netsum += inarray[1] * 0.584317
    netsum += inarray[2] * 1.565835
    netsum += inarray[3] * 0.590124
    netsum += inarray[4] * -0.0212557
    netsum += inarray[5] * 0.4186759
    feature2[21] = exp(-netsum * netsum)
     
    netsum = 0.5845789
    netsum += inarray[0] * -0.1406148
    netsum += inarray[1] * -0.2228251
    netsum += inarray[2] * 0.1779324
    netsum += inarray[3] * 0.656308
    netsum += inarray[4] * 0.2133271
    netsum += inarray[5] * -0.5973055
    feature2[22] = exp(-netsum * netsum)
     
    netsum = 0.3688083
    netsum += inarray[0] * -0.2189959
    netsum += inarray[1] * 0.2037942
    netsum += inarray[2] * 1.947813
    netsum += inarray[3] * 0.7088616
    netsum += inarray[4] * 0.1291618
    netsum += inarray[5] * -0.6116017
    feature2[23] = exp(-netsum * netsum)
     
    netsum = -0.1046373
    netsum += inarray[0] * -1.158702
    netsum += inarray[1] * -0.4492837
    netsum += inarray[2] * -0.7870948
    netsum += inarray[3] * 2.00638
    netsum += inarray[4] * 0.9550489
    netsum += inarray[5] * 0.6562409
    feature2[24] = exp(-netsum * netsum)
     
    netsum = -1.081508
    netsum += inarray[0] * -0.3658609
    netsum += inarray[1] * 0.4189199
    netsum += inarray[2] * 1.080172
    netsum += inarray[3] * -1.757771
    netsum += inarray[4] * 0.1868747
    netsum += inarray[5] * -0.109082
    feature2[25] = exp(-netsum * netsum)
     
    netsum = 3.644433
    netsum += inarray[0] * -0.6750519
    netsum += inarray[1] * -0.2229991
    netsum += inarray[2] * 1.325312E-02
    netsum += inarray[3] * 3.796813
    netsum += inarray[4] * 0.1319001
    netsum += inarray[5] * 7.845893E-02
    feature2[26] = exp(-netsum * netsum)
     
    netsum = -0.589656
    netsum += inarray[0] * 7.812689E-02
    netsum += inarray[1] * -0.2146528
    netsum += inarray[2] * 0.2398288
    netsum += inarray[3] * -0.5753763
    netsum += inarray[4] * -0.1255705
    netsum += inarray[5] * 0.4405847
    feature2[27] = exp(-netsum * netsum)
     
    netsum = 7.429782E-02
    netsum += inarray[0] * 0.1712232
    netsum += inarray[1] * -0.3111293
    netsum += inarray[2] * 0.3331786
    netsum += inarray[3] * 1.164848E-02
    netsum += inarray[4] * 5.616463E-03
    netsum += inarray[5] * -0.3435604
    feature2[28] = exp(-netsum * netsum)
     
    netsum = -2.183661
    netsum += inarray[0] * 1.111804
    netsum += inarray[1] * 0.8146189
    netsum += inarray[2] * 0.1518127
    netsum += inarray[3] * -2.240546
    netsum += inarray[4] * -0.2198972
    netsum += inarray[5] * 1.67358
    feature2[29] = exp(-netsum * netsum)
     
    netsum = 0.919542
    netsum += inarray[0] * -1.166544
    netsum += inarray[1] * 0.4446957
    netsum += inarray[2] * -0.2141484
    netsum += inarray[3] * 1.697274
    netsum += inarray[4] * 2.579784E-02
    netsum += inarray[5] * 0.3250428
    feature2[30] = exp(-netsum * netsum)
     
    netsum = 0.2196291
    netsum += inarray[0] * 0.3844324
    netsum += inarray[1] * 9.187879E-02
    netsum += inarray[2] * -0.2946859
    netsum += inarray[3] * 0.1142023
    netsum += inarray[4] * -0.3507376
    netsum += inarray[5] * 0.4426298
    feature2[31] = exp(-netsum * netsum)
     
    netsum = -3.519399
    netsum += inarray[0] * 0.2368211
    netsum += inarray[1] * -0.2658618
    netsum += inarray[2] * -0.5096287
    netsum += inarray[3] * -4.747102
    netsum += inarray[4] * -0.1362839
    netsum += inarray[5] * -2.245426
    feature2[32] = exp(-netsum * netsum)
     
    netsum = 0.8527454
    netsum += inarray[0] * -0.7059404
    netsum += inarray[1] * -0.3905541
    netsum += inarray[2] * -0.1306179
    netsum += inarray[3] * 1.55917
    netsum += inarray[4] * 0.4114594
    netsum += inarray[5] * -0.5364193
    feature2[33] = exp(-netsum * netsum)
     
    netsum = 0.7579919
    netsum += inarray[0] * 0.4976018
    netsum += inarray[1] * -0.7850044
    netsum += inarray[2] * 4.001371E-02
    netsum += inarray[3] * -0.1497146
    netsum += inarray[4] * -0.4280744
    netsum += inarray[5] * -2.639421E-02
    feature3[0] = 1 - exp(-netsum * netsum)
     
    netsum = -2.209163
    netsum += inarray[0] * -2.31703
    netsum += inarray[1] * -0.8069867
    netsum += inarray[2] * -1.663535
    netsum += inarray[3] * 2.407358
    netsum += inarray[4] * 1.909309
    netsum += inarray[5] * 1.187976
    feature3[1] = 1 - exp(-netsum * netsum)
     
    netsum = -0.7006936
    netsum += inarray[0] * -0.9101481
    netsum += inarray[1] * -0.1502438
    netsum += inarray[2] * -0.3998405
    netsum += inarray[3] * -1.768251
    netsum += inarray[4] * 0.8539936
    netsum += inarray[5] * 0.9184044
    feature3[2] = 1 - exp(-netsum * netsum)
     
    netsum = -6.960914
    netsum += inarray[0] * -3.465542
    netsum += inarray[1] * -1.21863
    netsum += inarray[2] * -2.664028
    netsum += inarray[3] * -0.9776041
    netsum += inarray[4] * 3.10458
    netsum += inarray[5] * -0.1514443
    feature3[3] = 1 - exp(-netsum * netsum)
     
    netsum = -0.4435208
    netsum += inarray[0] * -0.134418
    netsum += inarray[1] * 0.7124152
    netsum += inarray[2] * 2.170282
    netsum += inarray[3] * -0.8729901
    netsum += inarray[4] * 0.0750066
    netsum += inarray[5] * 1.061123
    feature3[4] = 1 - exp(-netsum * netsum)
     
    netsum = -0.2238339
    netsum += inarray[0] * 1.643265
    netsum += inarray[1] * -1.605479
    netsum += inarray[2] * -1.508398
    netsum += inarray[3] * -1.482364E-02
    netsum += inarray[4] * -0.2950399
    netsum += inarray[5] * -0.2010006
    feature3[5] = 1 - exp(-netsum * netsum)
     
    netsum = -1.146813
    netsum += inarray[0] * -0.2321567
    netsum += inarray[1] * 5.534812E-03
    netsum += inarray[2] * -1.067468
    netsum += inarray[3] * -0.1213757
    netsum += inarray[4] * 0.1234335
    netsum += inarray[5] * -0.5423688
    feature3[6] = 1 - exp(-netsum * netsum)
     
    netsum = -7.264486E-02
    netsum += inarray[0] * -6.528773E-02
    netsum += inarray[1] * 4.793605E-02
    netsum += inarray[2] * 0.1668123
    netsum += inarray[3] * 2.556697
    netsum += inarray[4] * -0.2516116
    netsum += inarray[5] * -3.119162
    feature3[7] = 1 - exp(-netsum * netsum)
     
    netsum = 1.597033
    netsum += inarray[0] * 0.6899796
    netsum += inarray[1] * 0.3501705
    netsum += inarray[2] * 6.409386E-02
    netsum += inarray[3] * 1.32902
    netsum += inarray[4] * 4.767419E-02
    netsum += inarray[5] * -0.8072698
    feature3[8] = 1 - exp(-netsum * netsum)
     
    netsum = 1.41619
    netsum += inarray[0] * 0.2710829
    netsum += inarray[1] * -0.5059657
    netsum += inarray[2] * -1.020178
    netsum += inarray[3] * 0.9413456
    netsum += inarray[4] * -0.3614626
    netsum += inarray[5] * -1.583415
    feature3[9] = 1 - exp(-netsum * netsum)
     
    netsum = -0.1050907
    netsum += inarray[0] * 1.242113
    netsum += inarray[1] * 0.5972585
    netsum += inarray[2] * 4.593644E-03
    netsum += inarray[3] * 0.1450088
    netsum += inarray[4] * -0.1729529
    netsum += inarray[5] * 1.373099
    feature3[10] = 1 - exp(-netsum * netsum)
     
    netsum = 0.4922536
    netsum += inarray[0] * 0.3363292
    netsum += inarray[1] * 0.770148
    netsum += inarray[2] * 0.3523988
    netsum += inarray[3] * -1.70229
    netsum += inarray[4] * 1.340834E-02
    netsum += inarray[5] * 1.261875
    feature3[11] = 1 - exp(-netsum * netsum)
     
    netsum = 1.066884
    netsum += inarray[0] * -2.429437E-02
    netsum += inarray[1] * -1.119532
    netsum += inarray[2] * 1.898761E-02
    netsum += inarray[3] * -0.7798601
    netsum += inarray[4] * -0.5480192
    netsum += inarray[5] * 0.865302
    feature3[12] = 1 - exp(-netsum * netsum)
     
    netsum = -6.09714
    netsum += inarray[0] * -1.831939E-02
    netsum += inarray[1] * -0.2555449
    netsum += inarray[2] * -0.6891471
    netsum += inarray[3] * -6.773226
    netsum += inarray[4] * -3.152465E-02
    netsum += inarray[5] * 3.053856E-03
    feature3[13] = 1 - exp(-netsum * netsum)
     
    netsum = 2.827041
    netsum += inarray[0] * -0.2619284
    netsum += inarray[1] * 0.638375
    netsum += inarray[2] * 0.7924762
    netsum += inarray[3] * 4.376039
    netsum += inarray[4] * 0.241523
    netsum += inarray[5] * -2.073022
    feature3[14] = 1 - exp(-netsum * netsum)
     
    netsum = -1.848365
    netsum += inarray[0] * -0.1109518
    netsum += inarray[1] * 0.2575763
    netsum += inarray[2] * 0.5459399
    netsum += inarray[3] * -4.478484
    netsum += inarray[4] * 0.1651636
    netsum += inarray[5] * -1.091999
    feature3[15] = 1 - exp(-netsum * netsum)
     
    netsum = -2.048573
    netsum += inarray[0] * -1.283699
    netsum += inarray[1] * -0.6812662
    netsum += inarray[2] * -0.6172915
    netsum += inarray[3] * -1.012995
    netsum += inarray[4] * 1.056027
    netsum += inarray[5] * -0.4868996
    feature3[16] = 1 - exp(-netsum * netsum)
     
    netsum = -0.2923197
    netsum += inarray[0] * 0.8032992
    netsum += inarray[1] * 0.5759339
    netsum += inarray[2] * 0.2003317
    netsum += inarray[3] * -1.479848
    netsum += inarray[4] * 0.2690604
    netsum += inarray[5] * 0.9145094
    feature3[17] = 1 - exp(-netsum * netsum)
     
    netsum = -4.523268
    netsum += inarray[0] * 3.653694E-02
    netsum += inarray[1] * -1.074733
    netsum += inarray[2] * -1.933933
    netsum += inarray[3] * -3.45098
    netsum += inarray[4] * -5.357601E-03
    netsum += inarray[5] * -0.5923494
    feature3[18] = 1 - exp(-netsum * netsum)
     
    netsum = 5.1321
    netsum += inarray[0] * 3.958659
    netsum += inarray[1] * 1.530399
    netsum += inarray[2] * 3.019997
    netsum += inarray[3] * -4.208408
    netsum += inarray[4] * -3.362905
    netsum += inarray[5] * -2.046824
    feature3[19] = 1 - exp(-netsum * netsum)
     
    netsum = 0.3730311
    netsum += inarray[0] * 0.3267936
    netsum += inarray[1] * -1.992004E-02
    netsum += inarray[2] * 1.393222
    netsum += inarray[3] * -2.744768
    netsum += inarray[4] * -0.5449148
    netsum += inarray[5] * -0.9933057
    feature3[20] = 1 - exp(-netsum * netsum)
     
    netsum = -0.4999798
    netsum += inarray[0] * -0.688598
    netsum += inarray[1] * -0.2644385
    netsum += inarray[2] * -0.3437606
    netsum += inarray[3] * -0.9519657
    netsum += inarray[4] * 0.7402512
    netsum += inarray[5] * -0.2853001
    feature3[21] = 1 - exp(-netsum * netsum)
     
    netsum = 2.068297
    netsum += inarray[0] * 0.2912332
    netsum += inarray[1] * -0.4556541
    netsum += inarray[2] * -0.7093301
    netsum += inarray[3] * 2.325591
    netsum += inarray[4] * 4.239777E-02
    netsum += inarray[5] * 1.654081E-02
    feature3[22] = 1 - exp(-netsum * netsum)
     
    netsum = 1.998786
    netsum += inarray[0] * 0.5104601
    netsum += inarray[1] * -9.145394E-02
    netsum += inarray[2] * 0.4257052
    netsum += inarray[3] * -8.046222E-02
    netsum += inarray[4] * -0.5253967
    netsum += inarray[5] * 2.538559
    feature3[23] = 1 - exp(-netsum * netsum)
     
    netsum = 4.584753
    netsum += inarray[0] * 0.1008678
    netsum += inarray[1] * -0.5281554
    netsum += inarray[2] * -1.189754
    netsum += inarray[3] * 4.960383
    netsum += inarray[4] * -0.2101993
    netsum += inarray[5] * -1.369859
    feature3[24] = 1 - exp(-netsum * netsum)
     
    netsum = -3.762112E-03
    netsum += inarray[0] * 0.4687877
    netsum += inarray[1] * -0.1563176
    netsum += inarray[2] * 0.2209737
    netsum += inarray[3] * -0.6399092
    netsum += inarray[4] * -0.6173603
    netsum += inarray[5] * -1.514595
    feature3[25] = 1 - exp(-netsum * netsum)
     
    netsum = -0.6217445
    netsum += inarray[0] * 1.054147
    netsum += inarray[1] * 1.901649
    netsum += inarray[2] * 1.278337
    netsum += inarray[3] * -2.334659
    netsum += inarray[4] * -0.5391058
    netsum += inarray[5] * 0.1779773
    feature3[26] = 1 - exp(-netsum * netsum)
     
    netsum = 1.198872
    netsum += inarray[0] * 2.29927E-03
    netsum += inarray[1] * 0.6157554
    netsum += inarray[2] * 1.594114
    netsum += inarray[3] * 0.6438758
    netsum += inarray[4] * 0.1437111
    netsum += inarray[5] * 2.591039
    feature3[27] = 1 - exp(-netsum * netsum)
     
    netsum = 0.9869338
    netsum += inarray[0] * 0.2357347
    netsum += inarray[1] * -0.6389729
    netsum += inarray[2] * -0.2497306
    netsum += inarray[3] * -1.369684
    netsum += inarray[4] * -0.6461128
    netsum += inarray[5] * 0.3055304
    feature3[28] = 1 - exp(-netsum * netsum)
     
    netsum = 0.4205779
    netsum += inarray[0] * -3.567313E-02
    netsum += inarray[1] * 0.323145
    netsum += inarray[2] * -8.167553E-02
    netsum += inarray[3] * 2.635495
    netsum += inarray[4] * 3.139522E-02
    netsum += inarray[5] * 2.832717
    feature3[29] = 1 - exp(-netsum * netsum)
     
    netsum = 0.6098891
    netsum += inarray[0] * -1.14869
    netsum += inarray[1] * -0.7055368
    netsum += inarray[2] * -0.1797591
    netsum += inarray[3] * 0.7954444
    netsum += inarray[4] * 1.021059
    netsum += inarray[5] * -0.6047441
    feature3[30] = 1 - exp(-netsum * netsum)
     
    netsum = -1.67581
    netsum += inarray[0] * 0.5532246
    netsum += inarray[1] * 0.8891231
    netsum += inarray[2] * 6.576145E-02
    netsum += inarray[3] * 1.015595
    netsum += inarray[4] * 1.010015
    netsum += inarray[5] * 0.4375064
    feature3[31] = 1 - exp(-netsum * netsum)
     
    netsum = 1.612202
    netsum += inarray[0] * -4.773217E-02
    netsum += inarray[1] * 1.226136E-02
    netsum += inarray[2] * 1.722918
    netsum += inarray[3] * 2.826659
    netsum += inarray[4] * -1.681293E-02
    netsum += inarray[5] * 0.0300523
    feature3[32] = 1 - exp(-netsum * netsum)
     
    netsum = 1.490042
    netsum += inarray[0] * -9.403924E-02
    netsum += inarray[1] * -0.9728081
    netsum += inarray[2] * -1.614913
    netsum += inarray[3] * 2.444813
    netsum += inarray[4] * 5.186298E-02
    netsum += inarray[5] * -1.419652
    feature3[33] = 1 - exp(-netsum * netsum)
     
    netsum = 0.2735161
    netsum += feature2[0] * 5.959876E-02
    netsum += feature2[1] * -1.383784E-02
    netsum += feature2[2] * 0.4911033
    netsum += feature2[3] * -0.2024737
    netsum += feature2[4] * 0.3754871
    netsum += feature2[5] * -3.469343E-02
    netsum += feature2[6] * 0.0144539
    netsum += feature2[7] * -0.2371082
    netsum += feature2[8] * -0.3579402
    netsum += feature2[9] * 0.8669408
    netsum += feature2[10] * -0.5239532
    netsum += feature2[11] * 0
    netsum += feature2[12] * 5.718947E-02
    netsum += feature2[13] * -0.2080274
    netsum += feature2[14] * -0.0063828
    netsum += feature2[15] * -1.745149
    netsum += feature2[16] * 0.1504962
    netsum += feature2[17] * 0.6947228
    netsum += feature2[18] * -0.5251881
    netsum += feature2[19] * 0.8514457
    netsum += feature2[20] * -0.4119942
    netsum += feature2[21] * -0.1612389
    netsum += feature2[22] * 0.3456592
    netsum += feature2[23] * -0.3243569
    netsum += feature2[24] * 0.0629444
    netsum += feature2[25] * 3.044558E-02
    netsum += feature2[26] * -0.3590586
    netsum += feature2[27] * 0.895155
    netsum += feature2[28] * -0.676325
    netsum += feature2[29] * 3.618046E-02
    netsum += feature2[30] * -1.998793E-02
    netsum += feature2[31] * 0.6161522
    netsum += feature2[32] * 4.585169E-02
    netsum += feature2[33] * -0.1498002
    netsum += 0.1573428
    netsum += feature3[0] * -0.3802629
    netsum += feature3[1] * -1.707426E-02
    netsum += feature3[2] * -1.981976E-02
    netsum += feature3[3] * 0.1652146
    netsum += feature3[4] * 3.128598E-02
    netsum += feature3[5] * -3.612335E-02
    netsum += feature3[6] * -0.930863
    netsum += feature3[7] * -0.0458991
    netsum += feature3[8] * 8.060002E-02
    netsum += feature3[9] * -5.854122E-03
    netsum += feature3[10] * 2.113987E-02
    netsum += feature3[11] * 0.3705913
    netsum += feature3[12] * -0.2013422
    netsum += feature3[13] * -0.1118073
    netsum += feature3[14] * -2.798178E-02
    netsum += feature3[15] * 1.389313E-02
    netsum += feature3[16] * 0.1744753
    netsum += feature3[17] * -5.334504E-02
    netsum += feature3[18] * 6.453327E-02
    netsum += feature3[19] * -0.1121702
    netsum += feature3[20] * -0.1819186
    netsum += feature3[21] * 0.4343027
    netsum += feature3[22] * -0.4943948
    netsum += feature3[23] * -1.869235E-02
    netsum += feature3[24] * -5.366623E-02
    netsum += feature3[25] * 0.1170909
    netsum += feature3[26] * -3.996839E-04
    netsum += feature3[27] * -6.031729E-03
    netsum += feature3[28] * -0.2548312
    netsum += feature3[29] * 3.904042E-02
    netsum += feature3[30] * 7.569411E-02
    netsum += feature3[31] * -8.825617E-02
    netsum += feature3[32] * -0.5181542
    netsum += feature3[33] * -2.294639E-02
    outarray[0] = 1 / (1 + exp(-netsum))
     
    netsum = -0.1146993
    netsum += feature2[0] * 0.7000574
    netsum += feature2[1] * 0.2301377
    netsum += feature2[2] * -0.145658
    netsum += feature2[3] * 6.787513E-02
    netsum += feature2[4] * 0.1118827
    netsum += feature2[5] * -0.8012405
    netsum += feature2[6] * -0.8343202
    netsum += feature2[7] * 0.6440349
    netsum += feature2[8] * 1.757573E-02
    netsum += feature2[9] * 0.2182112
    netsum += feature2[10] * -0.6085759
    netsum += feature2[11] * 0.1753709
    netsum += feature2[12] * 0.4194033
    netsum += feature2[13] * -0.2773445
    netsum += feature2[14] * -0.4080719
    netsum += feature2[15] * 0.9572216
    netsum += feature2[16] * 0.8081154
    netsum += feature2[17] * -0.2992148
    netsum += feature2[18] * 0.6515808
    netsum += feature2[19] * 0.6371306
    netsum += feature2[20] * 0.4410324
    netsum += feature2[21] * 0.3976742
    netsum += feature2[22] * -0.5721232
    netsum += feature2[23] * 2.195918E-02
    netsum += feature2[24] * -0.4045893
    netsum += feature2[25] * -6.563077E-02
    netsum += feature2[26] * 0.5626828
    netsum += feature2[27] * -0.634345
    netsum += feature2[28] * -0.2786896
    netsum += feature2[29] * -0.4064644
    netsum += feature2[30] * 0.1665453
    netsum += feature2[31] * 5.730223E-02
    netsum += feature2[32] * 0.2747712
    netsum += feature2[33] * -0.6781382
    netsum += -0.1065983
    netsum += feature3[0] * -0.1292579
    netsum += feature3[1] * 0.2498481
    netsum += feature3[2] * 0.1076604
    netsum += feature3[3] * -5.300703E-02
    netsum += feature3[4] * 0.2843404
    netsum += feature3[5] * 3.814204E-02
    netsum += feature3[6] * 0.2822843
    netsum += feature3[7] * -0.1257476
    netsum += feature3[8] * 0.4284963
    netsum += feature3[9] * 0.4726807
    netsum += feature3[10] * -0.2325874
    netsum += feature3[11] * 7.518622E-02
    netsum += feature3[12] * 2.221917E-02
    netsum += feature3[13] * -4.284835E-02
    netsum += feature3[14] * 6.951547E-02
    netsum += feature3[15] * 0.464974
    netsum += feature3[16] * -0.1816227
    netsum += feature3[17] * 0.1044917
    netsum += feature3[18] * -8.973236E-02
    netsum += feature3[19] * 0.394529
    netsum += feature3[20] * 0.7393378
    netsum += feature3[21] * -0.3027051
    netsum += feature3[22] * -0.2329604
    netsum += feature3[23] * 0.1554373
    netsum += feature3[24] * -0.2012921
    netsum += feature3[25] * 0.2266408
    netsum += feature3[26] * 5.224089E-02
    netsum += feature3[27] * -6.479687E-02
    netsum += feature3[28] * -0.5551189
    netsum += feature3[29] * -1.23819
    netsum += feature3[30] * -6.194295E-02
    netsum += feature3[31] * -0.8995034
    netsum += feature3[32] * 0.4192137
    netsum += feature3[33] * 1.29675E-03
    outarray[1] = 1 / (1 + exp(-netsum))
     
    netsum = -0.7220055
    netsum += feature2[0] * -2.083175
    netsum += feature2[1] * -0.3610741
    netsum += feature2[2] * 0.1378341
    netsum += feature2[3] * 0.2848273
    netsum += feature2[4] * -0.2798637
    netsum += feature2[5] * -1.618678E-02
    netsum += feature2[6] * -1.316236
    netsum += feature2[7] * -0.2432481
    netsum += feature2[8] * -0.1824279
    netsum += feature2[9] * -0.0742157
    netsum += feature2[10] * -0.2574705
    netsum += feature2[11] * 1.121096
    netsum += feature2[12] * 0.6038552
    netsum += feature2[13] * -0.7227964
    netsum += feature2[14] * 0.3303045
    netsum += feature2[15] * 0.3231693
    netsum += feature2[16] * -2.261356E-02
    netsum += feature2[17] * -6.480174E-02
    netsum += feature2[18] * -0.5714833
    netsum += feature2[19] * 0.319556
    netsum += feature2[20] * 0.2495454
    netsum += feature2[21] * 0.6391029
    netsum += feature2[22] * -0.4389904
    netsum += feature2[23] * 0.8081533
    netsum += feature2[24] * -0.5281509
    netsum += feature2[25] * -0.9515238
    netsum += feature2[26] * -1.486654
    netsum += feature2[27] * -0.2837105
    netsum += feature2[28] * 0.2233734
    netsum += feature2[29] * 0.1892719
    netsum += feature2[30] * -0.4821235
    netsum += feature2[31] * -0.7914949
    netsum += feature2[32] * -0.9656526
    netsum += feature2[33] * -0.1548557
    netsum += -0.8025805
    netsum += feature3[0] * -0.1325205
    netsum += feature3[1] * 0.3274681
    netsum += feature3[2] * 0.3759196
    netsum += feature3[3] * -8.463196E-02
    netsum += feature3[4] * -0.3871408
    netsum += feature3[5] * -0.209923
    netsum += feature3[6] * 1.466747E-02
    netsum += feature3[7] * 1.475133
    netsum += feature3[8] * -0.5466219
    netsum += feature3[9] * -0.558548
    netsum += feature3[10] * 0.2231175
    netsum += feature3[11] * 1.197846
    netsum += feature3[12] * -0.045179
    netsum += feature3[13] * 1.199547
    netsum += feature3[14] * 0.5528461
    netsum += feature3[15] * 1.438231
    netsum += feature3[16] * -0.4635527
    netsum += feature3[17] * 0.3285093
    netsum += feature3[18] * -0.7312363
    netsum += feature3[19] * 0.2936597
    netsum += feature3[20] * 0.6558375
    netsum += feature3[21] * -0.4657404
    netsum += feature3[22] * 0.5811822
    netsum += feature3[23] * 0.5674469
    netsum += feature3[24] * 0.4394772
    netsum += feature3[25] * 0.1731994
    netsum += feature3[26] * 0.2535648
    netsum += feature3[27] * -0.357803
    netsum += feature3[28] * -6.619808E-02
    netsum += feature3[29] * 7.793254E-02
    netsum += feature3[30] * -0.1913882
    netsum += feature3[31] * -0.4587024
    netsum += feature3[32] * 0.846521
    netsum += feature3[33] * 0.4046221
    outarray[2] = 1 / (1 + exp(-netsum))
     
    netsum = -0.1735701
    netsum += feature2[0] * -0.1832885
    netsum += feature2[1] * -0.107519
    netsum += feature2[2] * -0.5068482
    netsum += feature2[3] * -1.378698
    netsum += feature2[4] * -0.2160282
    netsum += feature2[5] * 2.749965E-02
    netsum += feature2[6] * -0.1383739
    netsum += feature2[7] * 1.364847E-02
    netsum += feature2[8] * -0.8690193
    netsum += feature2[9] * -9.150342E-02
    netsum += feature2[10] * -0.5988894
    netsum += feature2[11] * -1.163646E-02
    netsum += feature2[12] * 0.1061414
    netsum += feature2[13] * -0.3284851
    netsum += feature2[14] * -2.039452E-02
    netsum += feature2[15] * -0.6174875
    netsum += feature2[16] * -0.5757423
    netsum += feature2[17] * 0.4304953
    netsum += feature2[18] * 0.6690497
    netsum += feature2[19] * -0.2142984
    netsum += feature2[20] * 0.4450828
    netsum += feature2[21] * -0.1658648
    netsum += feature2[22] * 0.220265
    netsum += feature2[23] * -0.1173263
    netsum += feature2[24] * 0.8612968
    netsum += feature2[25] * -4.536046E-02
    netsum += feature2[26] * 0.1569739
    netsum += feature2[27] * 0.2818956
    netsum += feature2[28] * -5.019738E-02
    netsum += feature2[29] * 0.0418326
    netsum += feature2[30] * 0.1286864
    netsum += feature2[31] * -1.223903E-02
    netsum += feature2[32] * -6.631374E-02
    netsum += feature2[33] * 0.468149
    netsum += -0.1304529
    netsum += feature3[0] * -0.2445475
    netsum += feature3[1] * -1.578274
    netsum += feature3[2] * 9.783833E-02
    netsum += feature3[3] * 2.372457
    netsum += feature3[4] * 3.208755E-02
    netsum += feature3[5] * -9.755409E-02
    netsum += feature3[6] * -0.1952839
    netsum += feature3[7] * 0.4377203
    netsum += feature3[8] * 0.1443489
    netsum += feature3[9] * 3.713622E-02
    netsum += feature3[10] * 0.1184329
    netsum += feature3[11] * 0.4256321
    netsum += feature3[12] * 0.682803
    netsum += feature3[13] * 7.696144E-02
    netsum += feature3[14] * 0.1068686
    netsum += feature3[15] * 0.1790456
    netsum += feature3[16] * 0.6054494
    netsum += feature3[17] * 0.2541224
    netsum += feature3[18] * 0.1279896
    netsum += feature3[19] * -3.674188
    netsum += feature3[20] * 0.5750314
    netsum += feature3[21] * 0.610135
    netsum += feature3[22] * -3.114258E-02
    netsum += feature3[23] * -0.8969904
    netsum += feature3[24] * -5.494307E-02
    netsum += feature3[25] * -0.342831
    netsum += feature3[26] * 0.0153483
    netsum += feature3[27] * 4.374801E-02
    netsum += feature3[28] * 4.266493E-02
    netsum += feature3[29] * -0.1428587
    netsum += feature3[30] * 8.578555E-02
    netsum += feature3[31] * 4.601491E-02
    netsum += feature3[32] * 3.355273E-02
    netsum += feature3[33] * -3.290808E-02
    outarray[3] = 1 / (1 + exp(-netsum))
     
     
    outarray[0] = 778753.4 *  (outarray[0] - .1) / .8  + 300540.6
    if (outarray[0]<300540.6):
         outarray[0] = 300540.6
    if (outarray[0]>1079294):
         outarray[0] = 1079294
     
    outarray[1] = 2617954 *  (outarray[1] - .1) / .8  + 100
    if (outarray[1]<100):
         outarray[1] = 100
    if (outarray[1]>2618054):
         outarray[1] = 2618054
     
    outarray[2] = 416089.1 *  (outarray[2] - .1) / .8 
    if (outarray[2]<0):
         outarray[2] = 0
    if (outarray[2]>416089.1):
         outarray[2] = 416089.1
     
    outarray[3] = 8807.689 *  (outarray[3] - .1) / .8 
    if (outarray[3]<0):
         outarray[3] = 0
    if (outarray[3]>8807.689):
         outarray[3] = 8807.689
    for i in range (4):
        outarray[i] = round(outarray[i],1)     

    MeanP1NarkPa = outarray[0]
    MeanP1VnrkPa = outarray[1]
    MeanP2NarkPa = outarray[2]
    MeanP2VnrkPa = outarray[3] 

    '''
   opredelenie CKO znachenii
    napryagenii v tochke kontakta
    koleso-rels gruzovogo vagona
    Vxodnie dannie
    /* inarray[0] - это Vkmh */ skorost dvigeniya,
    /* inarray[1] - это Pts */ osevyaya nagruzka
    /* inarray[2] - это ftr */ koef treniya koleso-rels
    /* inarray[3] - это Rm */ radius krivoi
    /* inarray[4] - это Hmm */ vozvishenie krivoi
    /* inarray[5] - это ShKolmm * shirina kolei
    Vixodnie dannie
    /* outarray[0] - это RmsP1NarkPa */narygnii rels tochka 1
    /* outarray[1] - это RmsP1VnrkPa *
    vnutrenii rels tochka 1
    /* outarray[2] - это RmsP2NarkPa *
    narugnii rels tochka 2
    /* outarray[3] - это RmsP2VnrkPa *
    vnutrenii rels tochka 2
    tochka 1 - golovka relsa
    tochka 2 - bokovaya gran relsa  
    
    Vxodnie dannie
    /* inarray[0] - это Vkmh */
    /* inarray[1] - это Pts */
    /* inarray[2] - это ftr */
    /* inarray[3] - это Rm */
    /* inarray[4] - это Hmm */
    /* inarray[5] - это ShKolmm */
    Vixodnie dannie
    /* outarray[0] - это RmsP1NarkPa */
    /* outarray[1] - это RmsP1VnrkPa */
    /* outarray[2] - это RmsP2NarkPa */
    /* outarray[3] - это RmsP2VnrkPa */
    '''
     
    
    inarray = [0]*6
    outarray = [0]*4
    
    inarray[0] = input_val[0] 
    inarray[1] = input_val[1]
    inarray[2] = input_val[2]
    inarray[3] = input_val[3]
    inarray[4] = input_val[4]
    inarray[5] = input_val[5]

     
    feature2 = [0]*34
    feature3 = [0]*34

    if (inarray[0]<0):
         inarray[0] = 0
    if (inarray[0]>117.0887):
         inarray[0] = 117.0887
    inarray[0] =  2 * inarray[0] / 117.0887 -1
     
    if (inarray[1]<4):
         inarray[1] = 4
    if (inarray[1]>34.96661):
         inarray[1] = 34.96661
    inarray[1] =  2 * (inarray[1] - 4) / 30.96661 -1
     
    if (inarray[2]<0):
         inarray[2] = 0
    if (inarray[2]>0.6968256):
         inarray[2] = 0.6968256
    inarray[2] =  2 * inarray[2] / 0.6968256 -1
     
    if (inarray[3]<150):
         inarray[3] = 150
    if (inarray[3]>10000):
         inarray[3] = 10000
    inarray[3] =  2 * (inarray[3] - 150) / 9850 -1
     
    if (inarray[4]<0):
         inarray[4] = 0
    if (inarray[4]>160):
         inarray[4] = 160
    inarray[4] =  2 * inarray[4] / 160 -1
     
    if (inarray[5]<1487.456):
         inarray[5] = 1487.456
    if (inarray[5]>1565.044):
         inarray[5] = 1565.044
    inarray[5] =  2 * (inarray[5] - 1487.456) / 77.58789 -1
     
    netsum = 2.030594
    netsum += inarray[0] * 0.9229666
    netsum += inarray[1] * -0.75137
    netsum += inarray[2] * -1.763644
    netsum += inarray[3] * 12.24227
    netsum += inarray[4] * -2.279955
    netsum += inarray[5] * 8.534709
    feature2[0] = exp(-netsum * netsum)
     
    netsum = 4.154599
    netsum += inarray[0] * -1.05762
    netsum += inarray[1] * 2.980742
    netsum += inarray[2] * 0.4206856
    netsum += inarray[3] * 5.035431
    netsum += inarray[4] * 3.172524
    netsum += inarray[5] * 0.6164301
    feature2[1] = exp(-netsum * netsum)
     
    netsum = -0.3086867
    netsum += inarray[0] * 0.3593926
    netsum += inarray[1] * -1.925157
    netsum += inarray[2] * 0.2947011
    netsum += inarray[3] * -0.569023
    netsum += inarray[4] * -0.1646354
    netsum += inarray[5] * -0.0936015
    feature2[2] = exp(-netsum * netsum)
     
    netsum = -0.2358086
    netsum += inarray[0] * 0.3033647
    netsum += inarray[1] * -0.3431318
    netsum += inarray[2] * -0.6189394
    netsum += inarray[3] * 0.8502384
    netsum += inarray[4] * -0.6380749
    netsum += inarray[5] * 1.100961
    feature2[3] = exp(-netsum * netsum)
     
    netsum = -1.834956
    netsum += inarray[0] * 0.3680406
    netsum += inarray[1] * 1.129058
    netsum += inarray[2] * 0.2347932
    netsum += inarray[3] * -3.14763
    netsum += inarray[4] * -1.221421
    netsum += inarray[5] * 0.1772434
    feature2[4] = exp(-netsum * netsum)
     
    netsum = 1.209888
    netsum += inarray[0] * -3.138339
    netsum += inarray[1] * -0.229291
    netsum += inarray[2] * -3.72433
    netsum += inarray[3] * 2.526373
    netsum += inarray[4] * 0.4970961
    netsum += inarray[5] * -0.2470263
    feature2[5] = exp(-netsum * netsum)
     
    netsum = 0.1969477
    netsum += inarray[0] * 0.026788
    netsum += inarray[1] * -0.2433345
    netsum += inarray[2] * 6.119773E-02
    netsum += inarray[3] * 0.2913502
    netsum += inarray[4] * -0.1203686
    netsum += inarray[5] * -7.344706E-02
    feature2[6] = exp(-netsum * netsum)
     
    netsum = 4.643849
    netsum += inarray[0] * -0.8688977
    netsum += inarray[1] * -0.3691869
    netsum += inarray[2] * -0.8883011
    netsum += inarray[3] * 5.446286
    netsum += inarray[4] * 0.3496463
    netsum += inarray[5] * 8.153903E-02
    feature2[7] = exp(-netsum * netsum)
     
    netsum = -0.6275235
    netsum += inarray[0] * 0.1363837
    netsum += inarray[1] * -0.1455713
    netsum += inarray[2] * -1.432411
    netsum += inarray[3] * -0.2448982
    netsum += inarray[4] * 0.7107624
    netsum += inarray[5] * -0.5684376
    feature2[8] = exp(-netsum * netsum)
     
    netsum = -0.8885357
    netsum += inarray[0] * 0.5186368
    netsum += inarray[1] * 4.596108
    netsum += inarray[2] * 6.598529
    netsum += inarray[3] * 0.3240569
    netsum += inarray[4] * 0.8428171
    netsum += inarray[5] * 2.664966
    feature2[9] = exp(-netsum * netsum)
     
    netsum = 3.712486E-03
    netsum += inarray[0] * 7.094418E-04
    netsum += inarray[1] * -4.451035E-03
    netsum += inarray[2] * 8.829886E-04
    netsum += inarray[3] * 5.946829E-03
    netsum += inarray[4] * -2.639253E-03
    netsum += inarray[5] * 9.128568E-04
    feature2[10] = exp(-netsum * netsum)
     
    netsum = 8.364408
    netsum += inarray[0] * -0.3964036
    netsum += inarray[1] * 1.640533
    netsum += inarray[2] * 0.8955773
    netsum += inarray[3] * 14.51563
    netsum += inarray[4] * 0.7249586
    netsum += inarray[5] * 6.119374
    feature2[11] = exp(-netsum * netsum)
     
    netsum = -4.323256
    netsum += inarray[0] * 0.3505282
    netsum += inarray[1] * -3.352843
    netsum += inarray[2] * -1.975177
    netsum += inarray[3] * -11.40985
    netsum += inarray[4] * -1.941277
    netsum += inarray[5] * -9.285951
    feature2[12] = exp(-netsum * netsum)
     
    netsum = -1.575977
    netsum += inarray[0] * 3.72852
    netsum += inarray[1] * -1.4871
    netsum += inarray[2] * 0.8692094
    netsum += inarray[3] * -2.413016
    netsum += inarray[4] * -1.435374
    netsum += inarray[5] * -0.1983054
    feature2[13] = exp(-netsum * netsum)
     
    netsum = 0.2709953
    netsum += inarray[0] * 0.4573268
    netsum += inarray[1] * 0.4637841
    netsum += inarray[2] * -6.656381E-02
    netsum += inarray[3] * 0.2478632
    netsum += inarray[4] * 0.0516358
    netsum += inarray[5] * 0.1757832
    feature2[14] = exp(-netsum * netsum)
     
    netsum = 0.5179883
    netsum += inarray[0] * -2.078331
    netsum += inarray[1] * -1.223044
    netsum += inarray[2] * -0.3374733
    netsum += inarray[3] * 6.545147
    netsum += inarray[4] * 3.641
    netsum += inarray[5] * 1.741253
    feature2[15] = exp(-netsum * netsum)
     
    netsum = 0.6758174
    netsum += inarray[0] * -3.604222E-02
    netsum += inarray[1] * -1.982422
    netsum += inarray[2] * -0.8136192
    netsum += inarray[3] * 1.452583
    netsum += inarray[4] * -1.50282
    netsum += inarray[5] * 0.3583823
    feature2[16] = exp(-netsum * netsum)
     
    netsum = -3.986625
    netsum += inarray[0] * -2.698853
    netsum += inarray[1] * -2.9596
    netsum += inarray[2] * -0.6617997
    netsum += inarray[3] * -3.18124
    netsum += inarray[4] * 1.602978
    netsum += inarray[5] * -0.3305015
    feature2[17] = exp(-netsum * netsum)
     
    netsum = -3.321949
    netsum += inarray[0] * 3.445144
    netsum += inarray[1] * -1.87375
    netsum += inarray[2] * 0.5345124
    netsum += inarray[3] * 0.7063607
    netsum += inarray[4] * 4.600534
    netsum += inarray[5] * 0.4334214
    feature2[18] = exp(-netsum * netsum)
     
    netsum = -4.21314
    netsum += inarray[0] * -0.8134876
    netsum += inarray[1] * -3.334181E-02
    netsum += inarray[2] * -1.170955
    netsum += inarray[3] * -4.989483
    netsum += inarray[4] * 0.1639202
    netsum += inarray[5] * 0.5615274
    feature2[19] = exp(-netsum * netsum)
     
    netsum = -0.5679628
    netsum += inarray[0] * 0.678288
    netsum += inarray[1] * 1.374511
    netsum += inarray[2] * -0.5027024
    netsum += inarray[3] * -4.909833
    netsum += inarray[4] * -1.781427
    netsum += inarray[5] * -5.434855
    feature2[20] = exp(-netsum * netsum)
     
    netsum = -0.7808152
    netsum += inarray[0] * -4.623079E-02
    netsum += inarray[1] * 0.1352506
    netsum += inarray[2] * -0.3970298
    netsum += inarray[3] * 0.6627445
    netsum += inarray[4] * 0.3368387
    netsum += inarray[5] * 2.443345
    feature2[21] = exp(-netsum * netsum)
     
    netsum = 0.9819084
    netsum += inarray[0] * -0.4348
    netsum += inarray[1] * 1.579205
    netsum += inarray[2] * 0.5729729
    netsum += inarray[3] * 0.6280093
    netsum += inarray[4] * 0.9098899
    netsum += inarray[5] * -5.22445E-03
    feature2[22] = exp(-netsum * netsum)
     
    netsum = 0.6597465
    netsum += inarray[0] * 2.289586
    netsum += inarray[1] * 2.710865
    netsum += inarray[2] * -0.3484352
    netsum += inarray[3] * 5.567194
    netsum += inarray[4] * 3.533188
    netsum += inarray[5] * 2.548869
    feature2[23] = exp(-netsum * netsum)
     
    netsum = -0.8322363
    netsum += inarray[0] * 1.000433
    netsum += inarray[1] * -1.033631
    netsum += inarray[2] * 0.1215003
    netsum += inarray[3] * 1.370627
    netsum += inarray[4] * 2.643283
    netsum += inarray[5] * 0.107408
    feature2[24] = exp(-netsum * netsum)
     
    netsum = -1.616117
    netsum += inarray[0] * 1.293458
    netsum += inarray[1] * 0.2403879
    netsum += inarray[2] * 1.340959
    netsum += inarray[3] * -0.6484456
    netsum += inarray[4] * 1.20154
    netsum += inarray[5] * 0.7323048
    feature2[25] = exp(-netsum * netsum)
     
    netsum = -1.900848
    netsum += inarray[0] * 1.530277
    netsum += inarray[1] * -0.728411
    netsum += inarray[2] * -3.622421
    netsum += inarray[3] * -3.262019
    netsum += inarray[4] * -3.760069
    netsum += inarray[5] * 0.250816
    feature2[26] = exp(-netsum * netsum)
     
    netsum = 1.670182
    netsum += inarray[0] * -2.742256
    netsum += inarray[1] * 2.412158E-02
    netsum += inarray[2] * 4.172599
    netsum += inarray[3] * 2.981586
    netsum += inarray[4] * 1.37742
    netsum += inarray[5] * -0.2205704
    feature2[27] = exp(-netsum * netsum)
     
    netsum = 0.0939277
    netsum += inarray[0] * -2.148619E-04
    netsum += inarray[1] * 0.4408852
    netsum += inarray[2] * 0.2113651
    netsum += inarray[3] * 0.9523541
    netsum += inarray[4] * 0.2786655
    netsum += inarray[5] * 1.7942
    feature2[28] = exp(-netsum * netsum)
     
    netsum = 1.021887
    netsum += inarray[0] * -0.4641224
    netsum += inarray[1] * -0.4066875
    netsum += inarray[2] * -0.1691504
    netsum += inarray[3] * 1.211288
    netsum += inarray[4] * -0.5175842
    netsum += inarray[5] * -2.738861E-02
    feature2[29] = exp(-netsum * netsum)
     
    netsum = 1.189004E-02
    netsum += inarray[0] * 6.407152E-05
    netsum += inarray[1] * -4.380801E-03
    netsum += inarray[2] * -1.529733E-03
    netsum += inarray[3] * 1.676793E-02
    netsum += inarray[4] * -3.790262E-03
    netsum += inarray[5] * 4.889477E-04
    feature2[30] = exp(-netsum * netsum)
     
    netsum = -0.133856
    netsum += inarray[0] * 1.240596
    netsum += inarray[1] * 6.103351
    netsum += inarray[2] * -0.1101243
    netsum += inarray[3] * -6.772127
    netsum += inarray[4] * -1.713357
    netsum += inarray[5] * 0.3478912
    feature2[31] = exp(-netsum * netsum)
     
    netsum = -2.853996
    netsum += inarray[0] * 9.244233E-02
    netsum += inarray[1] * -1.436044
    netsum += inarray[2] * -2.375896
    netsum += inarray[3] * -5.728159
    netsum += inarray[4] * -0.4784093
    netsum += inarray[5] * -4.412597
    feature2[32] = exp(-netsum * netsum)
     
    netsum = 0.2352725
    netsum += inarray[0] * -7.136764E-02
    netsum += inarray[1] * -0.1523269
    netsum += inarray[2] * -4.262416E-02
    netsum += inarray[3] * 0.3286492
    netsum += inarray[4] * -4.347866E-02
    netsum += inarray[5] * -0.196693
    feature2[33] = exp(-netsum * netsum)
     
    netsum = 1.312202
    netsum += inarray[0] * 3.63748
    netsum += inarray[1] * 8.980172
    netsum += inarray[2] * 0.2329544
    netsum += inarray[3] * -7.364478
    netsum += inarray[4] * -1.646645
    netsum += inarray[5] * 8.327322E-02
    feature3[0] = 1 - exp(-netsum * netsum)
     
    netsum = 3.187348
    netsum += inarray[0] * -2.285564
    netsum += inarray[1] * 5.159831
    netsum += inarray[2] * -1.223218
    netsum += inarray[3] * 11.7896
    netsum += inarray[4] * 2.263062
    netsum += inarray[5] * 8.098322
    feature3[1] = 1 - exp(-netsum * netsum)
     
    netsum = 1.613687
    netsum += inarray[0] * -0.2197798
    netsum += inarray[1] * -0.7125556
    netsum += inarray[2] * -1.750167E-02
    netsum += inarray[3] * -1.53659
    netsum += inarray[4] * -0.3362291
    netsum += inarray[5] * 0.2293964
    feature3[2] = 1 - exp(-netsum * netsum)
     
    netsum = -0.2938181
    netsum += inarray[0] * -2.011337
    netsum += inarray[1] * 2.274685
    netsum += inarray[2] * -0.138999
    netsum += inarray[3] * 1.076024
    netsum += inarray[4] * 4.29484
    netsum += inarray[5] * 0.4910577
    feature3[3] = 1 - exp(-netsum * netsum)
     
    netsum = -0.4872201
    netsum += inarray[0] * -1.095595
    netsum += inarray[1] * -0.5372103
    netsum += inarray[2] * 0.4814157
    netsum += inarray[3] * -0.2602243
    netsum += inarray[4] * 2.474079
    netsum += inarray[5] * 7.713963
    feature3[4] = 1 - exp(-netsum * netsum)
     
    netsum = -1.91685
    netsum += inarray[0] * 0.7685798
    netsum += inarray[1] * 0.2967916
    netsum += inarray[2] * 0.499686
    netsum += inarray[3] * 0.9312869
    netsum += inarray[4] * 0.3833738
    netsum += inarray[5] * -0.75252
    feature3[5] = 1 - exp(-netsum * netsum)
     
    netsum = -1.062492
    netsum += inarray[0] * -0.5973643
    netsum += inarray[1] * 0.6463832
    netsum += inarray[2] * -0.6637364
    netsum += inarray[3] * 2.105509
    netsum += inarray[4] * -1.341728
    netsum += inarray[5] * -1.638582
    feature3[6] = 1 - exp(-netsum * netsum)
     
    netsum = -1.265818
    netsum += inarray[0] * 0.4933572
    netsum += inarray[1] * 0.1243107
    netsum += inarray[2] * 0.4312536
    netsum += inarray[3] * -1.810161
    netsum += inarray[4] * -0.2124315
    netsum += inarray[5] * -2.901026
    feature3[7] = 1 - exp(-netsum * netsum)
     
    netsum = 1.572212
    netsum += inarray[0] * -2.304779
    netsum += inarray[1] * 2.127913
    netsum += inarray[2] * 1.005858
    netsum += inarray[3] * -4.215553
    netsum += inarray[4] * -0.9767933
    netsum += inarray[5] * 0.455914
    feature3[8] = 1 - exp(-netsum * netsum)
     
    netsum = -3.701864
    netsum += inarray[0] * 0.2586107
    netsum += inarray[1] * 3.984073
    netsum += inarray[2] * 5.688683
    netsum += inarray[3] * -2.70024
    netsum += inarray[4] * 1.24073
    netsum += inarray[5] * 1.77324
    feature3[9] = 1 - exp(-netsum * netsum)
     
    netsum = -3.364771
    netsum += inarray[0] * -0.7563325
    netsum += inarray[1] * -0.2868436
    netsum += inarray[2] * 0.5564805
    netsum += inarray[3] * -4.968077
    netsum += inarray[4] * 1.797018
    netsum += inarray[5] * -6.936031
    feature3[10] = 1 - exp(-netsum * netsum)
     
    netsum = 2.26704
    netsum += inarray[0] * 1.276989
    netsum += inarray[1] * -1.018328
    netsum += inarray[2] * 1.549074
    netsum += inarray[3] * -0.684893
    netsum += inarray[4] * 2.108195
    netsum += inarray[5] * 2.848406
    feature3[11] = 1 - exp(-netsum * netsum)
     
    netsum = 0.3890584
    netsum += inarray[0] * -8.111764
    netsum += inarray[1] * -0.6860328
    netsum += inarray[2] * -2.839457
    netsum += inarray[3] * -11.56547
    netsum += inarray[4] * 2.085507
    netsum += inarray[5] * -6.87276
    feature3[12] = 1 - exp(-netsum * netsum)
     
    netsum = 1.775851
    netsum += inarray[0] * -2.418741
    netsum += inarray[1] * -1.218365
    netsum += inarray[2] * -1.884352
    netsum += inarray[3] * -1.209133
    netsum += inarray[4] * 2.981939
    netsum += inarray[5] * 3.415832
    feature3[13] = 1 - exp(-netsum * netsum)
     
    netsum = 1.40182
    netsum += inarray[0] * -1.55417
    netsum += inarray[1] * -0.9231133
    netsum += inarray[2] * -0.6979874
    netsum += inarray[3] * -3.022248
    netsum += inarray[4] * -3.732624
    netsum += inarray[5] * 2.531196
    feature3[14] = 1 - exp(-netsum * netsum)
     
    netsum = -1.49533
    netsum += inarray[0] * 0.313104
    netsum += inarray[1] * 1.03012
    netsum += inarray[2] * 7.637271E-02
    netsum += inarray[3] * 0.9081777
    netsum += inarray[4] * -9.951727E-03
    netsum += inarray[5] * -1.617779
    feature3[15] = 1 - exp(-netsum * netsum)
     
    netsum = -4.900025
    netsum += inarray[0] * -0.4075316
    netsum += inarray[1] * -0.5821678
    netsum += inarray[2] * -1.283671
    netsum += inarray[3] * -4.432806
    netsum += inarray[4] * 0.6005754
    netsum += inarray[5] * -2.169037
    feature3[16] = 1 - exp(-netsum * netsum)
     
    netsum = -0.9354485
    netsum += inarray[0] * -2.730954
    netsum += inarray[1] * -5.377693
    netsum += inarray[2] * -7.918156
    netsum += inarray[3] * 0.5796951
    netsum += inarray[4] * -3.004057
    netsum += inarray[5] * -0.9214038
    feature3[17] = 1 - exp(-netsum * netsum)
     
    netsum = -1.244755
    netsum += inarray[0] * 0.809218
    netsum += inarray[1] * 2.384445
    netsum += inarray[2] * 0.8506948
    netsum += inarray[3] * 2.767587
    netsum += inarray[4] * 2.277778
    netsum += inarray[5] * 0.5206548
    feature3[18] = 1 - exp(-netsum * netsum)
     
    netsum = 3.152684
    netsum += inarray[0] * -1.380288
    netsum += inarray[1] * 1.569146
    netsum += inarray[2] * 0.5021255
    netsum += inarray[3] * -3.453054
    netsum += inarray[4] * -4.943602
    netsum += inarray[5] * 0.1274633
    feature3[19] = 1 - exp(-netsum * netsum)
     
    netsum = -6.319303
    netsum += inarray[0] * 3.286099
    netsum += inarray[1] * -3.34903
    netsum += inarray[2] * 4.242351
    netsum += inarray[3] * -0.9695245
    netsum += inarray[4] * 1.792817
    netsum += inarray[5] * -0.6064181
    feature3[20] = 1 - exp(-netsum * netsum)
     
    netsum = -0.8039296
    netsum += inarray[0] * -0.9597088
    netsum += inarray[1] * -0.5599974
    netsum += inarray[2] * -1.077543
    netsum += inarray[3] * -4.257777
    netsum += inarray[4] * 1.684166
    netsum += inarray[5] * 5.173134
    feature3[21] = 1 - exp(-netsum * netsum)
     
    netsum = 1.825577
    netsum += inarray[0] * 3.737126
    netsum += inarray[1] * 6.625909
    netsum += inarray[2] * -1.83165
    netsum += inarray[3] * 0.792574
    netsum += inarray[4] * 4.436039
    netsum += inarray[5] * -1.35041
    feature3[22] = 1 - exp(-netsum * netsum)
     
    netsum = 2.895608
    netsum += inarray[0] * 2.834784
    netsum += inarray[1] * -5.404934
    netsum += inarray[2] * -2.857788
    netsum += inarray[3] * 8.347687
    netsum += inarray[4] * 1.812997
    netsum += inarray[5] * 1.240583
    feature3[23] = 1 - exp(-netsum * netsum)
     
    netsum = -6.175918
    netsum += inarray[0] * 0.2639709
    netsum += inarray[1] * -1.632994
    netsum += inarray[2] * -1.453704
    netsum += inarray[3] * -10.92906
    netsum += inarray[4] * -0.2867456
    netsum += inarray[5] * -7.279444
    feature3[24] = 1 - exp(-netsum * netsum)
     
    netsum = -1.027605
    netsum += inarray[0] * 2.345401
    netsum += inarray[1] * 1.008608
    netsum += inarray[2] * 0.2493783
    netsum += inarray[3] * 4.773959
    netsum += inarray[4] * 2.511879
    netsum += inarray[5] * -7.192843
    feature3[25] = 1 - exp(-netsum * netsum)
     
    netsum = 3.962045
    netsum += inarray[0] * 2.403018
    netsum += inarray[1] * 5.062217
    netsum += inarray[2] * 7.581748
    netsum += inarray[3] * 2.641402
    netsum += inarray[4] * 3.044659
    netsum += inarray[5] * 0.982594
    feature3[26] = 1 - exp(-netsum * netsum)
     
    netsum = -0.8960341
    netsum += inarray[0] * 4.113463
    netsum += inarray[1] * 9.723203E-03
    netsum += inarray[2] * 0.2036271
    netsum += inarray[3] * -0.4659611
    netsum += inarray[4] * -7.159029
    netsum += inarray[5] * -0.1133634
    feature3[27] = 1 - exp(-netsum * netsum)
     
    netsum = -3.814154
    netsum += inarray[0] * -3.457133
    netsum += inarray[1] * -1.259275
    netsum += inarray[2] * 0.1843103
    netsum += inarray[3] * -8.711478
    netsum += inarray[4] * -2.840014
    netsum += inarray[5] * -2.155158
    feature3[28] = 1 - exp(-netsum * netsum)
     
    netsum = 3.502862
    netsum += inarray[0] * -5.469507E-02
    netsum += inarray[1] * -2.12995
    netsum += inarray[2] * 1.933291
    netsum += inarray[3] * 15.09961
    netsum += inarray[4] * -1.306551
    netsum += inarray[5] * 7.828796
    feature3[29] = 1 - exp(-netsum * netsum)
     
    netsum = -9.425274E-02
    netsum += inarray[0] * -1.008992
    netsum += inarray[1] * -5.911864
    netsum += inarray[2] * 2.909356
    netsum += inarray[3] * 4.983648
    netsum += inarray[4] * 3.427126
    netsum += inarray[5] * 7.779063E-02
    feature3[30] = 1 - exp(-netsum * netsum)
     
    netsum = 3.386852
    netsum += inarray[0] * -0.9569891
    netsum += inarray[1] * 1.020422
    netsum += inarray[2] * 1.072306
    netsum += inarray[3] * 1.257105
    netsum += inarray[4] * 5.23349
    netsum += inarray[5] * 1.495884
    feature3[31] = 1 - exp(-netsum * netsum)
     
    netsum = -1.272292
    netsum += inarray[0] * -2.422375
    netsum += inarray[1] * -0.692721
    netsum += inarray[2] * 2.221453
    netsum += inarray[3] * 5.760062
    netsum += inarray[4] * -4.185505
    netsum += inarray[5] * 1.134742
    feature3[32] = 1 - exp(-netsum * netsum)
     
    netsum = -1.717543
    netsum += inarray[0] * 9.215626E-02
    netsum += inarray[1] * 0.2086339
    netsum += inarray[2] * 0.1586293
    netsum += inarray[3] * 1.446642
    netsum += inarray[4] * -0.0154877
    netsum += inarray[5] * -0.3015959
    feature3[33] = 1 - exp(-netsum * netsum)
     
    netsum = 0.5842419
    netsum += feature2[0] * 0.4621142
    netsum += feature2[1] * 0.2395849
    netsum += feature2[2] * 0.7898192
    netsum += feature2[3] * 0.3341044
    netsum += feature2[4] * -0.4593203
    netsum += feature2[5] * 0.5460318
    netsum += feature2[6] * 0.5556369
    netsum += feature2[7] * -0.5859515
    netsum += feature2[8] * -0.2497099
    netsum += feature2[9] * 0.4299183
    netsum += feature2[10] * 0.5093677
    netsum += feature2[11] * 3.441766E-02
    netsum += feature2[12] * 0.6687465
    netsum += feature2[13] * 0.3435295
    netsum += feature2[14] * 0.6072867
    netsum += feature2[15] * -0.4844365
    netsum += feature2[16] * -0.3911096
    netsum += feature2[17] * 0.3448124
    netsum += feature2[18] * -0.0299338
    netsum += feature2[19] * 1.068797E-03
    netsum += feature2[20] * -0.4550302
    netsum += feature2[21] * -0.4803776
    netsum += feature2[22] * 0.5134575
    netsum += feature2[23] * -0.4934925
    netsum += feature2[24] * 0.4357155
    netsum += feature2[25] * 0.1984311
    netsum += feature2[26] * -0.2068487
    netsum += feature2[27] * 0.4956127
    netsum += feature2[28] * 0.4928781
    netsum += feature2[29] * 0.4106096
    netsum += feature2[30] * 0.4161034
    netsum += feature2[31] * 0.8029865
    netsum += feature2[32] * 0.1489247
    netsum += feature2[33] * 0.7291292
    netsum += 0.468043
    netsum += feature3[0] * -1.546929
    netsum += feature3[1] * -0.388829
    netsum += feature3[2] * 0.1039572
    netsum += feature3[3] * 0.3072085
    netsum += feature3[4] * -6.633662E-02
    netsum += feature3[5] * 0.7640804
    netsum += feature3[6] * -0.3863593
    netsum += feature3[7] * 0.3095515
    netsum += feature3[8] * -3.4718
    netsum += feature3[9] * 0.3360212
    netsum += feature3[10] * 7.844005E-02
    netsum += feature3[11] * -0.1057489
    netsum += feature3[12] * -2.922971
    netsum += feature3[13] * 1.011151E-02
    netsum += feature3[14] * 0.2391992
    netsum += feature3[15] * 0.8679458
    netsum += feature3[16] * -0.2011455
    netsum += feature3[17] * 0.2692214
    netsum += feature3[18] * -0.98665
    netsum += feature3[19] * 2.039221
    netsum += feature3[20] * -0.8680427
    netsum += feature3[21] * 0.141783
    netsum += feature3[22] * 0.1064501
    netsum += feature3[23] * 0.3283634
    netsum += feature3[24] * 0.2619427
    netsum += feature3[25] * -9.52157E-03
    netsum += feature3[26] * -0.2909219
    netsum += feature3[27] * 0.2198609
    netsum += feature3[28] * -0.3373298
    netsum += feature3[29] * -1.42633
    netsum += feature3[30] * 0.3050179
    netsum += feature3[31] * -6.646286E-02
    netsum += feature3[32] * 0.5131766
    netsum += feature3[33] * 0.2730577
    outarray[0] = 1 / (1 + exp(-netsum))
     
    netsum = 0.4837898
    netsum += feature2[0] * 1.568622
    netsum += feature2[1] * 0.3115447
    netsum += feature2[2] * 0.2792281
    netsum += feature2[3] * 0.704707
    netsum += feature2[4] * -6.296925E-02
    netsum += feature2[5] * 0.2464476
    netsum += feature2[6] * 0.3711174
    netsum += feature2[7] * -0.4256063
    netsum += feature2[8] * -0.1868902
    netsum += feature2[9] * 0.2430132
    netsum += feature2[10] * 0.5081166
    netsum += feature2[11] * 5.228963E-02
    netsum += feature2[12] * 0.9396908
    netsum += feature2[13] * 3.518748E-02
    netsum += feature2[14] * -0.5257366
    netsum += feature2[15] * -0.7327641
    netsum += feature2[16] * -0.1665383
    netsum += feature2[17] * 0.2080667
    netsum += feature2[18] * 0.4122975
    netsum += feature2[19] * -0.1650388
    netsum += feature2[20] * -0.243654
    netsum += feature2[21] * 0.4439399
    netsum += feature2[22] * 0.1647935
    netsum += feature2[23] * -0.6540437
    netsum += feature2[24] * -3.168296E-02
    netsum += feature2[25] * 0.4569299
    netsum += feature2[26] * -0.1794062
    netsum += feature2[27] * 0.3411432
    netsum += feature2[28] * -0.7014255
    netsum += feature2[29] * 0.8340526
    netsum += feature2[30] * 0.5107028
    netsum += feature2[31] * 8.989318E-02
    netsum += feature2[32] * 0.7765998
    netsum += feature2[33] * 7.400413E-02
    netsum += 0.4918766
    netsum += feature3[0] * -0.1174575
    netsum += feature3[1] * -1.274991
    netsum += feature3[2] * -4.809857E-02
    netsum += feature3[3] * 0.350022
    netsum += feature3[4] * -0.0616407
    netsum += feature3[5] * 0.5659704
    netsum += feature3[6] * 1.330983E-02
    netsum += feature3[7] * 0.1881965
    netsum += feature3[8] * 1.6508
    netsum += feature3[9] * 0.4028956
    netsum += feature3[10] * 0.1619921
    netsum += feature3[11] * 3.418461E-02
    netsum += feature3[12] * -3.973388
    netsum += feature3[13] * 2.058932E-04
    netsum += feature3[14] * 0.5032537
    netsum += feature3[15] * 1.328341
    netsum += feature3[16] * -2.782469E-02
    netsum += feature3[17] * 0.4279225
    netsum += feature3[18] * -1.999551
    netsum += feature3[19] * -0.9341014
    netsum += feature3[20] * -3.022483E-02
    netsum += feature3[21] * 5.554702E-02
    netsum += feature3[22] * 0.2090679
    netsum += feature3[23] * 8.256842E-02
    netsum += feature3[24] * 0.8549371
    netsum += feature3[25] * -0.2790122
    netsum += feature3[26] * -0.3446527
    netsum += feature3[27] * 0.1874223
    netsum += feature3[28] * -0.3937803
    netsum += feature3[29] * -3.256029
    netsum += feature3[30] * 0.1613774
    netsum += feature3[31] * -5.663314E-02
    netsum += feature3[32] * 0.6415733
    netsum += feature3[33] * 0.146077
    outarray[1] = 1 / (1 + exp(-netsum))
     
    netsum = -0.1987713
    netsum += feature2[0] * -0.9418263
    netsum += feature2[1] * 0.8579806
    netsum += feature2[2] * 3.890892E-02
    netsum += feature2[3] * -4.620354E-02
    netsum += feature2[4] * -0.1878154
    netsum += feature2[5] * 0.7378255
    netsum += feature2[6] * -0.4235254
    netsum += feature2[7] * -0.4277034
    netsum += feature2[8] * -0.4393723
    netsum += feature2[9] * 1.232112
    netsum += feature2[10] * -6.317855E-02
    netsum += feature2[11] * 1.443126
    netsum += feature2[12] * 0.5482914
    netsum += feature2[13] * 3.627002E-02
    netsum += feature2[14] * -7.663301E-02
    netsum += feature2[15] * -0.5992354
    netsum += feature2[16] * 0.3021342
    netsum += feature2[17] * 0.2292498
    netsum += feature2[18] * 0.8230318
    netsum += feature2[19] * -0.6516698
    netsum += feature2[20] * -0.403835
    netsum += feature2[21] * 4.292984E-02
    netsum += feature2[22] * -0.3683805
    netsum += feature2[23] * -1.208057
    netsum += feature2[24] * -0.3518138
    netsum += feature2[25] * 0.1856817
    netsum += feature2[26] * -0.4609449
    netsum += feature2[27] * 0.6423957
    netsum += feature2[28] * 0.1167538
    netsum += feature2[29] * 5.183274E-02
    netsum += feature2[30] * -1.357844E-03
    netsum += feature2[31] * 0.5424591
    netsum += feature2[32] * 0.8651082
    netsum += feature2[33] * -0.2975464
    netsum += -0.2793596
    netsum += feature3[0] * -0.2783296
    netsum += feature3[1] * -1.005933
    netsum += feature3[2] * 2.980727E-02
    netsum += feature3[3] * 0.8107374
    netsum += feature3[4] * -0.359964
    netsum += feature3[5] * -0.3788767
    netsum += feature3[6] * -1.002511
    netsum += feature3[7] * 4.449647E-02
    netsum += feature3[8] * -0.4353136
    netsum += feature3[9] * 0.8697627
    netsum += feature3[10] * 0.5286965
    netsum += feature3[11] * -0.3906296
    netsum += feature3[12] * -2.359737
    netsum += feature3[13] * -0.705966
    netsum += feature3[14] * 1.766968
    netsum += feature3[15] * 0.5674295
    netsum += feature3[16] * -0.3697282
    netsum += feature3[17] * 1.438339
    netsum += feature3[18] * 0.3296949
    netsum += feature3[19] * 1.825667
    netsum += feature3[20] * 3.572346E-03
    netsum += feature3[21] * 1.098369
    netsum += feature3[22] * 0.3537023
    netsum += feature3[23] * 0.2994466
    netsum += feature3[24] * 1.103433
    netsum += feature3[25] * -1.905719
    netsum += feature3[26] * -1.222873
    netsum += feature3[27] * 0.5141879
    netsum += feature3[28] * -1.504388
    netsum += feature3[29] * -1.304565
    netsum += feature3[30] * 0.1926549
    netsum += feature3[31] * -0.3331795
    netsum += feature3[32] * 1.846108
    netsum += feature3[33] * -0.2826309
    outarray[2] = 1 / (1 + exp(-netsum))
     
    netsum = -0.3078614
    netsum += feature2[0] * 3.222993E-02
    netsum += feature2[1] * 2.625441E-02
    netsum += feature2[2] * 2.463555E-02
    netsum += feature2[3] * 2.431613E-02
    netsum += feature2[4] * -1.230035E-02
    netsum += feature2[5] * 0.0265327
    netsum += feature2[6] * -0.5208019
    netsum += feature2[7] * 1.642919E-02
    netsum += feature2[8] * -6.370982E-02
    netsum += feature2[9] * 7.713957E-03
    netsum += feature2[10] * -0.4773933
    netsum += feature2[11] * 6.39209E-03
    netsum += feature2[12] * -8.921984E-04
    netsum += feature2[13] * -1.420836E-02
    netsum += feature2[14] * 0.1723563
    netsum += feature2[15] * 0.10131
    netsum += feature2[16] * -5.075105E-02
    netsum += feature2[17] * -1.891429E-03
    netsum += feature2[18] * -6.490196E-02
    netsum += feature2[19] * -1.337343E-02
    netsum += feature2[20] * 1.348953E-02
    netsum += feature2[21] * 8.917481E-03
    netsum += feature2[22] * 5.502101E-02
    netsum += feature2[23] * -3.798924E-05
    netsum += feature2[24] * 7.220488E-02
    netsum += feature2[25] * -0.0101737
    netsum += feature2[26] * 1.528516E-02
    netsum += feature2[27] * -0.0110052
    netsum += feature2[28] * -0.0307862
    netsum += feature2[29] * 8.304694E-02
    netsum += feature2[30] * -0.3496855
    netsum += feature2[31] * 1.084083E-02
    netsum += feature2[32] * -5.912373E-03
    netsum += feature2[33] * -0.1230208
    netsum += -0.26474
    netsum += feature3[0] * -1.197815E-02
    netsum += feature3[1] * 3.836836E-02
    netsum += feature3[2] * -0.2151709
    netsum += feature3[3] * 1.454877E-02
    netsum += feature3[4] * -1.123506E-02
    netsum += feature3[5] * -0.4303654
    netsum += feature3[6] * -3.775813E-02
    netsum += feature3[7] * 6.152073E-03
    netsum += feature3[8] * 0.1550028
    netsum += feature3[9] * 9.604919E-03
    netsum += feature3[10] * 4.512889E-03
    netsum += feature3[11] * 5.353843E-03
    netsum += feature3[12] * 1.527887E-02
    netsum += feature3[13] * 9.974806E-03
    netsum += feature3[14] * -3.942256E-02
    netsum += feature3[15] * 0.2352884
    netsum += feature3[16] * 6.373397E-04
    netsum += feature3[17] * -1.544278E-02
    netsum += feature3[18] * -2.435777E-02
    netsum += feature3[19] * 3.117795E-02
    netsum += feature3[20] * -4.896773E-02
    netsum += feature3[21] * -2.132092E-02
    netsum += feature3[22] * -1.336722E-03
    netsum += feature3[23] * 2.797908E-02
    netsum += feature3[24] * 1.171528E-02
    netsum += feature3[25] * 0.0290506
    netsum += feature3[26] * 2.336262E-02
    netsum += feature3[27] * -4.519067E-03
    netsum += feature3[28] * -1.321647E-02
    netsum += feature3[29] * 4.555365E-02
    netsum += feature3[30] * 8.150374E-03
    netsum += feature3[31] * -7.579619E-03
    netsum += feature3[32] * 1.365219E-02
    netsum += feature3[33] * -0.1744924
    outarray[3] = 1 / (1 + exp(-netsum))
     
     
    outarray[0] = 3647.505 *  (outarray[0] - .1) / .8 
    if (outarray[0]<0):
         outarray[0] = 0
    if (outarray[0]>3647.505):
         outarray[0] = 3647.505
     
    outarray[1] = 200972.4 *  (outarray[1] - .1) / .8 
    if (outarray[1]<0):
         outarray[1] = 0
    if (outarray[1]>200972.4):
         outarray[1] = 200972.4
     
    outarray[2] = 15783.18 *  (outarray[2] - .1) / .8 
    if (outarray[2]<0):
         outarray[2] = 0
    if (outarray[2]>15783.18):
         outarray[2] = 15783.18
     
    outarray[3] = 729.5124 *  (outarray[3] - .1) / .8 
    if (outarray[3]<0):
         outarray[3] = 0
    if (outarray[3]>729.5124):
         outarray[3] = 729.5124

    for i in range (4):
        outarray[i] = round(outarray[i],1)     

    RmsP1NarkPa = outarray[0]
    RmsP1VnrkPa = outarray[1]
    RmsP2NarkPa = outarray[2]
    RmsP2VnrkPa = outarray[3] 

    return (MeanP1NarkPa, RmsP1NarkPa, MeanP1VnrkPa, RmsP1VnrkPa, MeanP2NarkPa, RmsP2NarkPa, MeanP2VnrkPa, RmsP2VnrkPa)





