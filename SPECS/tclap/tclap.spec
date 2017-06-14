Summary:    simple interface for defining and acessing commandline arguments
Name:       tclap
Version:    1.2.1
Release:    1%{?dist}
License:    MIT
URL:        http://tclap.sourceforge.net
Group:      Development/Libraries
Vendor:     VMware, Inc.
Distribution: Photon
Source0:    http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz 
%define sha1 tclap=4f124216dd6e6936f5af6372d921a6c51563f8fd

BuildArch:  noarch

%description
TCLAP is a small, flexible library that provides a simple interface for defining and accessing command line
arguments. It was intially inspired by the user friendly CLAP libary. The difference is that this library is
templatized, so the argument class is type independent. Type independence avoids identical-except-for-type
objects, such as IntArg, FloatArg, and StringArg. While the library is not strictly compliant with the GNU
or POSIX standards, it is close.

%package doc
Summary:    API Documentation for tclap
Group:      Documentation

%description doc
API documentation for TCLAP

%prep
%setup -q

%build
./configure --prefix=%{_prefix}

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%check
make %{?_smp_mflags} check

%files
%defattr(-,root,root)
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%files doc
%defattr(-,root,root)
%{_docdir}/*

%changelog
*   Tue Jun 13 2017 Dheeraj Shetty <dheerajs@vmware.com> 1.2.1-1
-   First version
