import serial
import time
ser = serial.Serial('COM5',9600) #checar a porta do Arduino dos sensores
#ser2 = serial.Serial('COM6',9600) #checar a porta do Arduino dos motores
ser.flushInput()
Ki = 0
Kd = 0
Kp = 0.7
baseSpeed = 25
speedR = baseSpeed
speedL = baseSpeed
setpoint = 490

def StringToInt(valorSensor):
	unidade=valorSensor[2]
	dezena=valorSensor[1]
	centena=valorSensor[0]
	intU = int(unidade)
	dezU = int(dezena)
	centU = int(centena)
	numero = centU*100 + dezU*10 + intU
	return numero

def ChangeSpeed(x,valor):
	speed = baseSpeed + Kp * valor
	if x == 'd':
		speedR = baseSpeed - Kp*valor
		speedL = baseSpeed + Kp*valor
	elif x == 'l':
		speedR = baseSpeed + Kp*valor
		speedL = -1*speed  - Kp*valor

	return speedR,speedL
while True:

    ser_bytes = ser.readline()
    valorSensor = ser_bytes[0:len(ser_bytes)-2].decode('utf-8', errors = 'replace')
    if len(valorSensor) == 3:
    	numero = StringToInt(valorSensor)
    else:
    	numero = 0
    print(numero)
    #valor = int(valorSensor)
   # x = input()
   # if valorSensor >= setpoint:
   # 	speedR,speedL = ChangeSpeed(x,600)
   # print('Velocidade direita: %d Velocidade esquerda: %d'%(speedR,speedL))
    speedR = baseSpeed
    speedL = baseSpeed

