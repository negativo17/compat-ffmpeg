%global         real_name ffmpeg

Summary:        A complete solution to record, convert and stream audio and video
Name:           compat-%{real_name}
Version:        3.4.5
Release:        4%{?dist}
License:        LGPLv3+
URL:            http://%{real_name}.org/
Epoch:          1

Source0:        http://%{real_name}.org/releases/%{real_name}-%{version}.tar.xz
Patch0:         %{real_name}-%{version}-fdk-aac-v2.patch

BuildRequires:  bzip2-devel
BuildRequires:  decklink-devel >= 10.6.1
BuildRequires:  doxygen
BuildRequires:  freetype-devel
BuildRequires:  frei0r-devel
BuildRequires:  gsm-devel
BuildRequires:  ilbc-devel
BuildRequires:  lame-devel >= 3.98.3
BuildRequires:  libcdio-paranoia-devel
BuildRequires:  libdrm-devel
BuildRequires:  libfdk-aac-devel
BuildRequires:  libndi-devel
BuildRequires:  libssh-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libxcb-devel >= 1.4
BuildRequires:  mesa-libGL-devel
# Nvidia NVENC/CUVID (both i686 and x86_64):
BuildRequires:  nvenc >= 8.0.14
Buildrequires:  ocl-icd-devel
Buildrequires:  openal-soft-devel
Buildrequires:  opencl-headers
Buildrequires:  opencore-amr-devel
BuildRequires:  openjpeg-devel
BuildRequires:  perl(Pod::Man)
BuildRequires:  soxr-devel
BuildRequires:  subversion
BuildRequires:  texinfo
BuildRequires:  twolame-devel >= 0.3.10
BuildRequires:  vo-amrwbenc-devel
BuildRequires:  xvidcore-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  zvbi-devel >= 0.2.28

BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(kvazaar) >= 0.8.1
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libdc1394-2)
BuildRequires:  pkgconfig(libmfx)
BuildRequires:  pkgconfig(libmodplug)
#BuildRequires:  pkgconfig(libopenmpt) >= 0.2.6557
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(librtmp)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libtcmalloc)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libwebp) >= 0.4.0
BuildRequires:  pkgconfig(libwebpmux) >= 0.4.0
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(openh264) >= 1.6
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(rubberband) >= 1.8.1
BuildRequires:  pkgconfig(sdl2)
#BuildRequires:  pkgconfig(shine)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(tesseract)
#BuildRequires:  pkgconfig(vidstab) >= 0.98
BuildRequires:  pkgconfig(vpx) >= 1.3.0
BuildRequires:  pkgconfig(xcb) >= 1.4
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(x264) >= 0.118
BuildRequires:  pkgconfig(x265) >= 0.68
#BuildRequires:  pkgconfig(zimg) >= 2.3.0

%ifarch %{ix86} x86_64
BuildRequires:  libXvMC-devel
BuildRequires:  libva-devel
BuildRequires:  nasm
%endif

%ifarch x86_64
BuildRequires:  cuda-devel
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
%autosetup -p1 -n %{real_name}-%{version}
# Use CUDA entry point versioned library (SONAME)
sed -i -e 's/libcuda.so/libcuda.so.1/g' libavcodec/nvenc.c

# Uncomment to enable debugging while configuring
#sed -i -e 's|#!/bin/sh|#!/bin/sh -x|g' configure

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
    --enable-cuvid \
    --enable-decklink \
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
    --enable-libdrm \
    --enable-libfdk-aac \
    --enable-libfreetype \
    --enable-libfribidi \
    --enable-libgsm \
    --enable-libilbc \
    --enable-libkvazaar \
    --enable-libmfx \
    --enable-libmp3lame \
    --enable-libopencore-amrnb \
    --enable-libopencore-amrwb \
    --enable-libopenh264 \
    --enable-libopenjpeg \
    --enable-libopus \
    --enable-libpulse \
    --enable-librsvg \
    --enable-librtmp \
    --enable-librubberband \
    --enable-libsoxr \
    --enable-libspeex \
    --enable-libssh \
    --enable-libtesseract \
    --enable-libtheora \
    --enable-libtwolame \
    --enable-libv4l2 \
    --enable-libvo-amrwbenc \
    --enable-libvorbis \
    --enable-libvpx \
    --enable-libwebp \
    --enable-libx264 \
    --enable-libx265 \
    --enable-libxcb \
    --enable-libxcb-shm \
    --enable-libxcb-xfixes \
    --enable-libxcb-shape \
    --enable-libxvid \
    --enable-libzvbi \
    --enable-lzma \
    --enable-libndi_newtek \
    --enable-nonfree \
    --enable-openal \
    --enable-opencl \
    --enable-nvenc \
    --enable-opengl \
    --enable-postproc \
    --enable-pthreads \
    --enable-sdl2 \
    --enable-shared \
    --enable-version3 \
    --enable-xlib \
    --enable-zlib \
    --extra-cflags="-I%{_includedir}/nvenc -I%{_includedir}/cuda" \
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
%ifarch x86_64
    --enable-cuda \
    --enable-libnpp \
%endif

%make_build
make documentation

%install
%make_install
# Let rpmbuild pick up the docs
rm -fr %{buildroot}%{_docdir}/*
rm -fr %{buildroot}%{_datadir}/%{name}/examples
mkdir doc/html
mv doc/*.html doc/html

%ldconfig_scriptlets libs

%files libs
%license COPYING.* LICENSE.md
%doc MAINTAINERS README.md CREDITS Changelog RELEASE_NOTES
%{_libdir}/lib*.so.*

%files devel
%doc doc/APIchanges doc/*.txt
%doc doc/html doc/examples
%{_includedir}/%{name}
%{_libdir}/pkgconfig/lib*.pc
%{_libdir}/lib*.so

%changelog
* Sun Apr 07 2019 Simone Caronni <negativo17@gmail.com> - 1:3.4.5-4
- Rebuild for CUDA 10.1.

* Thu Feb 28 2019 Simone Caronni <negativo17@gmail.com> - 1:3.4.5-3
- Rebuild for updated dependencies.

* Fri Jan 04 2019 Simone Caronni <negativo17@gmail.com> - 1:3.4.5-2
- Rebuild for CUDA 10.0.

* Mon Nov 12 2018 Simone Caronni <negativo17@gmail.com> - 1:3.4.5-1
- Update to 3.4.5.

* Sat Oct 20 2018 Simone Caronni <negativo17@gmail.com> - 1:3.4.4-4
- Rebuild for updated dependencies.

* Wed Sep 19 2018 Simone Caronni <negativo17@gmail.com> - 1:3.4.4-3
- Rebuild for updated dependencies.

* Tue Aug 28 2018 Simone Caronni <negativo17@gmail.com> - 1:3.4.4-2
- Rebuild for CUDA update.

* Fri Jul 20 2018 Simone Caronni <negativo17@gmail.com> - 1:3.4.4-1
- Update to 3.4.4.

* Mon Jul 16 2018 Simone Caronni <negativo17@gmail.com> - 1:3.4.3-1
- Update to 3.4.3.

* Fri Apr 27 2018 Simone Caronni <negativo17@gmail.com> - 1:3.4.2-1
- Update to 3.4.2, update all build requirements.
- Update SPEC file.

* Wed Apr 25 2018 Simone Caronni <negativo17@gmail.com> - 1:2.8.14-2
- Rebuild for updated libraries.

* Tue Apr 10 2018 Simone Caronni <negativo17@gmail.com> - 1:2.8.14-1
- Update to 2.8.14.

* Wed Jan 10 2018 Simone Caronni <negativo17@gmail.com> - 1:2.8.13-3
- Rebuild for the various updates.

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
