class RailWay: #Класс Железная дорога. Содержит в себе всю необходимую информацию для расчета повреждаемости и прогнозирования

    def __init__(self, Critical_values, Rail_plan, Rail_profile, VSP, Roadbed, Climate): #определяем необходимые атрибуты класса - это план, профиль, верхнее строение пути, зем.полотно, климат, общие эксплуатационные характеристики, характеристики вагонопотока, поездопотока

        self.Critical_values = Critical_values #атрибут содержит в себе общие правила эксплуатации (допустимые и критические отказы)

        self.Rail_plan = Rail_plan #атрибут содержит в себе данные о плане линии (радиус, возвышение, длины элементов)

        self.Rail_profile = Rail_profile ##атрибут содержит в себе данные о плане линии (уклон элемента, длину элемента)

        self.VSP = VSP #атрибут содержит в себе данные о верхнем строении пути (тип конструкции (бесс/зв путь, тип рельсов, категория качества, тип скреплений, шпал, род балласта, толщину итп)

        self.Roadbed = Roadbed #атрибут содержит в себе данные о земляном полотне (наыпь, выемка, высота/глубина, тип грунта тела з.п. и основаниия, наличие защитных слоев, итп) 

        self.Climate = Climate #атрибут содержит в себе данные про климат участка (номер климатической зоны, итп) 

        self.Rail_resource = rail_resource #TBI - атрибут содержит в себе текущий запас прочности рельс. По умолчанию он либо нормализован до 1, либо находится из входных данных

        self.VSP_resource = vsp_resource #TBI - атрибут содержит в себе текущий запас прочности элементов ВСП. По умолчанию он либо нормализован до 1, либо находится из входных данных

        self.Roadbed_resource = Roadbed_resource#TBI - атрибут содержит в себе текущий запас прочности элементов земного полотна. По умолчанию он либо нормализован до 1, либо находится из входных данных

        self.all_elements = [] #список всех элементов с их местоположением
 
    #функции вывода на экран параметров, характеризующих ж.д.

    def Show_critical_elements(self):
        critical = [element for element in  self.all_elements if element.condition()== "critical"]
        for element in critical:
            element.show()
        #функция выводит список элементов, с критическим уровнем ресурса
        
    def Show_subcritical_elements(self):
        subcritical = [element for element in  self.all_elements if element.condition()== "subcritical"]
        for element in subcritical:
            element.show()
        #функция выводит список элементов, с субкритическим уровнем ресурса
    
    def Critical_values_info(self):
        print (str(self.Critical_values) + "-это допустимые параметры эксплутатации")

    def Rail_plan_info(self):
        print (str(self.Rail_plan) + "-это характеристики плана линии")

    def Rail_profile_info(self):
        print (str(self.Rail_profile) + "-это характеристики профиля линии")

    def VSP_info(self):
        print (str(self.VSP) + "-это характеристики В.С.П. линии")

    def Roadbed_info(self):
        print (str(self.Roadbed) + "-это характеристики зем.полотна линии") 

    def Climate_info(self):
        print (str(self.Climate) + "-это характеристики климата линии")

    def Rail_resource_info(self):
        print (str(self.Rail_profile) + "-это текущий ресурс рельс")

    def VSP_resource_info(self):
        print (str(self.Rail_profile) + "-это текущий ресурс элементов В.С.П. линии")

    def Roadbed_resource_info(self):
        print (str(self.Rail_profile) + "-это текущий ресурс элементов земного полотна")
        return()

    def All_RailWay_info(self):
        print (str(self.Critical_values) + "-это допустимые параметры эксплутатации")
        print (str(self.Rail_plan) + "-это характеристики плана линии")
        print (str(self.Rail_profile) + "-это характеристики профиля линии")
        print (str(self.VSP) + "-это характеристики В.С.П. линии")
        print (str(self.Roadbed) + "-это характеристики зем.полотна линии") 
        print (str(self.Climate) + "-это характеристики климата линии")
        print (str(self.Rail_profile) + "-это текущий ресурс рельс")
        print (str(self.Rail_profile) + "-это текущий ресурс элементов В.С.П. линии")
        print (str(self.Rail_profile) + "-это текущий ресурс элементов земного полотна")
        return()
    #функции обработки вагонопотока
    def Rail_damage_info(self,wagon):
        return()
        # Функция выводит среднее израсходование ресурса рельс в зависимости от вагона ()
    
    def VSP_damage_info(self,wagon):
        return()
        # Функция выводит среднее израсходование ресурса ВСП в зависимости от вагона ()

    def Roadbed_damage_info(self,wagon):
        return()
        # Функция выводит среднее израсходование ресурса земного полотна в зависимости от вагона ()

    def Resource_update(self, traffic):
        return()
         # Функция обрабатывает вагонопоток и обновляет Rail_resource, VSP_resouce и Roadbed_resource

class Wagon: # Класс Вагон. Содержит все всю информацию, касающеюся одного вагона и необходимую для расчета взаимодействия с железной дорогой

    def __init__(self, type, speed):
        self.type = type

        #В зависимости от набора актуальных харакетристик (грузовой/пассажирский/локомотив масса, скорость, тип колесной пары, итп), 
        # добавляем нужные аттрибуты.
    # покажем главные характеристики вагона
    def show_wagon(self):
        return()
        #TBI


class Train: # Класс Поезд. Состоит из нескольких вагонов. 

    # по умолчанию поезд пустой. 
    def __init__(self):
        self.wagons = []
    # Добавим count вагонов какого-то типа
    def add_wagon(self, count, wagon):
        self.wagons.extend([wagon for wagon in range(count)])

    # Покажем состав поезда

    def show_wagons(self):
        for wagon in self.wagons:
            wagon.show() #

class Traffic: # Класс Вагонопоток. Состоит из набора поездов в некотором количестве. 

    # по умолчанию вагонопоток пустой. 
    def __init__(self):
        self.trains = []

    # добавим count поездов некоего типа:
    def add_trains(self,count,train):
        self.trains.append([count,train])
    
    # покажем состав вагонопотка
    def show_trains(self):
        for train in self.trains:
            print(str(train[0])+" поездов типа:")
            train.show_wagons()

