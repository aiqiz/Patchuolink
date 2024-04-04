enum ANALOG{
  OFF =        1*255/6, 
  LOW_DOWN =   2*255/6, 
  LOW_UP =     3*255/6, 
  HIGH_DOWN =  4*255/6, 
  HIGH_UP =    5*255/6
};

typedef struct command_format{
  uint8_t start_of_packet; // 4 bits
  uint8_t source;
  uint8_t control;
  uint32_t data;
  uint8_t error_check;
  uint8_t end_of_packet;  // 4 bits
} command_format;

#define USE_TIMER_1 true

#include "TimerInterrupt.h"

#define NODE_ID (uint8_t) (0x10)

#define RX_PIN 4
#define TX_PIN 3

#define TX_FREQ 1000//100
#define RX_FREQ (TX_FREQ * 100)

#define LED_PIN 13
#define RX_ENABLE false
#define TX_ENABLE true

void print_bin(uint32_t bin) {
  for (int i = 0; i < 32; i++) {
    Serial.print((bin & 0x80000000) >> 31);
    bin <<= 1;
  }
  Serial.println();
}

void print_bin(uint64_t bin) {
  for (int i = 0; i < 64; i++) {
    Serial.print((uint8_t)((bin & 0x8000000000000000) >> 63));
    bin <<= 1;
  }
  Serial.println();
}


uint64_t struct_to_packet(command_format s) {
  uint64_t packet;
  packet <<= 4;
  packet |= (uint64_t) (s.start_of_packet);
  packet <<= 8;
  packet |= (uint64_t) (s.source);
  packet <<= 8;
  packet |= (uint64_t) (s.control);
  packet <<= 32;
  packet |= (uint64_t) (s.data);
  packet <<= 8;
  packet |= (uint64_t) (s.error_check);
  packet <<= 4;
  packet |= (uint64_t) (s.end_of_packet);
  return packet;
}

int create_command(command_format *cmd, int value, int control){
  cmd->start_of_packet = 0xD;
  cmd->source = NODE_ID;
  cmd->control = control;
  cmd->data = value;
  int8_t err_chk = 0;
  for(int i = 0; i < 4; i++){
    err_chk += (int8_t) (value & 0x000000FF);
    value >>= 8;
  }
  cmd->error_check = -err_chk;
  cmd->end_of_packet = 0xB;

  return 0;
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
    digitalWrite(TX_PIN, send_bit);

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
    command_format s_cmd;
    int val = analogRead(A0);
    Serial.print("SENSOR DATA: ");
    Serial.println(val);


    create_command(&s_cmd, val, 0);
    uint64_t send_msg = struct_to_packet(s_cmd);
    Serial.print("FULL PACKET: ");
    print_bin(send_msg);
    Serial.print("SENSOR DATA AS BOOL: ");
    print_bin((uint32_t) val);

    tx_buffer = send_msg;
    tx_mode = 1;
  }
  // Serial.println(send_bit);
  interrupts();
}
