#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.08.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		pimcommon
Summary:	Common PIM libraries
Name:		ka6-%{kaname}
Version:	24.08.2
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	56afaecf4985cde86874464c2d302d91
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Designer-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6Test-devel
BuildRequires:	Qt6UiTools-devel >= 5.11.1
BuildRequires:	Qt6Widgets-devel
BuildRequires:	Qt6Xml-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	grantlee-qt6-devel >= 5.1
BuildRequires:	ka6-akonadi-contacts-devel >= %{kdeappsver}
BuildRequires:	ka6-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka6-kimap-devel >= %{kdeappsver}
BuildRequires:	ka6-kmime-devel >= %{kdeappsver}
BuildRequires:	ka6-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	ka6-libkdepim-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-karchive-devel >= %{kframever}
BuildRequires:	kf6-kcodecs-devel >= %{kframever}
BuildRequires:	kf6-kcompletion-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf6-kcontacts-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-kitemmodels-devel >= %{kframever}
BuildRequires:	kf6-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf6-knewstuff-devel >= %{kframever}
BuildRequires:	kf6-kservice-devel >= %{kframever}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	kf6-purpose-devel >= %{kframever}
BuildRequires:	ktextaddons-devel
BuildRequires:	libxslt-progs
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
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
Obsoletes:	ka5-%{kaname}-devel < %{version}

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

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libKPim6PimCommon.so.*.*
%ghost %{_libdir}/libKPim6PimCommon.so.6
%attr(755,root,root) %{_libdir}/libKPim6PimCommonAkonadi.so.*.*
%ghost %{_libdir}/libKPim6PimCommonAkonadi.so.6
%attr(755,root,root) %{_libdir}/qt6/plugins/designer/pimcommon6akonadiwidgets.so
%attr(755,root,root) %{_libdir}/qt6/plugins/designer/pimcommon6widgets.so
%{_datadir}/qlogging-categories6/pimcommon.categories
%{_datadir}/qlogging-categories6/pimcommon.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KPim6/PimCommon
%{_includedir}/KPim6/PimCommonAkonadi
%{_libdir}/cmake/KPim6PimCommon
%{_libdir}/cmake/KPim6PimCommonAkonadi
%{_libdir}/libKPim6PimCommon.so
%{_libdir}/libKPim6PimCommonAkonadi.so
