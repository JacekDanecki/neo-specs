%global major_version 19
%global minor_version 4
%global patch_version 1
%global api_patch_version 751

Name:		intel-gmmlib
Version:    19.4.1
Release:	1%{?dist}
Summary:	Intel(R) Graphics Memory Management Library Package

Group:	    System Environment/Libraries
License:	MIT
URL:		https://github.com/intel/gmmlib
Source0:	%{url}/archive/%{name}-%{version}.tar.gz
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
/usr/lib64/libigdgmm.so.*

%files devel
%defattr(-,root,root)
/usr/include/igdgmm/*
/usr/lib64/libigdgmm.so
/usr/lib64/pkgconfig/igdgmm.pc

%changelog
* Fri Jan 03 2020 Jacek Danecki <jacek.danecki@intel.com> - 19.4.1-1
- Update to 19.4.1

* Tue Nov 19 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.3.4-1
- Update to 19.3.4
