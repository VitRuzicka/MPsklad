//2020 copyright 
//Vít Růžička
//Pavel Hrstka
/*
                 regál


+----------------+---------------+----------------+----------------+--------------+
|                |               |                |                |              |
|                |               |                |                |              |
|                |               |                |                |              |
|        9       |       8       |        7       |        6       |      5       |
|                |               |                |                |              |
|                |               |                |                |              |
|                |               |                |                |              |
+---------------------------------------------------------------------------------+
|                |               |                |                |              |
|                |               |                |                |              |
|                |               |                |                |              |
|       4        |       3       |       2        |       1        |       0      |
|                |               |                |                |              |
|                |               |                |                |              |
|                |               |                |                |              |
+----------------+---------------+----------------+----------------+--------------+
   
*/

#include <AccelStepper.h>

//globalni promenne
#define akcelerace 1000  //výchozí akcelerace a rychlost pro celý systém
#define rychlost 800
#define uvolneniStopu 30 ///vzdálenost , kterou ujede aby neležel na endstopu
#define diag             //vypisuje diagnosticke zpravy do serioveho monitoru


#define delkaX 1000  //nastaveni delky osy v mm
#define delkaY 190
#define delkaZ 150

#define stoupaniX 80   //mm na milimetr
#define stoupaniY 80   //6400 by melo odpovidat T8x8 trapezu (na 200 krokách 400 kroku/mm, na 3200 krocich 6400...
#define stoupaniZ 400    //taky remen

#define logEndstopX true //obrácení smyslu endstopu
#define logEndstopY true 
#define logEndstopZ true 

int poziceX[] = {};  //10 pozic + dvě pro nakládání a skládání
int poziceY[] = {};  //hloubka skladu, naložení skladu, 
int poziceZ[] = {};  //10 pozic


byte ishomeX = false; //bez toho neví kde je
byte ishomeY = false;
byte ishomeZ = false;

byte xMotorDir = -1;
byte yMotorDir = -1; //pro opačný směr nahraďte za -1
byte zMotorDir = 1;

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


AccelStepper osaX(1, X_STEP_PIN,X_DIR_PIN);
AccelStepper osaY(1, Y_STEP_PIN,Y_DIR_PIN);
AccelStepper osaZ(1, Z_STEP_PIN,Z_DIR_PIN);

////////  KOMUNIKACE
#define MAX_BUF 64  //maximální velikost bufferu pro přijímání dat
int data;           //pocet dat v bufferu
char buffer[MAX_BUF];





void setup(){
//disable piny
osaX.setEnablePin(X_ENABLE_PIN);
osaY.setEnablePin(Y_ENABLE_PIN);
osaZ.setEnablePin(Z_ENABLE_PIN);  

//rychlosti
osaX.setMaxSpeed(rychlost);
osaY.setMaxSpeed(rychlost);
osaZ.setMaxSpeed(rychlost); 
 
//akcelerace
osaX.setAcceleration(akcelerace);
osaY.setAcceleration(akcelerace);
osaZ.setAcceleration(akcelerace);  

pinMode(X_MIN_PIN, INPUT); //zvážit použítí INPUT_PULLUP, záleží na typu endstopu
pinMode(Y_MIN_PIN, INPUT);
pinMode(Z_MIN_PIN, INPUT);
Serial.begin(115200);
data = 0;
}





void loop(){
 homeY();
 homeZ();
 homeX();
 
 delay(5000);


if(Serial.available() > 0){
  char c =  Serial.read();

  if(data < MAX_BUF){ //overeni jestli se data vejdou do bufferu
    buffer[data++]=c;    //pridani dat do bufferu na dalsi pozici
  }
  if(c == '\n'){
    Serial.print(F("\r\n"));   //return - může být nahrazeno za OK, když bude spolupracovat python
    buffer[data]=0;             //string v bufferu musí končit nulovým charakterem
    zpracovaniPrikazu();        //ehm vytvorit
  }
}
  
}








/////////////// OBECNÉ FUNKCE
float ziskejCislo(char pismeno,float hdn) {   //kdyz je po argumentu pismeno nejake cislo, vrátí ho, když ne, vrátí hodnotu hdn
  char *ptr=buffer;  // zacne na zacatku bufferu
  while((long)ptr > 1 && (*ptr) && (long)ptr < (long)buffer+data) {  //dojdi na konec
    if(*ptr==pismeno) {  // pokud narazis na pismeno vrat hodnotu po nem
      return atof(ptr+1);  // prevede nasledujici znaky na float
    }
    ptr=strchr(ptr,' ')+1;  //preskoci mezeru
  }
  return hdn;  //konec, vrati vychozi hodnotu
}

void zpracovaniPrikazu(){
  int gcode = ziskejCislo('G', -1);  //získá gcode
  switch(gcode){                     //porovná gcode s možnými případy
      case 0:
      //absolutní pohyb --napsat
      case 1:
      //relativní pohyb
      case 2:
      //pohyb do konkrétního políčka
      case 28:
      //home 
      case 18:
      //vypnutí proudu do motorů (změna oproti M18)
      default:
      break;;
    
  }
}

void vypnutiMOT(){
  osaX.enableOutputs();
  osaY.enableOutputs();
  osaZ.enableOutputs();
}
void zapnutiMOT(){
  osaX.disableOutputs();
  osaY.disableOutputs();
  osaZ.disableOutputs();
}



/////////////////////////////////////// OSA X /////////////////////////////////
void homeX(){
  osaX.disableOutputs();  //zapnutí motoru
  osaX.move(xMotorDir*((delkaX*stoupaniX) + 100)); //delka x stoupani pro pocet kroku a 100 aby jel za hranice osy
  while(osaX.currentPosition() != osaX.targetPosition() && digitalRead(X_MIN_PIN) == logEndstopX)  //beží dokud nedoběhne na konec osy (nikdy) nebo dokud se neobrátí stav endstopu
  {osaX.run();}
  osaX.stop();
  osaX.setCurrentPosition(0);
  osaX.setAcceleration(100);
  osaX.setMaxSpeed(100);
  osaX.move(uvolneniStopu);
  osaX.runToPosition();
  osaX.setAcceleration(akcelerace);
  osaX.setMaxSpeed(rychlost);
  ishomeX = 1;
  #ifdef diag
  Serial.println(F("Osa X home"));
  #endif
}
void moveX(float vzdalenost){
  vzdalenost = stoupaniX*vzdalenost;
  osaX.move(xMotorDir*vzdalenost);
  if(osaX.targetPosition() > delkaX){ //pokud chce jet za hranice osy
  #ifdef diag
  Serial.println(F("Chyba: konec osy"));
  #endif

  //zde ukoncit funkci
  }else{
  while(osaX.currentPosition() != osaX.targetPosition())
  {osaX.run();}
  }
   
}
void moveToX(float vzdalenost){
    vzdalenost = stoupaniX*vzdalenost;
  osaX.moveTo(xMotorDir*vzdalenost);
  if(osaX.targetPosition() > delkaX){ //pokud chce jet za hranice osy
  #ifdef diag
  Serial.println(F("Chyba: konec osy"));
  #endif

  //zde ukoncit funkci
  }else{
  while(osaX.currentPosition() != osaX.targetPosition())
  {osaX.run();}
  }
   
}

//////////////////////////////////////  OSA Y ///////////////////////////////////////
void homeY(){
  osaY.disableOutputs();  //zapnutí motoru
  osaY.move(yMotorDir*((delkaY*stoupaniY) + 100)); //delka y stoupani pro pocet kroku a 100 aby jel za hranice osy
  while(osaY.currentPosition() != osaY.targetPosition() && digitalRead(Y_MIN_PIN) == logEndstopY)  //beží dokud nedoběhne na konec osy (nikdy) nebo dokud se neobrátí stav endstopu
  {osaY.run();}
  osaY.stop();
  osaY.setCurrentPosition(0);
  osaY.setAcceleration(100);
  osaY.setMaxSpeed(100);
  osaY.move(uvolneniStopu);
  osaY.runToPosition();
  osaY.setAcceleration(akcelerace);
  osaY.setMaxSpeed(rychlost);
  ishomeY = 1;
  #ifdef diag
  Serial.println(F("Osa Y home"));
  #endif
}
void moveY(float vzdalenost){
  vzdalenost = stoupaniY*vzdalenost;
  osaY.move(yMotorDir*vzdalenost);
  if(osaY.targetPosition() > delkaY){ //pokud chce jet za hranice osy
  #ifdef diag
  Serial.println(F("Chyba: konec osy"));
  #endif

  //zde ukoncit funkci
  }else{
  while(osaY.currentPosition() != osaY.targetPosition())
  {osaY.run();}
  }
   
}
void moveToY(float vzdalenost){
    vzdalenost = stoupaniY*vzdalenost;
  osaY.moveTo(yMotorDir*vzdalenost);
  if(osaY.targetPosition() > delkaY){ //pokud chce jet za hranice osy
  #ifdef diag
  Serial.println(F("Chyba: konec osy"));
  #endif

  //zde ukoncit funkci
  }else{
  while(osaY.currentPosition() != osaY.targetPosition())
  {osaY.run();}
  }
   
}

///////////////////////////////////// OSA Z //////////////////////////////ú
void homeZ(){
  osaZ.disableOutputs();  //zapnutí motoru
  osaZ.move(zMotorDir*((delkaZ*stoupaniZ) + 100)); //delka z stoupani pro pocet kroku a 100 aby jel za hranice osy
  while(osaZ.currentPosition() != osaZ.targetPosition() && digitalRead(Z_MIN_PIN) == logEndstopZ)  //beží dokud nedoběhne na konec osy (nikdy) nebo dokud se neobrátí stav endstopu
  {osaZ.run();}
  osaZ.stop();
  osaZ.setCurrentPosition(0);
  osaZ.setAcceleration(100);
  osaZ.setMaxSpeed(100);
  osaZ.move(uvolneniStopu);
  osaZ.runToPosition();
  osaZ.setAcceleration(akcelerace);
  osaZ.setMaxSpeed(rychlost);
  ishomeZ = 1;
  #ifdef diag
  Serial.println(F("Osa Z home"));
  #endif
}
void moveZ(float vzdalenost){
  vzdalenost = stoupaniZ*vzdalenost;
  osaZ.move(zMotorDir*vzdalenost);
  if(osaZ.targetPosition() > delkaZ){ //pokud chce jet za hranice osy
  #ifdef diag
  Serial.println(F("Chyba: konec osy"));
  #endif

  //zde ukoncit funkci
  }else{
  while(osaZ.currentPosition() != osaZ.targetPosition())
  {osaZ.run();}
  }
   
}
void moveToZ(float vzdalenost){
    vzdalenost = stoupaniZ*vzdalenost;
  osaZ.moveTo(zMotorDir*vzdalenost);
  if(osaZ.targetPosition() > delkaZ){ //pokud chce jet za hranice osy
  #ifdef diag
  Serial.println(F("Chyba: konec osy"));
  #endif

  //zde ukoncit funkci
  }else{
  while(osaZ.currentPosition() != osaZ.targetPosition())
  {osaZ.run();}
  }
   
}
