// Copyright 2015 Open Source Robotics Foundation, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef RCL__VISIBILITY_CONTROL_H_
#define RCL__VISIBILITY_CONTROL_H_

#if __cplusplus
extern "C"
{
#endif

// This logic was borrowed (then namespaced) from the examples on the gcc wiki:
//     https://gcc.gnu.org/wiki/Visibility

#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define RCL_EXPORT __attribute__ ((dllexport))
    #define RCL_IMPORT __attribute__ ((dllimport))
  #else
    #define RCL_EXPORT __declspec(dllexport)
    #define RCL_IMPORT __declspec(dllimport)
  #endif
  #ifdef RCL_BUILDING_DLL
    #define RCL_PUBLIC RCL_EXPORT
  #else
    #define RCL_PUBLIC RCL_IMPORT
  #endif
  #define RCL_PUBLIC_TYPE RCL_PUBLIC
  #define RCL_LOCAL
#else
  #define RCL_EXPORT __attribute__ ((visibility("default")))
  #define RCL_IMPORT
  #if __GNUC__ >= 4
    #define RCL_PUBLIC __attribute__ ((visibility("default")))
    #define RCL_LOCAL  __attribute__ ((visibility("hidden")))
  #else
    #define RCL_PUBLIC
    #define RCL_LOCAL
  #endif
  #define RCL_PUBLIC_TYPE
#endif

#if __cplusplus
}
#endif

#endif  // RCL__VISIBILITY_CONTROL_H_
