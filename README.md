This repository provides files to build [Intel compute-runtime](https://github.com/intel/compute-runtime) and dependencies on 
- [copr://jdanecki/intel-opencl](https://copr.fedorainfracloud.org/coprs/jdanecki/intel-opencl) - master branch
- [copr://jdanecki/intel-opencl-ci](https://copr.fedorainfracloud.org/coprs/jdanecki/intel-opencl-ci) - ci branch
- [ppa:jdanecki/intel-opencl](https://launchpad.net/~jdanecki/+archive/ubuntu/intel-opencl)

## Supported Linux operating systems

- Centos 7, 8
- Fedora 30, 31, rawhide
- Mageia 7
- OpenSUSE Leap 15.1, Tumbleweed
- Ubuntu 16.04, 18.04, 19.04, 19.10
- 

## Outdated copr chroots

- RHEL 8 (beta)

## Branches

- master: scripts on this branch are based on weekly [Neo releases](https://github.com/intel/compute-runtime/releases)
- ci: scripts on this branch contain newer versions required by [Semaphore CI](https://semaphoreci.com/jacekdanecki/compute-runtime-2)

## Source code repositories used to build packages

- intel-gmmlib (https://github.com/intel/gmmlib)
- intel-igc (https://github.com/intel/intel-graphics-compiler)
- intel-opencl-clang (https://github.com/intel/opencl-clang)
- intel-opencl (https://github.com/intel/compute-runtime)
- llvm-patches (https://github.com/intel/llvm-patches)
- SPIRV-LLVM-Translator (https://github.com/KhronosGroup/SPIRV-LLVM-Translator)
- llvm-project (https://github.com/llvm/llvm-project)
