import math

def second_moment_power(mean,sigma,Xi):
    #второй момент случайной величины
    return((mean**2+sigma**2)**(0.5*Xi))
     

def damage_rails(mean_krom_outer,mean_krom_inner,sigma_krom_outer,sigma_krom_inner,Xi_sigma_plus,Xi_sigma_minus):
    #нагруженность рельсов
    damage_plus = (((mean_krom_outer+mean_krom_inner)*0.5)**2+((sigma_krom_inner^2+sigma_krom_outer^2)*0.25))**(0.5*Xi_sigma_plus)
    damage_minus = (((mean_krom_outer-mean_krom_inner)*0.5)**2+((sigma_krom_inner^2-sigma_krom_outer^2)*0.25))**(0.5*Xi_sigma_minus)
    return(damage_minus+damage_plus)

def damage_skrep(mean_F_shpal_vert, mean_F_shpal_side, sigma_F_shpal_vert, sigma_F_shpal_side, Xi_vert_skrep, Xi_side_skrep):
    #нагуженность скреп
    damage_vert = second_moment(mean_F_shpal_vert,sigma_F_shpal_vert,Xi_vert_skrep)
    damage_side = second_moment(mean_F_shpal_side,sigma_F_shpal_side,Xi_side_skrep)
    return(damage_side+damage_vert)

def damage_shpal(mean_F_shpal_vert,sigma_F_shpal_vert,Xi_shpal):
    #нагруженность шпал
    damage_spal = second_moment(mean_F_shpal_vert, sigma_F_shpal_vert,Xi_shpal)
    return(damage_spal)

def damage_kol_width(mean_F_shpal_vert, mean_F_shpal_side, sigma_F_shpal_vert, sigma_F_shpal_side, Xi_vert_kol, Xi_side_kol):
    #накопление неисправностей ширины колеи
    damage_vert = second_moment(mean_F_shpal_vert,sigma_F_shpal_vert,Xi_vert_kol)
    damage_side = second_moment(mean_F_shpal_side,sigma_F_shpal_side,Xi_side_kol)
    return(damage_side+damage_vert)

def damage_per_pros_urov(mean_F_ballast,sigma_F_ballast,Xi_ballast):
    #накопление перекоса, просадок, уровня
    damage_ballast = second_moment(mean_F_ballast,sigma_F_ballast,Xi_ballast)
    return(damage_ballast)

def damage_richtov(mean_F_shpal_vert, mean_F_shpal_side, sigma_F_shpal_vert, sigma_F_shpal_side, Xi_vert_richtov, Xi_side_richtov):
    #накопление неисправностей по рихтовке
    damage_richtov_1 = second_moment(mean_F_shpal_side,sigma_F_shpal_side,Xi_side_richtov)
    damage_richtov_2 = second_moment(mean_F_shpal_vert,sigma_F_shpal_vert,-Xi_vert_richtov)
    return(damage_richtov_1*damage_richtov_2)

def damage_ploch_zem_polot(mean_F_ploch,sigma_F_ploch, most_likely_F_ploch, dopusk_F_ploch):
    #накопление неисправностей основной площадки земляного полотна
    damage_ploch = second_moment(mean_F_ploch,sigma_F_ploch,2*(exp(most_likely_F_ploch*(dopusk_F_ploch)**(-1))))
    return(damage_ploch)

def damage_ballast_pollution(mean_F_ploch, mean_F_ballast, sigma_F_ploch, sigma_F_ballast, most_likely_F_ploch, dopusk_F_ploch,most_likely_F_ballast, dopusk_F_ballast):
    #накопление загрязненности балласта
    damage_pollution_ploch = second_moment(mean_F_ploch,sigma_F_ploch,2*(exp(most_likely_F_ploch*(dopusk_F_ploch)**(-1))))
    damage_pollution_ballast = second_moment(mean_F_ballast,sigma_F_ballast,2*(exp(most_likely_F_ballast*(dopusk_F_balast)**(-1))))
    return(damage_pollution_ballast+damage_pollution_ploch)
    



    
