Summary:	CCOLAMD: column approximate minimum degree
Summary(pl.UTF-8):	CCOLAMD - przybliżony algorytm minimalnego stopnia dla kolumn
Name:		ccolamd
Version:	2.7.1
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.cise.ufl.edu/research/sparse/ccolamd/CCOLAMD-%{version}.tar.gz
# Source0-md5:	04b0b27fae6795612ce779a3f6381cb7
Patch0:		%{name}-ufconfig.patch
Patch1:		%{name}-shared.patch
URL:		http://www.cise.ufl.edu/research/sparse/ccolamd/
BuildRequires:	UFconfig
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The COLAMD column approximate minimum degree ordering algorithm
computes a permutation vector P such that the LU factorization of A
(:,P) tends to be sparser than that of A. The Cholesky factorization
of (A (:,P))'*(A (:,P)) will also tend to be sparser than that of
A'*A. SYMAMD is a symmetric minimum degree ordering method based on
COLAMD, available as a MATLAB-callable function. It constructs a
matrix M such that M'*M has the same pattern as A, and then uses
COLAMD to compute a column ordering of M. Colamd and symamd tend to be
faster and generate better orderings than their MATLAB counterparts,
colmmd and symmmd.

%description -l pl.UTF-8
Przybliżony algorytm porządkowania minimalnego stopnia dla kolumn
(COLAMD) oblicza wektor permutacji P taki, że rozkład LU A (:,P) jest
bardziej rzadki niż A. Rozkład Cholesky'ego (A (:,P))'*(A (:,P)) także
jest rzadszy niż A'*A. SYMAND to przybliżony algorytm porządkowania
minimalnego stopnia dla macierzy symetrycznych oparty na COLAMD,
dostępny jako funkcja do wywołania z MATLAB-a. Tworzy macierz M taką,
że M'*M ma ten sam wzór co A, a następnie używa algorytmu COLAMD do
obliczenia porządku kolumn M. COLAMD i SYMAMD są szybsze i generują
lepsze uporządkowania niż ich odpowiedniki z MATLAB-a: colmmd i
symmmd.

%package devel
Summary:	Header files for ccolamd library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ccolamd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	UFconfig

%description devel
Header files for ccolamd library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ccolamd.

%package static
Summary:	Static ccolamd library
Summary(pl.UTF-8):	Statyczna biblioteka ccolamd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ccolamd library.

%description static -l pl.UTF-8
Statyczna biblioteka ccolamd.

%prep
%setup -q -n CCOLAMD
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C Lib install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install -D Include/ccolamd.h $RPM_BUILD_ROOT%{_includedir}/ccolamd.h

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_libdir}/libccolamd.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libccolamd.so
%{_libdir}/libccolamd.la
%{_includedir}/ccolamd.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libccolamd.a
