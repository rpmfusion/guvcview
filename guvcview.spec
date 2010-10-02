Name:           guvcview
Version:        1.4.2
Release:        1%{?dist}
Summary:        GTK+ UVC Viewer and Capturer
Group:          Amusements/Graphics
# fixme: ask upstream about license, many source files claim to be
# under GPLv2+
License:        GPLv3+
URL:            http://guvcview.berlios.de/
Source0:        http://download.berlios.de/%{name}/%{name}-src-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gtk2-devel
BuildRequires:  gettext
BuildRequires:  SDL-devel
BuildRequires:  libpng-devel
BuildRequires:  portaudio-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libv4l-devel


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
