//2020 copyright 
//Vít Růžička
//Pavel Hrstka
/*
        *        **                 *                                      
        *         *                 *                                      
        *         *                 *                                      
 ****   *   *     *     ****    *** *        * ***   *    *   ****    **** 
*    *  *  *      *         *  *   **        **   *  *    *  *    *  *    *
 **     ***       *     *****  *    *        *    *  *    *  *       *    *
   **   *  *      *    *    *  *    *        **   *  *   **  *       *    *
*    *  *   *     *    *   **  *   **        * ***    *** *  *    *  *    *
 ****   *    *  *****   *** *   *** *        *            *   ****    **** 
                                             *       *    *                
                                             *        ****    
*/

#include <AccelStepper.h>

//globalni promenne
#define akcelerace 1000  //výchozí akcelerace a rychlost pro celý systém
#define rychlost 1000
#define uvolneniStopu 50 ///vzdálenost , kterou ujede aby neležel na endstopu
#define diag             //vypisuje diagnosticke zpravy do serioveho monitoru


#define delkaX 1000  //nastaveni delky osy v mm
#define delkaY 300
#define delkaZ 150

#define stoupaniX 1280   //mm na milimetr
#define stoupaniY 6400   //6400 by melo odpovidat T8x8 trapezu (na 200 krokách 400 kroku/mm, na 3200 krocich 6400...
#define stoupaniZ 1280    //taky remen

#define logEndstopX true //obrácení smyslu endstopu
#define logEndstopY true 
#define logEndstopZ true 




byte ishomeX = false; //bez toho neví kde je
byte ishomeY = false;
byte ishomeZ = false;

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
}

void loop(){
 homeX();
 delay(10000); 
}



void homeX(){
  osaX.disableOutputs();  //zapnutí motoru
  osaX.move(((delkaX*stoupaniX) + 100)); // -1 pro opacny smer, delka x stoupani pro pocet kroku a 100 aby jel za hranice osy
  while(osaX.currentPosition() != osaX.targetPosition() && digitalRead(X_MIN_PIN) == logEndstopX)  //beží dokud nedoběhne na konec osy (nikdy) nebo dokud se neobrátí stav endstopu
  {osaX.run();}
  osaX.stop();
  osaX.setCurrentPosition(0);
  osaX.move(uvolneniStopu);
  osaX.runToPosition();
  ishomeX = 1;
  #ifdef diag
  Serial.println(F("Osa X home"));
  #endif
}
void moveX(float vzdalenost){
  vzdalenost = stoupaniX*vzdalenost;
  osaX.move(vzdalenost);
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
  osaX.moveTo(vzdalenost);
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
void vypnutiMOT(){
  osaX.enableOutputs();
  osaY.enableOutputs();
  osaZ.enableOutputs();
}
