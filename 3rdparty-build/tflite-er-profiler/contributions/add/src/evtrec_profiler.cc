/* Copyright 2020 The TensorFlow Authors. All Rights Reserved.

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

#include "tensorflow/lite/micro/evtrec_profiler/evtrec_profiler.h"
#include <cstdint>
#include "tensorflow/lite/kernels/internal/compatibility.h"
#include "tensorflow/lite/micro/micro_error_reporter.h"
#include "tensorflow/lite/micro/micro_time.h"
#include "EventRecorder/Include/EventRecorder.h"

namespace tflite {
  EvtRecProfiler::EvtRecProfiler() {
    EventRecorderInitialize(EventRecordAll, 1);
  }

  uint32_t EvtRecProfiler::BeginEvent(const char* tag) {
    EventRecord2(1, (int32_t)num_events_, (int32_t)GetCurrentTimeTicks());

    return num_events_++;
  }

  void EvtRecProfiler::EndEvent(uint32_t event_handle) {
    TFLITE_DCHECK(event_handle < kMaxEvents);
    EventRecord2(1, (int32_t)event_handle, (int32_t)GetCurrentTimeTicks());
  }

  int32_t EvtRecProfiler::GetTotalTicks() const {
    int32_t ticks = 0;
    for (int i = 0; i < num_events_; ++i) {
      ticks += end_ticks_[i] - start_ticks_[i];
    }
    return ticks;
  }

  void EvtRecProfiler::Log() const {}
}  // namespace tflite
