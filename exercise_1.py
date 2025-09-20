base_number = 0
people = 4
ticket = 500
taxi_to_park = 600
taxi_from_park = taxi_to_park * 1.2
pizza = 250
pizza_final_price = pizza * (1 - 0.15)
air_hockey = 80
total_cost = base_number + (ticket * people) + taxi_to_park + taxi_from_park + (pizza_final_price * 2) + (air_hockey * 8)
avarege_cost = total_cost / people
print("Всі разом заплотять", total_cost)
print("З одної людини буде", avarege_cost)
