# Set to bcond_without or use --with bootstrap if bootstrapping a new release
# or architecture
%bcond_with bootstrap

# Set to bcond_with or use --without gui to disable qt4 gui build
%bcond_without gui

# Do we add appdata-files?
%bcond_without appdata

%bcond_without sphinx

%bcond_without bundled_libarchive
%bcond_without bundled_jsoncpp

# Run tests
%bcond_without test

# Verbose test?
%bcond_with debug

# Place rpm-macros into proper location
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# Setup _pkgdocdir if not defined already
%{!?_pkgdocdir:%global _pkgdocdir %{_docdir}/%{name}-%{version}}

%if 0%{?rhel} && 0%{?rhel} > 7
%global python3_version 3
%endif

%global major_version 3
%global minor_version 17
# Set to RC version if building RC, else %%{nil}
%global rcver %{nil}

# Uncomment if building for EPEL
%global name_suffix %{major_version}
%global orig_name cmake

Name:           %{orig_name}%{?name_suffix}
Version:        %{major_version}.%{minor_version}.5
Release:        2%{?dist}
Summary:        Cross-platform make system

# most sources are BSD
# Source/CursesDialog/form/ a bunch is MIT
# Source/kwsys/MD5.c is zlib
# some GPL-licensed bison-generated files, which all include an
# exception granting redistribution under terms of your choice
License:        BSD and MIT and zlib
URL:            http://www.cmake.org
Source0:        https://github.com/Kitware/CMake/archive/v%{version}/CMake-%{version}%{?rcver:%rcver}.tar.gz
Source1:        https://raw.githubusercontent.com/JacekDanecki/neo-specs/master/specs/centos/8/cmake/%{name}-init.el
Source2:        https://raw.githubusercontent.com/JacekDanecki/neo-specs/master/specs/centos/8/cmake/macros.%{name}
# See https://bugzilla.redhat.com/show_bug.cgi?id=1202899
Source3:        https://raw.githubusercontent.com/JacekDanecki/neo-specs/master/specs/centos/8/cmake/%{name}.attr
Source4:        https://raw.githubusercontent.com/JacekDanecki/neo-specs/master/specs/centos/8/cmake/%{name}.prov
Source5:        https://raw.githubusercontent.com/JacekDanecki/neo-specs/master/specs/centos/8/cmake/CMake3.appdata.xml

# Patch to fix RindRuby vendor settings
# http://public.kitware.com/Bug/view.php?id=12965
# https://bugzilla.redhat.com/show_bug.cgi?id=822796
Patch2:         https://raw.githubusercontent.com/JacekDanecki/neo-specs/master/specs/centos/8/cmake/%{name}-findruby.patch
# replace release flag -O3 with -O2 for fedora
Patch3:         https://raw.githubusercontent.com/JacekDanecki/neo-specs/master/specs/centos/8/cmake/%{name}-fedora-flag_release.patch

# Patch for renaming on EPEL
%if 0%{?name_suffix:1}
Patch1000:      https://raw.githubusercontent.com/JacekDanecki/neo-specs/master/specs/centos/8/cmake/%{name}-rename.patch
%endif

BuildRequires:  gcc-gfortran, gcc-c++
BuildRequires:  ncurses-devel, libX11-devel
BuildRequires:  bzip2-devel
BuildRequires:  curl-devel
BuildRequires:  expat-devel
# Needed jsoncpp >= 1.4.1
%if %{without bundled_jsoncpp}
BuildRequires:  jsoncpp-devel
%endif
# Needed libarchive >= 3.3.3
%if %{without bundled_libarchive}
BuildRequires:  libarchive-devel
%endif
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  libzstd-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  emacs
%if %{with appdata}
BuildRequires:  libappstream-glib
%endif
%if %{without bootstrap}
#BuildRequires: xmlrpc-c-devel
%endif
%if %{with gui}
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: libappstream-glib
%else
BuildRequires: pkgconfig(QtGui)
%endif
BuildRequires: desktop-file-utils
%endif
BuildRequires: openssl-devel

Requires:      %{name}-data = %{version}-%{release}
Requires:      rpm

# Source/kwsys/MD5.c
# see https://fedoraproject.org/wiki/Packaging:No_Bundled_Libraries
Provides: bundled(md5-deutsch)

# https://fedorahosted.org/fpc/ticket/555
Provides: bundled(kwsys)

%if %{with bundled_libarchive}
Provides: bundled(libarchive) = 0:3.3.3
%endif
%if %{with bundled_jsoncpp}
Provides: bundled(json-cpp) = 0:1.8.2
%endif

# cannot do this in epel, ends up replacing os-provided cmake -- Rex
%if 0%{?fedora}
%{?name_suffix:Provides: %{orig_name} = %{version}}
%endif

%description
CMake is used to control the software compilation process using simple
platform and compiler independent configuration files. CMake generates
native makefiles and workspaces that can be used in the compiler
environment of your choice. CMake is quite sophisticated: it is possible
to support complex environments requiring system configuration, preprocessor
generation, code generation, and template instantiation.


%package        data
Summary:        Common data-files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       emacs-filesystem >= %{_emacs_version}

BuildArch:      noarch

%description    data
This package contains common data-files for %{name}.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains documentation for %{name}.

%prep
%autosetup -N -n CMake-%{version}%{?rcver:%rcver}

# Apply renaming on EPEL before all other patches
%if 0%{?name_suffix:1}
%patch1000 -p1 -b .rename
%endif

# We cannot use backups with patches to Modules as they end up being installed
%patch2 -p1 -b .findruby
%patch3 -p1 -b .fedora-flag

echo 'Start cleaning...'
for i in `find . -type f \( -name "*.orig" \)`; do
 rm -f $i
done
echo 'Cleaning finished.'

tail -n +2 %{SOURCE4} >> %{name}.prov
sed -i -e '1i#!%{__python3}' %{name}.prov

%build
export CC=gcc
export CXX=g++
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags} -std=gnu++11"
export LDFLAGS="%{__global_ldflags}"
mkdir build && pushd build
../bootstrap --prefix=%{_prefix} --datadir=/share/%{name} \
 --docdir=/share/doc/%{name} --mandir=/share/man \
 --%{?with_bootstrap:no-}system-libs \
 --parallel=`/usr/bin/getconf _NPROCESSORS_ONLN` \
 --system-zstd \
 --no-system-libuv \
%if %{with bundled_jsoncpp}
 --no-system-jsoncpp \
%endif
 --no-system-librhash \
%if %{with bundled_libarchive}
 --no-system-libarchive \
%endif

%make_build VERBOSE=1


%install
%make_install -C build

find %{buildroot}%{_datadir}/%{name}/Modules -type f | xargs chmod -x
[ -n "$(find %{buildroot}%{_datadir}/%{name}/Modules -name \*.orig)" ] &&
  echo "Found .orig files in %{_datadir}/%{name}/Modules, rebase patches" &&
  exit 1

# Install major_version name links
%{!?name_suffix:for f in ccmake cmake cpack ctest; do ln -s $f %{buildroot}%{_bindir}/${f}%{major_version}; done}
# Install bash completion symlinks
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
for f in %{buildroot}%{_datadir}/%{name}/completions/*
do
  ln -s ../../%{name}/completions/$(basename $f) %{buildroot}%{_datadir}/bash-completion/completions/
done
# Install emacs cmake mode
mkdir -p %{buildroot}%{_emacs_sitelispdir}/%{name}
install -p -m 0644 Auxiliary/cmake-mode.el %{buildroot}%{_emacs_sitelispdir}/%{name}/%{name}-mode.el
%{_emacs_bytecompile} %{buildroot}%{_emacs_sitelispdir}/%{name}/%{name}-mode.el
mkdir -p %{buildroot}%{_emacs_sitestartdir}
install -p -m 0644 %SOURCE1 %{buildroot}%{_emacs_sitestartdir}/
# RPM macros
install -p -m0644 -D %{SOURCE2} %{buildroot}%{rpm_macros_dir}/macros.%{name}
sed -i -e "s|@@CMAKE_VERSION@@|%{version}|" -e "s|@@CMAKE_MAJOR_VERSION@@|%{major_version}|" %{buildroot}%{rpm_macros_dir}/macros.%{name}
touch -r %{SOURCE2} %{buildroot}%{rpm_macros_dir}/macros.%{name}
%if 0%{?_rpmconfigdir:1}
# RPM auto provides
install -p -m0644 -D %{SOURCE3} %{buildroot}%{_prefix}/lib/rpm/fileattrs/%{name}.attr
install -p -m0755 -D %{name}.prov %{buildroot}%{_prefix}/lib/rpm/%{name}.prov
%endif
mkdir -p %{buildroot}%{_libdir}/%{name}
# Install copyright files for main package
find Source Utilities -type f -iname copy\* | while read f
do
  fname=$(basename $f)
  dir=$(dirname $f)
  dname=$(basename $dir)
  cp -p $f ./${fname}_${dname}
done
# Cleanup pre-installed documentation
rm -rf %{buildroot}%{_docdir}/%{name}
# Install documentation to _pkgdocdir
mkdir -p %{buildroot}%{_pkgdocdir}
cp -pr %{buildroot}%{_datadir}/%{name}/Help %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_pkgdocdir}/Help %{buildroot}%{_pkgdocdir}/rst

%files
%license Copyright.txt*
%license COPYING*
%{_bindir}/c%{name}
%{!?name_suffix:%{_bindir}/c%{name}%{major_version}}
%{_bindir}/%{name}
%{!?name_suffix:%{_bindir}/%{name}%{major_version}}
%{_bindir}/cpack%{?name_suffix}
%{!?name_suffix:%{_bindir}/cpack%{major_version}}
%{_bindir}/ctest%{?name_suffix}
%{!?name_suffix:%{_bindir}/ctest%{major_version}}
%{_libdir}/%{name}/

%files data
%{_datadir}/aclocal/%{name}.m4
%{_datadir}/bash-completion/
%{_datadir}/%{name}/
%{_emacs_sitelispdir}/%{name}
%{_emacs_sitestartdir}/%{name}-init.el
%{rpm_macros_dir}/macros.%{name}
%if 0%{?_rpmconfigdir:1}
%{_rpmconfigdir}/fileattrs/%{name}.attr
%{_rpmconfigdir}/%{name}.prov
%endif

%files doc
# Pickup license-files from main-pkg's license-dir
# If there's no license-dir they are picked up by %%doc previously
%{?_licensedir:%license %{_datadir}/licenses/%{name}*}
%{_pkgdocdir}/

%changelog
* Fri Feb 26 2021 Jacek Danecki <jacek.danecki@intel.com> - 3.17.5-2
- Port to Centos 8

* Wed Dec 09 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.17.5-1
- Release 3.17.5

* Sun Jul 19 2020 Neal Gompa <ngompa13@gmail.com> - 3.17.3-3
- Backport support for out-of-source builds controlled by __cmake3_in_source_build macro
- Backport cmake3_build and cmake3_install macros
- Backport ctest3 macro

* Thu Jun 11 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.17.3-2
- Change command to add Python shebang of the cmake3.prov file (epel bz#1845614)

* Mon Jun 01 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.17.3-1
- Release 3.17.3

* Wed Apr 29 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.17.2-1
- Release 3.17.2

* Mon Apr 27 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.17.1-2
- Fix macros for bundled libraries
- Add Provides for bundled libraries

* Sun Apr 26 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.17.1-1
- Release 3.17.1
- Drop EPEL6 support
- Add openssl BR
- Fix rhbz#1811358
- Use system zstd

* Sun Mar 08 2020 Antonio Trande <sagitter@fedoraproject.org> - 3.14.7-1
- Bugfix release 3.14.7

* Sun Sep 01 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.14.6-2
- Fix rename patches

* Tue Aug 27 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.14.6-1
- Update to cmake-3.14.6 (rhbz#1746146, rhbz#1746104)
- Do not use system jsoncpp
- Split off appdata file as external source file

* Sat May 25 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.13.5-1
- Update to cmake-3.13.5

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 3.13.4-2
- Rebuilt to change main python from 3.4 to 3.6

* Sun Feb 03 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.13.4-1
- Update to cmake-3.13.4

* Sat Jan 19 2019 Antonio Trande <sagitter@fedoraproject.org> - 3.13.3-1
- Update to cmake-3.13.3

* Sat Dec 29 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.13.1-1
- Update to cmake-3.13.1
- Use Python3 on epel7
- Perform all tests

* Thu Oct 04 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.12.2-1
- Update to cmake-3.12.2

* Mon Aug 20 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.12.1-1
- Update to cmake-3.12.1

* Fri Jul 27 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.12.0-1
- Update to cmake-3.12.0
- Use %%_metainfodir

* Sat May 19 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.11.2-1
- Update to cmake-3.11.2
- Fix appdata file's entries

* Sat Apr 07 2018 Antonio Trande <sagitter@fedoraproject.org> - 3.11.0-1
- Update to cmake-3.11.0
- Add libuv rhash development packages
- Adapt 'cmake3-rename' patch to CMake-3.11
- Move appdata file into the metainfo sub-data directory

* Thu Feb 09 2017 Orion Poplawski <orion@cora.nwra.com> 3.6.3-1
- Update to 3.6.3
- Fix cmake3.prov error

* Thu Sep 01 2016 Rex Dieter <rdieter@fedoraproject.org> 3.6.1-2
- drop Provides: cmake

* Tue Aug 23 2016 Björn Esser <fedora@besser82.io> - 3.6.1-1
- Update to 3.6.1 (#1353778)

* Fri Apr 22 2016 Björn Esser <fedora@besser82.io> - 3.5.2-2
- Do not own /usr/lib/rpm/fileattrs

* Sat Apr 16 2016 Björn Esser <fedora@besser82.io> - 3.5.2-1
- Update to 3.5.2 (#1327794)

* Fri Mar 25 2016 Björn Esser <fedora@besser82.io> - 3.5.1-1
- Update to 3.5.1 (#1321198)

* Fri Mar 11 2016 Björn Esser <fedora@besser82.io> - 3.5.0-2.1
- fix emacs-filesystem requires for epel6

* Thu Mar 10 2016 Björn Esser <fedora@besser82.io> - 3.5.0-2
- keep Help-directory and its contents in %%_datadir/%%name

* Wed Mar 09 2016 Björn Esser <fedora@besser82.io> - 3.5.0-1.2
- do not provide cmake = %%{version}

* Wed Mar 09 2016 Björn Esser <fedora@besser82.io> - 3.5.0-1.1
- fix macros

* Wed Mar 09 2016 Björn Esser <fedora@besser82.io> - 3.5.0-1
- update to 3.5.0 final

* Tue Mar 08 2016 Björn Esser <fedora@besser82.io> - 3.5.0-0.3.rc3
- bump after review (#1315193)

* Mon Mar 07 2016 Björn Esser <fedora@besser82.io> - 3.5.0-0.2.rc3
- addressing issues from review (#1315193)
  - fix emacs-packaging
  - use %%license-macro
  - fix arch'ed Requires
  - removed BuildRoot
  - use %%global instead of %%define
  - split documentation into noarch'ed doc-subpkg

* Mon Mar 07 2016 Björn Esser <fedora@besser82.io> - 3.5.0-0.1.rc3
- initial epel-release (#1315193)
