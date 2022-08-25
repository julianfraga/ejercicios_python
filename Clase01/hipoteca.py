# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 21:18:35 2022

@author: Julián
"""

#Parámetros del loop
saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_extra=1000
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108

#declaro mes, pagos y total pagado como ceros por el momento
total_pagado = 0.0
mes=0
pago=0 

while saldo > 0: # mientras el saldo sea mayor a cero
    if pago<saldo: # si el pago a realizar es menor al saldo restante
        if mes>= pago_extra_mes_comienzo and mes<=pago_extra_mes_fin: # y estoy en los meses 61 a 108
            pago= pago_mensual+pago_extra
    
        else: # si estoy en cualquier otro mes
            pago=pago_mensual
        
    else: # si el pago a realizar es mayor o igual al saldo
        pago= saldo * (1+tasa/12)
        
    saldo=saldo * (1+tasa/12)-pago
    total_pagado = total_pagado + pago
    mes=mes+1
    print(mes, round(total_pagado,2), round(saldo, 2))

print('Total pagado', round(total_pagado, 2), ' a lo largo de', mes, ' meses.')
print('Además, la función bool(x) arroja como resultado False únicamente cuando el argumento es x=0, x=False o no tiene argumento.\nEn cualquier otro caso da True')
