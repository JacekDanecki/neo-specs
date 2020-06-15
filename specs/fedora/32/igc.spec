%global igc_commit 18081c401f7bbfeefede84572a066f038a2d0709
%global patch_version 4062

Name: intel-igc
Version: 1.0.4062
Release: 1%{?dist}
Summary: Intel(R) Graphics Compiler for OpenCL(TM)

License: MIT
URL: https://github.com/intel/intel-graphics-compiler
Source0: %{url}/archive/%{igc_commit}/igc-%{version}.tar.gz
Patch0:  %{url}/commit/f4efb15429bdaca0122640ae63042a8950b491df.patch

BuildRequires: cmake gcc-c++ make flex bison python3 llvm-devel clang-devel
BuildRequires: intel-opencl-clang-devel >= 10.0.8

%description
Intel(R) Graphics Compiler for OpenCL(TM).

%package       core
Summary:       Intel(R) Graphics Compiler Core

%description   core

%package       opencl
Summary:       Intel(R) Graphics Compiler Frontend
Requires:      %{name}-core = %{version}-%{release}
Requires:      intel-opencl-clang >= 10.0.8

%description   opencl

%package       opencl-devel
Summary:       Intel(R) Graphics Compiler development package
Requires:      %{name}-opencl = %{version}-%{release}

%description   opencl-devel

%prep
%autosetup -p1 -n intel-graphics-compiler-%{igc_commit}

%build
mkdir build
pushd build

cmake .. -Wno-dev -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr  \
 -DIGC_PREFERRED_LLVM_VERSION=10.0.0 -DIGC_PACKAGE_RELEASE=%{patch_version}
%make_build
popd

%install
%make_install -C build
rm -fv %{buildroot}/usr/bin/GenX_IR

%files core
%{_libdir}/libiga64.so.1
%{_libdir}/libiga64.so.%{version}
%{_libdir}/libigc.so.1
%{_libdir}/libigc.so.%{version}
%{_bindir}/iga64

%files opencl
%{_libdir}/libigdfcl.so.1
%{_libdir}/libigdfcl.so.%{version}

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

