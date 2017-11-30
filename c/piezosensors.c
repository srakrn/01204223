#include <avr/io.h>
#include "piezosensors.h"

void init_peripheral()
{
  DDRC &= ~( (1<<PC0) | (1<<PC1) );
}

void set_led(uint8_t pin, uint8_t state)
{
  if (state)
    PORTC |= (1<<pin);
  else
    PORTC &= ~(1<<pin);
}

void set_led_value(uint8_t value)
{
  PORTC &= ~(0b00000111);
  PORTC |= (value & 0b00000111);
}

uint16_t analogRead(uint8_t channel)
{
    ADMUX = (0<<REFS1)|(1<<REFS0) // ระบุให้ใช้ VCC เป็นแรงดันอ้างอิง (Vref) และ
          | (0<<ADLAR)            // บันทึกผลลัพธ์ชิดขวาในคู่รีจีสเตอร์ ADCH/ADCL
          | (channel & 0b1111);   // ตั้งค่า MUX เป็นค่า channel

    ADCSRA = (1<<ADEN)            // เปิดวงจร ADC
           | (1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0) // ใช้ความเร็ว 1/128 ของคล็อกระบบ
           | (1<<ADSC);           // สั่งวงจร ADC ให้เริ่มต้นการแปลง

    while ((ADCSRA & (1<<ADSC)))  // รอจนบิต ADSC กลายเป็น 0 ซึ่งหมายถึงการแปลงเสร็จสิ้น
       ;

    return ADCL + ADCH*256;  // ผลลัพธ์ถูกเก็บอยู่ในรีจีสเตอร์ ADCL และ ADCH
}

