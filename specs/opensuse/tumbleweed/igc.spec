%global llvm_commit llvmorg-10.0.0
%global opencl_clang_commit 10.0.0-2
%global spirv_llvm_translator_commit 4d43f68a30a510b4e7607351caab3df8e7426a6b
%global llvm_patches_commit 595c1e3eeb30afc8b6c20855f6a69560f7a9864a
%global igc_commit 173eb2a0f5d0a16f4abc07bbd093056bf0c04ae5
%global patch_version 4154

Name: intel-igc
Version: 1.0.4154
Release: 1%{?dist}
Summary: Intel(R) Graphics Compiler for OpenCL(TM)

Group:   Development/Libraries/C and C++
License: MIT
URL: https://github.com/intel/intel-graphics-compiler
Source0: https://github.com/intel/intel-graphics-compiler/archive/%{igc_commit}/igc-%{version}.tar.gz
Patch0:  %{url}/commit/f4efb15429bdaca0122640ae63042a8950b491df.patch
Source1: https://github.com/intel/opencl-clang/archive/v%{opencl_clang_commit}/intel-opencl-clang.tar.gz
Source2: https://github.com/KhronosGroup/SPIRV-LLVM-Translator/archive/%{spirv_llvm_translator_commit}/spirv-llvm-translator.tar.gz
Source3: https://github.com/llvm/llvm-project/archive/%{llvm_commit}/llvm-project.tar.gz
Source4: https://github.com/intel/llvm-patches/archive/%{llvm_patches_commit}/llvm-patches.tar.gz

BuildRequires: cmake gcc-c++ make flex bison python3 pkg-config git

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
pushd igc
patch -p1 < $RPM_SOURCE_DIR/f4efb15429bdaca0122640ae63042a8950b491df.patch
popd
 
mkdir llvm_patches
tar xzf $RPM_SOURCE_DIR/llvm-patches.tar.gz -C llvm_patches --strip-components=1

%build
mkdir build
pushd build

cmake ../igc -Wno-dev -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr \
 -DIGC_PACKAGE_RELEASE=%{patch_version}
%make_build
popd

%install
cd build
%make_install

rm -fv $RPM_BUILD_ROOT/usr/bin/GenX_IR
rm -fv $RPM_BUILD_ROOT/usr/bin/clang-10
rm -fv $RPM_BUILD_ROOT/usr/include/opencl-c.h
rm -fv $RPM_BUILD_ROOT/usr/include/opencl-c-base.h
chmod +x $RPM_BUILD_ROOT/usr/lib64/libopencl-clang.so.10

%post -n intel-igc-core -p /sbin/ldconfig
%postun -n intel-igc-core -p /sbin/ldconfig

%post -n intel-igc-opencl -p /sbin/ldconfig
%postun -n intel-igc-opencl -p /sbin/ldconfig

%files core
%defattr(-,root,root)
/usr/lib64/libiga64.so.*
/usr/lib64/libigc.so.*
/usr/bin/iga64
%{_libdir}/igc/NOTICES.txt

%files opencl
%defattr(-,root,root)
/usr/lib64/libigdfcl.so.*
/usr/lib64/libopencl-clang.so.*

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
* Wed Jun 24 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4154-1
- Update to 1.0.4154

* Tue Jun 23 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4111-1
- Update to 1.0.4111

* Mon Jun 15 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4062-2
- Add patch from https://github.com/intel/intel-graphics-compiler/pull/135

* Tue Jun 09 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4062-1
- Update to 1.0.4062

* Mon Jun 01 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4053-1
- Update to 1.0.4053

* Tue May 26 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3977-1
- Update to 1.0.3977

* Fri May 15 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3951-1
- Update to 1.0.3951

* Fri May 08 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3899-1
- Update to 1.0.3899

* Mon May 04 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3864-1
- Update to 1.0.3864

* Fri Apr 24 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3826-1
- Update to 1.0.3826

* Tue Apr 21 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3771-1
- Update to 1.0.3771

* Tue Apr 14 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3698-1
- Update to 1.0.3698

* Thu Apr 09 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3627-1
- Update to 1.0.3627

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

* Wed Nov 20 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2878-1
- Update to 1.0.2878

* Thu Nov 14 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2805-1
- Update to 1.0.2805

* Wed Oct 30 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2714.1-1
- Update to 1.0.2714.1
- Switch to llvm/clang 9.0.0
- Include opencl-clang library

