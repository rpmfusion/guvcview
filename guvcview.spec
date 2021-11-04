Name:           guvcview
Version:        2.0.7
Release:        1%{?dist}
Summary:        GTK+ UVC Viewer and Capturer
# fixme: ask upstream about license, many source files claim to be
# under GPLv2+
License:        GPLv3+
URL:            http://guvcview.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.bz2
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.10.0
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(libpulse) >= 0.9.15
BuildRequires:  pkgconfig(libpng)
BuildRequires:  ffmpeg-devel
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(sdl2) >= 2.0
BuildRequires:  pkgconfig(gsl) >= 1.15

BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  desktop-file-utils
# for validating the appdata file
BuildRequires:  libappstream-glib

# for bootstrapping
Buildrequires:  autoconf automake libtool


%description
A simple GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
A simple GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

This package contains development files for %{name}.


%prep
%autosetup -c -n %{name}-src-%{version}
find . \( -name '*.h' -o -name '*.c' \) -exec chmod -x {} \;


%build
./bootstrap.sh
%configure CC=gcc CXX=g++ --disable-debian-menu --disable-silent-rules --disable-static
%make_build


%install
%make_install

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


%ldconfig_scriptlets


%files -f %{name}.lang
%doc _doc/AUTHORS
%doc _doc/ChangeLog
%doc _doc/README.md
%if 0%{?_licensedir:1}
%license _doc/COPYING
%else
%doc _doc/COPYING
%endif
%{_bindir}/%{name}
%{_libdir}/libgviewaudio-2.0.so.*
%{_libdir}/libgviewencoder-2.1.so.*
%{_libdir}/libgviewrender-2.0.so.*
%{_libdir}/libgviewv4l2core-2.0.so.*
%{_mandir}/man1/%{name}.1*
%{_datadir}/pixmaps/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml


%files devel
%{_includedir}/%{name}-2/
%{_libdir}/libgviewaudio.so
%{_libdir}/libgviewencoder.so
%{_libdir}/libgviewrender.so
%{_libdir}/libgviewv4l2core.so
%{_libdir}/pkgconfig/libgviewaudio.pc
%{_libdir}/pkgconfig/libgviewencoder.pc
%{_libdir}/pkgconfig/libgviewrender.pc
%{_libdir}/pkgconfig/libgviewv4l2core.pc


%changelog
* Thu Nov  4 2021 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.7-1
- Update to 2.0.7.

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Leigh Scott <leigh123linux@gmail.com> - 2.0.6-7
- Rebuilt for new ffmpeg snapshot

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.0.6-5
- Rebuild for ffmpeg-4.3 git

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 06 2019 Leigh Scott <leigh123linux@gmail.com> - 2.0.6-3
- Rebuild for new ffmpeg version

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.0.6-1
- Updated to 2.0.6
- Remove Group tag
- Use make macros
- Drop compat-ffmpeg28 changes
- Drop old patches
- Add BuildRequires gcc-c++

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 11 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.0.5-6
- Switch to compat-ffmpeg28 for F28

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.0.5-5
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.0.5-3
- Rebuilt for ffmpeg-3.5 git

* Wed Nov 22 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.5-2
- Fix patch for older libavcodec.
- Force building with gcc/g++ instead of clang.

* Thu Nov 16 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.0.5-1
- Updated to 2.0.5
- Add upstream patch for newer libavcodec

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.0.4-6
- Rebuild for ffmpeg update

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 09 2016 Sérgio Basto <sergio@serjux.com> - 2.0.4-4
- Fix Requires on guvcview-devel

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 2.0.4-3
- Rebuilt for ffmpeg-3.1.1

* Thu Jul  7 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2.0.4-2
- Remove rpath.
- Mark COPYING as %%license.

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
