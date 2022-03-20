# with open('weather_data.csv', mode='r+') as file:
#     data = file.readlines()

# import csv
# with open('weather_data.csv', mode='r+') as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])
#     temperatures.remove('temp')
#     print(temperatures)
import pandas
# data = pandas.read_csv('weather_data.csv')
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# monday_farenheit = monday_temp * 33.8
# print(monday_farenheit)
# data_dict = {
#     "people": ['Andrei', 'Alex', 'Casablanca', "Mihaela", 'Jordan'],
#     'money': [1235, 34, 453, 346, 985]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('banii_si_viata.csv')
data = pandas.read_csv('squirrel_data.csv')
based_on_color = data['Primary Fur Color']
gray_num = len(based_on_color[based_on_color == 'Gray'])
black_num = len(based_on_color[based_on_color == 'Black'])
cinnamon_num = len(based_on_color[based_on_color == 'Cinnamon'])

new_data_dict = {
    'Fur Color': ['Gray', 'Black', 'Cinnamon'],
    'Count': [gray_num, black_num, cinnamon_num]
}
new_data = pandas.DataFrame(new_data_dict)
new_data.to_csv('squirrel_color.csv')