enum ANALOG {
  OFF = 1 * 255 / 6,
  LOW_DOWN = 2 * 255 / 6,
  LOW_UP = 3 * 255 / 6,
  HIGH_DOWN = 4 * 255 / 6,
  HIGH_UP = 5 * 255 / 6
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

#define TEST_PATTERN 0x2614D134438F47DE
#define DEBUG_PRINT 1

void print_bin(uint32_t bin) {
  for (int i = 0; i < 32; i++) {
    Serial.print((bin & 0x80000000) >> 31);
    bin <<= 1;
  }
}

void print_bin(uint64_t bin) {
  for (int i = 0; i < 64; i++) {
    Serial.print((uint8_t)((bin & 0x8000000000000000) >> 63));
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

uint64_t input_buffer;
uint8_t prev_digital;


void RX_Handler() {
  static int prev_val = 0;
  val = digitalRead(RX_PIN);

  if (val != prev_val) {
    if (!prev_val) {
      ratio = ones * 100 / (ones + zeros);
      update_ones = ones;
      update_zeros = zeros;

      ones = 0;
      zeros = 1;
      ratio_ready = true;

      int digital_inter = ratio_to_bool(ratio);
      bool digital_read = 0;

      switch (digital_inter) {
        case LOW_DOWN: digital_read = false; break;
        case LOW_UP: digital_read = false; break;
        case HIGH_DOWN: digital_read = true; break;
        case HIGH_UP: digital_read = true; break;
      }

      if (reading == 1) {
        if (digital_inter != prev_digital) {
          input_buffer <<= 1;
          input_buffer |= digital_read;
          prev_digital = digital_inter;
        }
      }
    }
  }

  if (val) {
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
  Serial.print(F("CPU Frequency = "));
  Serial.print(F_CPU / 1000000);
  Serial.println(F(" MHz"));

  ITimer1.init();

  if (ITimer1.attachInterrupt(RX_FREQ, RX_Handler)) {
    Serial.print(F("Starting  ITimer1 OK, millis() = "));
    Serial.println(millis());
  } else {
    Serial.println(F("Can't set ITimer1. Select another freq. or timer"));
  }
}

ANALOG ratio_to_bool(int ratio) {
  if (ratio >= 55 && ratio < 70) {
    return LOW_DOWN;
  } else if (ratio >= 40 && ratio < 55) {
    return LOW_UP;
  } else if (ratio >= 30 && ratio < 40) {
    return HIGH_DOWN;
  } else if (ratio >= 10 & ratio < 30) {
    return HIGH_UP;
  } else {
    return OFF;
  }
}

uint8_t check_start = 1;
int reading = 0;  // 0 is to wait, 1 is to read


uint64_t struct_to_packet(command_format s) {
  uint64_t packet;
  packet |= s.start_of_packet;
  packet <<= 4;
  packet |= s.source;
  packet <<= 8;
  packet |= s.control;
  packet <<= 8;
  packet |= s.data;
  packet <<= 32;
  packet |= s.error_check;
  packet <<= 8;
  packet |= s.end_of_packet;
  packet <<= 4;
  return packet;
}


void packet_to_struct(uint64_t packet, command_packet *s) {
  (*s).end_of_packet = packet & 0x000000000000000F;
  packet >>= 4;
  (*s).error_check = packet & 0x00000000000000FF;
  packet >>= 8;
  (*s).data = packet & 0x00000000FFFFFFFF;
  packet >>= 32;
  (*s).control = packet & 0x00000000000000FF;
  packet >>= 8;
  (*s).source = packet & 0x00000000000000FF;
  packet >>= 8;
  (*s).start_of_packet = packet & 0x000000000000000F;
}


uint64_t async_input_buffer;

uint32_t loop_counter = 0;
void loop() {

  noInterrupts();
  if (ratio_ready) {
    int ratio_cpy = ratio;
    ratio_ready = false;
    // when 1101 is read while in the waiting mode, turn to reading mode and save the start packet indicator to raw_data
    if (reading == 0) {
      if (check_start == 1 && digital_read == 1) {
        check_start = 2;
      } else if (check_start == 2 && digital_read == 1) {
        check_start = 3;
      } else if (check_start == 3 && digital_read == 0) {
        check_start = 4;
      } else if (check_start == 4 && digital_read == 1) {
        reading = 1;
        check_start = 1;
        input_buffer = 0x000000000000000D;
        input_buffer <<= 4;

      } else {
        check_start = 1;
      }
    }
    interrupts();


    // if(input_buffer == TEST_PATTERN) {
    //   Serial.print(millis());
    //   Serial.print(":");
    //   Serial.println("TEST PATTERN RECIEVED");
    // }


#if (DEBUG_PRINT)
    Serial.print("Ratio_Raw:");
    Serial.print(ratio_cpy);
    Serial.print(",");
    Serial.print("Ratio_Digital:");
    Serial.print(ratio_to_bool(ratio_cpy) * 60 / 255);

    // if(!(loop_counter & 0x00000001F)){ //32: 1F, 64: 3F
    //   Serial.print(",");
    //   Serial.print("input_buffer:");
    //   print_bin(input_buffer);
    // }
    Serial.println();
#endif
  }
  interrupts();
  loop_counter++;
}
