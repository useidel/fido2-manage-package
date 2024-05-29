#!/usr/bin/bash -x

PATH=/usr/bin:/usr/sbin/
export PATH

# This will setup the needed directory structure to build RPM packages
# please note that this will not happen in the $GITHUB_WORKSPACE 
# but in the RPMBUILD space instead
rpmdev-setuptree

# Get the version from the SPEC file
MYNAME=`grep ^%define *spec|grep pkgname| awk '{print $3}'`
MYCOMMIT=`grep "^%global commit" *.spec|awk '{print $3}'`
MYSHORTCOMMIT=`echo $MYCOMMIT| cut -c1-7`
MYVERSION=`grep ^Version: *spec|awk '{print $2}'`

# copy the also needed patch file(s) to the RPMBUILD space
# again this is different from the $GITHUB_WORKSPACE
###cp *.patch /github/home/rpmbuild/SOURCES
#
## copy the also needed patch file(s) to the RPMBUILD space
# again this is different from the $GITHUB_WORKSPACE
cp * /github/home/rpmbuild/SOURCES
rm /github/home/rpmbuild/SOURCES/*spec


# Now download the sources to the correspoding RPMBUILD directory
cd /github/home/rpmbuild/SOURCES
git clone https://github.com/token2/$MYNAME
cd $MYNAME
git reset --hard $MYSHORTCOMMIT
cd ..
mv $MYNAME $MYNAME-$MYVERSION
tar czf v$MYVERSION.tar.gz $MYNAME-$MYVERSION
rm -rf $MYNAME-$MYVERSION



