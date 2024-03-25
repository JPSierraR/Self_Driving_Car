import RPi.GPIO as GPIO
from time import sleep

# Configuración de los pines para el primer motor
ENA = 2
IN1 = 3
IN2 = 4
# Configuración de los pines para el segundo motor
ENB = 22
IN3 = 17
IN4 = 27
# Configuración de los pines para el tercer motor
enaA = 10
in1A = 9
in2A = 11
# Configuración de los pines para el cuarto motor
in3A = 5
in4A = 6
enbA = 13


# Configuración de la biblioteca RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configuración de los pines como salida
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

GPIO.setup(enaA, GPIO.OUT)
GPIO.setup(in1A, GPIO.OUT)
GPIO.setup(in2A, GPIO.OUT)

GPIO.setup(enbA, GPIO.OUT)
GPIO.setup(in3A, GPIO.OUT)
GPIO.setup(in4A, GPIO.OUT)

# Inicialización de los objetos PWM para controlar la velocidad de los motores
pwm_motor1 = GPIO.PWM(ENA, 1000)  # Frecuencia de 1000 Hz
pwm_motor2 = GPIO.PWM(ENB, 1000)  # Frecuencia de 1000 Hz
pwm_motor3 = GPIO.PWM(enaA, 1000)  # Frecuencia de 1000 Hz
pwm_motor4 = GPIO.PWM(enbA, 1000)  # Frecuencia de 1000 Hz

# Iniciar los PWM con un ciclo de trabajo del 0%
pwm_motor1.start(0)
pwm_motor2.start(0)
pwm_motor3.start(0)
pwm_motor4.start(0)
#--------------------- funciones para avazar---------------------------------

def move_forward():
    # Motor 1
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm_motor1.ChangeDutyCycle(V1)  # Velocidad del motor 1 al 50%

    # Motor 2
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_motor2.ChangeDutyCycle(V1)  # Velocidad del motor 2 al 50%

    # Motor 3
    GPIO.output(in1A, GPIO.HIGH)
    GPIO.output(in2A, GPIO.LOW)
    pwm_motor3.ChangeDutyCycle(V2)  # Velocidad del motor 3 al 25%

    # Motor 4
    GPIO.output(in3A, GPIO.LOW)
    GPIO.output(in4A, GPIO.HIGH)
    pwm_motor4.ChangeDutyCycle(V2)  # Velocidad del motor 4 al 25%

def move_derecha():
    # Motor 1
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm_motor1.ChangeDutyCycle(V2)  # Velocidad del motor 1 al 50%

    # Motor 2
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    pwm_motor2.ChangeDutyCycle(0)  # Velocidad del motor 2 al 0%

    # Motor 3
    GPIO.output(in1A, GPIO.LOW)
    GPIO.output(in2A, GPIO.LOW)
    pwm_motor3.ChangeDutyCycle(0)  # Velocidad del motor 3 al 0%

    # Motor 4
    GPIO.output(in3A, GPIO.LOW)
    GPIO.output(in4A, GPIO.HIGH)
    pwm_motor4.ChangeDutyCycle(50)  # Velocidad del motor 4 al 25%

def move_izquierda():
    # Motor 1
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm_motor1.ChangeDutyCycle(0)  # Velocidad del motor 1 al 50%

    # Motor 2
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_motor2.ChangeDutyCycle(V2)  # Velocidad del motor 2 al 0%

    # Motor 3
    GPIO.output(in1A, GPIO.HIGH)
    GPIO.output(in2A, GPIO.LOW)
    pwm_motor3.ChangeDutyCycle(V1)  # Velocidad del motor 3 al 0%

    # Motor 4
    GPIO.output(in3A, GPIO.LOW)
    GPIO.output(in4A, GPIO.HIGH)
    pwm_motor4.ChangeDutyCycle(0)  # Velocidad del motor 4 al 25%
def move_buscar_izquierda():
    # Motor 1
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    pwm_motor1.ChangeDutyCycle(AV1)  # Velocidad del motor 1 al 50%

    # Motor 2
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    pwm_motor2.ChangeDutyCycle(AV1)  # V1 Velocidad del motor 2 al 50%

    # Motor 3
    GPIO.output(in1A, GPIO.HIGH)
    GPIO.output(in2A, GPIO.LOW)
    pwm_motor3.ChangeDutyCycle(AV2)  # Velocidad del motor 3 al 25%

    # Motor 4
    GPIO.output(in3A, GPIO.HIGH)
    GPIO.output(in4A, GPIO.LOW)
    pwm_motor4.ChangeDutyCycle(AV2)  # Velocidad del motor 4 al 25%

def move_buscar_derecha():
    # Motor 1
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    pwm_motor1.ChangeDutyCycle(AV1)  # Velocidad del motor 1 al 50%

    # Motor 2
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    pwm_motor2.ChangeDutyCycle(AV1)  # V1 Velocidad del motor 2 al 50%

    # Motor 3
    GPIO.output(in1A, GPIO.LOW)
    GPIO.output(in2A, GPIO.HIGH)
    pwm_motor3.ChangeDutyCycle(AV2)  # Velocidad del motor 3 al 25%

    # Motor 4
    GPIO.output(in3A, GPIO.LOW)
    GPIO.output(in4A, GPIO.HIGH)
    pwm_motor4.ChangeDutyCycle(AV2)  # Velocidad del motor 4 al 25%

def stop_motors():
    # Detener ambos motores
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    GPIO.output(in1A, GPIO.LOW)
    GPIO.output(in2A, GPIO.LOW)
    pwm_motor1.ChangeDutyCycle(0)  # Detener motor 1
    pwm_motor2.ChangeDutyCycle(0)  # Detener motor 2
    pwm_motor3.ChangeDutyCycle(0)  # Detener motor 3
    pwm_motor4.ChangeDutyCycle(0)  # Detener motor 4
