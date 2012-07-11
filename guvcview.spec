Name:           guvcview
Version:        1.5.3
Release:        3%{?dist}
Summary:        GTK+ UVC Viewer and Capturer
Group:          Amusements/Graphics
# fixme: ask upstream about license, many source files claim to be
# under GPLv2+
License:        GPLv3+
URL:            http://guvcview.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.10.0
BuildRequires:  pkgconfig(gdk-3.0) >= 3.0.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(sdl) >= 1.2.10
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  gettext
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  desktop-file-utils


%description
A simple GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.


%prep
%setup -q -n %{name}-src-%{version}
find src -type f -exec chmod u=rw,go=r {} \;


%build
CPPFLAGS=-I/usr/include/ffmpeg
export CPPFLAGS
%configure --enable-pulse --disable-debian-menu
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

desktop-file-install \
        --add-category='X-AudioVideoCapture' \
        --dir %{buildroot}%{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

mv %{buildroot}%{_datadir}/doc/%{name} _doc
rm _doc/INSTALL


%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc _doc/*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/pixmaps/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
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
