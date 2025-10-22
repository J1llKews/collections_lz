#импорт библиотек
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20, 20, 500)  #заданный размер
y = np.sin(x**2)               #тригонометрическая функция синуса
plt.plot(x, y)                 #соединение точек
plt.title("График функции sin(x**2)")  #заголовок графика
plt.xlabel("x")               #подпись оси x
plt.ylabel("sin(x**2)")       #подпись оси y
plt.grid(True)                #включение сетки
plt.show()                    #вывод графика