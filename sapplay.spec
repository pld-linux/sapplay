Summary:	plays Atari XL/XE tune files (files with .sap - Slight Atari Player extension)
Summary(pl):	program do odtwarzania melodii z Atari XL/XE (pliki z roszerzeniem .sap - Slight Atari Player)
Name:		sapplay
Version:	0.2
Release:	3
License:	freeware
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(es):	Aplicaciones/Sonido
Group(fr):	Aplica��es/Bruit
Group(pl):	Aplikacje/D�wi�k
Group(pt):	Aplica��es/Som
Group(pt_BR):	Aplica��es/Som
Source0:	http://kunik.republika.pl/sap/dl/%{name}-%{version}.tar.gz
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
roszerzeniem .sap - Slight Atari Player). Sapplay u�ywa biblioteki
libsap (kt�ra umo�liwia programow� emulacj� mikroprocesora 6502 oraz
chipsetu Pokey - uk�ad�w u�ywanych w komputerach Atari XL/XE). Libsap
umo�liwia uruchomienie kodu maszynowego Atari XL/XE kt�ry u�ywa u�ywa
uk�adu Pokey do odtwarzania d�wi�ku i muzyki. Pliki biblioteki libsap
s� za��czone w tym pakiecie.

Wi�cej informacji o muzyce z 8-bitowego Atari oraz utwory w formacie
.sap znajduj� si� pod adresem http://asma.dspaudio.com.

%prep -q
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
