//2020 copyright
//Vít Růžička
//Pavel Hrstka
/*
                 regál


  +----------------+---------------+----------------+----------------+--------------+
  |                |               |                |                |              |
  |                |               |                |                |              |
  |                |               |                |                |              |
  |        2       |       3       |        4       |        5       |      6       |
  |                |               |                |                |              |
  |                |               |                |                |              |
  |                |               |                |                |              |
  +---------------------------------------------------------------------------------+
  |                |               |                |                |              |
  |                |               |                |                |              |
  |                |               |                |                |              |
  |       7        |       8       |       9        |       10       |       11     |
  |                |               |                |                |              |
  |                |               |                |                |              |
  |                |               |                |                |              |
  +----------------+---------------+----------------+----------------+--------------+

*/

#include <AccelStepper.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>


//globalni promenne
#define akcelerace 1500  //výchozí akcelerace a rychlost pro celý systém
#define rychlost 700
#define uvolneniStopu 30 ///vzdálenost , kterou ujede aby neležel na endstopu
//#define diag             //vypisuje diagnosticke zpravy do serioveho monitoru


long delkaX = 1250;  //nastaveni delky osy v mm
long delkaY = 195;
long delkaZ = 180;

#define stoupaniX 4   //mm na milimetr
#define stoupaniY 4   //6400 by melo odpovidat T8x8 trapezu (na 200 krokách 400 kroku/mm, na 3200 krocich 6400...
#define stoupaniZ 25    //taky remen

#define logEndstopX true //obrácení smyslu endstopu
#define logEndstopY true
#define logEndstopZ true

#define nabiraciOffset 8
//čislo pozice nakládací plochy
int poziceX[] = {236,90,  1210, 1025, 820, 623, 425, 1210, 1025, 820, 630, 435   };  //10 pozic + dvě pro nakládání a skládání, nakl. vykl, 2 pozice
int poziceZ[] = {1, 3,     169, 169,  169, 169, 169,  39,  39,   39,   39,  39   };  //10 pozic
int poziceY[] = {0, 190,175, 175 };  //hloubka skladu, naložení skladu,  pozice: 0-pohybova pozice; 1-sklad; 2-nakladaci policko, 3- vykladaci policko


int nX = 0;          //nakladaci pozice  UPRAVIT
int nZ = 0;

int vX = 1;
int vZ = 1;

byte ishomeX = false; //bez toho neví kde je, ještě není používáno
byte ishomeY = false;
byte ishomeZ = false;

int xMotorDir = 1;
int yMotorDir = 1; //pro opačný směr nahraďte za -1
int zMotorDir = 1;

#define X_STEP_PIN         54
#define X_DIR_PIN          55
#define X_ENABLE_PIN       38
#define X_MIN_PIN           3
#define X_MAX_PIN           2

#define Y_STEP_PIN         60
#define Y_DIR_PIN          61
#define Y_ENABLE_PIN       56
#define Y_MIN_PIN          14
#define Y_MAX_PIN          15

#define Z_STEP_PIN         46
#define Z_DIR_PIN          48
#define Z_ENABLE_PIN       62
#define Z_MIN_PIN          18
#define Z_MAX_PIN          19

#define E_STEP_PIN         26
#define E_DIR_PIN          28
#define E_ENABLE_PIN       24


AccelStepper osaX(1, X_STEP_PIN, X_DIR_PIN);
AccelStepper osaY(1, Y_STEP_PIN, Y_DIR_PIN);
AccelStepper osaZ(1, Z_STEP_PIN, Z_DIR_PIN);

LiquidCrystal_I2C lcd(0x27, 16, 2);

////////  KOMUNIKACE
#define MAX_BUF 64  //maximální velikost bufferu pro přijímání dat
int data;           //pocet dat v bufferu
char buffer[MAX_BUF];





void setup() {
  //disable piny
  osaX.setEnablePin(X_ENABLE_PIN);
  osaY.setEnablePin(Y_ENABLE_PIN);
  osaZ.setEnablePin(Z_ENABLE_PIN);

  //rychlosti
  osaX.setMaxSpeed(rychlost);
  osaY.setMaxSpeed(rychlost);
  osaZ.setMaxSpeed(rychlost*1.3);

  //akcelerace
  osaX.setAcceleration(akcelerace);
  osaY.setAcceleration(akcelerace);
  osaZ.setAcceleration(akcelerace);

  pinMode(X_MIN_PIN, INPUT); //zvážit použítí INPUT_PULLUP, záleží na typu endstopu
  pinMode(Y_MIN_PIN, INPUT);
  pinMode(Z_MIN_PIN, INPUT);
  Serial.begin(115200);
  analogWrite(8, 255);

    lcd.init();
  lcd.backlight();
  lcd.print("frantisku");
  lcd.setCursor(0,1);
  lcd.print("vyser si voko");
  data = 0;
}





void loop() {
  //homeY();
  //homeZ();
  //homeX();

  //delay(5000);


  if (Serial.available() > 0) {
    char c =  Serial.read();

    if (data < MAX_BUF) { //overeni jestli se data vejdou do bufferu
      buffer[data++] = c;  //pridani dat do bufferu na dalsi pozici
      //Serial.println("pripisuji znak");
    }
    if (c == '\n') {
      //Serial.print(F("\r\n"));   //return - může být nahrazeno za OK, když bude spolupracovat python
      buffer[data] = 0;           //string v bufferu musí končit nulovým charakterem
      zpracovaniPrikazu();        //ehm vytvorit
      data = 0;
    }
  }

}








/////////////// OBECNÉ FUNKCE
float ziskejCislo(char pismeno, float hdn) {  //kdyz je po argumentu pismeno nejake cislo, vrátí ho, když ne, vrátí hodnotu hdn
  char *ptr = buffer; // zacne na zacatku bufferu
  while ((long)ptr > 1 && (*ptr) && (long)ptr < (long)buffer + data) { //dojdi na konec
    if (*ptr == pismeno) { // pokud narazis na pismeno vrat hodnotu po nem
      return atof(ptr + 1); // prevede nasledujici znaky na float
    }
    ptr = strchr(ptr, ' ') + 1; //preskoci mezeru
  }
  return hdn;  //konec, vrati vychozi hodnotu
}

void zpracovaniPrikazu() {
  Serial.println(buffer);
  int gcode = ziskejCislo('G', -1);  //získá gcode
  switch (gcode) {                   //porovná gcode s možnými případy
    case 0:
      zapnutiMOT();
      moveX(ziskejCislo('X', 0)); //ziskejCislo('X',0)
      moveY(ziskejCislo('Y', 0));
      moveZ(ziskejCislo('Z', 0));
      break;
    case 1:
      zapnutiMOT();
      moveToX(ziskejCislo('X', osaX.currentPosition() / stoupaniX));
      moveToY(ziskejCislo('Y', osaY.currentPosition() / stoupaniY));
      moveToZ(ziskejCislo('Z', osaZ.currentPosition() / stoupaniZ));
      break;
    case 2:
    zapnutiMOT();
      movePole(ziskejCislo('P', -1), ziskejCislo('Z', -1));
      break;
    case 28:
      zapnutiMOT();
      homeY();
      homeZ();
      homeX();
      break;

    default:

      Serial.println(F("neplatny prikaz G"));
      break;;

  }
  gcode = ziskejCislo('M', -1);
  switch (gcode) {

    case 10:
      vypisPozice();
      break;
    case 18:
      vypnutiMOT();
      break;
    case 108:
      analogWrite(8, ziskejCislo('S', 0));
      break;
    case 109:
      analogWrite(9, ziskejCislo('S', 0));
      break;
    case 110:
      analogWrite(10, ziskejCislo('S', 0));
      break;
    case 99:
      Serial.println("OK");                 //zpusob PING PONGU
      break;
    default:
      Serial.println(F("neplatny prikaz M"));
      break;;
  }


}

void vypnutiMOT() {
  osaX.enableOutputs();
  osaY.enableOutputs();
  osaZ.enableOutputs();
  ishomeX = 0;     //zrusi se kalibrace os, muzou se rozhodit souradnice
  ishomeY = 0;
  ishomeZ = 0;
}
void zapnutiMOT() {
  osaX.disableOutputs();
  osaY.disableOutputs();
  osaZ.disableOutputs();
}

void vypisPozice() {
  Serial.print(F("X: "));
  Serial.println(osaX.currentPosition() / stoupaniX);
  Serial.print(F("Y: "));
  Serial.println(osaY.currentPosition() / stoupaniY);
  Serial.print(F("Z: "));
  Serial.println(osaZ.currentPosition() / stoupaniZ);
}

void movePole(int pozice, byte naskladnit) {
  if (ishomeX && ishomeY && ishomeZ) {       //zjištění homu
#ifdef diag
    Serial.println(F("osy jsou v homu"));
#endif
  }
  else {
    zapnutiMOT();
    homeY();
    homeZ();
    homeX();

  }
  if(pozice >= 2 && pozice <= 11){
  if(naskladnit == 1){   //funkce pro naskladnění
    while(digitalRead(X_MAX_PIN)){ //pokud neni sepnut koncak na nakladaci plose
    if(Serial.available()){
    String odpoved = Serial.readStringUntil('#');
      if(odpoved == "jsem curak"){ //stisknuti jsem curak tlacitka na rpi
      
        goto konecNaskladneni;
    }
      
    }
    delay(500);
    }
      
      
    moveToX(poziceX[nX]);  //zajeti do nakladaci polohy
    moveToZ(poziceZ[nZ]);
    moveToY(poziceY[2]);

    moveZ(nabiraciOffset+20);
    moveToY(poziceY[0]);           //vytahnuti osy do pracovni pozice

    moveToX(poziceX[pozice]); //zajeti na uroven policka
    moveToZ(poziceZ[pozice]+nabiraciOffset);


    moveToY(poziceY[1]); //zajeti do pozice skladu

    moveZ(-nabiraciOffset);  //polozeni

    //moveToY(poziceY[0]); //cestovni pozice

    homeY(); //zajeti do homu
    homeZ();
    homeX();
      Serial.println("OK");
    konecNaskladneni:
    Serial.println("");
  }
  else if(naskladnit == 2){             //funkce pro vyskladnění
    
    moveToY(poziceY[0]);           //vytahnuti osy do cestovni pozice

    moveToX(poziceX[pozice]); //zajeti na uroven policka
    moveToZ(poziceZ[pozice]);

    moveToY(poziceY[1]+1); //zajeti do pozice skladu     5 je aby si podsekl paletu   pridavne zajizdeni
    moveZ(nabiraciOffset);

    moveToY(poziceY[0]); //cestovni pozice
    moveToZ(poziceZ[vZ]+20);  //aby nenarazil do displeje
    
    
    moveToX(poziceX[vX]);  //zajeti do vykladaci polohy
    moveToZ(poziceZ[vZ]+20);
    while(!digitalRead(Y_MAX_PIN)){  //pokud je obsazena vykl. plocha
      delay(500);
    }
    moveToY(poziceY[3]);

   
    moveZ(-nabiraciOffset-20);  //snizeni o vysku zajeti
    //moveToY(poziceY[0]); //bezpecna pozice
    

    homeY(); //zajeti do homu
    homeZ();
    homeX();
    Serial.println("OK");
    
  }
  else{
    //spatna hodnota (nebude nakladat ani vykladat)
  }
  }
    else{
      //spatne pole, nebude nic delat
}
  }


/////////////////////////////////////// OSA X /////////////////////////////////
void homeX() {
 
  osaX.move((-1)*xMotorDir * ((delkaX * stoupaniX) + 100)); //delka x stoupani pro pocet kroku a 100 aby jel za hranice osy
  while (osaX.currentPosition() != osaX.targetPosition() && digitalRead(X_MIN_PIN) == logEndstopX) //beží dokud nedoběhne na konec osy (nikdy) nebo dokud se neobrátí stav endstopu
  {
    osaX.run();
  }
  osaX.stop();
  osaX.setCurrentPosition(0);
  osaX.setAcceleration(500);
  osaX.setMaxSpeed(200);
  osaX.move(xMotorDir * uvolneniStopu);
  osaX.runToPosition();
  osaX.setAcceleration(akcelerace);
  osaX.setMaxSpeed(rychlost);
  ishomeX = 1;
#ifdef diag
  Serial.println(F("Osa X home"));
#endif
}
void moveX(float vzdalenost) {
   if (ishomeX && ishomeY && ishomeZ) {       //zjištění homu
#ifdef diag
    Serial.println(F("osy jsou v homu"));
#endif
  }
  else {
    zapnutiMOT();
    homeY();
    homeZ();
    homeX();

  }
  
  vzdalenost = stoupaniX * vzdalenost;
  osaX.move(xMotorDir * vzdalenost);
  while (osaX.currentPosition() != osaX.targetPosition())
  {
    osaX.run();
  }
  if (osaX.targetPosition() / stoupaniX > delkaX) { //pokud chce jet za hranice osy
#ifdef diag
    Serial.println(F("Chyba: konec osy"));
#endif

    //zde ukoncit funkci
  } else {
    while (osaX.currentPosition() != osaX.targetPosition())
    {
      osaX.run();
    }
  }

}
void moveToX(float vzdalenost) {
   if (ishomeX && ishomeY && ishomeZ) {       //zjištění homu
#ifdef diag
    Serial.println(F("osy jsou v homu"));
#endif
  }
  else {
    zapnutiMOT();
    homeY();
    homeZ();
    homeX();

  }
  vzdalenost = stoupaniX * vzdalenost;
  osaX.moveTo(xMotorDir * vzdalenost);
  if (osaX.targetPosition() / stoupaniX > delkaX) { //pokud chce jet za hranice osy
#ifdef diag
    Serial.println(F("Chyba: konec osy"));
#endif

    //zde ukoncit funkci
  } else {
    while (osaX.currentPosition() != osaX.targetPosition())
    {
      osaX.run();
    }
  }

}

//////////////////////////////////////  OSA Y ///////////////////////////////////////
void homeY() {
  
  osaY.move((-1)*yMotorDir * ((delkaY * stoupaniY) + 100)); //delka y stoupani pro pocet kroku a 100 aby jel za hranice osy
  while (osaY.currentPosition() != osaY.targetPosition() && digitalRead(Y_MIN_PIN) == logEndstopY) //beží dokud nedoběhne na konec osy (nikdy) nebo dokud se neobrátí stav endstopu
  {
    osaY.run();
  }
  osaY.stop();
  osaY.setCurrentPosition(0);
  osaY.setAcceleration(500);
  osaY.setMaxSpeed(200);
  osaY.move(yMotorDir * uvolneniStopu);
  osaY.runToPosition();
  osaY.setAcceleration(akcelerace);
  osaY.setMaxSpeed(rychlost);
  ishomeY = 1;
#ifdef diag
  Serial.println(F("Osa Y home"));
#endif
}
void moveY(float vzdalenost) {
   if (ishomeX && ishomeY && ishomeZ) {       //zjištění homu
#ifdef diag
    Serial.println(F("osy jsou v homu"));
#endif
  }
  else {
    zapnutiMOT();
    homeY();
    homeZ();
    homeX();

  }
  vzdalenost = stoupaniY * vzdalenost;
  osaY.move(yMotorDir * vzdalenost);
  if (osaY.targetPosition() / stoupaniY > delkaY) { //pokud chce jet za hranice osy
#ifdef diag
    Serial.println(F("Chyba: konec osy"));
#endif

    //zde ukoncit funkci
  } else {
    while (osaY.currentPosition() != osaY.targetPosition())
    {
      osaY.run();
    }
  }

}
void moveToY(float vzdalenost) {
   if (ishomeX && ishomeY && ishomeZ) {       //zjištění homu
#ifdef diag
    Serial.println(F("osy jsou v homu"));
#endif
  }
  else {
    zapnutiMOT();
    homeY();
    homeZ();
    homeX();

  }
  vzdalenost = stoupaniY * vzdalenost;
  osaY.moveTo(yMotorDir * vzdalenost);
  if (osaY.targetPosition() / stoupaniY > delkaY) { //pokud chce jet za hranice osy
#ifdef diag
    Serial.println(F("Chyba: konec osy"));
#endif

    //zde ukoncit funkci
  } else {
    while (osaY.currentPosition() != osaY.targetPosition())
    {
      osaY.run();
    }
  }

}

///////////////////////////////////// OSA Z //////////////////////////////ú
void homeZ() {
   
  osaZ.move((-1)*zMotorDir * ((delkaZ * stoupaniZ) + 100)); //delka z stoupani pro pocet kroku a 100 aby jel za hranice osy
  while (osaZ.currentPosition() != osaZ.targetPosition() && digitalRead(Z_MIN_PIN) == logEndstopZ) //beží dokud nedoběhne na konec osy (nikdy) nebo dokud se neobrátí stav endstopu
  {
    osaZ.run();
  }
  osaZ.stop();
  osaZ.setCurrentPosition(0);
  osaZ.setAcceleration(500);
  osaZ.setMaxSpeed(200);
  osaZ.move(zMotorDir * uvolneniStopu);
  osaZ.runToPosition();
  osaZ.setAcceleration(akcelerace);
  osaZ.setMaxSpeed(rychlost*1.3); //zrychleni o 30% kvuli sroubu
  ishomeZ = 1;
#ifdef diag
  Serial.println(F("Osa Z home"));
#endif
}
void moveZ(float vzdalenost) {
   if (ishomeX && ishomeY && ishomeZ) {       //zjištění homu
#ifdef diag
    Serial.println(F("osy jsou v homu"));
#endif
  }
  else {
    zapnutiMOT();
    homeY();
    homeZ();
    homeX();

  }
  vzdalenost = stoupaniZ * vzdalenost;
  osaZ.move(zMotorDir * vzdalenost);
  if (osaZ.targetPosition() / stoupaniZ > delkaZ) { //pokud chce jet za hranice osy
#ifdef diag
    Serial.println(F("Chyba: konec osy"));
#endif

    //zde ukoncit funkci
  } else {
    while (osaZ.currentPosition() != osaZ.targetPosition())
    {
      osaZ.run();
    }
  }

}
void moveToZ(float vzdalenost) {
   if (ishomeX && ishomeY && ishomeZ) {       //zjištění homu
#ifdef diag
    Serial.println(F("osy jsou v homu"));
#endif
  }
  else {
    zapnutiMOT();
    homeY();
    homeZ();
    homeX();

  }
  vzdalenost = stoupaniZ * vzdalenost;
  osaZ.moveTo(zMotorDir * vzdalenost);
  if (osaZ.targetPosition() / stoupaniZ > delkaZ) { //pokud chce jet za hranice osy
#ifdef diag
    Serial.println(F("Chyba: konec osy"));
#endif

    //zde ukoncit funkci
  } else {
    while (osaZ.currentPosition() != osaZ.targetPosition())
    {
      osaZ.run();
    }
  }

}
