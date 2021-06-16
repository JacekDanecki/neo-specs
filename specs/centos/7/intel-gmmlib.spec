%global major_version 21
%global minor_version 1
%global patch_version 3
%global api_patch_version  1111

Name:       intel-gmmlib
Version:    21.1.3
Release:    1%{?dist}
Summary:    Intel(R) Graphics Memory Management Library Package

Group:      System Environment/Libraries
License:    MIT
URL:        https://github.com/intel/gmmlib
Source0:    %{url}/archive/%{name}-%{version}.tar.gz
ExclusiveArch:  x86_64

BuildRequires: centos-release-scl epel-release
BuildRequires: devtoolset-7-gcc-c++ cmake3
BuildRequires: make

%description
Intel(R) Graphics Memory Management Library

%package       devel
Summary:       Intel(R) Graphics Memory Management Library development package
Group: Development
Requires:      %{name} = %{version}-%{release}

%description   devel
The %{name}-devel package contains library and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n gmmlib-intel-gmmlib-%{version}
find Source -name "*.cpp" -exec chmod -x {} ';'
find Source -name "*.h" -exec chmod -x {} ';'

%build
mkdir build
pushd build

scl enable devtoolset-7 "cmake3 -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_TYPE=release \
 -DMAJOR_VERSION=%{major_version} -DMINOR_VERSION=%{minor_version} -DPATCH_VERSION=%{patch_version} \
 -DGMMLIB_API_PATCH_VERSION=%{api_patch_version} \
 -DRUN_TEST_SUITE:BOOL='ON' .."
scl enable devtoolset-7 "make -j`nproc`"

%install
cd build
%make_install

%files
%defattr(-,root,root)
/usr/lib64/libigdgmm.so.11
/usr/lib64/libigdgmm.so.11.*

%files devel
%defattr(-,root,root)
/usr/include/igdgmm/*
/usr/lib64/libigdgmm.so
/usr/lib64/pkgconfig/igdgmm.pc

%changelog
* Fri May 21 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.1.3-1
- Update to 21.1.3

* Fri Mar 12 2021 Jacek Danecki <jacek.danecki@intel.com> - 20.3.2-1
- Update to 20.3.2

* Thu Sep 03 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.2.4-1
- Update to 20.2.4

* Thu Jul 30 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.2.3-1
- Update to 20.2.3

* Tue Jul 07 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.2.2-1
- Update to 20.2.2

* Wed Mar 25 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.1.1-1
- Update to 20.1.1

* Fri Jan 03 2020 Jacek Danecki <jacek.danecki@intel.com> - 19.4.1-1
- Update to 19.4.1

* Tue Nov 19 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.3.4-1
- Update to 19.3.4
