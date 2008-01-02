Summary:	Gerber file viewer
Name: 		gerbv
Version:	1.0.1
Release: 	%mkrel 2
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		gerbv-1.0.1-gcc4.patch.bz2
URL:		http://gerbv.sourceforge.net
License:	GPL 
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
%patch0 -p1 -b .gcc4

%build
%configure --enable-exportpng --enable-gtk2
make all

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
%{_datadir}/gerbv/scheme/init.scm

%files examples
%defattr(-,root,root)
%dir %{_datadir}/gerbv/example
%{_datadir}/gerbv/example/*

