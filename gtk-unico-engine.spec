%global engine_name unico

Name:           gtk-unico-engine
Version:        1.0.1
Release:        2
Summary:        Unico Gtk+ theming engine
Group:          Graphical desktop/GNOME
License:        LGPLv3
URL:            https://launchpad.net/unico/
Source0:        http://launchpad.net/unico/1.0/%{version}/+download/%{engine_name}-%{version}.tar.gz
BuildRequires:  pkgconfig(gtk+-3.0)

%description
Unico is a Gtk+ engine that aims to be the more complete yet powerful theming
engine for Gtk+ 3.0 and newer. It’s the first Gtk+ engine written with Gtk+
style context APIs in mind, using CSS as first class citizen.

%prep
%setup -qn %{engine_name}-%{version}

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc AUTHORS COPYING NEWS
%{_libdir}/gtk-3.0/3.0.0/theming-engines/lib%{engine_name}.so



%changelog
* Fri Mar 02 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.0.1-1
+ Revision: 781818
- cleaned up spec for mdv
- imported package gtk-unico-engine


* Mon Oct 03 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.1-2
- Remove useless IM scriptlets

* Thu Sep 29 2011 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.1-1
- Initial RPM release
