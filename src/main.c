#include "esp_event.h"
#include "esp_event_loop.h"
#include "esp_system.h"
#include "freertos/FreeRTOS.h"

void app_main(void) {

  // Array out of bounds example
  char a[10];
  a[10] = 0;

  // Division by zero example
  int b = 5 / 0;

  // List of all checks
  // https://sourceforge.net/p/cppcheck/wiki/ListOfChecks/
}
