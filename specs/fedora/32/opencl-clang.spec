%global opencl_clang_commit 92f3f7f1a06f25fb13708f87c26b0fbf50924c96

Name:       intel-opencl-clang
Version:    10.0.11
Release:    1%{?dist}
Summary:    Intel(R) OpenCL(TM) Clang

License:    MIT
Source0: https://github.com/intel/opencl-clang/archive/%{opencl_clang_commit}/intel-opencl-clang.tar.gz

BuildRequires: cmake gcc-c++ make git clang-devel
BuildRequires: spirv-llvm-translator-devel >= 10.0.8
BuildRequires: llvm-devel
Requires: clang-libs
Requires: spirv-llvm-translator >= 10.0.8

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
 -DSPIRV_TRANSLATOR_DIR=%{_libdir}
%make_build
popd

%install
%make_install -C build

%files

%{_libdir}/libopencl-clang.so.10

%files devel

%{_libdir}/libopencl-clang.so
%{_includedir}/cclang/*

%doc

%changelog
* Fri Jun 05 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.11-1
- Update to 10.0.11 (v10.0.0-2)

* Wed May 20 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.8-1
- Rebuild with spirv-llvm-translator 10.0.8
- Update to 10.0.8

* Wed Apr 08 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.6-1
* Update to 10.0.6

* Tue Mar 10 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.4-1
- Rebuild with spirv-llvm-translator 10.0.4
- Add workaround to link with clang-cpp library

* Wed Feb 12 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.3-1
- Package 10.0.3

