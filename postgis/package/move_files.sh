#!/bin/bash -l

mkdir -p $$GPHOME/share/postgresql/contrib/postgis-2.1/{install,upgrade,uninstall}/

mv  $$GPHOME/share/postgresql/contrib/postgis-2.1/postgis.sql $$GPHOME/share/postgresql/contrib/postgis-2.1/install/postgis.sql;
mv  $$GPHOME/share/postgresql/contrib/postgis-2.1/rtpostgis.sql $$GPHOME/share/postgresql/contrib/postgis-2.1/install/rtpostgis.sql;
mv  $$GPHOME/share/postgresql/contrib/postgis-2.1/postgis_comments.sql $$GPHOME/share/postgresql/contrib/postgis-2.1/install/postgis_comments.sql;
mv  $$GPHOME/share/postgresql/contrib/postgis-2.1/raster_comments.sql $$GPHOME/share/postgresql/contrib/postgis-2.1/install/raster_comments.sql;
mv  $$GPHOME/share/postgresql/contrib/postgis-2.1/spatial_ref_sys.sql $$GPHOME/share/postgresql/contrib/postgis-2.1/install/spatial_ref_sys.sql;


mv  $$GPHOME/share/postgresql/contrib/postgis-2.1/legacy.sql $$GPHOME/share/postgresql/contrib/postgis-2.1/upgrade/legacy.sql;
mv  $$GPHOME/share/postgresql/contrib/postgis-2.1/postgis_upgrade_20_21.sql $$GPHOME/share/postgresql/contrib/postgis-2.1/upgrade/postgis_upgrade_20_21.sql;
mv  $$GPHOME/share/postgresql/contrib/postgis-2.1/postgis_upgrade_21_minor.sql $$GPHOME/share/postgresql/contrib/postgis-2.1/upgrade/postgis_upgrade_21_minor.sql;


mv  $$GPHOME/share/postgresql/contrib/postgis-2.1/uninstall_rtpostgis.sql $$GPHOME/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_rtpostgis.sql;
mv  $$GPHOME/share/postgresql/contrib/postgis-2.1/uninstall_postgis.sql $$GPHOME/share/postgresql/contrib/postgis-2.1/uninstall/uninstall_postgis.sql;
