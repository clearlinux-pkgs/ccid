#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x78A1B4DFE8F9C57E (rousseau@debian.org)
#
Name     : ccid
Version  : 1.4.30
Release  : 2
URL      : https://ccid.apdu.fr/files/ccid-1.4.30.tar.bz2
Source0  : https://ccid.apdu.fr/files/ccid-1.4.30.tar.bz2
Source99 : https://ccid.apdu.fr/files/ccid-1.4.30.tar.bz2.asc
Summary  : A generic USB Chip/Smart Card Interface Devices driver
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: ccid-lib = %{version}-%{release}
Requires: ccid-license = %{version}-%{release}
BuildRequires : flex
BuildRequires : pkgconfig(libpcsclite)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : systemd-dev

%description
USB CCID IFD Handler
====================
This package provides the source code for a generic USB CCID (Chip/Smart
Card Interface Devices) and ICCD (Integrated Circuit(s) Card Devices)
driver. See the USB CCID [1] and ICCD [2] specifications from the USB
working group.

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
%setup -q -n ccid-1.4.30

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556551020
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1556551020
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ccid
cp COPYING %{buildroot}/usr/share/package-licenses/ccid/COPYING
cp src/openct/LICENSE %{buildroot}/usr/share/package-licenses/ccid/src_openct_LICENSE
cp src/towitoko/COPYING %{buildroot}/usr/share/package-licenses/ccid/src_towitoko_COPYING
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/pcsc/drivers/ifd-ccid.bundle/Contents/Info.plist

%files lib
%defattr(-,root,root,-)
/usr/lib64/pcsc/drivers/ifd-ccid.bundle/Contents/Linux/libccid.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ccid/COPYING
/usr/share/package-licenses/ccid/src_openct_LICENSE
/usr/share/package-licenses/ccid/src_towitoko_COPYING
