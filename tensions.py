def krom_tension(Q_mean,Q_rms,Y_mean,Y_rms,Kg,Kv,Wg,Wv):
    '''
       Функция вычисления кромочных напряжений в рельсах
       Исходные данные:
       Q_mean/rms, кН - вертикальная сила (среднее/СКО)
       Y_mean/rms, кН - боковая сила (среднее/СКО)
       Kg, cм^-1 - коэффициент отностительной жесткости рельсовой нити в гориз.плоскости
       Kv, cм^-1 - коэффициент отностительной жесткости рельсовой нити в вертик.плоскости
       Wg,см^3 - момент сопротивления рельса отностит вертикальной оси для подошвы рельса
       Wv,см^3 - момент сопротивления рельса отностит горизонтальной оси для подошвы рельса
       Выходные данные:
       (mean/sigma)krom_(outer/inner), МПа -среднее значение, СКО кромочных напряжения в наружней/внутренеей кромке
    '''

    mean_krom_outer = round((10*(Q_mean/(4*Kv*Wv))+10*(Y_mean/(4*Kg*Wg))),1)
    mean_krom_inner = round((10*(Q_mean/(4*Kv*Wv))-10*(Y_mean/(4*Kg*Wg))),1)
    sigma_krom_outer = round((((10*(Q_rms/(4*Kv*Wv)))**2+(10*(Y_rms/(4*Kg*Wg)))**2)**0.5),1)
    sigma_krom_inner = round((((10*(Q_rms/(4*Kv*Wv)))**2+(10*(Y_rms/(4*Kg*Wg)))**2)**0.5),1)
    return mean_krom_outer,sigma_krom_outer, mean_krom_inner, sigma_krom_inner

print ("Кромочные напряжения, МПа (среднее/СКО) для наружн и внутр кромок = \n",krom_tension(150,11,100,5.3,0.028,0.01509,75.2,435))


def F_shpal(Q_mean,Q_rms,Y_mean,Y_rms,Kg,Kv,l_shp):

    '''
       Функция вычисления сил, передающихся на шпалы от рельса
       Исходные данные:
       Q_mean/rms, кН - вертикальная сила (среднее/СКО)
       Y_mean/rms, кН - боковая сила (среднее/СКО)
       Kg, cм^-1 - коэффициент отностительной жесткости рельсовой нити в гориз.плоскости
       Kv, cм^-1 - коэффициент отностительной жесткости рельсовой нити в вертик.плоскости
       l_shp,см - расстояние между осями шпал
       Выходные данные:
       (mean/sigma) F_shpal_vert/side, кН - среднее значение/СКО сил действующая от рельса на шпалу в вертикальной/горизонтальной плоскости
    '''
    mean_F_shpal_vert = round((Q_mean*Kv*l_shp/2),1)
    mean_F_shpal_side = round ((Y_mean*Kg*l_shp/2),1)
    sigma_F_shpal_vert = round((Q_rms*Kv*l_shp/2),1)
    sigma_F_shpal_side = round ((Y_rms*Kg*l_shp/2),1)
    return (mean_F_shpal_vert,sigma_F_shpal_vert, mean_F_shpal_side, sigma_F_shpal_side)

print ("Среднее/СКО значений сил действующаих от рельса на шпалу в вертикальной/горизонтальной плоскости, кН = \n",F_shpal(150,11,100,5.3,0.028,0.01509,50))

def F_ballast (Q_mean,Q_rms, Kv, l_shp, f_shp):
    ''' Функция вычисления напряжений, передающихся от подошвы шпалы на балласт
       Исходные данные:
       Q_mean/rms, кН - вертикальная сила (среднее/СКО)
       Kv, cм^-1 - коэффициент отностительной жесткости рельсовой нити в вертик.плоскости
       l_shp,см - расстояние между осями шпал
       f_shp,см^2 - площадь опирания полушпалы
       Выходные данные:
       mean/sigma/most_F_ballast, кПа  - среднее/ско/макс.вер напряжения, передающихся от подошвы шпалы на балласт
    '''
    mean_F_ballast = round((10000*(Q_mean*Kv*l_shp/2)/f_shp),1)
    sigma_F_ballast = round((10000*(Q_rms*Kv*l_shp/2)/f_shp),1)
    most_likely_F_ballast = round((mean_F_ballast+2.5*sigma_F_ballast),1)
    return (mean_F_ballast,sigma_F_ballast, most_likely_F_ballast)
print ("Среднее/СКО/Макс.вероятное значения Напряжений, передающиеся от подошвы шпалы на балласт, кПа = \n",F_ballast(150,11,0.01509,50,3092))

def F_ploch (Q_mean,Q_rms, h_ballast, ballast_type):
    
    '''
       Функция вычисления напряжений, передающихся на основную площадку земляного полотна
       Исходные данные:
       Q_mean/rms, кН - вертикальная сила (среднее/СКО)
       h_ballast, мм - толщина балластного слоя
       ballast_type - признак рода балластного материала (1- щебень, 2 - песчано-гравийный, 3- песок, асбест
       mean/sigma/most_F_ploch, кПа  - среднее/ско/макс.вер напряжения, передающиеся на основную площадку земляного полотна

    '''

    import math
     
    if (Q_mean<0):
        Q_mean = 0
    if (Q_mean>200):
        Q_mean = 200
    Q_mean = Q_mean / 200
     
    if (h_ballast<0):
        h_ballast = 0
    if (h_ballast>1000):
        h_ballast = 1000
    h_ballast = h_ballast / 1000
     
    netsum = 0.9052925
    netsum = netsum + Q_mean * -3.153388
    netsum = netsum + h_ballast * 0.4850939
    feature21 = 1 / (1 + math.exp(-netsum))
     
    netsum = 2.962096
    netsum = netsum + Q_mean * -4.985137
    netsum = netsum + h_ballast * 6.291834
    feature22 = 1 / (1 + math.exp(-netsum))
     
    netsum = -5.346238
    netsum = netsum + Q_mean * 4.052691
    netsum = netsum + h_ballast * 1.583401
    feature23 = 1 / (1 + math.exp(-netsum))
     
    netsum = 3.149668
    netsum = netsum + Q_mean * -3.608208
    netsum = netsum + h_ballast * 5.797504
    feature24 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.9063327
    netsum = netsum + Q_mean * 3.767979
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

    mean_F_ploch = round ((k_ploch*outarray2),1)

    if (Q_rms<0):
        Q_rms = 0
    if (Q_rms>200):
        Q_rms = 200
    Q_rms = Q_rms / 200
     
    if (h_ballast<0):
        h_ballast = 0
    if (h_ballast>1000):
        h_ballast = 1000
    h_ballast = h_ballast / 1000
     
    netsum = 0.9052925
    netsum = netsum + Q_rms * -3.153388
    netsum = netsum + h_ballast * 0.4850939
    feature21 = 1 / (1 + math.exp(-netsum))
     
    netsum = 2.962096
    netsum = netsum + Q_rms * -4.985137
    netsum = netsum + h_ballast * 6.291834
    feature22 = 1 / (1 + math.exp(-netsum))
     
    netsum = -5.346238
    netsum = netsum + Q_rms * 4.052691
    netsum = netsum + h_ballast * 1.583401
    feature23 = 1 / (1 + math.exp(-netsum))
     
    netsum = 3.149668
    netsum = netsum + Q_rms * -3.608208
    netsum = netsum + h_ballast * 5.797504
    feature24 = 1 / (1 + math.exp(-netsum))
     
    netsum = -0.9063327
    netsum = netsum + Q_rms * 3.767979
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

    rms_F_ploch = round ((k_ploch*outarray2),1)
    
    most_likely_F_ploch = round ((mean_F_ploch+2.5*rms_F_ploch),1)
    
    return (mean_F_ploch,rms_F_ploch,most_likely_F_ploch)

print ("Среднее/СКО/Макс.вероятное значения напряжений, передающиеся на основную площадку земляного полотна, кПа = \n",F_ploch(150,15,400,1))


