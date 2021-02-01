Name:       level-zero
%global major_version 1
%global minor_version 0
%global patch_version 26
Version:    %{major_version}.%{minor_version}.%{patch_version}
Release:    1%{?dist}
Summary:    oneAPI Level Zero Specification Headers and Loader 

License:    MIT
URL:        https://github.com/oneapi-src/level-zero
Source0:    %{url}/archive/v%{version}.tar.gz
ExclusiveArch:  x86_64
%define debug_package %{nil}

BuildRequires: centos-release-scl epel-release
BuildRequires: devtoolset-7-gcc-c++ cmake3 make

%description
oneAPI Level Zero Specification Headers and Loader 

%package       devel
Summary:       oneAPI Level Zero Specification Headers and Loader development package
Requires:      %{name} = %{version}-%{release}

%description   devel
The %{name}-devel package contains library and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n level-zero-%{version}
echo %{patch_version} > VERSION_PATCH

%build
mkdir build
pushd build
scl enable devtoolset-7 'cmake3 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_CXX_FLAGS="${RPM_OPT_FLAGS}" ..'
scl enable devtoolset-7 "make -j`nproc`"
popd

%install
%make_install -C build

%files
%{_libdir}/libze_loader.so.%{major_version}
%{_libdir}/libze_loader.so.%{major_version}.%{minor_version}.%{patch_version}
%{_libdir}/libze_validation_layer.so.%{major_version}
%{_libdir}/libze_validation_layer.so.%{major_version}.%{minor_version}.%{patch_version}
%{_libdir}/libze_tracing_layer.so.%{major_version}
%{_libdir}/libze_tracing_layer.so.%{major_version}.%{minor_version}.%{patch_version}

%files devel
%{_includedir}/level_zero/*
%{_libdir}/libze_loader.so
%{_libdir}/libze_validation_layer.so
%{_libdir}/libze_tracing_layer.so
%{_libdir}/pkgconfig/libze_loader.pc
 
%changelog
* Fri Jan 22 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.26-1
- Update to 1.0.26

* Mon Jan 11 2021 Jacek Danecki <jacek.danecki@intel.com> - 1.0.22-1
- Update to 1.0.22

* Thu Nov 05 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.16-1
- Update to 1.0.16

* Thu Oct 15 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.13-1
- Update to 1.0.13

* Fri Oct 02 2020 Jacek Danecki <jacek.danecki@intel.com> - 1.0.0-1
- Update to 1.0.0

* Thu Apr 09 2020 Jacek Danecki <jacek.danecki@intel.com> - 0.91.10-1
- Update to 0.91.10

* Fri Mar 27 2020 Jacek Danecki <jacek.danecki@intel.com> - 0.91.2-1
- Initial packaging 0.91.2

