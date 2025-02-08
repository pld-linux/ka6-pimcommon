#
# Conditional build:
%bcond_with	tests	# test suite

%define		kdeappsver	24.12.2
# packages version, not cmake config version (which is 6.2.2)
%define		ka_ver		%{version}
%define		kf_ver		6.3.0
%define		qt_ver		6.6.0
%define		kaname		pimcommon
Summary:	Common PIM libraries
Summary(pl.UTF-8):	Wspólne biblioteki PIM
Name:		ka6-%{kaname}
Version:	24.12.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	74aef9521c72af0c3861007c95dd34a8
URL:		https://kde.org/
BuildRequires:	Qt6Core-devel >= %{qt_ver}
BuildRequires:	Qt6DBus-devel >= %{qt_ver}
BuildRequires:	Qt6Designer-devel >= %{qt_ver}
BuildRequires:	Qt6Gui-devel >= %{qt_ver}
BuildRequires:	Qt6Network-devel >= %{qt_ver}
%if %{with tests}
BuildRequires:	Qt6Test-devel >= %{qt_ver}
%endif
BuildRequires:	Qt6UiTools-devel >= %{qt_ver}
BuildRequires:	Qt6Widgets-devel >= %{qt_ver}
BuildRequires:	Qt6Xml-devel >= %{qt_ver}
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-tools
BuildRequires:	ka6-akonadi-contacts-devel >= %{ka_ver}
BuildRequires:	ka6-akonadi-devel >= %{ka_ver}
BuildRequires:	ka6-akonadi-search-devel >= %{ka_ver}
BuildRequires:	ka6-kimap-devel >= %{ka_ver}
BuildRequires:	ka6-kldap-devel >= %{ka_ver}
BuildRequires:	ka6-libkdepim-devel >= %{ka_ver}
BuildRequires:	kf6-extra-cmake-modules >= %{kf_ver}
BuildRequires:	kf6-karchive-devel >= %{kf_ver}
BuildRequires:	kf6-kcmutils-devel >= %{kf_ver}
BuildRequires:	kf6-kcodecs-devel >= %{kf_ver}
BuildRequires:	kf6-kcompletion-devel >= %{kf_ver}
BuildRequires:	kf6-kconfig-devel >= %{kf_ver}
BuildRequires:	kf6-kcontacts-devel >= %{kf_ver}
BuildRequires:	kf6-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf6-ki18n-devel >= %{kf_ver}
BuildRequires:	kf6-kio-devel >= %{kf_ver}
BuildRequires:	kf6-kitemmodels-devel >= %{kf_ver}
BuildRequires:	kf6-kjobwidgets-devel >= %{kf_ver}
BuildRequires:	kf6-knewstuff-devel >= %{kf_ver}
BuildRequires:	kf6-kservice-devel >= %{kf_ver}
BuildRequires:	kf6-ktextaddons-devel >= 1.5.4
BuildRequires:	kf6-ktextwidgets-devel >= %{kf_ver}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kf_ver}
BuildRequires:	kf6-kxmlgui-devel >= %{kf_ver}
BuildRequires:	kf6-purpose-devel >= %{kf_ver}
BuildRequires:	libxslt-progs
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qt_ver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt6Core >= %{qt_ver}
Requires:	Qt6DBus >= %{qt_ver}
Requires:	Qt6Gui >= %{qt_ver}
Requires:	Qt6Network >= %{qt_ver}
Requires:	Qt6Widgets >= %{qt_ver}
Requires:	ka6-akonadi >= %{ka_ver}
Requires:	ka6-akonadi-contacts >= %{ka_ver}
Requires:	ka6-akonadi-search >= %{ka_ver}
Requires:	ka6-kimap >= %{ka_ver}
Requires:	ka6-kldap >= %{ka_ver}
Requires:	ka6-libkdepim >= %{ka_ver}
Requires:	kf6-kcmutils >= %{kf_ver}
Requires:	kf6-kcodecs >= %{kf_ver}
Requires:	kf6-kcompletion >= %{kf_ver}
Requires:	kf6-kconfig >= %{kf_ver}
Requires:	kf6-kcontacts >= %{kf_ver}
Requires:	kf6-kcoreaddons >= %{kf_ver}
Requires:	kf6-ki18n >= %{kf_ver}
Requires:	kf6-kio >= %{kf_ver}
Requires:	kf6-kitemmodels >= %{kf_ver}
Requires:	kf6-knewstuff >= %{kf_ver}
Requires:	kf6-ktextaddons >= 1.5.4
Requires:	kf6-kwidgetsaddons >= %{kf_ver}
Requires:	kf6-kxmlgui >= %{kf_ver}
Requires:	kf6-purpose >= %{kf_ver}
Obsoletes:	ka5-pimcommon < 24
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Common PIM libraries.

%description -l pl.UTF-8
Wspólne biblioteki PIM.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6DBus-devel >= %{qt_ver}
Requires:	Qt6Gui-devel >= %{qt_ver}
Requires:	Qt6Widgets-devel >= %{qt_ver}
Requires:	kf6-kconfig-devel >= %{kf_ver}
Requires:	kf6-kio-devel >= %{kf_ver}
Requires:	kf6-ktextaddons-devel >= 1.5.4
Obsoletes:	ka5-pimcommon-devel < 24

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang libpimcommon6

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libpimcommon6.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libKPim6PimCommon.so.*.*.*
%ghost %{_libdir}/libKPim6PimCommon.so.6
%attr(755,root,root) %{_libdir}/libKPim6PimCommonAkonadi.so.*.*.*
%ghost %{_libdir}/libKPim6PimCommonAkonadi.so.6
%ghost %{_libdir}/libKPim6PimCommonActivities.so.6
%attr(755,root,root) %{_libdir}/libKPim6PimCommonActivities.so.*.*.*
%attr(755,root,root) %{_libdir}/qt6/plugins/designer/pimcommon6akonadiwidgets.so
%attr(755,root,root) %{_libdir}/qt6/plugins/designer/pimcommon6widgets.so
%{_datadir}/qlogging-categories6/pimcommon.categories
%{_datadir}/qlogging-categories6/pimcommon.renamecategories

%files devel
%defattr(644,root,root,755)
%{_libdir}/libKPim6PimCommon.so
%{_libdir}/libKPim6PimCommonAkonadi.so
%{_libdir}/libKPim6PimCommonActivities.so
%{_includedir}/KPim6/PimCommon
%{_includedir}/KPim6/PimCommonAkonadi
%{_includedir}/KPim6/PimCommonActivities
%{_libdir}/cmake/KPim6PimCommon
%{_libdir}/cmake/KPim6PimCommonAkonadi
%{_libdir}/cmake/KPim6PimCommonActivities
