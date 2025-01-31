---
layout: pw42-project

permalink: /:path/

project_title: Compile ITK for Android ARM64
category: Infrastructure

key_investigators:
- name: Attila Nagy
  affiliation: University of Szeged
  country: Hungary

- name: Attila Tanács
  affiliation: University of Szeged
  country: Hungary
---

# Project Description

<!-- Add a short paragraph describing the project. -->
To investigate if and how ITK (later VTK, and sometime, maybe, in the distant future, Slicer) can be compiled an run on a mobile phone. Especially interesting is Samung's DeX mode, with a desktop like experience.

## Objective

<!-- Describe here WHAT you would like to achieve (what you will have as end result). -->

1. Objective A. Set up a build environment
1. Objective B. See if and how ITK can be built
1. Objective C. Hopefully test it too

## Approach and Plan

<!-- Describe here HOW you would like to achieve the objectives stated above. -->

1. Review Android tools, cross-compilation options
1. Set up the environment

## Progress and Next Steps

<!-- Update this section as you make progress, describing of what you have ACTUALLY DONE.
     If there are specific steps that you could not complete then you can describe them here, too. -->

1. Environment setup done
1. Compilation done, at 100%! :)

After setting up the software and the environment variables, the build was done on a freshly installed Debian 12.
Only cmake was installed from a repo-

Several problems were encountered:

- ITK’s CMake configuration tries to determine whether libc++ (LLVM C++ standard library) is available when cross-compiling for Android, but the test fails due to the lack of a runtime execution environment. Since Android cross-compilation cannot execute tests on the build machine, we need to manually provide the expected results.
It is fixed by addig
	    -D_libcxx_run_result=0 \
      -D_libcxx_run_result__TRYRUN_OUTPUT="" \
to the configure line.

- ld complained about ZLIB, likely because the build system tried to use a different zlib, so we have to force ITK to use the Android NDK zlib.
Example (several similar others popped up too):
ld.lld: error: version script assignment of 'ZLIB_1.2.0' to symbol 'compressBound' failed: symbol not defined
It is fixed by:
-DITK_USE_SYSTEM_ZLIB=ON

- Android does not provide iconv, so it had to be built, as GDCM needs it.
After some play, it was easy, and it could be compilaed, and later linked into ITK by using the following ENV vars and configure line:
export ANDROID_NDK_HOME=/home/attila/Android/Sdk/ndk/28.0.12916984
export TOOLCHAIN=$ANDROID_NDK_HOME/toolchains/llvm/prebuilt/linux-x86_64
export TARGET=aarch64-linux-android
export API=21  # Adjust API level as needed
export AR=$TOOLCHAIN/bin/llvm-ar
export AS=$TOOLCHAIN/bin/llvm-as
export CC=$TOOLCHAIN/bin/$TARGET$API-clang
export CXX=$TOOLCHAIN/bin/$TARGET$API-clang++
export LD=$TOOLCHAIN/bin/ld
export RANLIB=$TOOLCHAIN/bin/llvm-ranlib
export STRIP=$TOOLCHAIN/bin/llvm-strip

./configure --host=$TARGET --prefix=$PWD/android-build --disable-static --enable-shared

The built iconv of course had to be set in the cmake configure stage:
  	  -DGDCM_USE_SYSTEM_ICONV=ON \
	    -DCMAKE_C_FLAGS:STRING="-I/home/attila/libiconv-1.18/android-build/include -Dfar=far_nifti" \
      -DCMAKE_CXX_FLAGS:STRING="-Dfar=far_nifti" \
      -DCMAKE_EXE_LINKER_FLAGS="-L/home/attila/libiconv-1.18/android-build/lib /home/attila/libiconv-1.18/android-build/lib/libiconv.so" \
      -DCMAKE_SHARED_LINKER_FLAGS="-L/home/attila/libiconv-1.18/android-build/lib /home/attila/libiconv-1.18/android-build/lib/libiconv.so"
      -DGDCM_ICONV_INCLUDE_DIR=/home/attila/libiconv-1.18/android-build/include


There was another problem:
On Android, far is sometimes defined as a macro (especially in <sys/types.h> or <math.h>) for compatibility with legacy 16-bit platforms.
This means that the compiler throws errors in:
```
/home/attila/ITK/Modules/ThirdParty/NIFTI/src/nifti/niftilib/nifti1_io.c:5022:20: error: expected identifier or '('
 5022 |         float *far = (float *)dataptr ; size_t jj,nj ;
      |                    ^
/home/attila/ITK/Modules/ThirdParty/NIFTI/src/nifti/niftilib/nifti1_io.c:5025:34: error: expected expression
 5025 |            if( !IS_GOOD_FLOAT(far[jj]) ){
      |                                  ^
/home/attila/ITK/Modules/ThirdParty/NIFTI/src/nifti/niftilib/nifti1_io.c:5026:18: error: expected expression
 5026 |               far[jj] = 0 ;
      |                  ^
/home/attila/ITK/Modules/ThirdParty/NIFTI/src/nifti/niftilib/nifti1_io.c:5034:21: error: expected identifier or '('
 5034 |         double *far = (double *)dataptr ; size_t jj,nj ;
      |                     ^
/home/attila/ITK/Modules/ThirdParty/NIFTI/src/nifti/niftilib/nifti1_io.c:5037:34: error: expected expression
 5037 |            if( !IS_GOOD_FLOAT(far[jj]) ){
      |                                  ^
/home/attila/ITK/Modules/ThirdParty/NIFTI/src/nifti/niftilib/nifti1_io.c:5038:18: error: expected expression
 5038 |               far[jj] = 0 ;
      |                  ^
```

This could be overcome by forcing CMake to override the far macro by adding this flag to the configure line:
-DCMAKE_C_FLAGS="-Dfar=far_nifti" \

So the final configure line was this:
```cmake
cmake  -DCMAKE_TOOLCHAIN_FILE=$ANDROID_HOME/ndk/28.0.12916984/build/cmake/android.toolchain.cmake \
      -S /home/attila/ITK \
	    -B /home/attila/ITK/itk-build \
	    -DANDROID_ABI=arm64-v8a \
      -DANDROID_PLATFORM=android-21 \
      -DCMAKE_BUILD_TYPE=Release \
      -DBUILD_SHARED_LIBS=ON \
      -DITK_BUILD_DEFAULT_MODULES=ON \
      -DITK_WRAP_PYTHON=OFF \
	    -DCMAKE_CROSSCOMPILING_EMULATOR="" \
	    -DHAVE_CLOCK_GETTIME_RUN=1 \
	    -DITK_USE_SYSTEM_ZLIB=ON \
	    -D_libcxx_run_result=0 \
      -D_libcxx_run_result__TRYRUN_OUTPUT="" \
	    -DGDCM_USE_SYSTEM_ICONV=ON \
  	  -DCMAKE_C_FLAGS:STRING="-I/home/attila/libiconv-1.18/android-build/include -Dfar=far_nifti" \
      -DCMAKE_CXX_FLAGS:STRING="-Dfar=far_nifti" \
      -DCMAKE_EXE_LINKER_FLAGS="-L/home/attila/libiconv-1.18/android-build/lib /home/attila/libiconv-1.18/android-build/lib/libiconv.so" \
      -DCMAKE_SHARED_LINKER_FLAGS="-L/home/attila/libiconv-1.18/android-build/lib /home/attila/libiconv-1.18/android-build/lib/libiconv.so"
      -DGDCM_ICONV_INCLUDE_DIR=/home/attila/libiconv-1.18/android-build/include
```

A few shortcomings:
- Python bindings were not built
- No deployment has yet been made to test it on device

# Illustrations

<!-- Add pictures and links to videos that demonstrate what has been accomplished.
![Description of picture](Example2.jpg)
![Some more images](Example2.jpg)
-->

# Background and References

This project relies on the "Builds of Slicer for ARM-based systems Mac and Linux" project [[https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/BuildsOfSlicerForArmBasedSystemsMacAndLinux/](https://projectweek.na-mic.org/PW42_2025_GranCanaria/Projects/BuildsOfSlicerForArmBasedSystemsMacAndLinux/)]
