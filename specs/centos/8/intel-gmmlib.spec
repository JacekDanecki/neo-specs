%global major_version 19
%global minor_version 3
%global patch_version 2
%global package_release 1
%global api_patch_version 702

Name:		intel-gmmlib
Version:    %{major_version}.%{minor_version}.%{patch_version}
Release:	%{package_release}%{?dist}
Summary:	Intel(R) Graphics Memory Management Library Package

Group:	    System Environment/Libraries
License:	MIT
URL:		https://github.com/intel/gmmlib
Source0:	%{url}/archive/%{name}-%{version}.tar.gz
ExclusiveArch:  x86_64

BuildRequires: gcc-c++ cmake make

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
%defattr(-,root,root)
/usr/lib64/libigdgmm.so.*

%files devel
%defattr(-,root,root)
/usr/include/igdgmm/*
/usr/lib64/libigdgmm.so
/usr/lib64/pkgconfig/igdgmm.pc
