#include <px4_platform_common/module.h>
#include <px4_platform_common/log.h>

extern "C" __EXPORT int custom_flight_control_main(int argc, char *argv[]);

int custom_flight_control_main(int argc, char *argv[]) {
    PX4_INFO("Custom flight control initialized.");
    // 自定义飞控逻辑
    return 0;
}
