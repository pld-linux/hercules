Summary:	Hercules S/370, ESA/390, and z/Architecure emulator
Name:		hercules
Version:	2.16.2
Release:	1
License:	QPL
Group:		Applications/Emulators
Source0:	http://www.conmicro.cx/hercules/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fxes.patch
URL:		http://www.conmicro.cx/hercules/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hercules is an emulator for the IBM System/370, ESA/390, and
z/Architecture series of mainframe computers. It is capable of running
any IBM operating system and applications that a real system will run,
as long as the hardwre needed is emulated. Hercules can emulate FBA
and CKD DASD, tape, printer, card reader, card punch,
channel-to-channel adapter, LCS Ethernet, and printer-keyboard and
3270 terminal devices.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make} 

%install
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/hercules,%{_bindir},%{_datadir}/hercules}

%{__make} install DESTDIR=$RPM_BUILD_ROOT 

cp hercules.cnf $RPM_BUILD_ROOT%{_sysconfdir}/hercules/sample.cnf
cp util/zzsacard.bin $RPM_BUILD_ROOT%{_datadir}/hercules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%config %{_sysconfdir}/hercules/sample.cnf
%{_datadir}/hercules/*.bin
%{_datadir}/hercules/*.html
%{_datadir}/hercules/*.jcl
%{_datadir}/hercules/*.hla
%{_datadir}/hercules/*.css
%{_datadir}/hercules/images/*
%{_datadir}/hercules/include/*
