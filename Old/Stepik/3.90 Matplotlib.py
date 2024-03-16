import matplotlib.pyplot as plt
from pylab import *

x = linspace(0, 5, 10)
y = x**2
print(x)
print(y)
print('----------------------------------------------------------------------------')

figure()
plot(x, y, 'g')
xlabel('Месяцы')
ylabel('Тыс.$')
title('Рост твоих доходов')
show()
