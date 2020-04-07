%global llvm_commit llvmorg-9.0.0
%global opencl_clang_commit 6c384160d03b7b8eb9c0a5e5eff265aa2b0084fd
%global spirv_llvm_translator_commit 9.0.1-1
%global llvm_patches_commit 1c93162ab33af968c22fe1cbfb12ea87f5a25bfa
%global igc_commit 3605a569ac938ef2cb50ac69e30f8619cd44ceb3
%global patch_version 3586

Name: intel-igc
Version: 1.0.3586
Release: 1%{?dist}
Summary: Intel(R) Graphics Compiler for OpenCL(TM)

Group: System Environment/Libraries
License: MIT
URL: https://github.com/intel/intel-graphics-compiler
Source0: %{url}/archive/%{igc_commit}/igc-%{version}.tar.gz
Source1: https://github.com/intel/opencl-clang/archive/%{opencl_clang_commit}/intel-opencl-clang.tar.gz
Source2: https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/v%{spirv_llvm_translator_commit}/spirv-llvm-translator.tar.gz
Source3: https://github.com/llvm/llvm-project/archive/%{llvm_commit}/llvm-project.tar.gz
Source4: https://github.com/intel/llvm-patches/archive/%{llvm_patches_commit}/llvm-patches.tar.gz

BuildRequires: centos-release-scl epel-release
BuildRequires: devtoolset-7-gcc-c++ cmake3
BuildRequires: git make patch pkgconfig python3 bison flex
BuildRequires: flex >= 2.6.1

%description
Intel(R) Graphics Compiler for OpenCL(TM).

%package       core
Summary:       Intel(R) Graphics Compiler Core

%description   core

%package       opencl
Summary:       Intel(R) Graphics Compiler Frontend
Requires:      %{name}-core = %{version}-%{release}

%description   opencl

%package       opencl-devel
Summary:       Intel(R) Graphics Compiler development package
Requires:      %{name}-opencl = %{version}-%{release}

%description   opencl-devel

%prep

mkdir llvm-project
tar xzf $RPM_SOURCE_DIR/llvm-project.tar.gz -C llvm-project --strip-components=1
mv llvm-project/clang llvm-project/llvm/tools/

pushd llvm-project/llvm/projects
mkdir opencl-clang llvm-spirv
tar xzf $RPM_SOURCE_DIR/intel-opencl-clang.tar.gz -C opencl-clang --strip-components=1
tar xzf $RPM_SOURCE_DIR/spirv-llvm-translator.tar.gz -C llvm-spirv --strip-components=1
popd

mkdir igc
tar xzf $RPM_SOURCE_DIR/igc-%{version}.tar.gz -C igc --strip-components=1

mkdir llvm_patches
tar xzf $RPM_SOURCE_DIR/llvm-patches.tar.gz -C llvm_patches --strip-components=1

%build
mkdir build

pushd build
scl enable devtoolset-7 "cmake3 ../igc -Wno-dev -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr \
 -DCOMMON_CLANG_LIBRARY_NAME=opencl-clang -DIGC_PACKAGE_RELEASE=%{patch_version}"
scl enable devtoolset-7 "make -j `nproc`"
popd

%install
cd build
%make_install

rm -fv $RPM_BUILD_ROOT/usr/bin/GenX_IR
rm -fv $RPM_BUILD_ROOT/usr/bin/clang-9
rm -fv $RPM_BUILD_ROOT/usr/include/opencl-c.h
rm -fv $RPM_BUILD_ROOT/usr/include/opencl-c-base.h
chmod +x $RPM_BUILD_ROOT/usr/lib64/libopencl-clang.so.9

%files core
%{_libdir}/libiga64.so.*
%{_libdir}/libigc.so.*
%{_bindir}/iga64

%files opencl
%{_libdir}/libigdfcl.so.*
%{_libdir}/libopencl-clang.so.*

%files opencl-devel
%{_includedir}/igc/*
%{_includedir}/iga/*
%{_includedir}/visa/*
%{_libdir}/libiga64.so
%{_libdir}/libigc.so
%{_libdir}/libigdfcl.so
%{_libdir}/pkgconfig/*

%doc

%changelog
* Fri Mar 27 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3586-1
- Update to 1.0.3586

* Fri Mar 20 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3529-1
- Update to 1.0.3529

* Fri Mar 13 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3471-1
- Update to 1.0.3471

* Fri Mar 06 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3445-1
- Update to 1.0.3445

* Fri Feb 28 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3390-1
- Update to 1.0.3390

* Fri Feb 21 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3342-1
- Update to 1.0.3342

* Fri Feb 14 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3289-1
- Update to 1.0.3289

* Fri Jan 24 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3151-1
- Update to 1.0.3151

* Fri Dec 20 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3041-1
- Update to 1.0.3041

* Mon Dec 16 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3032-1
- Update to 1.0.3032

* Fri Dec 06 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2990-1
- Update to 1.0.2990

* Fri Nov 29 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2934-1
- Update to 1.0.2934
- Use flex 2.6.1 from copr

* Wed Nov 20 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2878-1
- Update to 1.0.2878

* Thu Nov 14 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2805-1
- Update to 1.0.2805

* Wed Oct 30 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2714.1-1
- Update to 1.0.2714.1

