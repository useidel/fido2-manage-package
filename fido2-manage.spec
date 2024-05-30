%define         pkgname         fido2-manage
%global         forgeurl        https://github.com/token2/%{pkgname}
%global 	debug_package %{nil}
%define 	_build_id_links none
%global commit  db585a3ad323a00e909f2b9535f2e13113d2d23e

Name:		%{pkgname}
Version:        0.0.1
Release:	3%{?dist}
License:	BSD-Clause 2 
Vendor:		Token2
URL:		%{forgeurl}
Source0:	https://github.com/token2/%{pkgname}/%{pkgname}/releases/download/v%{version}/v%{version}.tar.gz
Summary: 	Tool allowing to manage FIDO2.1 devices over USB or NFC	

BuildRequires:  pkgconf-pkg-config gcc cmake libcbor-devel openssl-devel libgudev-devel pcsc-lite-devel dos2unix

%if 0%{?fedora} < 40
BuildRequires: zlib-ng-devel
%else
BuildRequires: zlib-ng-compat-devel
%endif

Requires:  libcbor openssl libgudev pcsc-lite

%if 0%{?fedora} < 40
Requires: zlib-ng
%else
Requires: zlib-ng-compat
%endif

%description 
Tool allowing to manage FIDO2.1 devices over USB or NFC, including Passkey (resident keys) management

%package	gui
Summary: 	Python-TK GUI to manage FIDO2.1 devices over USB or NFC	
%description	gui
Python-TK file as GUI frontend for %{pkgname}


%prep
%autosetup

%setup


%build
rm -rf build && mkdir build && cd build && cmake -USE_PCSC=ON -DCMAKE_INSTALL_PREFIX:PATH=/usr ..

cd ..

make -C build


%install
make -C build install DESTDIR=$RPM_BUILD_ROOT
%{__cp} %{name}.sh %{buildroot}%{_bindir}
echo '#!/usr/bin/env python3' > %{buildroot}%{_bindir}/fido2-manage-gui
%{__cat} gui.py >> %{buildroot}%{_bindir}/fido2-manage-gui
dos2unix %{buildroot}%{_bindir}/fido2-manage-gui
chmod 755 %{buildroot}%{_bindir}/fido2-manage-gui

%files
%{_bindir}/fido2-token
%{_bindir}/fido2-manage.sh
%{_libdir}/libfido2.so*
%{_libdir}/libfido2.a
%{_libdir}/pkgconfig/libfido2.pc
%{_includedir}/fido.h
%{_includedir}/fido/*
%{_mandir}/man1/fido*
%{_mandir}/man3/fido*
%{_mandir}/man3/*pk*

%files gui
%{_bindir}/fido2-manage-gui



%changelog
* Wed May 30 2024 Udo Seidel <udoseidel@gmx.de> 0.0.1-3
- correction of statements in SPEC file 

* Wed May 30 2024 Udo Seidel <udoseidel@gmx.de> 0.0.1-2
- using a subpackage for the GUI

* Wed May 29 2024 Udo Seidel <udoseidel@gmx.de> 0.0.1-1
- first version of RPM
