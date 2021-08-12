/*
 * Copyright (c) 2017-2019 Arm Limited
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

#ifndef __TIMEOUT_H__
#define __TIMEOUT_H__

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include "device_definition.h"

/* Structure to maintain elapsed time */
struct timeout_t {
    void *dev_ptr;
    bool is_initialized;
};

/**
 * \brief Initializes timout structure
 *
 * \param[in] timeout Pointer to the timeout structure
 * \param[in] delay   Delay in ms to check timeout against
 *
 * \return Returns true if the delay value was set,
 *         false otherwise
 */
bool timeout_init(struct timeout_t *timeout, uint32_t delay);

/**
 * \brief Checks if the given time has passed or not
 *
 * \param[in] timer Pointer to the timer structure
 *
 * \details This function compares the timestamp stored in the timeout structure
 *          and the current time. If the difference is more than the given delay,
 *          the current time is stored and will be used for the next comparison
 *
 * \return 1 if the given time has passed, 0 if not
 */
bool timeout_delay_is_elapsed(struct timeout_t *timeout);

/**
 * \brief Uninitializes timout structure and stops timer operation.
 *
 * \param[in] timeout Pointer to the timeout structure
 */
void timeout_uninit(struct timeout_t *timeout);

/**
 * \brief Waits the specified time in milliseconds.
 *
 * \param[in] ms Time to wait in milliseconds
 */
void wait_ms(uint32_t ms);

#ifdef __cplusplus
}
#endif
#endif /* __TIMEOUT_H__ */
