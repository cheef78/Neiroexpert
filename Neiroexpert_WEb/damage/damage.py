class ForceNeiroCalc():
    def  __init__(self,projekt_path, projekt_pk):
        self.projekt_path = projekt_path 
        self.projekt_pk = projekt_pk 
        
    def damage (self):    
        try:
            print ("Ипорт библиотек")
            import pathlib
            import os
            # from array import array
            # import time
            import numpy as np
            import pandas as pd
            import matplotlib
            import zipfile
            import matplotlib.pyplot as plt
            # from numpy import random, arange
            # import datetime
            # import random
            import sys
            import warnings
            warnings.simplefilter('ignore')
            import matplotlib.backends.backend_pdf
            plt.rcParams['figure.figsize'] = [15, 10]

            from django.conf import settings
            from projektapp.models import Projekt
            from mainapp import views as mainapp 
            from projektapp.models import projekt_directory_path
            from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
            from django.shortcuts import render
            
            projekt_item = get_object_or_404(Projekt, pk=self.projekt_pk)
            
            files_path = self.projekt_path + str('/') + str(self.projekt_pk)
            if not os.path.exists(files_path):
                os.mkdir(files_path)
            files_path = files_path + str('/neiro_damage')
            pic_path = files_path + str('//') + "graf" +  str('//')
            init_file =  self.projekt_path + str('//') + str(projekt_item.document)
            print(files_path, pic_path, init_file, projekt_item , 'до проверки папок в нейродамадж')
        
            if not os.path.exists(files_path):
                os.mkdir(files_path)
            else:
                path = pathlib.Path(files_path)
                for p in path.glob('*.*'):
                    os.remove(p)
            
            if not os.path.exists(pic_path):
                os.mkdir(pic_path)
            else:
                path = pathlib.Path(pic_path)
                for p in path.glob('*.*'):
                    os.remove(p)
            
            



            print(files_path, pic_path, init_file, projekt_item , 'после проверки папок в нейродамадж')
            
            #gruzim biblioteki
            # obshie
            

            # lichnie
            # from forces import vagon_1
            # from forces import vagon_2
            # from forces import vagon_3
            # from forces import vagon_4
            # from tensions import krom_tension
            # from tensions import f_shpal
            # from tensions import f_ballast_opzp
            from damage.forces import vagon_1
            from damage.forces import vagon_2
            from damage.forces import vagon_3
            from damage.forces import vagon_4
            from damage.tensions import f_ballast_opzp
            from damage.tensions import f_shpal
            from damage.tensions import krom_tension
            
            print ("начало расчетов. Загрузка исходных данных")
            # schitivanie isxodnix dannix
        
            line = pd.read_excel(open(init_file, 'rb'), sheet_name='line')

            print ("начало расчетов. Загружены данные по линии")

            trains = pd.read_excel(init_file, sheet_name='trains')
            pod_sos = pd.read_excel(init_file, sheet_name='pod_sos')
            vsp_konstr = pd.read_excel(init_file, sheet_name='vsp_constr')
            damage_koef = pd.read_excel(init_file, sheet_name='damage_koeff')
            criteria = pd.read_excel(init_file, sheet_name='criteria')
            
            line.to_csv(files_path + '/line.csv', sep=";") 
            trains.to_csv(files_path + '/trains.csv', sep=";")
            pod_sos.to_csv(files_path + '/pod_sos.csv', sep=";")
            vsp_konstr.to_csv(files_path + '/vsp_konstr.csv', sep=";")
            damage_koef.to_csv(files_path + '/damage.csv', sep=";")
            criteria.to_csv(files_path + '/criteria.csv', sep=";")
            
            print ("расчеты. Расчеты сил")
            # бЛОК вычисления сил для каждого элемента плана с полным учетом вагонопотока на линии
            force_line = np.zeros((len(line.index),22))
            for index_line in range(len(line.index)):
                #print (index)
                input_val = np.array([0, 0, 0,0,0,0,0,0.00])
                input_val[0]= line['vsp_type'].loc[line['vsp_type'].index == index_line].values
                input_val[1]= line['vsp_cnd'].loc[line['vsp_cnd'].index == index_line].values
                input_val[2]= line['rad_m'].loc[line['rad_m'].index == index_line].values
                input_val[3]= line['h_mm'].loc[line['h_mm'].index == index_line].values
                input_val[6]= line['Shkol_mm'].loc[line['Shkol_mm'].index == index_line].values
                input_val[7]= 0.25 
                force_index = [0.0]*22
                for index_vagon in range(len(pod_sos.index)):
                    gamma = pod_sos['gamma'].loc[pod_sos['gamma'].index == index_vagon].values
                    p_os = pod_sos['p_os'].loc[pod_sos['p_os'].index == index_vagon].values
                    vag_type = pod_sos['vag_type'].loc[pod_sos['vag_type'].index == index_vagon].values  
                    meankver_force = pod_sos['meankver_force'].loc[pod_sos['meankver_force'].index == index_vagon].values  
                    meankgor_force = pod_sos['meankgor_force'].loc[pod_sos['meankgor_force'].index == index_vagon].values  
                    meankprd_force = pod_sos['meankprd_force'].loc[pod_sos['meankprd_force'].index == index_vagon].values  
                    meankram_force = pod_sos['meankram_force'].loc[pod_sos['meankram_force'].index == index_vagon].values  
                    rmskver_force = pod_sos['rmskver_force'].loc[pod_sos['rmskver_force'].index == index_vagon].values  
                    rmskgor_force = pod_sos['rmskgor_force'].loc[pod_sos['rmskgor_force'].index == index_vagon].values  
                    rmskprd_force = pod_sos['rmskprd_force'].loc[pod_sos['rmskprd_force'].index == index_vagon].values  
                    rmskram_force = pod_sos['rmskram_force'].loc[pod_sos['rmskram_force'].index == index_vagon].values  
                    force_v = [0.0]*22
                    
                    for v in (10,30,50,70,90,110,130):
                        gamma_v_name = 'gamma_' + str(10+v)
                        gamma_v = pod_sos[gamma_v_name].loc[pod_sos[gamma_v_name].index == index_vagon].values 
                        input_val[4] = v
                        input_val[5] = p_os
                        #print (input_val)
                        #print (vag_type, gamma_v)
                        if vag_type == 1:
                            force = vagon_1 (input_val, 'return')*gamma_v
                            for i in [0,1,2,14,16]:
                                force[i] = force[i]*meankver_force
                            for i in [3,4,5,15,17]:
                                force[i] = force[i]*rmskver_force
                            for i in [6,7,8,18,20]:
                                force[i] = force[i]*meankgor_force
                            for i in [9,10,11,19,21]:
                                force[i] = force[i]*rmskgor_force
                            force[12] = force[12]*meankram_force
                            force[13] = force[13]*rmskram_force
                            #print (force)
                        elif vag_type == 2:
                            force = vagon_2 (input_val, 'return')*gamma_v
                            #print (force)
                            for i in [0,1,2,14,16]:
                                force[i] = force[i]*meankver_force
                            for i in [3,4,5,15,17]:
                                force[i] = force[i]*rmskver_force
                            for i in [6,7,8,18,20]:
                                force[i] = force[i]*meankgor_force
                            for i in [9,10,11,19,21]:
                                force[i] = force[i]*rmskgor_force
                            force[12] = force[12]*meankram_force
                            force[13] = force[13]*rmskram_force
                            
                        elif vag_type == 3:
                            force = vagon_3 (input_val, 'return')*gamma_v
                            #print (force)
                            for i in [0,1,2,14,16]:
                                force[i] = force[i]*meankver_force
                            for i in [3,4,5,15,17]:
                                force[i] = force[i]*rmskver_force
                            for i in [6,7,8,18,20]:
                                force[i] = force[i]*meankgor_force
                            for i in [9,10,11,19,21]:
                                force[i] = force[i]*rmskgor_force
                            force[12] = force[12]*meankram_force
                            force[13] = force[13]*rmskram_force
                        elif vag_type == 4:
                            force = vagon_4 (input_val, 'return')*gamma_v
                            #print (force)
                            for i in [0,1,2,14,16]:
                                force[i] = force[i]*meankver_force
                            for i in [3,4,5,15,17]:
                                force[i] = force[i]*rmskver_force
                            for i in [6,7,8,18,20]:
                                force[i] = force[i]*meankgor_force
                            for i in [9,10,11,19,21]:
                                force[i] = force[i]*rmskgor_force
                            force[12] = force[12]*meankram_force
                            force[13] = force[13]*rmskram_force
                        #else:
                            #print ("Номер типа подвижного состава указан неверно или отстуствует в базе")
                        force_v = force_v + force
                    force_index = force_index +  force_v*gamma 
                for i in range(0,22):
                    force_line[index_line, i] = force_index[i]

            # бЛОК вычисления сил для каждого элемента плана с полным учетом поездопотока и уклона на линии
            force_poezd = np.zeros((len(line.index),22))
            aprox_masxi = [-1.8656*(10**-18), 2.4627*(10**-12), 2.0676*(10**-7),1.0262] # коэфф к апроксимации зависимости сил от массы и уклона
            for index_line in range(len(line.index)):
                grad = line['i_prm'].loc[line['i_prm'].index == index_line].values 
                
                force_t = [0.0]*22
                
                for index_poezd in range(len(trains.index)):
                    massa_poezd = trains['mpoezda_mean'].loc[trains['mpoezda_mean'].index == index_poezd].values
                    gamma_poezd = trains['poezd_gamma'].loc[trains['poezd_gamma'].index == index_poezd].values
                    k_massxi = (((grad*massa_poezd)**3)*aprox_masxi[0] + ((grad*massa_poezd)**2)*aprox_masxi[1]\
                                + (grad*massa_poezd)*aprox_masxi[2] + aprox_masxi[3])       
                    meankver_force = trains['meankver_force'].loc[trains['meankver_force'].index == index_poezd].values  
                    meankgor_force = trains['meankgor_force'].loc[trains['meankgor_force'].index == index_poezd].values  
                    meankprd_force = trains['meankprd_force'].loc[trains['meankprd_force'].index == index_poezd].values  
                    meankram_force = trains['meankram_force'].loc[trains['meankram_force'].index == index_poezd].values  
                    rmskver_force = trains['rmskver_force'].loc[trains['rmskver_force'].index == index_poezd].values  
                    rmskgor_force = trains['rmskgor_force'].loc[trains['rmskgor_force'].index == index_poezd].values  
                    rmskprd_force = trains['rmskprd_force'].loc[trains['rmskprd_force'].index == index_poezd].values  
                    rmskram_force = trains['rmskram_force'].loc[trains['rmskram_force'].index == index_poezd].values
                    for i in [0,1,2,14,16]:
                        force[i] = force_line[index_line][i]*meankver_force*gamma_poezd*k_massxi
                    for i in [3,4,5,15,17]:
                        force[i] = force_line[index_line][i]*rmskver_force*gamma_poezd*k_massxi
                    for i in [6,7,8,18,20]:
                        force[i] = force_line[index_line][i]*meankgor_force*gamma_poezd*k_massxi
                    for i in [9,10,11,19,21]:
                        force[i] = force_line[index_line][i]*rmskgor_force*gamma_poezd*k_massxi 
                    force[12] = force_line[index_line][12]*meankram_force*gamma_poezd*k_massxi
                    force[13] = force_line[index_line][13]*rmskram_force*gamma_poezd*k_massxi 
                    
                    
                    #print(force)
                    force_t = force_t + force 
                #print (force_t)
                for i in range(0,22):
                    force_poezd[index_line, i] = force_t[i]

            # Формирование итогового массива с силами для каждого элемента
            forces_itogo = pd.DataFrame(force_poezd)
            forces_itogo.columns = ['Mean_F_vertR_kN', 'Mean_F_vertL_kN', 'Mean_F_vert_kN', 'sigma_F_vertR_kN', 'sigma_F_vertL_kN',\
                                    'sigma_F_vert_kN','Mean_F_sideR_kN', 'Mean_F_sideL_kN', 'Mean_F_side_kN', 'sigma_F_sideR_kN',\
                                    'sigma_F_sideL_kN', 'sigma_F_side_kN', 'Mean_Hp_kN', 'sigma_Hp_kN',\
                                    'MeanP1NarkPa', 'RmsP1NarkPa', 'MeanP1VnrkPa', 'RmsP1VnrkPa',\
                                    'MeanP2NarkPa', 'RmsP2NarkPa', 'MeanP2VnrkPa', 'RmsP2VnrkPa']

            # Формирование файла с силами для каждого элемента
            force_line = line.join(forces_itogo)
            force_line.to_csv(files_path + '/force_line.csv', sep=";")
            
            # Формирование графического отображения данных силового расчета в точке взаимодействия
            
            pdf = matplotlib.backends.backend_pdf.PdfPages(files_path + '/neiro_damage_graf_result.pdf')
            
            # print(len(force_line.index))
            values = ['Mean_F_vertR_kN', 'Mean_F_vertL_kN', 'Mean_F_vert_kN', 'sigma_F_vertR_kN', 'sigma_F_vertL_kN',\
                                    'sigma_F_vert_kN','Mean_F_sideR_kN', 'Mean_F_sideL_kN', 'Mean_F_side_kN', 'sigma_F_sideR_kN',\
                                    'sigma_F_sideL_kN', 'sigma_F_side_kN', 'Mean_Hp_kN', 'sigma_Hp_kN',\
                                    'MeanP1NarkPa', 'RmsP1NarkPa', 'MeanP1VnrkPa', 'RmsP1VnrkPa',\
                                    'MeanP2NarkPa', 'RmsP2NarkPa', 'MeanP2VnrkPa', 'RmsP2VnrkPa']
            for value in values:
                fig = plt.figure()
                plt.bar(force_line.index, force_line[value])
                plt.title('Распределение значений параметра_' + value + "_по длине линии")
                plt.ylabel('Значение параметра_' + value)
                plt.xlabel('Номер участка в ведомости')
                plt.xticks(rotation='vertical')
                plt.xticks(np.arange(0, len(force_line.index), 1))
                fig.savefig(pic_path + value + ".png")
                pdf.savefig(fig)  
                
                # plt.show()
            # pdf.close()
            



            print (' начало расчета напряжений' )
            # бЛОК вычисления напряжений в рельсах для каждого элемента линии с полным учетом поездопотока и уклона на линии
            #вычисления ведутся для осредненных значений
            rail_streses = np.zeros((len(line.index),7))
            tie_forces = np.zeros((len(line.index),10))
            balast_opzp_streses = np.zeros((len(line.index),7))

            for index_line in range(len(line.index)):
                input_val = np.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
                # rail = line['rail'].loc[line['rail'].index == index_line].values 
                # tie = line['tie'].loc[line['tie'].index == index_line].values
                # fasten = line['fasten'].loc[line['fasten'].index == index_line].values
                # input_val[10] = line['hball_sm'].loc[line['hball_sm'].index == index_line].values
                # rad_m = line['rad_m'].loc[line['rad_m'].index == index_line].values
                # print ('выборки из таблицы ВСП - начало' )
                vsp_index = line['vsp_const_numb'].loc[line['vsp_const_numb'].index == index_line].values[0]
                # print (vsp_index, 'выборки из таблицы - номер конструкции ВСП' )
                epur = vsp_konstr['epur'].loc[vsp_konstr['epur'].index == vsp_index+1].values[0]
                # print (epur, 'выборки из таблицы - epur' )
                input_val[10] = vsp_konstr['hball_sm'].loc[vsp_konstr['hball_sm'].index == vsp_index+1].values[0]
                # print (input_val[10], 'выборки из таблицы - hball_sm' )
                input_val[11] = vsp_konstr['ballast_type'].loc[vsp_konstr['ballast_type'].index == vsp_index+1].values[0]
                # print (input_val[11], 'выборки из таблицы - ballast_type' )
                # if rad_m > 1200:
                #     epur = 1840
                # else:
                #     epur = 2000
                # ballast = 'sheb'
                # proklad = 'tipov'
                input_val[6] = 100000/epur
                
                
                # vsp_index = vsp_konstr.index[(vsp_konstr['rail'] == rail[0]) & (vsp_konstr['epur'] == epur)\
                #                             & (vsp_konstr['tie'] == tie[0]) & (vsp_konstr['fasten'] == fasten[0])].tolist()
                # if len(vsp_index) == 0:
                #     vsp_index = vsp_konstr.index[(vsp_konstr['rail'] == rail[0]) & (vsp_konstr['epur'] == epur)\
                #                             & (vsp_konstr['tie'] == tie[0]) & (vsp_konstr['fasten'] == 'all')].tolist()
                # if len(vsp_index) == 0:
                #     vsp_index = vsp_konstr.index[(vsp_konstr['rail'] == rail[0]) & (vsp_konstr['epur'] == epur)\
                #                             & (vsp_konstr['tie'] == tie[0])].tolist()
                # if len(vsp_index) == 0:
                #     print ('В базе отсуствует соответствующая конструкция пути')
                #     print ('Для расчета будет принята типовая конструкция пути - Р65, жб шпалы, щеб, 1840 шт/км, ЖБР-Ш')
                #     vsp_index = [4]
                # if len(vsp_index) > 1:
                #     vsp_index = [vsp_index[0]] 
                # if isinstance(vsp_index, list):
                #     vsp_index = vsp_index[0]
              

                input_val[4] = vsp_konstr['kg_sm'].loc[vsp_konstr['kg_sm'].index == vsp_index].values 
                input_val[5] = vsp_konstr['kv_sm'].loc[vsp_konstr['kv_sm'].index == vsp_index].values 
                input_val[7] = vsp_konstr['wg_cm3'].loc[vsp_konstr['wg_cm3'].index == vsp_index].values 
                input_val[8] = vsp_konstr['wv_cm3'].loc[vsp_konstr['wv_cm3'].index == vsp_index].values  
                
                input_val[9] = vsp_konstr['omega_sm2'].loc[vsp_konstr['omega_sm2'].index == vsp_index].values 
                force_names = ['Mean_F_vert_kN', 'sigma_F_vert_kN', 'Mean_F_side_kN','sigma_F_side_kN']
                i = 0
                for force_name in force_names:
                    input_val[i] = force_line[force_name].loc[force_line[force_name].index == index_line].values
                    input_val[12] = force_line['Mean_Hp_kN'].loc[force_line['Mean_Hp_kN'].index == index_line].values
                    input_val[13] = force_line['sigma_Hp_kN'].loc[force_line['sigma_Hp_kN'].index == index_line].values
                    i = i+1
                
                
                input_val[14] = damage_koef['degre_1'].loc[damage_koef['name'] == 'rail_dr'].values
                input_val[15] = damage_koef['degre_2'].loc[damage_koef['name'] == 'rail_dr'].values
                tensions = krom_tension(input_val)
                for i in range(0,7):
                    rail_streses[index_line, i] = tensions[i]
                
                input_val[14] = damage_koef['degre_1'].loc[damage_koef['name'] == 'fasten'].values
                input_val[15] = damage_koef['degre_2'].loc[damage_koef['name'] == 'fasten'].values
                input_val[16] = damage_koef['degre_1'].loc[damage_koef['name'] == 'tie'].values
                input_val[17] = damage_koef['degre_2'].loc[damage_koef['name'] == 'tie'].values
                input_val[18] = damage_koef['degre_1'].loc[damage_koef['name'] == 'shkol_dop'].values
                input_val[19] = damage_koef['degre_2'].loc[damage_koef['name'] == 'shkol_dop'].values
                input_val[20] = damage_koef['degre_1'].loc[damage_koef['name'] == 'plan_dop'].values
                input_val[21] = damage_koef['degre_2'].loc[damage_koef['name'] == 'plan_dop'].values
                tie_force =  f_shpal(input_val) 
                for i in range(0,10):
                    tie_forces[index_line, i] = tie_force[i]
                
                
                input_val[14] = damage_koef['degre_1'].loc[damage_koef['name'] == 'prof_dop'].values
                input_val[15] = damage_koef['degre_2'].loc[damage_koef['name'] == 'prof_dop'].values
                input_val[16] = damage_koef['degre_1'].loc[damage_koef['name'] == 'ballast'].values
                input_val[17] = damage_koef['degre_2'].loc[damage_koef['name'] == 'ballast'].values
                input_val[18] = damage_koef['degre_1'].loc[damage_koef['name'] == 'opzp'].values
                input_val[19] = damage_koef['degre_2'].loc[damage_koef['name'] == 'opzp'].values
                balast_opzp_stress = f_ballast_opzp(input_val) 
                for i in range(0,7):
                    balast_opzp_streses[index_line, i] = balast_opzp_stress[i] 
                
            
            rail_streses_itogo = pd.DataFrame(rail_streses)
            rail_streses_itogo.columns = ['Mean_nar_krom_MPa', 'RMS_nar_krom_MPa', 'Mean_vntr_krom_MPa', 'RMS_vntr_krom_MPa',\
                                        'Mean_osev_MPa', 'RMS_osev_MPa','d_rail_MPa^Xrail']

            rail_streses = line.join(rail_streses_itogo)
            rail_streses.to_csv(files_path + '/rail_streses_line.csv', sep = ";") 

            # files_path1 = project_path + str('\\') + str(project_number) + str('\\') + 'rail_streses'
            # pdf = matplotlib.backends.backend_pdf.PdfPages(files_path1 + "\statistica_rail_streses_.pdf")
            # # print(len(force_line.index))
            values = ['Mean_nar_krom_MPa', 'RMS_nar_krom_MPa', 'Mean_vntr_krom_MPa', 'RMS_vntr_krom_MPa','Mean_osev_MPa', 'RMS_osev_MPa']
            for value in values:
                fig = plt.figure()
                plt.bar(rail_streses.index, rail_streses[value])
                plt.title('Распределение значений параметра_' + value + "_по длине линии")
                plt.ylabel('Значение параметра_' + value)
                plt.xlabel('Номер участка в ведоомости')
                plt.xticks(rotation='vertical')
                plt.xticks(np.arange(0, len(rail_streses.index), 1))
                fig.savefig(pic_path + value + ".png")
                pdf.savefig(fig)  
                
                # plt.show()
            # pdf.close()
            
            tie_forces_itogo = pd.DataFrame(tie_forces)
            tie_forces_itogo.columns = ['mean_F_shpal_vert_kN','sigma_F_shpal_vert_kN',\
                                        'mean_F_shpal_side_kN', 'sigma_F_shpal_side_kN',\
                                    'mean_Hp_kN', 'sigma_Hp_kN',\
                                        'd_fast_kN^Xfast', 'd_tie_kN^Xtie', 'd_shkol_kN^Xshkol', 'd_plan_kN^Xplan']

            tie_forces = line.join(tie_forces_itogo)
            tie_forces.to_csv(files_path + '/tie_forces_line.csv', sep= ";")

            # Формирование графического отображения данных силового расчета в точке взаимодействия
            # print(len(force_line.index))
            values = ['mean_F_shpal_vert_kN','sigma_F_shpal_vert_kN','mean_F_shpal_side_kN','sigma_F_shpal_side_kN']
            for value in values:
                fig = plt.figure()
                plt.bar(tie_forces.index, tie_forces[value])
                plt.title('Распределение значений параметра_' + value + "_по длине линии")
                plt.ylabel('Значение параметра_' + value)
                plt.xlabel('Номер участка в ведомости')
                plt.xticks(rotation='vertical')
                plt.xticks(np.arange(0, len(tie_forces.index), 1))
                fig.savefig(pic_path + value + ".png")
                pdf.savefig(fig)  
                
                # plt.show()
            # pdf.close()
            

            balast_opzp_streses_itogo = pd.DataFrame(balast_opzp_streses)
            balast_opzp_streses_itogo.columns = ['mean_F_ballast_kPa', 'sigma_F_ballast_kPa', 'mean_F_OPZP_kPa', 'sigma_F_OPZP_kPa',\
                                                'd_prof_kPa^Xprof', 'd_ball_kPa^Xball', 'd_opzp_kPa^Xopzp']

            balast_opzp_streses = line.join(balast_opzp_streses_itogo)
            balast_opzp_streses.to_csv(files_path + '/balast_opzp_streses_line.csv', sep=";")
            
            # Формирование графического отображения данных силового расчета в точке взаимодействия
            # print(len(force_line.index))
            values = ['mean_F_ballast_kPa', 'sigma_F_ballast_kPa', 'mean_F_OPZP_kPa', 'sigma_F_OPZP_kPa']
            for value in values:
                fig = plt.figure()
                plt.bar(balast_opzp_streses.index, balast_opzp_streses[value])
                plt.title('Распределение значений параметра_' + value + "_по длине линии")
                plt.ylabel('Значение параметра_' + value)
                plt.xlabel('Номер участка в ведомости')
                plt.xticks(rotation='vertical')
                plt.xticks(np.arange(0, len(balast_opzp_streses.index), 1))
                fig.savefig(pic_path + value + ".png")
                pdf.savefig(fig)  
                
                # plt.show()
            # pdf.close()
            

            damage_itogo = pd.DataFrame()
            damage_itogo['d_rail_MPa^Xrail'] = rail_streses['d_rail_MPa^Xrail']
            damage_itogo['d_fast_kN^Xfast'] = tie_forces['d_fast_kN^Xfast']
            damage_itogo['d_tie_kN^Xtie'] = tie_forces['d_tie_kN^Xtie']
            damage_itogo['d_shkol_kN^Xshkol'] = tie_forces['d_shkol_kN^Xshkol']
            damage_itogo['d_prof_kPa^Xprof'] = balast_opzp_streses['d_prof_kPa^Xprof']
            damage_itogo['d_plan_kN^Xplan'] = tie_forces['d_plan_kN^Xplan']
            damage_itogo['d_ball_kPa^Xball'] = balast_opzp_streses['d_ball_kPa^Xball']
            damage_itogo['d_opzp_kPa^Xopzp'] = balast_opzp_streses['d_opzp_kPa^Xopzp']
            damage = line.join(damage_itogo)
            damage.to_csv(files_path + '/damage_line.csv', sep= ";")

            # Формирование графического отображения данных силового расчета в точке взаимодействия
            # print(len(force_line.index))
            values = ['d_rail_MPa^Xrail', 'd_fast_kN^Xfast', 'd_tie_kN^Xtie', 'd_shkol_kN^Xshkol', 'd_prof_kPa^Xprof', 'd_plan_kN^Xplan', 'd_ball_kPa^Xball', 'd_opzp_kPa^Xopzp']
            for value in values:
                fig = plt.figure()
                plt.bar(damage.index, damage[value])
                plt.title('Распределение значений параметра_' + value + "_по длине линии")
                plt.ylabel('Значение параметра_' + value)
                plt.xlabel('Номер участка в ведомости')
                plt.xticks(rotation='vertical')
                plt.xticks(np.arange(0, len(damage.index), 1))
                fig.savefig(pic_path + value + ".png")
                pdf.savefig(fig)  
                
                # plt.show()
            pdf.close()
            # import zipfile
            # result_zip = zipfile.ZipFile((files_path + '\\neiro_damage_result.zip'), 'w')
            # zip_path = pathlib.Path(files_path)
            # print (zip_path)
            
            # for p in zip_path.glob('*.*'):
            #     print (zip_path.glob('*.*'))
            #     result_zip.write(p, compress_type=zipfile.ZIP_DEFLATED)
            # result_zip.close()
            # # path_init_file = projekt_item.document
            
            # pdf_file = r'C:\Users\suslo\Google Диск\2,5 млрд\Neiroexpert\Neiroexpert_WEb\projekts\10\all_result.pdf'
            # print (pdf_file)
            # projekt_directory_path(insteance, pdf_file)
            
            # prevent adding zip to itself if the old zip is left in the directory
            zip_path = os.path.join(files_path,'neiro_damage_result.zip')
            if os.path.exists(zip_path):
                os.unlink(zip_path)
            dirlist = os.listdir(files_path)
            zip_file = zipfile.ZipFile(zip_path, 'w')
            for file_name in dirlist:
                zip_file.write(os.path.join(files_path, file_name), file_name)
            zip_file.close()
            projekt_item.neiro_damage_flag = True
            # projekt_item.neiro_damage_result = settings.MEDIA_ROOT + str('/') + str(self.projekt_pk) + str('/neiro_damage/neiro_damage_result.zip')
            projekt_item.neiro_damage_result = ('/') + str(self.projekt_pk) + str('/neiro_damage/neiro_damage_result.zip')
            projekt_item.process_info = ('Процесс завершен успешно.')
            projekt_item.save()


            return (True)
        except:
            projekt_item.process_info = ('Ошибка исполнения. Процесс прерван.')
            projekt_item.neiro_damage_flag = False
            projekt_item.save()
            return (False) 