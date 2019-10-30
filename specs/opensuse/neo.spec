Name: intel-opencl
Version: 19.41.14441
Release: 1%{?dist}
Summary: Intel(R) Graphics Compute Runtime for OpenCL(TM)

Group: System Environment/Libraries
License: MIT
URL: https://github.com/intel/compute-runtime
Source0: %{url}/archive/%{version}/compute-runtime-%{version}.tar.gz

BuildRequires: make libva-devel gcc-c++ cmake

BuildRequires: intel-gmmlib-devel = 19.3.2
BuildRequires: intel-igc-opencl-devel >= 1.0.2597

Requires: intel-gmmlib = 19.3.2
Requires: intel-igc-opencl >= 1.0.2597

%description
Intel(R) Graphics Compute Runtime for OpenCL(TM).

%prep
%autosetup -n compute-runtime-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DNEO_DRIVER_VERSION=%{version} -DSKIP_UNIT_TESTS=1
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

%doc

%changelog
* Thu Oct 24 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.41.14441-1
- Update to 19.41.14441


