%global opencl_clang_commit c1b069759162e1d3caaaf1ab2cdc7a8db7e3de8b
%global spirv_llvm_translator_commit cc7eff18ad99019adb3730437ffd577116fc116b

Name:       intel-opencl-clang
Version:    9.0.13
Release:    1%{?dist}
Summary:    Intel(R) OpenCL(TM) Clang

License:    MIT
URL: https://github.com/intel/opencl-clang
Source0: https://github.com/intel/opencl-clang/archive/%{opencl_clang_commit}/intel-opencl-clang.tar.gz
Source1: https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/%{spirv_llvm_translator_commit}/spirv-llvm-translator.tar.gz

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
%{_includedir}/cclang/common_clang.h
%{_includedir}/LLVMSPIRVLib/*
%{_libdir}/pkgconfig/LLVMSPIRVLib.pc
%{_libdir}/libLLVMSPIRVLib.so

%doc

%changelog
* Tue Feb 18 2020 Jacek Danecki <jacek.danecki@intel.com> - 9.0.13-1
- Update to 9.0.13

* Wed Oct 30 2019 Jacek Danecki <jacek.danecki@intel.com> - 9.0.9-1
- Update to 9.0.9

