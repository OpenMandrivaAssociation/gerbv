%define major 1
%define libname %mklibname %name %major
%define develname %mklibname -d %name

Summary:	Gerber file viewer
Name: 		gerbv
Version:	2.6.0
Release: 	2
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://gerbv.gpleda.org/
License:	GPLv2+
Group: 		Graphics
BuildRequires:	gtk+2-devel glib2-devel pango-devel atk-devel pkgconfig(freetype2)
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
%makeinstall_std
find %{buildroot} -name *.la -delete

cp -fr doc example %buildroot%_datadir/%name

%files 
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
%{_datadir}/gerbv/example

%files -n %libname
%_libdir/*.so.%{major}*

%files -n %develname
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/*


%changelog
* Fri Feb 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.6.0-1
+ Revision: 772403
- version update 2.6.0

* Wed Mar 09 2011 Stéphane Téletchéa <steletch@mandriva.org> 2.5.0-1
+ Revision: 643209
- update to new version 2.5.0

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4.0-3mdv2011.0
+ Revision: 610842
- rebuild

* Thu Feb 25 2010 Funda Wang <fwang@mandriva.org> 2.4.0-2mdv2010.1
+ Revision: 511119
- new version 2.4.0

* Sat Nov 14 2009 Funda Wang <fwang@mandriva.org> 2.3.0-1mdv2010.1
+ Revision: 466087
- new version 2.3.0

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 2.1.0-2mdv2010.0
+ Revision: 437670
- rebuild

* Sat Dec 27 2008 Funda Wang <fwang@mandriva.org> 2.1.0-1mdv2009.1
+ Revision: 319961
- new version 2.1.0

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.0.0-3mdv2009.0
+ Revision: 245941
- rebuild

* Thu Feb 07 2008 Funda Wang <fwang@mandriva.org> 2.0.0-1mdv2008.1
+ Revision: 163358
- New version 2.0.0

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.0.1-2mdv2008.1
+ Revision: 140735
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import gerbv

