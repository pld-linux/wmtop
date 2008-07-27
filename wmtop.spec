Summary:	Dockapp version of the cpu moniotring utility top
Summary(pl.UTF-8):	Aplet będący odmianą narzędzia monitorującego top
Name:		wmtop
Version:	0.84
Release:	4
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/wmtop/%{name}-%{version}.tar.bz2
# Source0-md5:	2bab22c5bc3a5b887e7c03d6dbfe59d7
Source1:	%{name}.desktop
URL:		http://wmtop.sourceforge.net/
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wmtop is a WindowMaker dockapp that is a mini graphical version of the
cpu monitoring utility top.

%description -l pl.UTF-8
Wmtop jest apletem WindowMakera, który jest graficzną wersją narzędzia
monitorującego procesor top.

%prep
%setup -q

%build
%{__make} linux \
	CC="%{__cc}" \
	INCS="/usr/include/X11" \
	OPTS="%{rpmcflags}" \
	LIBDIR=

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

install wmtop $RPM_BUILD_ROOT%{_bindir}
install wmtop.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/docklets/*
