%global         real_name ffmpeg

Summary:        A complete solution to record, convert and stream audio and video
Name:           compat-%{real_name}
Version:        2.8.13
Release:        2%{?dist}
License:        LGPLv3+
URL:            http://%{real_name}.org/
Epoch:          1

Source0:        http://%{real_name}.org/releases/%{real_name}-%{version}.tar.xz

BuildRequires:  bzip2-devel
BuildRequires:  doxygen
BuildRequires:  faac-devel
BuildRequires:  freetype-devel
BuildRequires:  frei0r-devel
BuildRequires:  fribidi-devel
BuildRequires:  gnutls-devel
BuildRequires:  gsm-devel
BuildRequires:  lame-devel >= 3.98.3
BuildRequires:  libass-devel
BuildRequires:  libbluray-devel
BuildRequires:  libcdio-paranoia-devel
BuildRequires:  libdc1394-devel
BuildRequires:  libfdk-aac-devel
Buildrequires:  libmfx-devel
Buildrequires:  libmodplug-devel
BuildRequires:  librtmp-devel
BuildRequires:  libssh-devel
BuildRequires:  libtheora-devel
BuildRequires:  libv4l-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libvo-aacenc-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libvpx-devel
BuildRequires:  libwebp-devel >= 0.2.0
BuildRequires:  nvenc
Buildrequires:  ocl-icd-devel
Buildrequires:  openal-soft-devel
Buildrequires:  opencl-headers
Buildrequires:  opencore-amr-devel
Buildrequires:  openh264-devel
BuildRequires:  openjpeg-devel
BuildRequires:  opus-devel
BuildRequires:  perl(Pod::Man)
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  schroedinger-devel
BuildRequires:  SDL-devel
BuildRequires:  soxr-devel
BuildRequires:  speex-devel
BuildRequires:  subversion
BuildRequires:  texinfo
BuildRequires:  twolame-devel >= 0.3.10
BuildRequires:  vo-amrwbenc-devel
BuildRequires:  x264-devel >= 0.118
BuildRequires:  x265-devel >= 0.57
BuildRequires:  xvidcore-devel
BuildRequires:  zlib-devel

%ifarch %{ix86} x86_64
BuildRequires:  libXvMC-devel
BuildRequires:  libva-devel
BuildRequires:  yasm
%endif

%description
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.

%package        libs
Summary:        Libraries for %{name}

%description    libs
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains the libraries for %{name}.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}-libs%{_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       pkgconfig

%description    devel
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains development files for %{name}.

%prep
%setup -qn %{real_name}-%{version}
# Dynamically load libcuda.so.1 (SONAME)
sed -i -e 's/libcuda.so/libcuda.so.1/g' libavcodec/nvenc.c

%build
./configure \
    --arch=%{_target_cpu} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir}/%{name} \
    --disable-debug \
    --disable-programs \
    --disable-static \
    --disable-stripping \
    --enable-avfilter \
    --enable-avresample \
    --enable-bzlib \
    --enable-doc \
    --enable-fontconfig \
    --enable-frei0r \
    --enable-gnutls \
    --enable-gpl \
    --enable-iconv \
    --enable-libass \
    --enable-libbluray \
    --enable-libcdio \
    --enable-libdc1394 \
    --enable-libfaac \
    --enable-libfdk-aac \
    --enable-libfreetype \
    --enable-libfribidi \
    --enable-libgsm \
    --disable-libkvazaar \
    --enable-libmfx \
    --enable-libmp3lame \
    --enable-libopencore-amrnb \
    --enable-libopencore-amrwb \
    --enable-libopenjpeg \
    --enable-libopus \
    --enable-libpulse \
    --enable-librtmp \
    --enable-libschroedinger \
    --enable-libsoxr \
    --enable-libspeex \
    --enable-libssh \
    --enable-libtheora \
    --enable-libtwolame \
    --enable-libv4l2 \
    --enable-libvo-aacenc \
    --enable-libvo-amrwbenc \
    --enable-libvorbis \
    --enable-libvpx \
    --enable-libwebp \
    --enable-libx264 \
    --enable-libx265 \
    --enable-libxvid \
    --enable-lzma \
    --enable-nonfree \
    --enable-openal \
    --enable-opencl \
    --enable-nvenc --extra-cflags=-I%{_includedir}/nvenc \
    --enable-opengl \
    --enable-postproc \
    --enable-pthreads \
    --enable-sdl \
    --enable-shared \
    --enable-version3 \
    --enable-x11grab \
    --enable-xlib \
    --enable-zlib \
    --incdir=%{_includedir}/%{name} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --optflags="%{optflags}" \
    --prefix=%{_prefix} \
    --shlibdir=%{_libdir} \
%ifarch %{ix86}
    --cpu=%{_target_cpu} \
%endif
%ifarch %{ix86} x86_64 ppc ppc64
    --enable-runtime-cpudetect \
%endif
%ifarch ppc
    --cpu=g3 \
    --enable-pic \
%endif
%ifarch ppc64
    --cpu=g5 \
    --enable-pic \
%endif
%ifarch %{arm}
    --disable-runtime-cpudetect --arch=arm \
%ifarch armv6hl
    --cpu=armv6 \
%else
    --enable-thumb \
%endif
%ifarch armv7hnl
    --enable-neon \
%endif
%endif

%make_build
make documentation

%install
%make_install
# Let rpmbuild pick up the docs
rm -fr %{buildroot}%{_docdir}/*
mkdir doc/html
mv doc/*.html doc/html

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files libs
%{!?_licensedir:%global license %%doc}
%license COPYING.* LICENSE.md
%doc MAINTAINERS README.md CREDITS Changelog RELEASE_NOTES
%{_libdir}/lib*.so.*

%files devel
%doc doc/APIchanges doc/*.txt
%doc doc/html
%{_includedir}/%{name}
%{_libdir}/pkgconfig/lib*.pc
%{_libdir}/lib*.so

%changelog
* Wed Oct 25 2017 Simone Caronni <negativo17@gmail.com> - 1:2.8.13-2
- Rebuild for x264 and x265 update.

* Sun Sep 10 2017 Simone Caronni <negativo17@gmail.com> - 1:2.8.13-1
- Update to 2.8.13.

* Mon Aug 14 2017 Simone Caronni <negativo17@gmail.com> - 1:2.8.12-2
- Rebuild for libwebp 0.6 drop.

* Thu Jun 08 2017 Simone Caronni <negativo17@gmail.com> - 1:2.8.12-1
- Update to 2.8.12.

* Thu May 11 2017 Simone Caronni <negativo17@gmail.com> - 1:2.8.11-4
- Rebuild for x265 upgrade.

* Wed Mar 22 2017 Simone Caronni <negativo17@gmail.com> - 1:2.8.11-3
- Rebuild for libbluray update.

* Sun Feb 26 2017 Simone Caronni <negativo17@gmail.com> - 1:2.8.11-2
- Rebuild for x265 update.

* Thu Feb 16 2017 Simone Caronni <negativo17@gmail.com> - 1:2.8.11-1
- Update to 2.8.11.
- Remove support for deprecated HE-AAC audio (libaacplus).

* Tue Jan 03 2017 Simone Caronni <negativo17@gmail.com> - 1:2.8.10-2
- Rebuild for x265 2.2.

* Mon Dec 12 2016 Simone Caronni <negativo17@gmail.com> - 1:2.8.10-1
- Update to 2.8.10.

* Thu Nov 10 2016 Simone Caronni <negativo17@gmail.com> - 1:2.8.8-4
- Create compat package from latest 2.8 ffmpeg package.
- Do not recommend Nvidia driver libraries anymore for dynamic NVENC support.
- Remove Kvazaar and OpenH264 support.
- Merge libavdevice in main libs package.

* Sat Oct 08 2016 Simone Caronni <negativo17@gmail.com> - 1:2.8.8-3
- Rebuild for fdk-aac update.

* Sun Oct 02 2016 Simone Caronni <negativo17@gmail.com> - 1:2.8.8-2
- Rebuild for x265 update.

* Mon Sep 19 2016 Simone Caronni <negativo17@gmail.com> - 1:2.8.8-1
- Update to 2.8.8.

* Sat Aug 20 2016 Simone Caronni <negativo17@gmail.com> - 1:2.8.7-2
- Rebuild for Nvidia Video SDK update.

* Mon May 30 2016 Simone Caronni <negativo17@gmail.com> - 1:2.8.7-1
- Update to 2.8.7.

* Mon Apr 04 2016 Simone Caronni <negativo17@gmail.com> - 1:2.8.6-2
- Rebuild for libva update.

* Wed Mar 16 2016 Simone Caronni <negativo17@gmail.com> - 1:2.8.6-1
- Update to 2.8.6.

* Sat Jan 16 2016 Simone Caronni <negativo17@gmail.com> - 1:2.8.5-1
- Update to 2.8.5.
- Build with NVENC SDK 6.

* Wed Jan 06 2016 Simone Caronni <negativo17@gmail.com> - 1:2.8.4-1
- Update to 2.8.4.
- Look for libcuda.so.1 instead of libcuda.so.

* Sun Dec 13 2015 Simone Caronni <negativo17@gmail.com> - 1:2.8.3-2
- Remove VA-API conditional.
- Add libaacplus support.

* Tue Dec 01 2015 Simone Caronni <negativo17@gmail.com> - 1:2.8.3-1
- Update to 2.8.3.

* Mon Nov 30 2015 Simone Caronni <negativo17@gmail.com> - 1:2.8.2-4
- Add libcdio, opencl, frei0r and iconv support (fixes support for subtitles in
  HandBrake).

* Fri Nov 27 2015 Simone Caronni <negativo17@gmail.com> - 1:2.8.2-3
- Enable libmfx (Intel Quick Sync) and openal.
- Recommend instead of suggesting Nvidia CUDA libraries so they are installed
  automatically if the Nvidia repository is available.

* Fri Nov 20 2015 Simone Caronni <negativo17@gmail.com> - 1:2.8.2-2
- Add doxygen for building docs.
- Bump Epoch so that is not overwritten by RPMFusion package.

* Fri Nov 20 2015 Simone Caronni <negativo17@gmail.com> - 2.8.2-1
- Update to 2.8.2.
- Enabled the following encoders/decoders/transports:
    libvpx, libwebp, fdk-aac, opengl, fontconfig, openal, lzma, libbluray,
    libssh, libvo-aacenc, libvo-amrwbenc, libopencore-amrwb, libopencore-amrnb,
    librtmp, libopenh264, libfribidi.
- Remove CrystalHD and libcelt options.
- Hardcode some other enablements.
- Introduce weak dependency for CUDA libraries to be used with NVENC.
- Sort buildrequires.
- Add additional license information and documentation.

* Mon Sep 28 2015 Simone Caronni <negativo17@gmail.com> - 2.7.2-1
- Update to 2.7.2.

* Wed Jul 29 2015 Simone Caronni <negativo17@gmail.com> - 2.6.4-1
- Update to 2.6.4.
- Switch to xz tarball.

* Mon Jun 08 2015 Simone Caronni <negativo17@gmail.com> - 2.6.3-1
- Update to 2.6.3.
- Disable OpenCL by default on CentOS/RHEL.
- Add license/make_install/_pkgdocdir macro.

* Wed May 06 2015 Simone Caronni <negativo17@gmail.com> - 2.6.2-2
- Add Nvidia library dependency for NVENC.

* Tue Apr 28 2015 Simone Caronni <negativo17@gmail.com> - 2.6.2-1
- Update to 2.6.2.

* Wed Apr 22 2015 Simone Caronni <negativo17@gmail.com> - 2.6.1-2
- Rebuild for x265 update.

* Fri Apr 10 2015 Simone Caronni <negativo17@gmail.com> - 2.4.8-2
- Update to 2.6.1.
- Remove support for snapshots from SPEC file, simplify a bit.
- Remove libdirac support.
- Add optional nvenc (Nvidia Encoder) support.

* Mon Mar 30 2015 Julian Sikorski <belegdol@fedoraproject.org> - 2.4.8-1
- Updated to 2.4.8

* Sun Feb 15 2015 Julian Sikorski <belegdol@fedoraproject.org> - 2.4.7-1
- Updated to 2.4.7

* Sun Feb 01 2015 Dominik Mierzejewski <rpm at greysector.net> - 2.4.6-3
- enable LADSPA support (rfbz#3134)

* Sun Feb 01 2015 Dominik Mierzejewski <rpm at greysector.net> - 2.4.6-2
- enable OpenCL support
- BR texinfo instead of texi2html to reduce BRs by half
- drop support for building on SPARC (no longer a Fedora Secondary Arch)
- move libavdevice to a subpackage (rfbz#3075)

* Wed Jan 14 2015 Julian Sikorski <belegdol@fedoraproject.org> - 2.4.6-1
- Updated to 2.4.6
