const int sensorR = 0;
const int sensorL = 1;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(sensorR,INPUT);
  pinMode(sensorL,INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  int maiorLeitura;
  int nivelR = analogRead(sensorR);
  int nivelL = analogRead(sensorL);
  if(nivelR > nivelL)
  {
    maiorLeitura = nivelR;
    aux = "l";
  }
  if(nivelL > nivelR)
  {
    maiorLeitura = nivelL;
    aux = "r";
  }
  else
  {
    maiorLeitura = "111";
    aux = "f";
  }
  leituraString = String(maiorLeitura);
  valorSensor = maiorLeitura;
  Serial.println(valorSensor);
}

