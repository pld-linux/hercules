Summary:	Hercules S/370, ESA/390, and z/Architecture emulator
Summary(pl):	Emulator S/370, ESA/390 i z/Architecture
Name:		hercules
Version:	2.16.2
Release:	2
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
as long as the hardware needed is emulated. Hercules can emulate FBA
and CKD DASD, tape, printer, card reader, card punch,
channel-to-channel adapter, LCS Ethernet, and printer-keyboard and
3270 terminal devices.

%description -l pl
Hercules to emulator komputerów mainframe IBM serii System/370,
ESA/390 i z/Architecture. Pozwala na uruchomienie dowolnego systemu
operacyjnego IBM i aplikacji dzia³aj±cych na rzeczywistym systemie -
w takim zakresie, na jaki pozwala emulowany sprzêt. Hercules potrafi
emulowaæ FBA i CKD DASD, napêdy ta¶mowe, drukarki, czytniki kart,
dziurkarki kart, interfejsy kana³owe, LCS Ethernet,
drukarko-klawiatury oraz terminale 3270.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} 

%install
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/hercules,%{_bindir},%{_datadir}/hercules}

%{__make} install DESTDIR=$RPM_BUILD_ROOT 

install hercules.cnf $RPM_BUILD_ROOT%{_sysconfdir}/hercules/sample.cnf
install util/zzsacard.bin $RPM_BUILD_ROOT%{_datadir}/hercules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%dir %{_sysconfdir}/hercules
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/hercules/sample.cnf
%dir %{_datadir}/hercules
%{_datadir}/hercules/*.bin
%{_datadir}/hercules/*.html
%{_datadir}/hercules/*.jcl
%{_datadir}/hercules/*.hla
%{_datadir}/hercules/*.css
%dir %{_datadir}/hercules/images
%{_datadir}/hercules/images/*
%dir %{_datadir}/hercules/include
%{_datadir}/hercules/include/*
