%global llvm_commit llvmorg-10.0.0
%global opencl_clang_commit c8cd72e32b6abc18ce6da71c357ea45ba78b52f0
%global igc_commit igc-1.0.7181
%global patch_version 7181
%global vc_commit 069ced1e8a408d8b602b3b210017603792df6260
%global src 21.12.19358

Name: intel-igc
Version: 1.0.7181
Release: 1%{?dist}
Summary: Intel(R) Graphics Compiler for OpenCL(TM)

License: MIT
URL: https://github.com/intel/intel-graphics-compiler
Source0: %{url}/archive/%{igc_commit}/igc-%{version}.tar.gz
Source1: https://downloads.sourceforge.net/project/intel-compute-runtime/%{src}/src/opencl-clang.tar.gz
Source2: https://downloads.sourceforge.net/project/intel-compute-runtime/%{src}/src/spirv-llvm-translator.tar.gz
Source3: https://downloads.sourceforge.net/project/intel-compute-runtime/%{src}/src/llvm-project.tar.gz
Source4: https://github.com/intel/vc-intrinsics/archive/%{vc_commit}/vc-intrinsics.tar.gz

BuildRequires: cmake gcc-c++ make flex bison python3 git

%description
Intel(R) Graphics Compiler for OpenCL(TM).

%package       core
Summary:       Intel(R) Graphics Compiler Core

%description   core

%package       opencl
Summary:       Intel(R) Graphics Compiler Frontend
Requires:      %{name}-core = %{version}-%{release}
Conflicts:     intel-opencl-clang

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

mkdir vc-intrinsics
tar xzf $RPM_SOURCE_DIR/vc-intrinsics.tar.gz -C vc-intrinsics --strip-components=1

git config --global user.email "jacek.danecki@intel.com"
git config --global user.name "Jacek Danecki"

%build
mkdir build
pushd build

cmake ../igc -Wno-dev -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr  \
 -DIGC_PREFERRED_LLVM_VERSION=10.0.0 -DIGC_PACKAGE_RELEASE=%{patch_version} \
 -B "x86_64-redhat-linux-gnu"
%cmake_build
popd

%install
cd build
%cmake_install

rm -fv $RPM_BUILD_ROOT/usr/bin/GenX_IR
rm -fv $RPM_BUILD_ROOT/usr/bin/clang-10
rm -fv $RPM_BUILD_ROOT/usr/include/opencl-c.h
rm -fv $RPM_BUILD_ROOT/usr/include/opencl-c-base.h
chmod +x $RPM_BUILD_ROOT/usr/lib64/libopencl-clang.so.10

%files core
%{_libdir}/libiga64.so.1
%{_libdir}/libiga64.so.%{version}
%{_libdir}/libigc.so.1
%{_libdir}/libigc.so.%{version}
%{_bindir}/iga64
%{_libdir}/igc/NOTICES.txt
%{_libdir}/libSPIRVDLL.so

%files opencl
%{_libdir}/libigdfcl.so.1
%{_libdir}/libigdfcl.so.%{version}
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

* Tue Feb 23 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.6087-1
- Add patch for Fedora 34

* Fri Nov 27 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.5585-1
- Update to 1.0.5585

* Mon Nov 16 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.5435-1
- Update to 1.0.5435

* Thu Nov 05 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.5353-1
- Update to 1.0.5353

* Wed Jul 08 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4241-1
- Update to 1.0.4241

* Mon Jun 29 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4155-1
- Update to 1.0.4155

* Wed Jun 24 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4154-1
- Update to 1.0.4154

* Tue Jun 23 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4111-1
- Update to 1.0.4111

* Tue Jun 09 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4062-1
- Update to 1.0.4062

* Mon Jun 01 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.4053-1
- Update to 1.0.4053

* Tue May 26 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3977-1
- Update to 1.0.3977

* Mon May 25 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3951-1
- Update to 1.0.3951
- Add patch for building
- Add workaround from https://github.com/intel/intel-graphics-compiler/pull/135

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

* Mon Mar 02 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3390-1
- Update to 1.0.3390

* Mon Feb 17 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3289-1
- Update to 1.0.3289
- Build with llvm/clang 10

* Tue Jan 28 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3151-2
- fix compilation under Fedora 32

* Fri Jan 24 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3151-1
- Update to 1.0.3151

* Fri Dec 20 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3041-1
- Update to 1.0.3041

* Mon Dec 16 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.3032-1
- Update to 1.0.3032

* Mon Dec 16 2019 Jacek Danecki <jacek.danecki@intel.com> - 1.0.2990-2
- Correct commit ID for IGC 1.0.2990

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

