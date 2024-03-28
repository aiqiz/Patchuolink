// Ratio TX file but it reads moisture sensor data from serial. 

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

#define TEST_PATTERN 0x2614D134438F47DE

#define TX_FREQ 100

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

// #define CALIBRATION 1
#define CAL_MODE HIGH_UP

void TX_Handler(){
  #ifdef CALIBRATION

  analogWrite(TX_PIN, CAL_MODE);

  #else

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
  #endif
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

typedef struct command_format{
  uint8_t start_of_packet; // 4 bits
  uint8_t source;
  uint8_t control;
  uint32_t data;
  uint8_t error_check;
  uint8_t end_of_packet;  // 4 bits
} command_format;

void loop() {
  noInterrupts();

  command_format current_data

  moist_value = analogRead(A0);
  current_packet.data = moist_value; 

  uint32_t tx_buf = tx_buffer;
  uint64_t data_packet = struct_to_packet(current_data); 
  if(!tx_mode) {
    tx_buffer = TEST_PATTERN;
    tx_mode = 1;
  }
  Serial.println(prev_write_val);
  interrupts();
  
}
