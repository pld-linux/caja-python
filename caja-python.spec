# NOTE: despite upstream name python-caja, it's not a binding from Python to Caja,
# but from Caja to Python, allowing to write Caja extensions in Python - thus our Name.
Summary:	Python bindings for libcaja-extension library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki libcaja-extension
Name:		caja-python
Version:	1.8.1
Release:	1
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://pub.mate-desktop.org/releases/1.8/python-caja-%{version}.tar.xz
# Source0-md5:	9419ca3e13de36efe1c3fd60696d22cf
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.10
BuildRequires:	caja-devel >= 1.6.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.7
# pygobject3 is preferred over pygobject 2 with no configure switch
BuildRequires:	python-pygobject3-devel >= 3.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	caja >= 1.6.0
Requires:	python-libs
Obsoletes:	mate-file-manager-python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for libcaja-extension library, allowing to write Caja
extensions in Python.

%description -l pl.UTF-8
Wiązania Pythona do biblioteki libcaja-extension, pozwalające na
tworzenie rozszerzeń zarządcy plików Caja w Pythonie.

%package devel
Summary:	Development files for Python Caja extensions
Summary(pl.UTF-8):	Pliki programistyczne dla pythonowych rozszerzeń zarządcy plików Caja
Group:		Development/Libraries
# doesn't require base; the only file is pkg-config specific, so let's require it
Requires:	pkgconfig
Obsoletes:	mate-file-manager-python-devel

%description devel
Development files for Caja extensions written in Python.

%description devel -l pl.UTF-8
Pliki programistyczne dla rozszerzeń zarządcy plików Caja pisanych w
Pythonie.

%package apidocs
Summary:	Python Caja API documentation
Summary(pl.UTF-8):	Dokumentacja API Pythona dla rozszerzeń zarządcy plików Caja
Group:		Documentation
Obsoletes:	mate-file-manager-python-apidocs

%description apidocs
Python Caja API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Pythona dla rozszerzeń zarządcy plików Caja.

%package examples
Summary:	Example Python extensions for Caja file manager
Summary(pl.UTF-8):	Przykładowe pythonowe rozszerzenia dla zarządcy plików Caja
Group:		Documentation
Obsoletes:	mate-file-manager-python-examples

%description examples
Example Python extensions for Caja file manager.

%description examples -l pl.UTF-8
Przykładowe rozszerzenia dla zarządcy plików Caja napisane w Pythonie.

%prep
%setup -q -n python-caja-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTMLdir=%{_gtkdocdir}/caja-python

%{__rm} $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/*.la

# not installed because of incomplete docs/Makefile
cp -p docs/html/* $RPM_BUILD_ROOT%{_gtkdocdir}/caja-python

# examples
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/python-caja/README $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__mv} $RPM_BUILD_ROOT%{_docdir}/python-caja/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# directory for python plugins for caja - see src/caja-python.c or caja-python.pc
install -d $RPM_BUILD_ROOT%{_datadir}/caja-python/extensions

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-python.so
%dir %{_datadir}/caja-python
%dir %{_datadir}/caja-python/extensions

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/caja-python.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/caja-python

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
