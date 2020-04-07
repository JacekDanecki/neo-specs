Name:       level-zero
%global patch_version 2
%global major_version 0
%global minor_version 91
Version:    %{major_version}.%{minor_version}.%{patch_version}
Release:    1%{?dist}
Summary:    oneAPI Level Zero Specification Headers and Loader 

License:    MIT
URL:        https://github.com/oneapi-src/level-zero
Source0:    %{url}/archive/v%{major_version}.%{minor_version}.tar.gz
Patch0:     %{url}/commit/950f710571c357a0cd654f40253d970ee216a73c.patch
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
%autosetup -p1 -n level-zero-%{major_version}.%{minor_version}
echo %{patch_version} > VERSION_PATCH

%build
mkdir build
pushd build
%cmake -DCMAKE_BUILD_TYPE=Release ..
%make_build
popd

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
* Fri Mar 27 2020 Jacek Danecki <jacek.danecki@intel.com> - 0.91.2-1
- Initial packaging 0.91.2

