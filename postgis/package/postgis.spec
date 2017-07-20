Summary:        Geospatial extensions for Greenplum Database
License:        GPLv2
Name:           postgis
Version:        %{postgis_ver}
Release:        %{postgis_rel}
Group:          Development/Tools
Prefix:         /temp
AutoReq:        no
AutoProv:       no
Provides:       postgis = %{postgis_ver}
Requires:       geos = %{geos_ver}, proj = %{proj_ver}, json-c = %{json_ver}, gdal = %{gdal_ver}

%description
The PostGIS module provides geospatial extensions for Greenplum Database.

%install
make -C %{postgis_dir} BLD_TOP=%{bld_top} install prefix=%{buildroot}/temp

mkdir -p %{buildroot}/temp/bin
cp $GPHOME/bin/pgsql2shp %{buildroot}/temp/bin
cp $GPHOME/bin/shp2pgsql %{buildroot}/temp/bin
cp $GPHOME/bin/raster2pgsql %{buildroot}/temp/bin

mkdir -p %{buildroot}/temp/lib/postgresql
cp $GPHOME/lib/postgresql/postgis-2.1.so %{buildroot}/temp/lib/postgresql/postgis-2.1.so
cp $GPHOME/lib/postgresql/rtpostgis-2.1.so %{buildroot}/temp/lib/postgresql/rtpostgis-2.1.so

mkdir -p %{buildroot}/temp/share/postgresql/contrib/postgis-2.1/
mkdir -p %{buildroot}/temp/share/postgresql/contrib/postgis-2.1/{install,upgrade,uninstall}/

cp $GPHOME/share/postgresql/contrib/postgis-2.1/postgis.sql %{buildroot}/temp/share/postgresql/contrib/postgis-2.1/install/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/postgis_comments.sql %{buildroot}/temp/share/postgresql/contrib/postgis-2.1/install/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/rtpostgis.sql %{buildroot}/temp/share/postgresql/contrib/postgis-2.1/install/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/raster_comments.sql %{buildroot}/temp/share/postgresql/contrib/postgis-2.1/install/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/spatial_ref_sys.sql %{buildroot}/temp/share/postgresql/contrib/postgis-2.1/install/

cp $GPHOME/share/postgresql/contrib/postgis-2.1/*upgrade*.sql %{buildroot}/temp/share/postgresql/contrib/postgis-2.1/upgrade/
cp $GPHOME/share/postgresql/contrib/postgis-2.1/*legacy*.sql %{buildroot}/temp/share/postgresql/contrib/postgis-2.1/upgrade/

cp $GPHOME/share/postgresql/contrib/postgis-2.1/uninstall*.sql %{buildroot}/temp/share/postgresql/contrib/postgis-2.1/uninstall/

%files
/temp
/temp/bin
/temp/bin/pgsql2shp
/temp/bin/raster2pgsql
/temp/bin/shp2pgsql
/temp/include
/temp/include/liblwgeom.h
/temp/lib
/temp/lib/liblwgeom-2.1.5.so
/temp/lib/liblwgeom.a
/temp/lib/liblwgeom.la
/temp/lib/liblwgeom.so
/temp/lib/postgresql
/temp/lib/postgresql/postgis-2.1.so
/temp/lib/postgresql/rtpostgis-2.1.so
/temp/share
/temp/share/postgresql
/temp/share/postgresql/contrib
/temp/share/postgresql/contrib/postgis-2.1
/temp/share/postgresql/contrib/postgis-2.1/legacy.sql
/temp/share/postgresql/contrib/postgis-2.1/legacy_gist.sql
/temp/share/postgresql/contrib/postgis-2.1/legacy_minimal.sql
/temp/share/postgresql/contrib/postgis-2.1/postgis.sql
/temp/share/postgresql/contrib/postgis-2.1/postgis_comments.sql
/temp/share/postgresql/contrib/postgis-2.1/postgis_upgrade_20_21.sql
/temp/share/postgresql/contrib/postgis-2.1/postgis_upgrade_21_minor.sql
/temp/share/postgresql/contrib/postgis-2.1/raster_comments.sql
/temp/share/postgresql/contrib/postgis-2.1/rtpostgis.sql
/temp/share/postgresql/contrib/postgis-2.1/rtpostgis_legacy.sql
/temp/share/postgresql/contrib/postgis-2.1/rtpostgis_upgrade_20_21.sql
/temp/share/postgresql/contrib/postgis-2.1/rtpostgis_upgrade_21_minor.sql
/temp/share/postgresql/contrib/postgis-2.1/spatial_ref_sys.sql
/temp/share/postgresql/contrib/postgis-2.1/topology_comments.sql
/temp/share/postgresql/contrib/postgis-2.1/uninstall_legacy.sql
/temp/share/postgresql/contrib/postgis-2.1/uninstall_postgis.sql
/temp/share/postgresql/contrib/postgis-2.1/uninstall_rtpostgis.sql
/temp/share/postgresql/contrib/postgis-2.1/uninstall_sfcgal.sql
