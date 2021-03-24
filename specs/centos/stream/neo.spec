%global NEO_MAJOR 21
%global NEO_MINOR 11
%global NEO_BUILD 19310
%global NEO_ver %{NEO_MAJOR}.%{NEO_MINOR}.%{NEO_BUILD}
%global L0_ver 1.0
%global IGC_BUILD 6646
%global GMM_BUILD 20.3.2
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
BuildRequires: level-zero-devel = 1.2.3

Requires: intel-gmmlib >= %{GMM_BUILD}
Requires: intel-igc-opencl = 1.0.%{IGC_BUILD}

%description -n intel-opencl
Intel(R) Graphics Compute Runtime for OpenCL(TM).

%package -n intel-level-zero-gpu
Summary: Intel(R) Graphics Compute Runtime for Level Zero
Version: %{L0_ver}.%{NEO_BUILD}
%description -n intel-level-zero-gpu
Intel(R) Graphics Compute Runtime for Level Zero
Requires: level-zero = 1.2.3

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
* Fri Mar 19 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.11.19310-1
- Update to 21.11.19310

* Tue Mar 16 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.10.19208-1
- Update to 21.10.19208

* Fri Mar 05 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.09.19150-1
- Update to 21.09.19150

* Fri Feb 26 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.08.19096-1
- Build 21.08.19096
