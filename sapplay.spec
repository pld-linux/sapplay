Summary:	plays Atari XL/XE tune files (files with .sap - Slight Atari Player extension)
Summary(pl):	program do odtwarzania melodii z Atari XL/XE (pliki z roszerzeniem .sap - Slight Atari Player)
Name:		sapplay
Version:	0.2
Release:	3
License:	Freeware
Group:		Applications/Sound
Source0:	http://kunik.republika.pl/sap/dl/%{name}-%{version}.tar.gz
# Source0-md5:	ac62ed3234abb79aa3f96f93fefe0c89
URL:		http://kunik.republika.pl/sap/
BuildRequires:	libsap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sapplay is a console based player for Atari XL/XE tune files (with
.sap extension - Slight Atari Player). Sapplay uses libsap (which is a
software emulation of CPU 6502 microporcessor and Pokey chip - two
chips that are used in Atari XL/XE). Libsap runs programs written in
6502 machine language, programs that use Pokey chip to play tunes and
sounds. Libsap files are included in this package.

For tunes and more information about 8-bit Atari music, visit
http://asma.dspaudio.com/.

%description -l pl
Sapplay jest konsolowym odtwarzaczem muzyczek z Atari XL/XE (pliki z
roszerzeniem .sap - Slight Atari Player). Sapplay u¿ywa biblioteki
libsap (która umo¿liwia programow± emulacjê mikroprocesora 6502 oraz
chipsetu Pokey - uk³adów u¿ywanych w komputerach Atari XL/XE). Libsap
umo¿liwia uruchomienie kodu maszynowego Atari XL/XE który u¿ywa u¿ywa
uk³adu Pokey do odtwarzania d¼wiêku i muzyki. Pliki biblioteki libsap
s± za³±czone w tym pakiecie.

Wiêcej informacji o muzyce z 8-bitowego Atari oraz utwory w formacie
.sap znajduj± siê pod adresem http://asma.dspaudio.com.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" OPTS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install sapplay $RPM_BUILD_ROOT%{_bindir}
install sapplay.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sapplay
%{_mandir}/man1/sapplay.1*
