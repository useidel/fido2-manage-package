%define         pkgname         fido2-manage
%global         forgeurl        https://github.com/token2/%{pkgname}
%global 	debug_package %{nil}
%define 	_build_id_links none

Name:		%{pkgname}
Version:        0.0.1
Release:	1%{?dist}
License:	BSD-Clause 2 
Vendor:		Token2
URL:		%{forgeurl}
Source0:	https://github.com/token2/%{pkgname}/%{pkgname}/releases/download/v%{version}/v%{version}.tar.gz
Summary: 	Tool allowing to manage FIDO2.1 devices over USB or NFC	

BuildRequires:  pkgconf-pkg-config zlib-ng-compat-devel cmake libcbor-devel openssl-devel libgudev-devel pcsc-lite-devel dos2unix
Requires:  zlib-ng-compat libcbor openssl libgudev pcsc

%description 
Tool allowing to manage FIDO2.1 devices over USB or NFC, including Passkey (resident keys) management

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
%{_bindir}/fido2-manage-gui
%{_libdir}/libfido2.so*
%{_libdir}/libfido2.a
%{_libdir}/pkgconfig/libfido2.pc
%{_includedir}/fido.h
%{_includedir}/fido/*
%{_mandir}/man1/fido*
%{_mandir}/man3/fido*
%{_mandir}/man3/*pk*


%changelog
* Wed May 29 2024 Udo Seidel <udoseidel@gmx.de> 0.0.1-1
- first version of RPM
