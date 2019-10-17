/*
  Projeto para a Fatec Aberta em Araçatuba
  Análise e Desenvolvimento de Sistemas
  Desenvolvido por: Equipe Pseudo Geeks
  Fabiano Silva | Fernando Bergamasco | Gabriel Gregorio
*/

// Declaração de variáveis
// Definindo o número dos pinos dos LEDs
const int greenLED1 = 22;
const int blueLED1 = 23;

const int greenLED2 = 24;
const int blueLED2 = 25;

const int greenLED3 = 26;
const int blueLED3 = 27;

const int greenLED4 = 28;
const int blueLED4 = 29;

const int greenLED5 = 30;
const int blueLED5 = 31;

const int greenLED6 = 32;
const int blueLED6 = 33;

const int greenLED7 = 34;
const int blueLED7 = 35;

const int greenLED8 = 36;
const int blueLED8 = 37;

const int greenLED9 = 38;
const int blueLED9 = 39;

// Definindo o número dos pinhos dos pushButtons
const int pushButton1 = 41;
const int pushButton2 = 42;
const int pushButton3 = 43;
const int pushButton4 = 44;
const int pushButton5 = 45;
const int pushButton6 = 46;
const int pushButton7 = 47;
const int pushButton8 = 48;
const int pushButton9 = 49;

// Definindo o estado inicial dos pushButtons
int pushButtonState1 = 0;
int pushButtonState2 = 0;
int pushButtonState3 = 0;
int pushButtonState4 = 0;
int pushButtonState5 = 0;
int pushButtonState6 = 0;
int pushButtonState7 = 0;
int pushButtonState8 = 0;
int pushButtonState9 = 0;

void setup ()
{
  // Iniciando a porta serial
  Serial.begin(9600);

  // Definindo os pinos dos LEDs como OUTPUT

  pinMode(greenLED1, OUTPUT);
  pinMode(blueLED1, OUTPUT);
  pinMode(pushButton1, INPUT);

  pinMode(greenLED2, OUTPUT);
  pinMode(blueLED2, OUTPUT);
  pinMode(pushButton2, INPUT);

  pinMode(greenLED3, OUTPUT);
  pinMode(blueLED3, OUTPUT);
  pinMode(pushButton3, INPUT);

  pinMode(greenLED4, OUTPUT);
  pinMode(blueLED4, OUTPUT);
  pinMode(pushButton4, INPUT);

  pinMode(greenLED5, OUTPUT);
  pinMode(blueLED5, OUTPUT);
  pinMode(pushButton5, INPUT);

  pinMode(greenLED6, OUTPUT);
  pinMode(blueLED6, OUTPUT);
  pinMode(pushButton6, INPUT);

  pinMode(greenLED7, OUTPUT);
  pinMode(blueLED7, OUTPUT);
  pinMode(pushButton7, INPUT);

  pinMode(greenLED8, OUTPUT);
  pinMode(blueLED8, OUTPUT);
  pinMode(pushButton8, INPUT);

  pinMode(greenLED9, OUTPUT);
  pinMode(blueLED9, OUTPUT);
  pinMode(pushButton9, INPUT);
}

void loop()
{
  // Nesta parte do código nós enviaremos um sinal de entrada para a porta serial se o estado do pushButton for HIGH

  int buttonSignal = 0;

  pushButtonState1 = digitalRead(pushButton1);
  if (pushButtonState1 == HIGH);
  {
    buttonSignal = 1;
  }

  pushButtonState2 = digitalRead(pushButton2);
  if (pushButtonState2 == HIGH);
  {
    buttonSignal = 2;
  }

  pushButtonState3 = digitalRead(pushButton3);
  if (pushButtonState3 == HIGH);
  {
    buttonSignal = 3;
  }

  pushButtonState4 = digitalRead(pushButton4);
  if (pushButtonState4 == HIGH);
  {
    buttonSignal = 4;
  }

  pushButtonState5 = digitalRead(pushButton5);
  if (pushButtonState5 == HIGH);
  {
    buttonSignal == 5;
  }

  pushButtonState6 = digitalRead(pushButton6);
  if (pushButtonState6 == HIGH);
  {
    buttonSignal = 6;
  }

  pushButtonState7 = digitalRead(pushButton7);
  if (pushButtonState7 == HIGH);
  {
    buttonSignal = 7;
  }

  pushButtonState8 = digitalRead(pushButton8);
  if (pushButtonState8 == HIGH);
  {
    buttonSignal = 8;
  }

  pushButtonState9 = digitalRead(pushButton9);
  if (pushButtonState9 == HIGH);
  {
    buttonSignal = 9;
  }

  // Nesta parte estamos lendo o sinal de entrada da porta serial
  // Os LEDs acenderão de acordo com o sinal recebido

  char inputSignal = Serial.read();

  if (inputSignal == 'a')
  {
    digitalWrite(greenLED1, HIGH);
  }
  else if (inputSignal == 'b')
  {
    digitalWrite(blueLED1, HIGH);
  }
  else if (inputSignal == 'c')
  {
    digitalWrite(greenLED2, HIGH);
  }
  else if (inputSignal == 'd')
  {
    digitalWrite(blueLED2, HIGH);
  }
  else if (inputSignal == 'e')
  {
    digitalWrite(greenLED3, HIGH);
  }
  else if (inputSignal == 'f')
  {
    digitalWrite(blueLED3, HIGH);
  }
  else if (inputSignal == 'g')
  {
    digitalWrite(greenLED4, HIGH);
  }
  else if (inputSignal == 'h')
  {
    digitalWrite(blueLED4, HIGH);
  }
  else if (inputSignal == 'i')
  {
    digitalWrite(greenLED5, HIGH);
  }
  else if (inputSignal == 'j')
  {
    digitalWrite(blueLED5, HIGH);
  }
  else if (inputSignal == 'k')
  {
    digitalWrite(greenLED6, HIGH);
  }
  else if (inputSignal == 'l')
  {
    digitalWrite(blueLED6, HIGH);
  }
  else if (inputSignal == 'm')
  {
    digitalWrite(greenLED7, HIGH);
  }
  else if (inputSignal == 'n')
  {
    digitalWrite(blueLED7, HIGH);
  }
  else if (inputSignal == 'o')
  {
    digitalWrite(greenLED8, HIGH);
  }
  else if (inputSignal == 'p')
  {
    digitalWrite(blueLED8, HIGH);
  }
  else if (inputSignal == 'q')
  {
    digitalWrite(greenLED9, HIGH);
  }
  else if (inputSignal == 'r')
  {
    digitalWrite(blueLED9, HIGH);
  }
  else if (inputSignal == 'z')
  {
    digitalWrite(greenLED1, LOW);
    digitalWrite(blueLED1, LOW);

    digitalWrite(greenLED2, LOW);
    digitalWrite(blueLED2, LOW);

    digitalWrite(greenLED3, LOW);
    digitalWrite(blueLED3, LOW);

    digitalWrite(greenLED4, LOW);
    digitalWrite(blueLED4, LOW);

    digitalWrite(greenLED5, LOW);
    digitalWrite(blueLED5, LOW);

    digitalWrite(greenLED6, LOW);
    digitalWrite(blueLED6, LOW);

    digitalWrite(greenLED7, LOW);
    digitalWrite(blueLED7, LOW);

    digitalWrite(greenLED8, LOW);
    digitalWrite(blueLED8, LOW);

    digitalWrite(greenLED9, LOW);
    digitalWrite(blueLED9, LOW);
  }
}