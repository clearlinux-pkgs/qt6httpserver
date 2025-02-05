#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : qt6httpserver
Version  : 6.8.2
Release  : 23
URL      : https://download.qt.io/official_releases/qt/6.8/6.8.2/submodules/qthttpserver-everywhere-src-6.8.2.zip
Source0  : https://download.qt.io/official_releases/qt/6.8/6.8.2/submodules/qthttpserver-everywhere-src-6.8.2.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0
Requires: qt6httpserver-lib = %{version}-%{release}
Requires: qt6httpserver-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the qt6httpserver package.
Group: Development
Requires: qt6httpserver-lib = %{version}-%{release}
Provides: qt6httpserver-devel = %{version}-%{release}
Requires: qt6httpserver = %{version}-%{release}

%description dev
dev components for the qt6httpserver package.


%package lib
Summary: lib components for the qt6httpserver package.
Group: Libraries
Requires: qt6httpserver-license = %{version}-%{release}

%description lib
lib components for the qt6httpserver package.


%package license
Summary: license components for the qt6httpserver package.
Group: Default

%description license
license components for the qt6httpserver package.


%prep
%setup -q -n qthttpserver-everywhere-src-6.8.2
cd %{_builddir}/qthttpserver-everywhere-src-6.8.2
pushd ..
cp -a qthttpserver-everywhere-src-6.8.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738725614
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1738725614
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6httpserver
cp %{_builddir}/qthttpserver-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6httpserver/79453f55fa8ee32d7b95581473edcbfd043e088f || :
cp %{_builddir}/qthttpserver-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6httpserver/7713a1753ce88f2c7e6b054ecc8e4c786df76300 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/QtHttpServer/6.8.2/QtHttpServer/private/qabstracthttpserver_p.h
/usr/include/QtHttpServer/6.8.2/QtHttpServer/private/qhttpserver_p.h
/usr/include/QtHttpServer/6.8.2/QtHttpServer/private/qhttpserverhttp1protocolhandler_p.h
/usr/include/QtHttpServer/6.8.2/QtHttpServer/private/qhttpserverhttp2protocolhandler_p.h
/usr/include/QtHttpServer/6.8.2/QtHttpServer/private/qhttpserverliterals_p.h
/usr/include/QtHttpServer/6.8.2/QtHttpServer/private/qhttpserverrequest_p.h
/usr/include/QtHttpServer/6.8.2/QtHttpServer/private/qhttpserverresponder_p.h
/usr/include/QtHttpServer/6.8.2/QtHttpServer/private/qhttpserverresponse_p.h
/usr/include/QtHttpServer/6.8.2/QtHttpServer/private/qhttpserverrouter_p.h
/usr/include/QtHttpServer/6.8.2/QtHttpServer/private/qhttpserverrouterrule_p.h
/usr/include/QtHttpServer/6.8.2/QtHttpServer/private/qhttpserverstream_p.h
/usr/include/QtHttpServer/QAbstractHttpServer
/usr/include/QtHttpServer/QHttpServer
/usr/include/QtHttpServer/QHttpServerRequest
/usr/include/QtHttpServer/QHttpServerResponder
/usr/include/QtHttpServer/QHttpServerResponse
/usr/include/QtHttpServer/QHttpServerRouter
/usr/include/QtHttpServer/QHttpServerRouterRule
/usr/include/QtHttpServer/QHttpServerRouterViewTraits
/usr/include/QtHttpServer/QHttpServerWebSocketUpgradeResponse
/usr/include/QtHttpServer/QtHttpServer
/usr/include/QtHttpServer/QtHttpServerDepends
/usr/include/QtHttpServer/QtHttpServerVersion
/usr/include/QtHttpServer/qabstracthttpserver.h
/usr/include/QtHttpServer/qhttpserver.h
/usr/include/QtHttpServer/qhttpserverrequest.h
/usr/include/QtHttpServer/qhttpserverresponder.h
/usr/include/QtHttpServer/qhttpserverresponse.h
/usr/include/QtHttpServer/qhttpserverrouter.h
/usr/include/QtHttpServer/qhttpserverrouterrule.h
/usr/include/QtHttpServer/qhttpserverrouterviewtraits.h
/usr/include/QtHttpServer/qhttpserverviewtraits_impl.h
/usr/include/QtHttpServer/qhttpserverwebsocketupgraderesponse.h
/usr/include/QtHttpServer/qthttpserverexports.h
/usr/include/QtHttpServer/qthttpserverglobal.h
/usr/include/QtHttpServer/qthttpserverversion.h
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtHttpServerTestsConfig.cmake
/usr/lib64/cmake/Qt6HttpServer/Qt6HttpServerAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6HttpServer/Qt6HttpServerConfig.cmake
/usr/lib64/cmake/Qt6HttpServer/Qt6HttpServerConfigVersion.cmake
/usr/lib64/cmake/Qt6HttpServer/Qt6HttpServerConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6HttpServer/Qt6HttpServerDependencies.cmake
/usr/lib64/cmake/Qt6HttpServer/Qt6HttpServerTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6HttpServer/Qt6HttpServerTargets.cmake
/usr/lib64/cmake/Qt6HttpServer/Qt6HttpServerVersionlessAliasTargets.cmake
/usr/lib64/cmake/Qt6HttpServer/Qt6HttpServerVersionlessTargets.cmake
/usr/lib64/libQt6HttpServer.prl
/usr/lib64/libQt6HttpServer.so
/usr/lib64/pkgconfig/Qt6HttpServer.pc
/usr/lib64/qt6/mkspecs/modules/qt_lib_httpserver.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_httpserver_private.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6HttpServer.so.6.8.2
/usr/lib64/libQt6HttpServer.so.6
/usr/lib64/libQt6HttpServer.so.6.8.2
/usr/lib64/qt6/metatypes/qt6httpserver_relwithdebinfo_metatypes.json
/usr/lib64/qt6/modules/HttpServer.json
/usr/lib64/qt6/sbom/qthttpserver-6.8.2.spdx

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6httpserver/7713a1753ce88f2c7e6b054ecc8e4c786df76300
/usr/share/package-licenses/qt6httpserver/79453f55fa8ee32d7b95581473edcbfd043e088f
