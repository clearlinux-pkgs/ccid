#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x78A1B4DFE8F9C57E (rousseau@debian.org)
#
Name     : ccid
Version  : 1.5.1
Release  : 11
URL      : https://ccid.apdu.fr/files/ccid-1.5.1.tar.bz2
Source0  : https://ccid.apdu.fr/files/ccid-1.5.1.tar.bz2
Source1  : https://ccid.apdu.fr/files/ccid-1.5.1.tar.bz2.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: ccid-config = %{version}-%{release}
Requires: ccid-lib = %{version}-%{release}
Requires: ccid-license = %{version}-%{release}
BuildRequires : flex
BuildRequires : pkgconfig(libpcsclite)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : systemd-dev

%description
The files buffer.[c|h], checksum.c and proto-t1.c comes from the OpenCT
project <http://www.opensc.org/>

%package config
Summary: config components for the ccid package.
Group: Default

%description config
config components for the ccid package.


%package lib
Summary: lib components for the ccid package.
Group: Libraries
Requires: ccid-license = %{version}-%{release}

%description lib
lib components for the ccid package.


%package license
Summary: license components for the ccid package.
Group: Default

%description license
license components for the ccid package.


%prep
%setup -q -n ccid-1.5.1
cd %{_builddir}/ccid-1.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671054566
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1671054566
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ccid
cp %{_builddir}/ccid-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ccid/9a1929f4700d2407c70b507b3b2aaf6226a9543c
cp %{_builddir}/ccid-%{version}/src/openct/LICENSE %{buildroot}/usr/share/package-licenses/ccid/f25c7f6146e4ac975b9e0c4fb3936a9af04d437a
cp %{_builddir}/ccid-%{version}/src/towitoko/COPYING %{buildroot}/usr/share/package-licenses/ccid/207a4f23aeb278d4d863854e3d3787247da1ca43
%make_install
## install_append content
mkdir -p %{buildroot}/usr/lib/udev/rules.d/
cp src/92_pcscd_ccid.rules %{buildroot}/usr/lib/udev/rules.d/
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/pcsc/drivers/ifd-ccid.bundle/Contents/Info.plist

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/92_pcscd_ccid.rules

%files lib
%defattr(-,root,root,-)
/usr/lib64/pcsc/drivers/ifd-ccid.bundle/Contents/Linux/libccid.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ccid/207a4f23aeb278d4d863854e3d3787247da1ca43
/usr/share/package-licenses/ccid/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/ccid/f25c7f6146e4ac975b9e0c4fb3936a9af04d437a
