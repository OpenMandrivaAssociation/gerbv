Summary:	Gerber file viewer
Name: 		gerbv
Version:	2.0.0
Release: 	%mkrel 1
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://gerbv.sourceforge.net
License:	GPLv2+
Group: 		Graphics
BuildRoot:    	%{_tmppath}/%{name}-root
BuildRequires:	gtk+2-devel glib2-devel pango-devel atk-devel freetype2-devel	

%description
Gerbv is a viewer for Gerber files. Gerber files are generated from PCB CAD 
system and sent to PCB manufacturers as basis for the manufacturing process.

%package examples
Summary:	Gerber file examples for gerbv
Requires:	gerbv
Group: 		Graphics

%description examples
Example files for gerbv.


%prep
%setup -q 

%build
%configure2_5x --enable-exportpng --enable-gtk2
%make

%install
make install DESTDIR=$RPM_BUILD_ROOT
strip $RPM_BUILD_ROOT%{_bindir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gerbv
cp -r example $RPM_BUILD_ROOT%{_datadir}/gerbv
cp -r doc $RPM_BUILD_ROOT%{_datadir}/gerbv

%clean
rm -Rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%dir %{_datadir}/gerbv
%dir %{_datadir}/gerbv/doc
%dir %{_datadir}/gerbv/scheme
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/gerbv
%{_mandir}/man1/gerbv.*
%{_datadir}/gerbv/doc/*
%{_datadir}/gerbv/scheme/*

%files examples
%defattr(-,root,root)
%dir %{_datadir}/gerbv/example
%{_datadir}/gerbv/example/*
