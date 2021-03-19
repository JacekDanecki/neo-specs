%global major_version 20
%global minor_version 3
%global patch_version 2
%global api_patch_version 905

Name:       intel-gmmlib
Version:    20.3.2
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
%{_libdir}/libigdgmm.so.11.1.%{api_patch_version}

%files devel
%{_includedir}/igdgmm/*
%{_libdir}/libigdgmm.so
%{_libdir}/pkgconfig/igdgmm.pc

%changelog
* Tue Nov 10 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.3.2-1
- Update to 20.3.2

* Thu Apr 09 2020 Jacek Danecki <jacek.danecki@intel.com> - 20.1.1-1
- Update to 20.1.1

* Fri Jan 10 2020 Jacek Danecki <jacek.danecki@intel.com> - 19.4.1-1
- Update to 19.4.1

* Tue Nov 19 2019 Jacek Danecki <jacek.danecki@intel.com> - 19.3.4-1
- Update to 19.3.4
