Name:           nvidia-vaapi-driver
Version:        0.0.7
Release:        0
Summary:        Nvidia Driver for Video Acceleration (VA) API for Linux
License:        MIT
Group:          System/Libraries
URL:            https://github.com/elFarto/nvidia-vaapi-driver
Source0:        https://github.com/elFarto/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  meson >= 0.58.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(ffnvcodec) >= 11.1.5.1
BuildRequires:  pkgconfig(gstreamer-codecparsers-1.0)
BuildRequires:  pkgconfig(libva) >= 1.8.0
Conflicts:      libva-vdpau-driver

%description
This is an VA-API implementation that uses NVDEC as a backend.
This implementation is specifically designed to be used by Firefox
for accelerated decode of web content, and may not operate correctly
in other applications.

This library requires that the nvidia_drm kernel module
is configured with the parameter nvidia-drm.modeset=1

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%dir %{_libdir}/dri
%{_libdir}/dri/nvidia_drv_video.so
