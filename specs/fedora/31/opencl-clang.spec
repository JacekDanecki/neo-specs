%global cclang_commit_id 6f8c329bea44321aef1a1716dd206c1f7bed23cf
%global spirv_llvm_commit_id beaa8850f47d2b436917881c1de19f3427629b89
%global package_version 9.0.4
%global package_release 1

Name:       intel-opencl-clang
Version:    %{package_version}
Release:    %{package_release}%{?dist}
Summary:    Intel(R) OpenCL(TM) Clang

Group:      System Environment/Libraries
License:    MIT
URL:        https://github.com/intel/opencl-clang
Source0:    %{url}/archive/%{cclang_commit_id}/%{name}-%{cclang_commit_id}.tar.gz
Source1:    https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/%{spirv_llvm_commit_id}/spirv-llvm-translator-%{spirv_llvm_commit_id}.tar.gz

BuildRequires: cmake clang gcc-c++ make llvm-devel clang-devel pkg-config python2 git

%description
Common clang is a thin wrapper library around clang. Common clang has OpenCL-oriented API and is capable to compile OpenCL C kernels to SPIR-V modules.

%package        devel
Summary:        Development files Intel(R) OpenCL(TM) Clang
Requires:       %{name} = %{version}-%{release}

%description devel
Development package for opencl-clang

%clean

%prep
%setup -n opencl-clang-%{cclang_commit_id}
cd ..
rm -rf SPIRV-LLVM-Translator-%{spirv_llvm_commit_id}
%setup -T -D -n SPIRV-LLVM-Translator-%{spirv_llvm_commit_id} -b 1
cd ..

%build
mkdir build
pushd build
%cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_POSITION_INDEPENDENT_CODE=ON -DCMAKE_BUILD_TYPE=Release
%make_build
%make_install
popd
cd ../opencl-clang-%{cclang_commit_id}
mkdir build
pushd build
%cmake .. -DCOMMON_CLANG_LIBRARY_NAME=opencl-clang -DLLVMSPIRV_INCLUDED_IN_LLVM=OFF -DLLVM_NO_DEAD_STRIP=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX='/usr' \
 -DSPIRV_TRANSLATOR_DIR=${RPM_BUILD_ROOT}/usr
%make_build
popd

%install
export QA_SKIP_BUILD_ROOT=yes
pushd build
%{__make} install DESTDIR=%{?buildroot} INSTALL="%{__install} -p"
popd
pushd ../opencl-clang-%{cclang_commit_id}/build
%{__make} install DESTDIR=%{?buildroot} INSTALL="%{__install} -p"
popd

%files

/usr/lib64/libopencl-clang.so.*
/usr/lib64/libLLVMSPIRVLib.so.*

%files devel

/usr/lib64/libopencl-clang.so
/usr/include/cclang/common_clang.h
/usr/include/LLVMSPIRVLib/LLVMSPIRVLib.h
/usr/lib64/pkgconfig/LLVMSPIRVLib.pc
/usr/lib64/libLLVMSPIRVLib.so

%doc

%changelog
