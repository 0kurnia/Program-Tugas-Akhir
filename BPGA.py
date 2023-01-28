import  random
import math
from Load_data import  Load_data

class BPGA:
    data_mentah = Load_data.get_data(Load_data,'dataset/data_latih.csv')
    neuron_hidden = 15
    Vji = (len(data_mentah[0]) - 1) * 15
    Vj0 = (15 * 1)
    Wkj = (1 * 15)
    Wk0 = (1 * 1)
    kromosom = Vji + Vj0 + Wkj + Wk0
    mulai = 0

    def data_random(self):
        data_kromosom = []
        for x in range(0,1):
            data_kromosom_temp = []
            for y in range(self.kromosom):
                data_kromosom_temp.append(round(random.uniform(0, 1), 4))
            data_kromosom.append(data_kromosom_temp)
        return data_kromosom

    def data_kromosom(self,populasi):
        data_kromosom = []
        for x in range(populasi):
            data_kromosom_temp = []
            for y in range(self.kromosom):
                data_kromosom_temp.append(round(random.uniform(0, 1), 4))
            data_kromosom.append(data_kromosom_temp)
        return data_kromosom

    def bobot_input_hidden(self,data,i):
        bobot_Vji = []
        self.mulai=0
        for x in range(self.neuron_hidden):
            bobot_Vji_temp = []
            for y in range(len(self.data_mentah[0])-1):
                bobot_Vji_temp.append(data[i][self.mulai])
                self.mulai+=1
            bobot_Vji.append(bobot_Vji_temp)
        return bobot_Vji

    def bobot_bias_hidden(self,data,i):
        bobot_Vj0 = []
        for x in range(self.neuron_hidden):
            bobot_Vj0.append(data[i][self.mulai])
            self.mulai += 1
        return bobot_Vj0

    def bobot_hidden_output(self,data,i):
        bobot_Wkj = []
        for x in range(self.neuron_hidden):
            bobot_Wkj.append(data[i][self.mulai])
            self.mulai += 1
        return bobot_Wkj


    def bobot_bias_output(self,data,i):
        bobot_Wk0 = data[i][self.mulai]
        return bobot_Wk0

    def z_net(self,data,bobot_Vji,bobot_Vj0,b):
        z_net =[]
        for x in range(self.neuron_hidden):
            temp = 0
            for y in range(len(data[0]) - 1):
                temp += (data[b][y] * bobot_Vji[x][y])
            temp += bobot_Vj0[x]
            z_net.append(round(temp, 2))
        return z_net

    def z_hidden(self, z_net):
        z_hidden = []
        for x in range(len(z_net)):
            z_hidden.append(1 / (1 + (math.exp(-(z_net[x])))))
        return z_hidden

    def y_net(self,bobot_Wkj,bobot_Wk0,z_hidden):
        y_net = 0
        for x in range(len(z_hidden)):
            y_net += z_hidden[x] * bobot_Wkj[x]
        y_net += bobot_Wk0
        return y_net

    def y_output(self,y_net):
        return 1 / (1 + (math.exp(-(y_net))))

    def error_prediksi(self,data,y_output,banyak_data,b):
        return (data[b][banyak_data - 1] - y_output) * y_output * (1 - y_output)

    def delta_Wkj(self,eror_prediksi,z_hidden,learning_rate):
        delta_Wkj = []
        for x in range(len(z_hidden)):
            delta_Wkj.append(eror_prediksi * learning_rate * z_hidden[x])
        return delta_Wkj

    def delta_Wk0(self,eror_prediksi,learning_rate):
        delta_Wk0=[]
        delta_Wk0 = eror_prediksi * learning_rate
        return delta_Wk0

    def s_net(self,eror_prediksi,bobot_Wkj):
        s_net = []
        for x in range(len(bobot_Wkj)):
            s_net.append(eror_prediksi * bobot_Wkj[x])
        return s_net

    def error_hidden(self,s_net,z_hidden):
        error_hidden = []
        for x in range(len(s_net)):
            error_hidden.append((s_net[x] * z_hidden[x]) * (1 - z_hidden[x]))
        return error_hidden

    def delta_Vji(self,error_hidden,data,learning_rate,b):
        delta_Vji = []
        for x in range(len(error_hidden)):
            delta_Vji_temp = []
            for y in range(len(data[b]) - 1):
                delta_Vji_temp.append(learning_rate * error_hidden[x] * data[b][y])
            delta_Vji.append(delta_Vji_temp)
        return delta_Vji

    def delta_Vjo(self,error_hidden,learning_rate):
        delta_Vj0 = []
        for x in range(len(error_hidden)):
            delta_Vj0.append(error_hidden[x] * learning_rate)
        return delta_Vj0

    def mse(self,data,y_output_all,banyak_data):
        mse = 0
        for x in range(len(y_output_all)):
            mse += math.pow((data[x][banyak_data - 1] - y_output_all[x]), 2)
        mse = mse / len(data)
        return mse

    def fitness(self,mse_all):
        fitness = []
        for x in range(len(mse_all)):
            fitness.append(1 / mse_all[x])
        return fitness

    def sum_fitness(self,fitness):
        sum_fitness = 0
        for x in range(len(fitness)):
            sum_fitness += fitness[x]
        return sum_fitness

    def probability_kromosom(self,fitness,sum_fitness):
        probability = []
        for x in range(len(fitness)):
            probability.append(round(fitness[x] / sum_fitness, 4))
        return probability

    def cummulative_probability(self,probability_kromosom):
        c_probability = []
        start = 0
        for x in range(len(probability_kromosom)):
            temp = 0
            for y in range(start + 1):
                temp += probability_kromosom[y]
            start += 1
            c_probability.append(temp)
        return c_probability

    def roullete_wheel(self,c_probability,data_kromosom,populasi):
        index_chromosom = []
        random_nilai = []
        for x in range(populasi):
            random_nilai.append(round(random.uniform(0, 0.99), 4))
        for x in range(len(random_nilai)):
            for y in range(len(c_probability)):
                if (random_nilai[x] <= c_probability[y]):
                    index_chromosom.append(y)
                    break
        #print("index",index_chromosom)
        kromosom_roullete_wheel = []
        for x in range(len(index_chromosom)):
            #salah bagian ini
            kromosom_roullete_wheel.append(data_kromosom[index_chromosom[x]])
        return kromosom_roullete_wheel

    def cross_over(self,crosover_rate,data_kromosom,populasi):
        index_chromosom = []
        random_nilai = []
        for x in range(populasi):
            random_nilai.append(round(random.uniform(0, 1), 4))
        for x in range(len(random_nilai)):
            if (random_nilai[x] <= crosover_rate):
                index_chromosom.append(x)
        banyak_kromosom_ditukar = []
        for x in range(len(random_nilai)):
            if (random_nilai[x] <= crosover_rate):
                banyak_kromosom_ditukar.append(int(round(random.uniform(0, self.kromosom - 1), 0)))
        if (len(banyak_kromosom_ditukar) > 1):
            kromosom_temp = data_kromosom
            kromosom_baru = []
            for x in range(len(index_chromosom) - 1):
                kromosom_baru_temp = []
                for y in range(banyak_kromosom_ditukar[x]):
                    kromosom_baru_temp.append(kromosom_temp[index_chromosom[x]][y])
                for y in range(banyak_kromosom_ditukar[x], len(kromosom_temp[index_chromosom[x]])):
                    kromosom_baru_temp.append(kromosom_temp[index_chromosom[x + 1]][y])
                kromosom_baru.append(kromosom_baru_temp)
            kromosom_baru_temp = []
            x = len(index_chromosom) - 1
            for y in range(banyak_kromosom_ditukar[len(index_chromosom) - 1]):
                kromosom_baru_temp.append(kromosom_temp[index_chromosom[x]][y])
            for y in range(banyak_kromosom_ditukar[x], len(kromosom_temp[index_chromosom[x]])):
                kromosom_baru_temp.append(kromosom_temp[index_chromosom[0]][y])
            kromosom_baru.append(kromosom_baru_temp)

            for x in range(len(index_chromosom)):
                data_kromosom[index_chromosom[x]] = kromosom_baru[x]
        return data_kromosom

    def mutasi(self,mutasi_rate,populasi,data_kromosom):
        jumlah_mutasi = int(mutasi_rate * populasi * self.kromosom)
        r_3 = []
        for x in range(jumlah_mutasi):
            r_3.append(int(round(random.uniform(0, (self.kromosom * populasi) - 1))))
        for a in range(len(r_3)):
            mulai = 0
            for x in range(len(data_kromosom)):
                for y in range(len(data_kromosom[x])):
                    if (mulai == r_3[a]):
                        data_kromosom[x][y] = round(random.uniform(0, 1), 4)
                    mulai += 1
        return data_kromosom

    def feed_forward(self,data_normalisasi,bobot_Vji,bobot_Vj0,bobot_Wkj,bobot_Wk0,b):
        banyak_data = len(data_normalisasi[b])

        z_net = BPGA.z_net(BPGA, data_normalisasi, bobot_Vji, bobot_Vj0, b)
        z_hidden = BPGA.z_hidden(BPGA, z_net)

        y_net = BPGA.y_net(BPGA, bobot_Wkj, bobot_Wk0, z_hidden)
        y_output = BPGA.y_output(BPGA, y_net)

        eror_prediksi = BPGA.error_prediksi(BPGA, data_normalisasi, y_output, banyak_data, b)
        return z_net,z_hidden, y_net,y_output, eror_prediksi


    def backward(self,data_normalisasi,bobot_Wkj,eror_prediksi,z_hidden,learning_rate,b):
        delta_Wkj = BPGA.delta_Wkj(BPGA, eror_prediksi, z_hidden, learning_rate)
        delta_Wk0 = BPGA.delta_Wk0(BPGA, eror_prediksi, learning_rate)
        s_net = BPGA.s_net(BPGA, eror_prediksi, bobot_Wkj)
        error_hidden = BPGA.error_hidden(BPGA, s_net, z_hidden)
        delta_Vji = BPGA.delta_Vji(BPGA, error_hidden, data_normalisasi, learning_rate, b)
        delta_Vj0 = BPGA.delta_Vjo(BPGA, error_hidden, learning_rate)

        return delta_Vji,delta_Vj0,delta_Wkj,delta_Wk0

    def parent_selection(self,fitness,populasi,data_kromosom):
        sum_fitness = BPGA.sum_fitness(BPGA, fitness)
        probability_kromosom = BPGA.probability_kromosom(BPGA, fitness, sum_fitness)

        c_probability = BPGA.cummulative_probability(BPGA, probability_kromosom)
        kromosom_roullete_wheel = BPGA.roullete_wheel(BPGA, c_probability, data_kromosom, populasi)
        return kromosom_roullete_wheel


















