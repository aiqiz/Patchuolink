/**
 * Integrated_TX.ino
 * @authors Kevin Caldwell, Rachel Yang
 * 
 * Arduino C++ file for integrating Sensors and 
 * Communication Networks.
 * 
 * Gathers data from the sensors, packages it into
 * command_format structures, translates it into
 * 64 bit messages and transmits it in serial 
 * through the TX_PIN. 
 * 
 * Uses the TimerInterrupt Library by Khoi Hoang 
 * to access precise timing using Timer1.

*/

/**
 * MessageFormat is a struct which contains all the 
 * Fields for the message. Used as an intermediary 
 * between raw data and the 64-bit message. 
*/
typedef struct MessageFormat{
  uint8_t start_of_packet; // 4 bits
  uint8_t source;
  uint8_t control;
  uint32_t data;
  uint8_t error_check;
  uint8_t end_of_packet;  // 4 bits
} MessageFormat;

// Define used by TimerInterrupt
#define USE_TIMER_1 true

#include "TimerInterrupt.h"

// Node ID is a number identifying each Node. Used
// in the Source field, and needs to be set for each
// Node
#define NODE_ID (uint8_t) (0x10)

// Pin assignment for TX/RX
#define RX_PIN 4
#define TX_PIN 3

// Frequencies for Transmission and receiving
// Wireless: RX frequency = 10 to 100 times TX Frequency
// Wired: RX frequency = TX frequency
#define TX_FREQ 100
#define RX_FREQ TX_FREQ


// Debug Function for Printing True Binary of 32-bit int
void print_bin(uint32_t bin) {
  for (int i = 0; i < 32; i++) {
    Serial.print((bin & 0x80000000) >> 31);
    bin <<= 1;
  }
  Serial.println();
}

// Debug Function for Printing True Binary of 64-bit int
void print_bin(uint64_t bin) {
  for (int i = 0; i < 64; i++) {
    Serial.print((uint8_t)((bin & 0x8000000000000000) >> 63));
    bin <<= 1;
  }
  Serial.println();
}

// Encodes a MessageFormat Struct into a 64-bit integer
uint64_t struct_to_packet(MessageFormat s) {
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

// Generates a MessageFormat instance for a value and control
int create_command(MessageFormat *cmd, int value, int control){
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


volatile uint64_t tx_buffer = 0;     // Buffer for TX to send data
volatile uint8_t tx_mode =    0;     // 1 if TX is transmitting, 0 otherwise

uint8_t tx_index =            0;     // Keeps track of the buffer index
bool prev_tx_mode =           0;     
bool send_bit =               0;     // Global send_bit

/**
 * TX_Handler is responsible for handling the code needed to run 
 * when a new bit needs to be sent. Everytime the TX_Handler is 
 * called, the Most Significant Bit is popped and written to the 
 * output.
*/
void TX_Handler(){

  if(tx_mode){
    if(!prev_tx_mode) {
      tx_index = 0;
    }

    // Pop the Most Significant Bit
    send_bit = (tx_buffer & 0x8000000000000000) >> 63;
    tx_buffer <<= 1;

    digitalWrite(TX_PIN, send_bit);
    
    // Index Handling
    tx_index++;
    if(tx_index == 64){
      tx_index = 0;
      tx_mode = 0;
    } 
  }

  prev_tx_mode = tx_mode;
}


void setup() {
  pinMode(TX_PIN, OUTPUT);

  // Serial Start and Debug
  Serial.begin(2000000);
  
  // TimerInterrupt Boilerplate code
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

MessageFormat s_cmd;

void loop() {

  // Remove chance of Overwriting common memory
  noInterrupts();

  // Wait till TX is not transmitting
  if(!tx_mode) {

    // Data Pipeline
    int val = analogRead(A0);
    create_command(&s_cmd, val, 0);
    uint64_t send_msg = struct_to_packet(s_cmd);
    
    // TX Transmit Initialization
    tx_buffer = send_msg;
    tx_mode = 1;

    // Debug Packet and Ground truth
    Serial.print("SENSOR DATA: ");
    Serial.println(val);
    Serial.print("FULL PACKET: ");
    print_bin(send_msg);
    Serial.print("SENSOR DATA AS BINARY: ");
    print_bin((uint32_t) val);

  }
  interrupts();
  // Configurable Delay for transmit delay
  delay(1000);
}
