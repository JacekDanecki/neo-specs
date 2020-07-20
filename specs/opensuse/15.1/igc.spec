%global llvm_commit llvmorg-10.0.0
%global opencl_clang_commit 6a9cd2c7dc37f168dae327564a98cab7c4382a2c
%global spirv_llvm_translator_commit 424e375edc4b915218ab5d1f08670a8d1e92c9d3
%global llvm_patches_commit 50058902254167a4587d01d14bd6eaaa238d69ab
%global igc_commit 6baed3e124026a1c3e4296fb356f7b6d0481421c
%global patch_version 4361

Name: intel-igc
Version: 1.0.4361
Release: 1%{?dist}
Summary: Intel(R) Graphics Compiler for OpenCL(TM)

Group: System Environment/Libraries
License: MIT
URL: https://github.com/intel/intel-graphics-compiler
Source0: %{url}/archive/%{igc_commit}/igc-%{version}.tar.gz
Source1: https://github.com/intel/opencl-clang/archive/%{opencl_clang_commit}/intel-opencl-clang.tar.gz
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
* Mon Jul 20 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4361-1
- Update to 1.0.4361

* Fri Jul 10 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4312-1
- Update to 1.0.4312

* Mon Jun 29 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4241-1
- Update to 1.0.4241

* Tue Jun 09 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4154-1
- Update to 1.0.4154

* Fri Jun 05 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4116-1
- Update to 1.0.4116

* Tue May 26 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4062-1
- Update to 1.0.4062

* Wed May 20 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4036-1
- Update to 1.0.4036

* Tue May 12 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3977-1
- Update to 1.0.3977

* Thu May 07 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3951-1
- Update to 1.0.3951

* Wed Apr 29 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3899-1
- Update to 1.0.3899

* Tue Apr 21 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3826-1
- Update to 1.0.3826

* Wed Apr 15 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3800-1
- Update to 1.0.3800

* Wed Apr 08 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3752-1
- Update to 1.0.3752

* Tue Apr 07 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3750-1
- Update to 1.0.3750

* Wed Mar 25 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3627-1
- Update to 1.0.3627

* Tue Mar 17 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3572-1
- Update to 1.0.3572

* Mon Mar 09 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3529-1
- Update to 1.0.3529

* Mon Feb 24 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3445-1
- Update to 1.0.3445

* Tue Feb 18 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3390-1
- Update to 1.0.3390

* Wed Feb 12 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3342-1
- Update to 1.0.3342

* Tue Feb 04 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3289-1
- Update to 1.0.3289

* Wed Jan 15 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3151-1
- Update to 1.0.3151

* Tue Dec 10 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3041-1
- Update to 1.0.3041

* Mon Dec 02 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2990-1
- Update to 1.0.2990

* Tue Nov 26 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2972-1
- Update to 1.0.2972

* Tue Nov 26 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2934-1
- Update to 1.0.2934

* Thu Nov 21 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2916-1
- Update to 1.0.2916

* Wed Nov 20 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2878-1
- Update to 1.0.2878

* Thu Nov 14 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2805-1
- Update to 1.0.2805

* Wed Oct 30 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2714.1-1
- Update to 1.0.2714.1
- Switch to llvm/clang 9.0.0
- Include opencl-clang library

