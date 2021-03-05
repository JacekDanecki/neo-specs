This repository provides scripts to build and download packages for [Intel compute-runtime](https://github.com/intel/compute-runtime) and dependencies on
* [copr://jdanecki/intel-opencl](https://copr.fedorainfracloud.org/coprs/jdanecki/intel-opencl)
* [copr://jdanecki/intel-opencl-ci](https://copr.fedorainfracloud.org/coprs/jdanecki/intel-opencl-ci)
* [ppa:jdanecki/intel-opencl](https://launchpad.net/~jdanecki/+archive/ubuntu/intel-opencl)
* [ppa:ocl-dev/intel-opencl](https://launchpad.net/~ocl-dev/+archive/ubuntu/intel-opencl)

Packages from [ppa:jdanecki/intel-opencl](https://launchpad.net/~jdanecki/+archive/ubuntu/intel-opencl) are copied to
 [ppa:intel-opencl/intel-opencl](https://launchpad.net/~intel-opencl/+archive/ubuntu/intel-opencl) when Neo weekly release is ready.


## Supported Linux operating systems

* Centos 7, 8, Stream
* Fedora 32, 33, 34, rawhide
* Mageia 7, 8, cauldron
* OpenSUSE Leap 15.2, Tumbleweed
* Ubuntu 18.04, 20.04
 
## Branches

* **master** contains scripts to build packages on [copr://jdanecki/intel-opencl](https://copr.fedorainfracloud.org/coprs/jdanecki/intel-opencl)
* **launchpad** contains scripts to prepare packages on [ppa:jdanecki/intel-opencl](https://launchpad.net/~jdanecki/+archive/ubuntu/intel-opencl)
* **ci** contains scripts to build packages on [ppa:ocl-dev/intel-opencl](https://launchpad.net/~ocl-dev/+archive/ubuntu/intel-opencl) and
 [copr://jdanecki/intel-opencl-ci](https://copr.fedorainfracloud.org/coprs/jdanecki/intel-opencl-ci) 
 
**master** and **launchpad** branches prepare packages for weekly [Neo releases](https://github.com/intel/compute-runtime/releases)

**ci** branch prepares newer packages required by CI systems:
  * [Semaphore CI](https://semaphoreci.com/jacekdanecki/compute-runtime-2)
  * [Travis CI](https://travis-ci.org/intel/compute-runtime)

## Downloading built packages

In **builds** directory there are scripts to download packages prepared for specific Linux distribution. These scripts use different repositories on different branches.

Branch | rpm repository | deb repository 
------ | -------------- | -------------- 
master | [copr://jdanecki/intel-opencl](https://copr.fedorainfracloud.org/coprs/jdanecki/intel-opencl) | [ppa:intel-opencl/intel-opencl](https://launchpad.net/~intel-opencl/+archive/ubuntu/intel-opencl) 
launchpad | N/A | [ppa:jdanecki/intel-opencl](https://launchpad.net/~jdanecki/+archive/ubuntu/intel-opencl)
ci |  [copr://jdanecki/intel-opencl-ci](https://copr.fedorainfracloud.org/coprs/jdanecki/intel-opencl-ci) |  [ppa:ocl-dev/intel-opencl](https://launchpad.net/~ocl-dev/+archive/ubuntu/intel-opencl)

## Source code repositories used to build packages

* [intel-gmmlib](https://github.com/intel/gmmlib)
* [intel-igc](https://github.com/intel/intel-graphics-compiler)
* [intel-opencl-clang](https://github.com/intel/opencl-clang)
* [intel-opencl](https://github.com/intel/compute-runtime)
* [llvm-patches](https://github.com/intel/llvm-patches)
* [SPIRV-LLVM-Translator](https://github.com/KhronosGroup/SPIRV-LLVM-Translator)
* [llvm-project](https://github.com/llvm/llvm-project)
* [Level Zero Loader](https://github.com/oneapi-src/level-zero)
