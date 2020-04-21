%global NEO_MAJOR 20
%global NEO_MINOR 15
%global NEO_BUILD 16524
%global NEO_ver %{NEO_MAJOR}.%{NEO_MINOR}.%{NEO_BUILD}
%global L0_ver 0.8

Name: intel-opencl
Version: %{NEO_ver}
Release: 1%{?dist}
Summary: Intel(R) Graphics Compute Runtime
Group: System Environment/Libraries
License: MIT
URL: https://github.com/intel/compute-runtime
Source0: %{url}/archive/%{version}/compute-runtime-%{version}.tar.gz

BuildRequires: make libva-devel gcc-c++ cmake

BuildRequires: intel-gmmlib-devel = 20.1.1
BuildRequires: intel-igc-opencl-devel = 1.0.3771
BuildRequires: level-zero-devel = 0.91.10

Requires: intel-gmmlib = 20.1.1
Requires: intel-igc-opencl = 1.0.3771

%description -n intel-opencl
Intel(R) Graphics Compute Runtime for OpenCL(TM).

%package -n intel-level-zero-gpu
Summary: Intel(R) Graphics Compute Runtime for Level Zero
Version: %{L0_ver}.%{NEO_BUILD}
%description -n intel-level-zero-gpu
Intel(R) Graphics Compute Runtime for Level Zero
Requires: level-zero = 0.91.10

%prep
%autosetup -n compute-runtime-%{NEO_ver}

%build
mkdir build
cd build
%cmake -DCMAKE_BUILD_TYPE=Release -DNEO_OCL_VERSION_MAJOR=%{NEO_MAJOR} -DNEO_OCL_VERSION_MINOR=%{NEO_MINOR} -DNEO_VERSION_BUILD=%{NEO_BUILD} -DSKIP_UNIT_TESTS=1 ..
%make_build

%install
cd build
%make_install
chmod +x ${RPM_BUILD_ROOT}/usr/lib64/intel-opencl/libigdrcl.so

%files
/usr/lib64/intel-opencl/libigdrcl.so
/usr/bin/ocloc

%config(noreplace)
/etc/OpenCL/vendors/intel.icd

%files -n intel-level-zero-gpu
%{_libdir}/libze_intel_gpu.so.%{L0_ver}
%{_libdir}/libze_intel_gpu.so.%{L0_ver}.%{NEO_BUILD}

%doc

%changelog
* Tue Apr 21 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.15.16524-1
- Update to 20.15.16524

* Tue Apr 14 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.14.16441-1
- Update to 20.14.16441

* Thu Apr 09 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.13.16352-1
- Update to 20.13.16352

* Tue Mar 31 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.12.16259-2
- Fix reported version

* Fri Mar 27 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.12.16259-1
- Update to 20.12.16259
- Compile with Level Zero

* Fri Mar 20 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.11.16158-1
- Update to 20.11.16158

* Fri Mar 13 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.10.16087-1
- Update to 20.10.16087

* Mon Mar 09 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.09.15980-2
- Fix ocloc permissions

* Fri Mar 06 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.09.15980-1
- Update to 20.09.15980

* Fri Feb 28 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.08.15750-1
- Update to 20.08.15750

* Fri Feb 21 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.07.15711-1
- Update to 20.07.15711

* Fri Feb 14 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.06.15619-1
- Update to 20.06.15619

* Fri Feb 07 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.05.15524-1
- Update to 20.05.15524

* Fri Jan 31 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.04.15428-1
- Update to 20.04.15428

* Fri Jan 24 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.03.15346-1
- Update to 20.03.15346

* Fri Jan 17 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.02.15268-1
- Update to 20.02.15268

* Fri Jan 10 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.01.15264-1
- Update to 20.01.15264

* Fri Jan 03 2020 Jacek Danecki <jacek.danecki@intel.com> - 19.52.15209-1
- Update to 19.52.15209

* Fri Dec 27 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.51.15145-1
- Update to 19.51.15145

* Fri Dec 20 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.50.15079-1
- Update to 19.50.15079
- Updated IGC

* Mon Dec 16 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.49.15055-1
- Update to 19.49.15055
- Updated IGC

* Fri Dec 06 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.48.14977-1
- Update to 19.48.14977
- Updated IGC

* Fri Nov 29 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.47.14903-1
- Update to 19.47.14903
- Updated IGC

* Fri Nov 22 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.46.14807-1
- Update to 19.46.14807
- Updated IGC

* Tue Nov 19 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.45.14764-1
- Update to 19.45.14764

* Wed Nov 13 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.44.14658-1
- Update to 19.44.14658

* Wed Oct 30 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.43.14583-1
- Update to 19.43.14583

* Thu Oct 24 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.41.14441-1
- Update to 19.41.14441

