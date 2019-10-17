%global major_version 1
%global minor_version 0
%global patch_version 2597
%global package_release 1
%global commit_id b3ed5e584dac45d560e6f68e5f6e84af8a661e6e

Name: intel-igc
Version: %{major_version}.%{minor_version}.%{patch_version}
Release: %{package_release}%{?dist}
Summary: Intel(R) Graphics Compiler for OpenCL(TM)

Group: System Environment/Libraries
License: MIT
URL: https://github.com/intel/intel-graphics-compiler
Source0: %{url}/archive/%{commit_id}/igc-%{major_version}.%{minor_version}.%{patch_version}.tar.gz

BuildRequires: cmake clang gcc-c++ make procps flex bison python2 llvm-devel clang-devel pkg-config
BuildRequires: intel-opencl-clang-devel

%description
Intel(R) Graphics Compiler for OpenCL(TM).

%package       core
Summary:       Intel(R) Graphics Compiler Core

%description   core

%package       opencl
Summary:       Intel(R) Graphics Compiler Frontend
Requires:      %{name}-core = %{version}-%{release}
Requires:      intel-opencl-clang >= 8.0.72

%description   opencl

%package       opencl-devel
Summary:       Intel(R) Graphics Compiler development package
Requires:      %{name}-opencl = %{version}-%{release}

%description   opencl-devel

%prep
%autosetup -p1 -n intel-graphics-compiler-%{commit_id}

%build
mkdir build
pushd build

cmake .. -Wno-dev -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr  \
 -DCOMMON_CLANG_LIBRARY_NAME=opencl-clang -DIGC_PREFERRED_LLVM_VERSION=8.0.0 -DIGC_PACKAGE_RELEASE=%{patch_version}
%make_build
popd

%install
cd build
%make_install
rm -fv $RPM_BUILD_ROOT/usr/bin/GenX_IR

%files core
%defattr(-,root,root)
/usr/lib64/libiga64.so.*
/usr/lib64/libigc.so.*
/usr/bin/iga64

%files opencl
%defattr(-,root,root)
/usr/lib64/libigdfcl.so.*

%files opencl-devel
%defattr(-,root,root)
/usr/include/igc/*
/usr/include/iga/*
/usr/include/visa/*
/usr/lib64/libiga64.so
/usr/lib64/libigc.so
/usr/lib64/libigdfcl.so
/usr/lib64/pkgconfig/*

%doc


%changelog

