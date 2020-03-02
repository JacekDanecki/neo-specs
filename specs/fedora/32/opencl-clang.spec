%global opencl_clang_commit 9.0.0
%global spirv_llvm_translator_commit 9.0.0-1

Name:       intel-opencl-clang
Version:    9.0.9
Release:    1%{?dist}
Summary:    Intel(R) OpenCL(TM) Clang

License:    MIT
URL: https://github.com/intel/opencl-clang
Source0: https://github.com/intel/opencl-clang/archive/%{opencl_clang_commit}/intel-opencl-clang.tar.gz
Patch0: https://raw.githubusercontent.com/JacekDanecki/neo-specs/master/specs/fedora/32/clang.patch

BuildRequires: cmake gcc-c++ make llvm-devel clang-devel pkg-config python3 git

%description
Common clang is a thin wrapper library around clang. Common clang has OpenCL-oriented API and is capable to compile OpenCL C kernels to SPIR-V modules.

%package        devel
Summary:        Development files Intel(R) OpenCL(TM) Clang
Requires:       %{name} = %{version}-%{release}

%description devel
Development package for opencl-clang

%prep
%setup -n opencl-clang-%{opencl_clang_commit}
cd ..
rm -rf SPIRV-LLVM-Translator-%{spirv_llvm_translator_commit}
%setup -T -D -n SPIRV-LLVM-Translator-%{spirv_llvm_translator_commit} -b 1
cd ..

%build
mkdir build
pushd build
%cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_POSITION_INDEPENDENT_CODE=ON -DCMAKE_BUILD_TYPE=Release
%make_build
%make_install
popd
cd ../opencl-clang-%{opencl_clang_commit}
mkdir build
pushd build
%cmake .. -DLLVMSPIRV_INCLUDED_IN_LLVM=OFF -DLLVM_NO_DEAD_STRIP=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX='/usr' \
 -DSPIRV_TRANSLATOR_DIR=%{buildroot}/usr
%make_build
popd

%install
export QA_SKIP_BUILD_ROOT=yes
pushd build
make install DESTDIR=%{buildroot}
popd
pushd ../opencl-clang-%{opencl_clang_commit}/build
make install DESTDIR=%{buildroot}
popd

%files

%{_libdir}/libopencl-clang.so.*
%{_libdir}/libLLVMSPIRVLib.so.*

%files devel

%{_libdir}/libopencl-clang.so
/usr/include/cclang/common_clang.h
/usr/include/LLVMSPIRVLib/*
%{_libdir}/pkgconfig/LLVMSPIRVLib.pc
%{_libdir}/libLLVMSPIRVLib.so

%doc

%changelog
* Wed Oct 30 2019 Jacek Danecki <jacek.danecki@intel.com> - 9.0.9-1
- Update to 9.0.9

