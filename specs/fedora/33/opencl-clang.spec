%global opencl_clang_commit 10.0.0-2

Name:       intel-opencl-clang
Version:    10.0.12
Release:    2%{?dist}
Summary:    Intel(R) OpenCL(TM) Clang

License:    MIT
URL: https://github.com/intel/opencl-clang
Source0: https://github.com/intel/opencl-clang/archive/v%{opencl_clang_commit}/intel-opencl-clang.tar.gz

BuildRequires: cmake gcc-c++ make git clang10-devel
BuildRequires: spirv-llvm-translator-devel = 10.0.12
BuildRequires: llvm10-devel
Requires: clang10-libs
Requires: spirv-llvm-translator = 10.0.12

%description
OpenCL clang is a thin wrapper library around clang. OpenCL clang has OpenCL-oriented API and is capable to compile OpenCL C kernels to SPIR-V modules.

%package        devel
Summary:        Development files Intel(R) OpenCL(TM) Clang
Requires:       %{name} = %{version}-%{release}

%description devel
Development package for opencl-clang

%prep
%autosetup -n opencl-clang-%{opencl_clang_commit}

%build
mkdir build
pushd build
%cmake .. -DLLVMSPIRV_INCLUDED_IN_LLVM=OFF -DLLVM_NO_DEAD_STRIP=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX='/usr' \
 -DSPIRV_TRANSLATOR_DIR=/usr/lib -DLLVM_DIR=/usr/lib64/llvm10/lib/cmake/llvm/
%cmake_build
popd

%install
cd build
%cmake_install

%files

%{_libdir}/libopencl-clang.so.10

%files devel

%{_libdir}/libopencl-clang.so
%{_includedir}/cclang/*

%doc

%changelog
* Wed Nov 04 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.12-2
- Rebuild 10.0.12

* Wed Jun 24 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.12-1
- Update to 10.0.12

* Tue Jun 23 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.11-1
- Update to 10.0.11

* Mon Jun 01 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.8-1
- Update to 10.0.8

* Thu Apr 09 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.6-1
- Update to 10.0.6

* Mon Mar 02 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.4-1
- Update to 10.0.4

* Mon Feb 17 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.3-1
- Package 10.0.3

* Wed Oct 30 2019 Jacek Danecki <jacek.danecki@intel.com> - 9.0.9-1
- Update to 9.0.9

