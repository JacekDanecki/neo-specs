%global major_version 21
%global minor_version 1
%global patch_version 3
%global api_patch_version 1111

Name:       intel-gmmlib
Version:    21.1.3
Release:    1%{?dist}
Summary:    Intel(R) Graphics Memory Management Library Package

License:    MIT
URL:        https://github.com/intel/gmmlib
Source0:    %{url}/archive/%{name}-%{version}.tar.gz
ExclusiveArch:  x86_64

BuildRequires: gcc-c++ cmake make

%description
Intel(R) Graphics Memory Management Library

%package       devel
Summary:       Intel(R) Graphics Memory Management Library development package
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

%cmake -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_TYPE=release \
 -DMAJOR_VERSION=%{major_version} -DMINOR_VERSION=%{minor_version} -DPATCH_VERSION=%{patch_version} \
 -DGMMLIB_API_PATCH_VERSION=%{api_patch_version} \
 -DRUN_TEST_SUITE:BOOL='ON' ..
%make_build
popd

%install
cd build
%make_install

%files
%{_libdir}/libigdgmm.so.11
%{_libdir}/libigdgmm.so.11.*

%files devel
%{_includedir}/igdgmm/*
%{_libdir}/libigdgmm.so
%{_libdir}/pkgconfig/igdgmm.pc

%changelog
* Fri May 21 2021 Jacek Danecki <jacek.danecki@intel.com> - 21.1.3-1
- Update to 21.1.3

* Fri Feb 26 2021 Jacek Danecki <jacek.danecki@intel.com> - 20.3.2-1
- Build 20.3.2
