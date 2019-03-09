def krom_tension(Q_all,Y_all,Kg,Kv,Wg,Wv):
    '''
       Функция вычисления кромочных напряжений в рельсах
       Исходные данные:
       Q_all, кН - вертикальная сила (можно использовать как среднее так и СКО)
       Y_all, кН - боковая сила (-""-)
       Kg, cм^-1 - коэффициент отностительной жесткости рельсовой нити в гориз.плоскости
       Kv, cм^-1 - коэффициент отностительной жесткости рельсовой нити в вертик.плоскости
       Wg,см^3 - момент сопротивления рельса отностит вертикальной оси для подошвы рельса
       Wv,см^3 - момент сопротивления рельса отностит горизонтальной оси для подошвы рельса
       Выходные данные:
       krom_outer/inner, МПа - кромочные напряжения в наружней/внутренеей кромке
    '''

    krom_outer = round((10*(Q_all/(4*Kv*Wv))+10*(Y_all/(4*Kg*Wg))),1)
    krom_inner = round((10*(Q_all/(4*Kv*Wv))-10*(Y_all/(4*Kg*Wg))),1)
    return krom_outer, krom_inner

print ("Кромочные напряжения, МПа (наружняя/внутренняя) = \n",krom_tension(150,100,0.028,0.01509,75.2,435))


def F_shpal(Q_all,Y_all,Kg,Kv,l_shp):

    '''
       Функция вычисления сил, передающихся на шпалы от рельса
       Исходные данные:
       Q_all, кН - вертикальная сила (можно использовать как среднее так и СКО)
       Y_all, кН - боковая сила (-""-)
       Kg, cм^-1 - коэффициент отностительной жесткости рельсовой нити в гориз.плоскости
       Kv, cм^-1 - коэффициент отностительной жесткости рельсовой нити в вертик.плоскости
       l_shp,см - расстояние между осями шпал
       Выходные данные:
       F_shpal_vert/side, кН - сила действующая от рельса на шпалу в вертикальной/горизонтальной плоскости
    '''
    F_shpal_vert = round((Q_all*Kv*l_shp/2),1)
    F_shpal_side = round ((Y_all*Kg*l_shp/2),1)
    return (F_shpal_vert, F_shpal_side)

print ("Cила действующая от рельса на шпалу в вертикальной/горизонтальной плоскости, кН = \n",F_shpal(150,100,0.028,0.01509,50))

def F_ballast (Q_all, Kv, l_shp, f_shp):
    ''' Функция вычисления напряжений, передающихся от подошвы шпалы на балласт
       Исходные данные:
       Q_all, кН - вертикальная сила (можно использовать как среднее так и СКО)
       Kv, cм^-1 - коэффициент отностительной жесткости рельсовой нити в вертик.плоскости
       l_shp,см - расстояние между осями шпал
       f_shp,см^2 - площадь опирания полушпалы
       Выходные данные:
       F_ballast, кПа  - напряжения, передающихся от подошвы шпалы на балласт
    '''
    F_ballast = round((10000*(Q_all*Kv*l_shp/2)/f_shp),1)
    return (F_ballast)
print ("Напряжения, передающиеся от подошвы шпалы на балласт, кПа = \n",F_ballast(150,0.01509,50,3092))

def F_ploch (Q_all, h_ballast, ballast_type):
    
    '''
       Функция вычисления напряжений, передающихся на основную площадку земляного полотна
       Исходные данные:
       Q_all, кН - вертикальная сила (можно использовать как среднее так и СКО)
       h_ballast, мм - толщина балластного слоя
       ballast_type - признак рода балластного материала (1- щебень, 2 - песчано-гравийный, 3- песок, асбест
       F_ploch, КПа  - напряжения, передающиеся на основную площадку земляного полотна

    '''

    import math
     
    if (Q_all<0):
        Q_all = 0
    if (Q_all>200):
        Q_all = 200
    Q_all = Q_all / 200
     
    if (h_ballast<0):
        h_ballast = 0
    if (h_ballast>1000):
        h_ballast = 1000
    h_ballast = h_ballast / 1000
     
    netsum = 0.9052925
    netsum = netsum + Q_all * -3.153388
    netsum = netsum + h_ballast * 0.4850939
    feature21 = 1 / (1 + math.exp(-netsum))
     
    netsum = 2.962096
    netsum = netsum + Q_all * -4.985137
    netsum = netsum + h_ballast * 6.291834
    feature22 = 1 / (1 + math.exp(-netsum))
     
    netsum = -5.346238
    netsum = netsum + Q_all * 4.052691
    netsum = netsum + h_ballast * 1.583401
    feature23 = 1 / (1 + math.exp(-netsum))
     
    netsum = 3.149668
    netsum = netsum + Q_all * -3.608208
    netsum = netsum + h_ballast * 5.797504
    feature24 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.9063327
    netsum = netsum + Q_all * 3.767979
    netsum = netsum + h_ballast * 0.7040534
    feature25 = 1 / (1 + math.exp(-netsum))
     
    netsum = -3.016221
    netsum = netsum + feature21 * -3.12984
    netsum = netsum + feature22 * -2.488589
    netsum = netsum + feature23 * 3.911146
    netsum = netsum + feature24 * 5.361169
    netsum = netsum + feature25 * 0.9646798
    outarray1 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.3693021
    netsum = netsum + feature21 * -1.526163
    netsum = netsum + feature22 * -1.860191
    netsum = netsum + feature23 * -4.302728E-02
    netsum = netsum + feature24 * 0.6121774
    netsum = netsum + feature25 * 1.686295
    outarray2 = 1 / (1 + math.exp(-netsum))
     
     
    outarray1 = 200 *  (outarray1 - .1) / .8 
    if (outarray1<0):
        outarray1 = 0
    if (outarray1>200):
        outarray1 = 200
     
    outarray2 = 150 *  (outarray2 - .1) / .8 
    if (outarray2<0):
        outarray2 = 0
    if (outarray2>150):
        outarray2 = 150

    k_ploch = 1

    if ballast_type ==2:
        k_ploch = 1.15
    if ballast_type ==3:
        k_ploch = 1.25    

    F_ploch = round ((k_ploch*outarray2),1)

    return (F_ploch)

print ("Напряжения, передающиеся на основную площадку земляного полотна, кПа = \n",F_ploch(150,400,1))



