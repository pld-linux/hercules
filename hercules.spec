Summary:	Hercules S/370, ESA/390, and z/Architecture emulator
Summary(pl.UTF-8):	Emulator S/370, ESA/390 i z/Architecture
Name:		hercules
Version:	3.01
Release:	2
License:	QPL
Group:		Applications/Emulators
Source0:	http://www.conmicro.cx/hercules/%{name}-%{version}.tar.gz
# Source0-md5:	a410fa6446da025ef8aba0b25bf08caa
Patch0:		%{name}-gcrypt.patch
Patch1:		%{name}-nolibs.patch
URL:		http://www.conmicro.cx/hercules/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
BuildRequires:	libgcrypt-devel >= 1.1.42
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

%description -l pl.UTF-8
Hercules to emulator komputerów mainframe IBM serii System/370,
ESA/390 i z/Architecture. Pozwala na uruchomienie dowolnego systemu
operacyjnego IBM i aplikacji działających na rzeczywistym systemie - w
takim zakresie, na jaki pozwala emulowany sprzęt. Hercules potrafi
emulować FBA i CKD DASD, napędy taśmowe, drukarki, czytniki kart,
dziurkarki kart, interfejsy kanałowe, LCS Ethernet,
drukarko-klawiatury oraz terminale 3270.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/hercules,%{_bindir},%{_datadir}/hercules}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install hercules.cnf $RPM_BUILD_ROOT%{_sysconfdir}/hercules/sample.cnf
install util/zzsacard.bin $RPM_BUILD_ROOT%{_datadir}/hercules

# modules are dlopened by *.so
rm -f $RPM_BUILD_ROOT%{_libdir}/{*.la,hercules/*.la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_libdir}/hercules
%attr(755,root,root) %{_libdir}/hercules/*.so
%dir %{_sysconfdir}/hercules
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/hercules/sample.cnf
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
%{_mandir}/man1/cckddiag.1*
%{_mandir}/man1/dasdseq.1*
%{_mandir}/man4/cckd.4*
