import csv
class Load_data:

    def get_data(self,lokasi):
        #data = [[0,1,0],[0,0,0],[1,0,0],[1,1,1],[1,0,0],[1,1,1]]
        data = []
        with open(lokasi) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            for row in csv_reader:
                data.append(row)
            data.pop(0)

            for x in range(len(data)):
                del data[x][0]
                for y in range(len(data[0])):
                    data[x][y] = int(data[x][y])
        return data

    def preprocess_data(self,data_mentah):
        x_max = []
        x_min = []
        data_normalisasi = []
        for x in range(len(data_mentah[0])):
            temp = data_mentah[0][x]
            for y in range(len(data_mentah)):
                if (temp <= data_mentah[y][x]):
                    temp = data_mentah[y][x]
            x_max.append(temp)

        for x in range(len(data_mentah[0])):
            temp = data_mentah[0][x]
            for y in range(len(data_mentah)):
                if (temp >= data_mentah[y][x]):
                    temp = data_mentah[y][x]
            x_min.append(temp)

        for x in range(len(data_mentah)):
            temp_data_normalisasi = []
            for y in range(len(data_mentah[x])):
                temp = (data_mentah[x][y] - x_min[y]) / (x_max[y] - x_min[y])
                temp_data_normalisasi.append(round(temp, 2))
            data_normalisasi.append(temp_data_normalisasi)
        return data_normalisasi

