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
#define RX_FREQ (TX_FREQ * 10)

#define LED_PIN 13
#define RX_ENABLE false
#define TX_ENABLE true

void print_bin(uint32_t bin){
  for(int i = 0; i < 32; i++){
    Serial.print((bin & 0x80000000) >> 31);
    bin <<= 1;
  }
}

enum ANALOG bitstream_to_analogwrite(enum ANALOG prev, uint8_t next){
  if(next) {
    if(prev == HIGH_UP) {
      return HIGH_DOWN;
    } else {
      return HIGH_UP;
    }
  } else {
    if(prev == LOW_DOWN){
      return LOW_UP;
    } else {
      return LOW_DOWN;
    }
  } 
}

volatile uint64_t tx_buffer = 0;   // Buffer for TX to send data
volatile uint8_t tx_mode =    0;     // 1 if TX is transmitting, 0 otherwise

uint8_t prev_tx_mode =        0;
uint8_t tx_index =            0;
ANALOG prev_write_val =       OFF;
uint8_t send_bit =            0;


void TX_Handler(){

  if(tx_mode){
    if(!prev_tx_mode) {
      tx_index = 0;
    }

    send_bit = (tx_buffer & 0x8000000000000000) >> 63;
    tx_buffer <<= 1;
    ANALOG write_val = bitstream_to_analogwrite(prev_write_val, send_bit);
    prev_write_val = write_val;
    analogWrite(TX_PIN, write_val);

    tx_index++;
    if(tx_index == 64){
      tx_index = 0;
      tx_mode = 0;
    } 
  } else {
    analogWrite(TX_PIN, OFF);
  }

  prev_tx_mode = tx_mode;
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

  if(ITimer1.attachInterrupt(TX_FREQ, TX_Handler)) {
    Serial.print(F("Starting  ITimer1 OK, millis() = ")); Serial.println(millis());
  } else {
    Serial.println(F("Can't set ITimer1. Select another freq. or timer"));
  }
}

void loop() {
  noInterrupts();
  uint32_t tx_buf = tx_buffer;
  if(!tx_mode) {
    tx_buffer = 0xFFFF0000FFFF0000;
    tx_mode = 1;
  }
  Serial.println(prev_write_val);
  interrupts();
}
