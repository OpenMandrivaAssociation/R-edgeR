%global packname  edgeR
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          3.2.4
Release:          1
Summary:          Empirical analysis of digital gene expression data in R
Group:            Sciences/Mathematics
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/edgeR_3.2.4.tar.gz
Requires:         R-methods R-limma R-locfit
Requires:         R-MASS R-statmod R-splines 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-limma
BuildRequires:    R-MASS R-statmod R-splines R-locfit
BuildRequires:    blas-devel lapack-devel

%description
Differential expression analysis of RNA-seq and digital gene expression
profiles with biological replication.  Uses empirical Bayes estimation and
exact tests based on the negative binomial distribution.  Also useful for
differential signal analysis with other types of genome-scale count data.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS*
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs

