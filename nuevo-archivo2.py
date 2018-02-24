# Ejercicio de caso práctico # 5 Segunda parte
 
 
n = 0

file_out = open('tabla2.csv', 'w')

file_out.write('ESTACION,ANO,MES,DIA,HORA,VEL\n')


for filename in glob.glob("*.txt"):


    file_in = open(filename, 'r')

    lines = file_in.readlines()

    text = [float(x) for x in lines]

    filename = filename.replace('-', ',')

    prom = sum(text) / len(text)

    prom = '%.2f' % prom

    file_out.write(filename[:-4] + ',' + str(prom) + '\n')

    file_in.close()



    n += 1

    if n == 10:

        break



file_out.close()
