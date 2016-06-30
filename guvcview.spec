Name:           guvcview
Version:        2.0.4
Release:        1%{?dist}
Summary:        GTK+ UVC Viewer and Capturer
Group:          Amusements/Graphics
# fixme: ask upstream about license, many source files claim to be
# under GPLv2+
License:        GPLv3+
URL:            http://guvcview.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.gz
Patch0:         ffmpeg3.patch
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.10.0
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(libpulse) >= 0.9.15
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(sdl2) >= 2.0
BuildRequires:  pkgconfig(gsl) >= 1.15

BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  desktop-file-utils
# for validating the appdate file
BuildRequires:  libappstream-glib


%description
A simple GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.


%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
A simple GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

This package contains development files for %{name}.


%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p1 -b .ffmpeg3
find . \( -name '*.h' -o -name '*.c' \) -exec chmod -x {} \;


%build
%configure --disable-debian-menu --disable-silent-rules --disable-static
make -k %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

desktop-file-install \
        --add-category='X-AudioVideoCapture' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name} --all-name

mv %{buildroot}%{_datadir}/doc/%{name} _doc
rm _doc/INSTALL

# does not validate currently
appstream-util validate-relax --nonet \
        %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files -f %{name}.lang
%doc _doc/*
%{_bindir}/%{name}
%{_libdir}/libgviewaudio-2.0.so.*
%{_libdir}/libgviewencoder-2.0.so.*
%{_libdir}/libgviewrender-2.0.so.*
%{_libdir}/libgviewv4l2core-2.0.so.*
%{_mandir}/man1/%{name}.1*
%{_datadir}/pixmaps/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml


%files devel
%{_includedir}/%{name}-2
%{_libdir}/libgviewaudio.so
%{_libdir}/libgviewencoder.so
%{_libdir}/libgviewrender.so
%{_libdir}/libgviewv4l2core.so
%{_libdir}/pkgconfig/libgviewaudio.pc
%{_libdir}/pkgconfig/libgviewencoder.pc
%{_libdir}/pkgconfig/libgviewrender.pc
%{_libdir}/pkgconfig/libgviewv4l2core.pc


%changelog
* Thu Jun 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 2.0.4-1
- Updated to 2.0.4
- Fixed build with ffmpeg-3.0.x using a patch from Gentoo

* Fri Jun 26 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.1-1
- Update to 2.0.1.
- Update build requirements.
- Create -devel subpackage.

* Sun Oct 19 2014 Sérgio Basto <sergio@serjux.com> - 1.7.3-4
- Rebuilt for FFmpeg 2.4.3

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 1.7.3-2
- Rebuilt for ffmpeg-2.3

* Sat Jun 14 2014 Thomas Moschny <thomas.moschny@gmx.de> - 1.7.3-1
- Update to 1.7.3.

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> - 1.6.1-7
- Rebuilt for ffmpeg-2.2

* Mon Sep 30 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.6.1-6
- Rebuilt

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.6.1-5
- Rebuilt for FFmpeg 2.0.x

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.6.1-4
- Rebuilt for x264/FFmpeg

* Sun Apr 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.6.1-3
- https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.6.1-2
- Rebuilt for FFmpeg 1.0

* Sun Oct  7 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.6.1-1
- Update to the released 1.6.1 version.

* Mon Jul 16 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.6.1-0.1.20120714gitd7e9ed30
- Update to latest git version, for FFmpeg compatibility.
- Pulseaudio support is enabled per default now.
- Enable more verbose compile output.
- Add missing BR.

* Wed Jul 11 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.5.3-3
- Rebuilt for libudev1

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.5.3-2
- Rebuilt for FFmpeg

* Mon Mar  5 2012 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.3-1
- Update to 1.5.3.
- Remove patch applied upstream.
- Update build requirements.

* Mon Dec 19 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.1-2
- Add patch for compiling with glib2 2.31 or later.

* Sun Dec 18 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.1-1
- Update to 1.5.1.
- Rewrite build requirements using pkgconfig(...).
- Update URL and Source tags (project moved to sf.net).

* Sun Sep  4 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.5.0-1
- Update to 1.5.0.

* Thu Apr 28 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.5-1
- Update to 1.4.5.

* Tue Jan 18 2011 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.4-1
- Update to 1.4.4.

* Mon Nov 29 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.3-1
- Update to 1.4.3.

* Thu Sep 30 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.2-1
- Update to 1.4.2.

* Wed Jun 30 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.1-1
- Update to 1.4.1.

* Wed Jun 16 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.4.0-1
- Update to 1.4.0.

* Thu Apr 29 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.1-3
- Desktop file fixes:
  - Don't apply a vendor prefix.
  - Add X-AudioVideoCapture category.
- Don't pack INSTALL file.

* Sat Apr 24 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.1-2
- Remove BR autoconf, not needed anymore.
- Disable Debian menu file.

* Sat Apr 24 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.1-1
- Update to 1.3.1.

* Thu Mar 11 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.0-1
- Update to 1.3.0.
- Add build time dependency on libv4l-devel.
- Patching configure.in is no longer necessary.

* Sat Feb  6 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.2.2-2
- Set CPPFLAGS, so configure finds avcodec.h.

* Sat Feb  6 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.2.2-1
- Update to 1.2.2.

* Tue Jan 12 2010 Thomas Moschny <thomas.moschny@gmx.de> - 1.2.1-1
- Initial version.
