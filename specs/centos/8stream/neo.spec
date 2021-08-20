%global NEO_MAJOR 21
%global NEO_MINOR 32
%global NEO_BUILD 20609
%global NEO_ver %{NEO_MAJOR}.%{NEO_MINOR}.%{NEO_BUILD}
%global L0_ver 1.1
%global IGC_BUILD 8279
%global GMM_BUILD 21.2.1
%define debug_package %{nil}

Name: intel-opencl
Version: %{NEO_ver}
Release: 1%{?dist}
Summary: Intel(R) Graphics Compute Runtime
License: MIT
URL: https://github.com/intel/compute-runtime
Source0: %{url}/archive/%{version}/compute-runtime-%{version}.tar.gz

BuildRequires: make libva-devel gcc-c++ cmake

BuildRequires: intel-gmmlib-devel >= %{GMM_BUILD}
BuildRequires: intel-igc-opencl-devel = 1.0.%{IGC_BUILD}
BuildRequires: level-zero-devel = 1.4.1

Requires: intel-gmmlib >= %{GMM_BUILD}
Requires: intel-igc-opencl = 1.0.%{IGC_BUILD}

%description -n intel-opencl
Intel(R) Graphics Compute Runtime for OpenCL(TM).

%package -n intel-level-zero-gpu
Summary: Intel(R) Graphics Compute Runtime for Level Zero
Version: %{L0_ver}.%{NEO_BUILD}
%description -n intel-level-zero-gpu
Intel(R) Graphics Compute Runtime for Level Zero
Requires: level-zero = 1.4.1

%prep
%autosetup -n compute-runtime-%{NEO_ver}

%build
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DNEO_OCL_VERSION_MAJOR=%{NEO_MAJOR} \
    -DNEO_OCL_VERSION_MINOR=%{NEO_MINOR} -DNEO_VERSION_BUILD=%{NEO_BUILD} \
    -DSKIP_UNIT_TESTS=1 -DCMAKE_INSTALL_PREFIX=/usr ..
%make_build

%install
%make_install -C build
chmod +x %{buildroot}/%{_libdir}/intel-opencl/libigdrcl.so
rm -f %{buildroot}/%{_libdir}/intel-opencl/libigdrcl.so.debug
rm -f %{buildroot}/%{_libdir}/libocloc.so.debug
rm -rf %{buildroot}/usr/lib/debug/

%files
%{_libdir}/intel-opencl/libigdrcl.so
%{_bindir}/ocloc
%{_includedir}/ocloc_api.h
%{_libdir}/libocloc.so

%config(noreplace)
%{_sysconfdir}/OpenCL/vendors/intel.icd

%files -n intel-level-zero-gpu
%{_libdir}/libze_intel_gpu.so.1
%{_libdir}/libze_intel_gpu.so.%{L0_ver}.%{NEO_BUILD}

%doc

%changelog
* Thu Aug 19 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.32.20609-1
- Update to 21.32.20609

* Fri Aug 13 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.31.20514-1
- Update to 21.31.20514

* Thu Aug 12 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.30.20482-1
- Update to 21.30.20482

* Thu Aug 12 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.29.20389-1
- Update to 21.29.20389

* Mon Jul 19 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.28.20343-1
- Update to 21.28.20343

* Fri Jul 09 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.27.20266-1
- Update to 21.27.20266

* Mon Jul 05 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.26.20194-1
- Update to 21.26.20194

* Thu Jul 01 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.25.20114-1
- Update to 21.25.20114

* Tue Jun 22 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.24.20098-1
- Update to 21.24.20098

* Fri Jun 11 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.23.20043-1
- Update to 21.23.20043

* Wed Jun 09 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.22.19967-1
- Update to 21.22.19967

* Wed Jun 02 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.21.19914-1
- Update to 21.21.19914

* Tue May 25 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.20.19883-1
- Update to 21.20.19883

* Wed May 19 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.19.19792-1
- Update to 21.19.19792

* Wed May 12 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.18.19737-1
- Update to 21.18.19737

* Mon May 10 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.17.19709-1
- Update to 21.17.19709

* Wed Apr 28 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.16.19610-1
- Update to 21.16.19610

* Fri Apr 16 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.15.19533-1
- Update to 21.15.19533

* Fri Apr 09 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.14.19498-1
- Update to 21.14.19498

* Thu Apr 08 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.13.19438-1
- Update to 21.13.19438

* Fri Mar 26 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.12.19358-1
- Update to 21.12.19358

* Fri Mar 19 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.11.19310-1
- Update to 21.11.19310

* Tue Mar 16 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.10.19208-1
- Update to 21.10.19208

* Fri Mar 05 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.09.19150-1
- Update to 21.09.19150

* Fri Feb 26 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.08.19096-1
- Build 21.08.19096
