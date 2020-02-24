%global opencl_clang_commit 0a5a9f67b56431ef7b9436d1af812df6dfb44975

Name:       intel-opencl-clang
Version:    10.0.3
Release:    1%{?dist}
Summary:    Intel(R) OpenCL(TM) Clang

License:    MIT
Source0: https://github.com/intel/opencl-clang/archive/%{opencl_clang_commit}/intel-opencl-clang.tar.gz

BuildRequires: cmake gcc-c++ make git clang-devel
BuildRequires: spirv-llvm-translator-devel
BuildRequires: llvm-devel
Requires: clang-libs
Requires: spirv-llvm-translator

%description
Common clang is a thin wrapper library around clang. Common clang has OpenCL-oriented API and is capable to compile OpenCL C kernels to SPIR-V modules.

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
/usr/include/cclang/common_clang.h

%doc

%changelog
* Wed Feb 12 2020 Jacek Danecki <jacek.danecki@intel.com> - 10.0.3-1
- Package 10.0.3

