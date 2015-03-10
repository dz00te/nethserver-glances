
%define name nethserver-glances
%define version 1.0.0
%define release 2
Summary: NethServer integration of glances
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GNU GPL version 2
URL: http://dev.nethserver.org/projects/nethforge/wiki/%{name} 
Group: Neth/addon
Source: %{name}-%{version}.tar.gz

BuildArchitectures: noarch
BuildRequires: perl
BuildRequires: nethserver-devtools 
BuildRoot: /var/tmp/%{name}-%{version}
Requires: collectd-sensors gcc python-pip python-devel
AutoReqProv: no

%description
NethServer integration of glances
Glances is a cross-platform curses-based system monitoring tool written in Python.

%prep
%setup
%build
perl ./createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
  > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add glances

%preun
if [ "$1" = 0 ]; then
    # stop glances  silently, but only if it's running
    /sbin/service glances stop &>/dev/null
    /sbin/chkconfig --del glances
fi

exit 0

%postun
if [ "$1" != 0 ]; then
	/sbin/service glances restart 2>&1 > /dev/null
fi

exit 0

%changelog

* Sat Mar 7 2015 stephane de labrusse <stephdl@de-labrusse.fr> 1.0.0-1.ns6
- First release to Nethserver
