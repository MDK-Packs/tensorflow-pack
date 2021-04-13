/* Copyright 2021 The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/

#ifndef TENSORFLOW_LITE_MICRO_EVTREC_PROFILER_EVTREC_PROFILER_H_
#define TENSORFLOW_LITE_MICRO_EVTREC_PROFILER_EVTREC_PROFILER_H_

#include "tensorflow/lite/micro/micro_profiler.h"

namespace tflite {

class EvtRecProfiler : public MicroProfiler {
  public:
    EvtRecProfiler();
    uint32_t BeginEvent(const char* tag);
    void EndEvent(uint32_t event_handle);
    int32_t GetTotalTicks() const;
    void Log() const;

  private:
    static constexpr int kMaxEvents = 200;

    int32_t start_ticks_[kMaxEvents];
    int32_t end_ticks_[kMaxEvents];
    int num_events_ = 0;

    TF_LITE_REMOVE_VIRTUAL_DELETE;
};

}

#endif // TENSORFLOW_LITE_MICRO_EVTREC_PROFILER_EVTREC_PROFILER_H_
