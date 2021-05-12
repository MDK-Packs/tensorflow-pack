/*
* Copyright (c) 2019-2020 Arm Limited
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/

#include "timeout.h"
#include "device_cfg.h"
#include "systimer_armv8-m_drv.h"
#include "syscounter_armv8-m_cntrl_drv.h"
#include "platform_description.h"

#define MS_TO_TICK(ms)  ((ms) * (SystemCoreClock / 1000))

/* Systimer is configured over the 32-bit down-counting Timer view, so maximum
 * delay is defined by its bit width. */
#define MAX_DELAY_MS    (UINT32_MAX / \
                            (SystemCoreClock / 1000))

static uint32_t delay_in_tick;

bool timeout_init(struct timeout_t *timeout, uint32_t delay)
{
    struct systimer_armv8_m_dev_t *dev;

    if (!timeout || delay > MAX_DELAY_MS) {
        return false;
    }

    if (timeout->is_initialized) {
        return false;
    }

    syscounter_armv8_m_cntrl_init(&SYSCOUNTER_CNTRL_ARMV8_M_DEV);

    dev = &SYSTIMER0_ARMV8_M_DEV;
    systimer_armv8_m_init(dev);

    delay_in_tick =  MS_TO_TICK(delay);
    systimer_armv8_m_set_timer_value(dev, delay_in_tick);

    timeout->dev_ptr = (void *)dev;
    timeout->is_initialized = true;

    return true;
}

bool timeout_delay_is_elapsed(struct timeout_t *timeout)
{
    struct systimer_armv8_m_dev_t* dev;

    if (!timeout || !timeout->is_initialized) {
        return false;
    }

    dev = (struct systimer_armv8_m_dev_t*)timeout->dev_ptr;
    if (systimer_armv8_m_is_interrupt_asserted(dev)) {
        systimer_armv8_m_set_timer_value(dev, delay_in_tick);
        return true;
    }

    return false;
}
