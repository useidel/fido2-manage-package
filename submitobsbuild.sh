#!/usr/bin/bash -x

PATH=/usr/bin:/usr/sbin/
export PATH

MYDATE=`date`

# checkout the OSB package
osc co home:useidel fido2-manage-package

cd home*

# copy (updated) files to working directory
# note that the content from github is now in the upper directory
# and the tar archives is in the RPM build area
cp ../*spec fido2-manage-package/
osc delete fido2-manage-package/*.tar.gz
cp /github/home/rpmbuild/SOURCES/*.tar.gz fido2-manage-package/
osc add fido2-manage-package/*.tar.gz

# mark files for update if there are new ones
#cd dummy
#osc add *spec
#cd ..

# upload changed content
osc ci -m "$MY_GITHUB_COMMIT_MSG: $MYDATE" fido2-manage-package

