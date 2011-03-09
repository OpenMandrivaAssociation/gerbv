%define major 1
%define libname %mklibname %name %major
%define develname %mklibname -d %name

Summary:	Gerber file viewer
Name: 		gerbv
Version:	2.5.0
Release: 	%mkrel 1
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://gerbv.gpleda.org/
License:	GPLv2+
Group: 		Graphics
BuildRoot:    	%{_tmppath}/%{name}-root
BuildRequires:	gtk+2-devel glib2-devel pango-devel atk-devel freetype2-devel
Suggests:	%name-examples = %version

%description
Gerbv is a viewer for Gerber files. Gerber files are generated from PCB CAD 
system and sent to PCB manufacturers as basis for the manufacturing process.

%package examples
Summary:	Gerber file examples for gerbv
Requires:	gerbv
Group: 		Graphics

%description examples
Example files for gerbv.

%package -n %libname
Summary:	Libraries for gerbv
Group:		Graphics

%description -n %libname
Libraries for gerbv.

%package -n %develname
Summary:	Development files for gerbv
Group:		Graphics
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}

%description -n %develname
Development files for gerbv

%prep
%setup -q

%build
%configure2_5x --enable-exportpng --enable-gtk2 --disable-static --disable-update-desktop-database
%make

%install
rm -fr %buildroot
%makeinstall_std

cp -fr doc example %buildroot%_datadir/%name

%clean
rm -Rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/gerbv
%{_mandir}/man1/gerbv.*
%dir %{_datadir}/gerbv
%{_datadir}/gerbv/gerbv_icon.ico
%{_datadir}/gerbv/doc
%{_datadir}/gerbv/scheme
%_iconsdir/hicolor/*/*/*
%_datadir/applications/*.desktop

%files examples
%defattr(-,root,root)
%{_datadir}/gerbv/example

%files -n %libname
%defattr(-,root,root)
%_libdir/*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_libdir/*.so
%_libdir/*.la
%_libdir/pkgconfig/*.pc
%_includedir/*
