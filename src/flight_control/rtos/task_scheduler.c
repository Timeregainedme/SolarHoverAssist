#include <FreeRTOS.h>
#include <task.h>
#include <stdio.h>

void flight_task(void *pvParameters) {
    while (1) {
        printf("Flight task running...\n");
        vTaskDelay(pdMS_TO_TICKS(1000));  // 延迟 1 秒
    }
}

int main() {
    xTaskCreate(flight_task, "Flight Task", 1000, NULL, 1, NULL);
    vTaskStartScheduler();
    return 0;
}
