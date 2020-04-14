Name:       level-zero
%global patch_version 10
%global major_version 0
%global minor_version 91
Version:    %{major_version}.%{minor_version}.%{patch_version}
Release:    1%{?dist}
Summary:    oneAPI Level Zero Specification Headers and Loader 

License:    MIT
URL:        https://github.com/oneapi-src/level-zero
Source0:    %{url}/archive/v%{version}.tar.gz
ExclusiveArch:  x86_64
%define debug_package %{nil}

BuildRequires: gcc-c++ cmake make opencl-headers

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
%cmake -DCMAKE_BUILD_TYPE=Release ..
%make_build

%install
%make_install -C build

%files
%{_libdir}/libze_loader.so.%{major_version}.%{minor_version}
%{_libdir}/libze_loader.so.%{major_version}.%{minor_version}.%{patch_version}
%{_libdir}/libze_validation_layer.so.%{major_version}.%{minor_version}
%{_libdir}/libze_validation_layer.so.%{major_version}.%{minor_version}.%{patch_version}

%files devel
%{_includedir}/level_zero/*
%{_libdir}/libze_loader.so
%{_libdir}/libze_validation_layer.so

%changelog
* Thu Apr 09 2020 Jacek Danecki <jacek.danecki@intel.com> - 0.91.10-1
- Update to 0.91.10

* Fri Mar 27 2020 Jacek Danecki <jacek.danecki@intel.com> - 0.91.2-1
- Initial packaging 0.91.2

