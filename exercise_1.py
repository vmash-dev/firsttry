car_parameters = {
    "car_model": 'Camry Prestige',
    "price": '1 755 740 грн',
    "engine_displacement": '2487 см³',
    "max_weight": '2030 кг',
    "max_speed": '210 км/год',
    "lugagge_compartment": '469 л'
}

interior_features = {
    "feature_number_1": 'Оздоблення дверних карт синтетичною шкірою',
    "feature_number_2": 'Оздоблення переднього центрального підлокітника синтетичною шкірою',
    "feature_number_3": 'Кермо оздоблене шкірою',
    "feature_number_4": 'Фонова ілюмінація центральної консолі'
}

car_parameters.update(interior_features)

car_parameters['Equipped_mass'] = '1610-1620 кг'

car_model = car_parameters["car_model"]
print(car_model)
price = car_parameters["price"]
print(price)
feature_number_1 = car_parameters["feature_number_1"]
print(feature_number_1)