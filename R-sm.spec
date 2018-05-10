#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sm
Version  : 2.2.5.4
Release  : 8
URL      : https://cran.r-project.org/src/contrib/sm_2.2-5.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sm_2.2-5.4.tar.gz
Summary  : Smoothing methods for nonparametric regression and density
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-sm-lib
Requires: R-gam
BuildRequires : R-gam
BuildRequires : clr-R-helpers

%description
'Applied Smoothing Techniques for Data Analysis -
  The Kernel Approach with S-Plus Illustrations' Oxford University Press.

%package lib
Summary: lib components for the R-sm package.
Group: Libraries

%description lib
lib components for the R-sm package.


%prep
%setup -q -c -n sm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521219860

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521219860
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library sm|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sm/CITATION
/usr/lib64/R/library/sm/COPYING
/usr/lib64/R/library/sm/DESCRIPTION
/usr/lib64/R/library/sm/INDEX
/usr/lib64/R/library/sm/Meta/Rd.rds
/usr/lib64/R/library/sm/Meta/data.rds
/usr/lib64/R/library/sm/Meta/features.rds
/usr/lib64/R/library/sm/Meta/hsearch.rds
/usr/lib64/R/library/sm/Meta/links.rds
/usr/lib64/R/library/sm/Meta/nsInfo.rds
/usr/lib64/R/library/sm/Meta/package.rds
/usr/lib64/R/library/sm/NAMESPACE
/usr/lib64/R/library/sm/R/sm
/usr/lib64/R/library/sm/R/sm.rdb
/usr/lib64/R/library/sm/R/sm.rdx
/usr/lib64/R/library/sm/data/Rdata.rdb
/usr/lib64/R/library/sm/data/Rdata.rds
/usr/lib64/R/library/sm/data/Rdata.rdx
/usr/lib64/R/library/sm/help/AnIndex
/usr/lib64/R/library/sm/help/aliases.rds
/usr/lib64/R/library/sm/help/paths.rds
/usr/lib64/R/library/sm/help/sm.rdb
/usr/lib64/R/library/sm/help/sm.rdx
/usr/lib64/R/library/sm/history.txt
/usr/lib64/R/library/sm/html/00Index.html
/usr/lib64/R/library/sm/html/R.css
/usr/lib64/R/library/sm/libs/symbols.rds
/usr/lib64/R/library/sm/scripts/air_band.q
/usr/lib64/R/library/sm/scripts/air_boot.q
/usr/lib64/R/library/sm/scripts/air_cont.q
/usr/lib64/R/library/sm/scripts/air_dens.q
/usr/lib64/R/library/sm/scripts/air_hcv.q
/usr/lib64/R/library/sm/scripts/air_imag.q
/usr/lib64/R/library/sm/scripts/air_ind.q
/usr/lib64/R/library/sm/scripts/air_inds.q
/usr/lib64/R/library/sm/scripts/air_scat.q
/usr/lib64/R/library/sm/scripts/bin_use.q
/usr/lib64/R/library/sm/scripts/birth1.q
/usr/lib64/R/library/sm/scripts/birth2.q
/usr/lib64/R/library/sm/scripts/bissell1.q
/usr/lib64/R/library/sm/scripts/bissell2.q
/usr/lib64/R/library/sm/scripts/bissell3.q
/usr/lib64/R/library/sm/scripts/citrate.q
/usr/lib64/R/library/sm/scripts/dogs.q
/usr/lib64/R/library/sm/scripts/edfgrad.q
/usr/lib64/R/library/sm/scripts/follicle.q
/usr/lib64/R/library/sm/scripts/geys3d.q
/usr/lib64/R/library/sm/scripts/geys_ts.q
/usr/lib64/R/library/sm/scripts/index.doc
/usr/lib64/R/library/sm/scripts/lc_comp.q
/usr/lib64/R/library/sm/scripts/lc_dens.q
/usr/lib64/R/library/sm/scripts/lc_rr.q
/usr/lib64/R/library/sm/scripts/lynx.q
/usr/lib64/R/library/sm/scripts/mackgam.q
/usr/lib64/R/library/sm/scripts/mackmap.q
/usr/lib64/R/library/sm/scripts/mackplot.q
/usr/lib64/R/library/sm/scripts/mag_dens.q
/usr/lib64/R/library/sm/scripts/mag_scat.q
/usr/lib64/R/library/sm/scripts/mildew.q
/usr/lib64/R/library/sm/scripts/muscle.q
/usr/lib64/R/library/sm/scripts/noeff.q
/usr/lib64/R/library/sm/scripts/nyc.q
/usr/lib64/R/library/sm/scripts/onionbnd.q
/usr/lib64/R/library/sm/scripts/onionplt.q
/usr/lib64/R/library/sm/scripts/rc_alter.q
/usr/lib64/R/library/sm/scripts/rc_boot.q
/usr/lib64/R/library/sm/scripts/rc_plot.q
/usr/lib64/R/library/sm/scripts/rc_vband.q
/usr/lib64/R/library/sm/scripts/sin_cv.q
/usr/lib64/R/library/sm/scripts/sin_prop.q
/usr/lib64/R/library/sm/scripts/smackgam.q
/usr/lib64/R/library/sm/scripts/smackplt.q
/usr/lib64/R/library/sm/scripts/sp_alter.q
/usr/lib64/R/library/sm/scripts/sp_build.q
/usr/lib64/R/library/sm/scripts/sp_comp.q
/usr/lib64/R/library/sm/scripts/sp_comp2.q
/usr/lib64/R/library/sm/scripts/sp_hist.q
/usr/lib64/R/library/sm/scripts/sp_test1.q
/usr/lib64/R/library/sm/scripts/sp_test2.q
/usr/lib64/R/library/sm/scripts/speed.q
/usr/lib64/R/library/sm/scripts/speedvar.q
/usr/lib64/R/library/sm/scripts/stananim.q
/usr/lib64/R/library/sm/scripts/stanplot.q
/usr/lib64/R/library/sm/scripts/te_band.q
/usr/lib64/R/library/sm/scripts/te_hcvsj.q
/usr/lib64/R/library/sm/scripts/te_norm.q
/usr/lib64/R/library/sm/scripts/te_var.q
/usr/lib64/R/library/sm/scripts/trees.q
/usr/lib64/R/library/sm/scripts/trout1.q
/usr/lib64/R/library/sm/scripts/trout2.q
/usr/lib64/R/library/sm/scripts/trw_lf.q
/usr/lib64/R/library/sm/scripts/trw_lfsg.q
/usr/lib64/R/library/sm/scripts/trw_nebd.q
/usr/lib64/R/library/sm/scripts/trw_nesg.q
/usr/lib64/R/library/sm/scripts/trwlband.q
/usr/lib64/R/library/sm/scripts/trwlboot.q
/usr/lib64/R/library/sm/scripts/trwlcmp2.q
/usr/lib64/R/library/sm/scripts/trwlcomp.q
/usr/lib64/R/library/sm/scripts/trwlgam1.q
/usr/lib64/R/library/sm/scripts/trwlgam2.q
/usr/lib64/R/library/sm/scripts/trwlgam3.q
/usr/lib64/R/library/sm/scripts/trwlplot.q
/usr/lib64/R/library/sm/scripts/wormcomp.q
/usr/lib64/R/library/sm/smdata/aircraft.dat
/usr/lib64/R/library/sm/smdata/aircraft.doc
/usr/lib64/R/library/sm/smdata/airpc.dat
/usr/lib64/R/library/sm/smdata/airpc.doc
/usr/lib64/R/library/sm/smdata/birth.dat
/usr/lib64/R/library/sm/smdata/birth.doc
/usr/lib64/R/library/sm/smdata/bissell.dat
/usr/lib64/R/library/sm/smdata/bissell.doc
/usr/lib64/R/library/sm/smdata/bonions.dat
/usr/lib64/R/library/sm/smdata/bonions.doc
/usr/lib64/R/library/sm/smdata/britpts.dat
/usr/lib64/R/library/sm/smdata/citrate.dat
/usr/lib64/R/library/sm/smdata/citrate.doc
/usr/lib64/R/library/sm/smdata/coalash.dat
/usr/lib64/R/library/sm/smdata/coalash.doc
/usr/lib64/R/library/sm/smdata/dogs.dat
/usr/lib64/R/library/sm/smdata/dogs.doc
/usr/lib64/R/library/sm/smdata/follicle.dat
/usr/lib64/R/library/sm/smdata/follicle.doc
/usr/lib64/R/library/sm/smdata/geys3d.dat
/usr/lib64/R/library/sm/smdata/geys3d.doc
/usr/lib64/R/library/sm/smdata/lcancer.dat
/usr/lib64/R/library/sm/smdata/lcancer.doc
/usr/lib64/R/library/sm/smdata/mackerel.dat
/usr/lib64/R/library/sm/smdata/mackerel.doc
/usr/lib64/R/library/sm/smdata/magrem.dat
/usr/lib64/R/library/sm/smdata/magrem.doc
/usr/lib64/R/library/sm/smdata/mildew.dat
/usr/lib64/R/library/sm/smdata/mildew.doc
/usr/lib64/R/library/sm/smdata/muscle.dat
/usr/lib64/R/library/sm/smdata/muscle.doc
/usr/lib64/R/library/sm/smdata/nile.dat
/usr/lib64/R/library/sm/smdata/nile.doc
/usr/lib64/R/library/sm/smdata/phosphat.doc
/usr/lib64/R/library/sm/smdata/poles.dat
/usr/lib64/R/library/sm/smdata/poles.doc
/usr/lib64/R/library/sm/smdata/propsim.dat
/usr/lib64/R/library/sm/smdata/radioc.dat
/usr/lib64/R/library/sm/smdata/radioc.doc
/usr/lib64/R/library/sm/smdata/smacker.dat
/usr/lib64/R/library/sm/smdata/smacker.doc
/usr/lib64/R/library/sm/smdata/stanford.dat
/usr/lib64/R/library/sm/smdata/stanford.doc
/usr/lib64/R/library/sm/smdata/tephra.dat
/usr/lib64/R/library/sm/smdata/tephra.doc
/usr/lib64/R/library/sm/smdata/trawl.dat
/usr/lib64/R/library/sm/smdata/trawl.doc
/usr/lib64/R/library/sm/smdata/trees.dat
/usr/lib64/R/library/sm/smdata/trees.doc
/usr/lib64/R/library/sm/smdata/trout.dat
/usr/lib64/R/library/sm/smdata/trout.doc
/usr/lib64/R/library/sm/smdata/wonions.dat
/usr/lib64/R/library/sm/smdata/wonions.doc
/usr/lib64/R/library/sm/smdata/worm.dat
/usr/lib64/R/library/sm/smdata/worm.doc

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/sm/libs/sm.so
/usr/lib64/R/library/sm/libs/sm.so.avx2
/usr/lib64/R/library/sm/libs/sm.so.avx512
