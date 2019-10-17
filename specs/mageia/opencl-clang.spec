%global cclang_commit_id 41cad395859684b18e762ca4a2c713c2fa349622
%global spirv_llvm_commit_id 83298e3c9b124486c16d0fde54c764a6c5a2b554
%global package_version 8.0.72
%global package_release 1
%define debug_package %{nil}

Name:       intel-opencl-clang
Version:    %{package_version}
Release:    %{package_release}%{?dist}
Summary:    Intel(R) OpenCL(TM) Clang

Group:      System Environment/Libraries
License:    MIT
URL:        https://github.com/intel/opencl-clang
Source0:    %{url}/archive/%{cclang_commit_id}/%{name}-%{cclang_commit_id}.tar.gz
Source1:    https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/%{spirv_llvm_commit_id}/spirv-llvm-translator-%{spirv_llvm_commit_id}.tar.gz

BuildRequires: git cmake clang gcc-c++ make patch llvm-devel clang-devel pkg-config python2 dos2unix

%description
Common clang is a thin wrapper library around clang. Common clang has OpenCL-oriented API and is capable to compile OpenCL C kernels to SPIR-V modules.

%package        devel
Summary:        Development files Intel(R) OpenCL(TM) Clang
Requires:       %{name} = %{version}-%{release}

%description devel


%clean


%prep
%setup -n opencl-clang-%{cclang_commit_id}
cd ..
rm -rf SPIRV-LLVM-Translator-%{spirv_llvm_commit_id}
%setup -T -D -n SPIRV-LLVM-Translator-%{spirv_llvm_commit_id} -b 1
dos2unix ../opencl-clang-%{cclang_commit_id}/patches/spirv/0001-Update-LowerOpenCL-pass-to-handle-new-blocks-represn.patch
dos2unix ../opencl-clang-%{cclang_commit_id}/patches/spirv/0002-Translation-of-llvm.dbg.declare-in-case-the-local-va.patch
patch -p1 < ../opencl-clang-%{cclang_commit_id}/patches/spirv/0001-Update-LowerOpenCL-pass-to-handle-new-blocks-represn.patch
patch -p1 < ../opencl-clang-%{cclang_commit_id}/patches/spirv/0002-Translation-of-llvm.dbg.declare-in-case-the-local-va.patch
cd ..

%build
mkdir build
pushd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_POSITION_INDEPENDENT_CODE=ON -DCMAKE_BUILD_TYPE=Release
%make_build
%make_install
popd
cd ../opencl-clang-%{cclang_commit_id}
mkdir build
pushd build
cmake .. -DCOMMON_CLANG_LIBRARY_NAME=opencl-clang -DLLVMSPIRV_INCLUDED_IN_LLVM=OFF -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX='/usr' \
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

/usr/lib64/libopencl-clang.so.8

%files devel

/usr/lib64/libopencl-clang.so
/usr/include/cclang/common_clang.h
/usr/include/LLVMSPIRVLib/LLVMSPIRVLib.h
/usr/lib64/pkgconfig/LLVMSPIRVLib.pc
/usr/lib64/libLLVMSPIRVLib.a

%doc

%changelog
