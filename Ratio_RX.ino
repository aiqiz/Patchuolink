enum ANALOG{
  OFF =        1*255/6, 
  LOW_DOWN =   2*255/6, 
  LOW_UP =     3*255/6, 
  HIGH_DOWN =  4*255/6, 
  HIGH_UP =    5*255/6
};

#define USE_TIMER_1 true

#include "TimerInterrupt.h"

#define RX_PIN 4
#define TX_PIN 3

#define TX_FREQ 100
#define RX_FREQ 10000

#define LED_PIN 13
#define RX_ENABLE false
#define TX_ENABLE true

void print_bin(uint32_t bin){
  for(int i = 0; i < 32; i++){
    Serial.print((bin & 0x80000000) >> 31);
    bin <<= 1;
  }
}

int prev;
volatile int ratio;
int val;
volatile bool ratio_ready;
int ones;
int zeros;

int update_ones;
int update_zeros;

void RX_Handler(){
  static int prev_val = 0;
  val = digitalRead(RX_PIN);

  if(val != prev_val){
    if(!prev_val) {
      ratio = ones * 100 / (ones +  zeros);
      update_ones = ones;
      update_zeros = zeros;

      ones = 0;
      zeros = 1;
      ratio_ready = true;
    }
  }

  if(val) {
    ones++;
  } else {
    zeros++;
  }
  prev_val = val;
}


void setup() {
  pinMode(TX_PIN, OUTPUT);
  pinMode(RX_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);

  // Serial Start and Debug
  Serial.begin(2000000);

  Serial.print(F("\nStarting TimerInterruptTest on "));
  Serial.println(BOARD_TYPE);
  Serial.println(TIMER_INTERRUPT_VERSION);
  Serial.print(F("CPU Frequency = ")); Serial.print(F_CPU / 1000000); Serial.println(F(" MHz"));

  ITimer1.init();

  if(ITimer1.attachInterrupt(RX_FREQ, RX_Handler)) {
    Serial.print(F("Starting  ITimer1 OK, millis() = ")); Serial.println(millis());
  } else {
    Serial.println(F("Can't set ITimer1. Select another freq. or timer"));
  }
}

int8_t ratio_to_bool(int ratio){
  if(ratio >= 0 && ratio < 20) {
    return 0;
  } else if(ratio >= 20 && ratio < 40) {
    return 1;
  } else if(ratio >= 40 && ratio < 60) {
    return 2;
  } else if (ratio >= 60 & ratio < 100) {
    return 3;
  } else {
    return -1;
  }
}


void loop() {
  
  noInterrupts();
  if(ratio_ready){
    int ratio_cpy = ratio;
    ratio_ready = false;
    interrupts();

    Serial.print("Scale_lower:");
    Serial.print(0);
    Serial.print(",");
    Serial.print("Scale_higher:");
    Serial.print(60);
    Serial.print(",");
    Serial.print("Num_ones:");
    Serial.print(update_ones);
    Serial.print(",");
    Serial.print("Num_zeros:");
    Serial.print(update_zeros);
    Serial.print(",");
    Serial.print("Ratio_Raw:");
    Serial.print(ratio_cpy);
    Serial.print(",");
    Serial.print("Ratio_Digital:");
    Serial.println(ratio_to_bool(ratio_cpy) * 30);
  }
  interrupts();
}
