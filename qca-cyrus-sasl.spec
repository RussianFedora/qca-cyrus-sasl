Name:           qca-cyrus-sasl
Version:        2.0.0
Release:        beta3.1%{?dist}.R
Summary:        QCA Cyrus SASL plugin

License:        GPLv2
URL:            http://delta.affinix.com/qca/
Source0:        http://delta.affinix.com/download/qca/2.0/plugins/%{name}-%{version}-beta3.tar.bz2

BuildRequires:  qca2-devel
BuildRequires:  cyrus-sasl-devel       

%description
This plugin provides features based on Cyrus SASL version 2.

%prep
%setup -q -n %{name}-%{version}-beta3


%build
./configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL_ROOT=$RPM_BUILD_ROOT


%files
%{_libdir}/qt4/plugins/crypto/libqca-cyrus-sasl.so*
%doc



%changelog
* Tue Aug 16 2011 Vasiliy N. Glazov <vascom2@gmail.com> 2.0.0-beta3.1.R
- Initial release
