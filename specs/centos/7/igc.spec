%global llvm_commit llvmorg-10.0.0
%global opencl_clang_commit c8cd72e32b6abc18ce6da71c357ea45ba78b52f0
%global igc_commit igc-1.0.8517
%global patch_version 8517
%global vc_commit d9ffe1f9cbe45b296f098669173bcaeff12bfe99
%global src 21.32.20609

Name: intel-igc
Version: 1.0.8517
Release: 1%{?dist}
Summary: Intel(R) Graphics Compiler for OpenCL(TM)

Group: System Environment/Libraries
License: MIT
URL: https://github.com/intel/intel-graphics-compiler
Source0: %{url}/archive/%{igc_commit}/igc-%{version}.tar.gz
Source1: https://downloads.sourceforge.net/project/intel-compute-runtime/%{src}/src/opencl-clang.tar.gz
Source2: https://downloads.sourceforge.net/project/intel-compute-runtime/%{src}/src/spirv-llvm-translator.tar.gz
Source3: https://downloads.sourceforge.net/project/intel-compute-runtime/%{src}/src/llvm-project.tar.gz
Source4: https://github.com/intel/vc-intrinsics/archive/%{vc_commit}/vc-intrinsics.tar.gz
Patch0:  %{url}/commit/c9eb6d65deccc25f358375b57193e825f4a0bb37.patch

BuildRequires: centos-release-scl epel-release
BuildRequires: devtoolset-7-gcc-c++ cmake3
BuildRequires: git make patch pkgconfig python3 bison
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

pushd llvm-project/llvm/projects
mkdir opencl-clang llvm-spirv
tar xzf $RPM_SOURCE_DIR/opencl-clang.tar.gz -C opencl-clang --strip-components=1
tar xzf $RPM_SOURCE_DIR/spirv-llvm-translator.tar.gz -C llvm-spirv --strip-components=1
popd

mkdir igc
tar xzf $RPM_SOURCE_DIR/igc-%{version}.tar.gz -C igc --strip-components=1
cd igc
patch -p1 < $RPM_SOURCE_DIR/c9eb6d65deccc25f358375b57193e825f4a0bb37.patch
cd ..

mkdir vc-intrinsics
tar xzf $RPM_SOURCE_DIR/vc-intrinsics.tar.gz -C vc-intrinsics --strip-components=1

git config --global user.email "jacek.danecki@intel.com"
git config --global user.name "Jacek Danecki"

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
rm -fv $RPM_BUILD_ROOT/usr/bin/clang-10
rm -fv $RPM_BUILD_ROOT/usr/include/opencl-c.h
rm -fv $RPM_BUILD_ROOT/usr/include/opencl-c-base.h
chmod +x $RPM_BUILD_ROOT/usr/lib64/libopencl-clang.so.10
rm -fv $RPM_BUILD_ROOT/usr/bin/lld
rm -fv $RPM_BUILD_ROOT/usr/lib/debug/usr/bin/lld*.debug

%files core
%defattr(-,root,root)
/usr/lib64/libiga64.so.*
/usr/lib64/libigc.so.*
/usr/lib64/libSPIRVDLL.so
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
* Wed Sep 08 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.8517-1
- Update to 1.0.8517

* Fri Aug 20 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.8365-1
- Update to 1.0.8365

* Wed Aug 18 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.8279-1
- Update to 1.0.8279

* Fri Aug 13 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.8173-1
- Update to 1.0.8173

* Fri Jul 09 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.7862-1
- Update to 1.0.7862

* Mon Jul 05 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.7781-1
- Update to 1.0.7781

* Thu Jul 01 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.7712-1
- Update to 1.0.7712

* Tue Jun 22 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.7683-1
- Update to 1.0.7683

* Tue May 25 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.7423-1
- Update to 1.0.7423

* Wed May 19 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.7181-1
- Update to 1.0.7181

* Mon May 10 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.7152-1
- Update to 1.0.7152

* Wed Apr 28 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.7041-1
- Update to 1.0.7041

* Fri Apr 09 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.6812-1
- Update to 1.0.6812

* Thu Apr 08 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.6748-1
- Update to 1.0.6748

* Fri Mar 26 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.6712-1
- Update to 1.0.6712

* Fri Mar 19 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.6646-1
- Update to 1.0.6646

* Fri Mar 05 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.6410-1
- Update to 1.0.6410

* Fri Feb 12 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.6087-1
- Update to 1.0.6087

* Mon Feb 01 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.6083-1
- Update to 1.0.6083

* Mon Jan 11 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.5964-1
- Update to 1.0.5964

* Fri Nov 27 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.5585-1
- Update to 1.0.5585

* Mon Nov 16 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.5435-1
- Update to 1.0.5435

* Wed Nov 04 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.5353-1
- Update to 1.0.5353

* Fri Oct 16 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.5186-1
- Update to 1.0.5186

* Thu Oct 15 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.5176-1
- Update to 1.0.5176

* Wed Oct 14 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.5064-1
- Update to 1.0.5064

* Wed Sep 30 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4944-1
- Update to 1.0.4944

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

* Mon Nov 25 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2916-2
- Rebuild with flex 2.6.1 from copr

* Thu Nov 21 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2916-1
- Update to 1.0.2916

* Wed Nov 20 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2878-1
- Update to 1.0.2878

* Thu Nov 14 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2805-1
- Update to 1.0.2805

* Wed Oct 30 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2714.1-1
- Update to 1.0.2714.1

