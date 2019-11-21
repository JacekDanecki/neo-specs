This repository provides scripts to build and download packages for [Intel compute-runtime](https://github.com/intel/compute-runtime) and dependencies on
* [copr://jdanecki/intel-opencl](https://copr.fedorainfracloud.org/coprs/jdanecki/intel-opencl)
* [copr://jdanecki/intel-opencl-ci](https://copr.fedorainfracloud.org/coprs/jdanecki/intel-opencl-ci)
* [ppa:jdanecki/intel-opencl](https://launchpad.net/~jdanecki/+archive/ubuntu/intel-opencl)

Packages from [ppa:jdanecki/intel-opencl](https://launchpad.net/~jdanecki/+archive/ubuntu/intel-opencl) are copied to
 [ppa:intel-opencl/intel-opencl](https://launchpad.net/~intel-opencl/+archive/ubuntu/intel-opencl) when Neo weekly release is ready.


## Supported Linux operating systems

* Centos 7, 8
* Fedora 30, 31, rawhide
* Mageia 7
* OpenSUSE Leap 15.1, Tumbleweed
* Ubuntu 16.04, 18.04, 19.04, 19.10
 
## Outdated copr chroots

* RHEL 8 (beta)

## Branches

* **master** contains scripts based on weekly [Neo releases](https://github.com/intel/compute-runtime/releases)
* **launchpad** contains scripts to prepare packages on [ppa:jdanecki/intel-opencl](https://launchpad.net/~jdanecki/+archive/ubuntu/intel-opencl)
* **ci** contains scripts required by CI systems:
  * [Semaphore CI](https://semaphoreci.com/jacekdanecki/compute-runtime-2)
  * [Travis CI](https://travis-ci.org/intel/compute-runtime)
  * [Shippable](https://app.shippable.com/github/intel/compute-runtime)

## Source code repositories used to build packages

* intel-gmmlib (https://github.com/intel/gmmlib)
* intel-igc (https://github.com/intel/intel-graphics-compiler)
* intel-opencl-clang (https://github.com/intel/opencl-clang)
* intel-opencl (https://github.com/intel/compute-runtime)
* llvm-patches (https://github.com/intel/llvm-patches)
* SPIRV-LLVM-Translator (https://github.com/KhronosGroup/SPIRV-LLVM-Translator)
* llvm-project (https://github.com/llvm/llvm-project)
