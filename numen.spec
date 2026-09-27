%global forgeurl https://github.com/vicinaehq/numen

Name: numen
Version: 0.7.0
Release: %autorelease
Summary: Zero dependency calculator library with first class support for units and timezone conversions

%{forgemeta}
License: BSD-3-Clause
URL: %{forgeurl}
Source0: %{forgesource}

BuildRequires: cmake
BuildRequires: g++
BuildRequires: ninja-build

%description
libnumen is a library to evaluate mathematical expressions, with an emphasis on
natural language as well as unit and date-time operations.

%package devel
Summary: Development files for numen
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the development files for numen.

%prep
%forgeautosetup

%conf
%cmake -G Ninja

%build
%cmake_build

%install
%cmake_install

%check
%ctest


%files
%license LICENSE
%doc README.md
%{_libdir}/libnumen.so.*

%files devel
%{_includedir}/numen/*
%{_libdir}/cmake/numen/*
%{_libdir}/libnumen.so

%changelog
%autochangelog
