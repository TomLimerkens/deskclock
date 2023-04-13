// Include libraries
#include <Arduino_GFX_Library.h>

#define DISPLAY_DEV_KIT
#define WAVESHARE_RP2040_LCD_1_28
#define DF_GFX_SCK 10
#define DF_GFX_MOSI 11
#define DF_GFX_MISO 13
#define DF_GFX_CS 9
#define DF_GFX_DC 8
#define DF_GFX_RST 12
#define DF_GFX_BL 25
#define DF_GFX_SPI spi1



// global variables
int counter =0;




void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  counter = 0;
}

void loop() {
  // put your main code here, to run repeatedly:
  // int counter = 0;
  counter +=1;
  Serial.println(counter);
  delay(500);
  
}
