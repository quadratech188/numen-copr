%global forgeurl https://github.com/vicinaehq/numen

Name: numen
Version: 0.4.1
Release: %autorelease
Summary: Zero dependency calculator library with first class support for units and timezone conversions

%{forgemeta}
License: BSD-3-Clause
URL: %{forgeurl}
Source0: %{forgesource}

BuildRequires: cmake
BuildRequires: g++

%description
libnumen is a library to evaluate mathematical expressions, with an emphasis on
natural language as well as unit and date-time operations.

%prep
%forgeautosetup

%conf
%cmake

%build
%cmake_build

%install
%cmake_install

%check
%ctest


%files
%license LICENSE
%doc README.md

/usr/include/numen/*
/usr/lib64/cmake/numen/*
/usr/lib64/libnumen*

%changelog
%autochangelog
