%global engine_name unico

Name:           gtk-unico-engine
Version:        1.0.1
Release:        2%{?dist}
Summary:        Unico Gtk+ theming engine

Group:          User Interface/Desktops
License:        LGPLv3
URL:            https://launchpad.net/unico/
Source0:        http://launchpad.net/unico/1.0/%{version}/+download/%{engine_name}-%{version}.tar.gz

BuildRequires:  gtk3-devel >= 3.1.10

%description
Unico is a Gtk+ engine that aims to be the more complete yet powerful theming
engine for Gtk+ 3.0 and newer. It’s the first Gtk+ engine written with Gtk+
style context APIs in mind, using CSS as first class citizen.


%prep
%setup -q -n %{engine_name}-%{version}


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/3.0.0/theming-engines/*.la


%files
# TODO: add ChangeLog and README if non-empty
%doc AUTHORS COPYING NEWS
%{_libdir}/gtk-3.0/3.0.0/theming-engines/lib%{engine_name}.so


