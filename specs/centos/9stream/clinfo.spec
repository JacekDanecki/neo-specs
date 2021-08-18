Name:           clinfo
Summary:        Enumerate OpenCL platforms and devices
Version:        2.1.17.02.09
Release:        3%{?dist}

License:        CC0
URL:            https://github.com/Oblomov/clinfo
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ocl-icd-devel

%description
A simple OpenCL application that enumerates all possible platform and
device properties. Inspired by AMD's program of the same name, it is
coded in pure C99 and it tries to output all possible information,
including that provided by platform-specific extensions, and not to
crash on platform-unsupported properties (e.g. 1.2 properties on 1.1
platforms).

%prep
%autosetup

%build
export CFLAGS="%{__global_cflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build

%install
install -Dpm0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license LICENSE legalcode.txt
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Aug 13 2021 Jacek Danecki <jacek.danecki@intel.com> - 2.1.17.02.09-3
- Rebuild on Centos 9 stream
