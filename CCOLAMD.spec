Summary:	CCOLAMD: constrained column approximate minimum degree
Summary(pl.UTF-8):	CCOLAMD - przybliżony ograniczony algorytm minimalnego stopnia dla kolumn
Name:		CCOLAMD
Version:	2.7.1
Release:	3
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.cise.ufl.edu/research/sparse/ccolamd/%{name}-%{version}.tar.gz
# Source0-md5:	04b0b27fae6795612ce779a3f6381cb7
Patch0:		ccolamd-ufconfig.patch
Patch1:		ccolamd-shared.patch
URL:		http://www.cise.ufl.edu/research/sparse/ccolamd/
BuildRequires:	UFconfig
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The CCOLAMD column approximate minimum degree ordering algorithm
computes a permutation vector P such that the LU factorization of A
(:,P) tends to be sparser than that of A. The Cholesky factorization
of (A (:,P))'*(A (:,P)) will also tend to be sparser than that of
A'*A. CSYMAMD is a symmetric minimum degree ordering method based on
CCOLAMD, available as a MATLAB-callable function. It constructs a
matrix M such that M'*M has the same pattern as A, and then uses
CCOLAMD to compute a column ordering of M.

%description -l pl.UTF-8
Przybliżony algorytm porządkowania minimalnego stopnia dla kolumn
CCOLAMD oblicza wektor permutacji P taki, że rozkład LU A (:,P) jest
bardziej rzadki niż A. Rozkład Cholesky'ego (A (:,P))'*(A (:,P)) także
jest rzadszy niż A'*A. CSYMAND to przybliżony algorytm porządkowania
minimalnego stopnia dla macierzy symetrycznych oparty na CCOLAMD,
dostępny jako funkcja do wywołania z MATLAB-a. Tworzy macierz M taką,
że M'*M ma ten sam wzór co A, a następnie używa algorytmu CCOLAMD do
obliczenia porządku kolumn M.

%package devel
Summary:	Header files for CCOLAMD library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CCOLAMD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	UFconfig

%description devel
Header files for CCOLAMD library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CCOLAMD.

%package static
Summary:	Static CCOLAMD library
Summary(pl.UTF-8):	Statyczna biblioteka CCOLAMD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static CCOLAMD library.

%description static -l pl.UTF-8
Statyczna biblioteka CCOLAMD.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/ccolamd

%{__make} -C Lib install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install Include/*.h $RPM_BUILD_ROOT%{_includedir}/ccolamd

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt Doc/ChangeLog
%attr(755,root,root) %{_libdir}/libccolamd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libccolamd.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libccolamd.so
%{_libdir}/libccolamd.la
%{_includedir}/ccolamd

%files static
%defattr(644,root,root,755)
%{_libdir}/libccolamd.a
