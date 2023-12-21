#!/usr/bin/python3
class CSVReader:
    def __init__(self, filename):
        self.filename = filename
    
    def read_csv(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            headers = lines[0].strip().split(',')
            data = []
            for line in lines[1:]:
                values = line.strip().split(',')
                data.append(dict(zip(headers, values)))
            return data
    
    def process_data(self, data):
        for row in data:
            name = row['name']
            device_type = row['device_type']
            browser = row['browser']
            sex = row['sex']
            age = row['age']
            bill = row['bill']
            region = row['region']
            if sex == 'female':
                verb = 'совершила'
                sex_rus = 'женского пола'
            else:
                verb = 'совершил'
                sex_rus = 'мужского пола'
            print(f"Пользователь {name} {sex_rus}, {age} лет {verb} покупку на {bill} у.е. с {device_type} браузера {browser}. Регион, из которого совершалась покупка: {region}.")

reader = CSVReader('web_clients_correct.csv')
data = reader.read_csv()
reader.process_data(data)
