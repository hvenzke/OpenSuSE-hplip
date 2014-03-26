OpenSuSE-hplip
==============

hplip - "HP Linux Imaging and Printing"
Orign source from hplip-3.14.3.run downloaded from http://hplipopensource.com/hplip-web/install/install/index.html

We had the need to get Our HP 6500 Desktop Printer alive on Our RPI Print server with Samba and CUPS.
Thus re created simply an RPM build  for that based on Opensuse 13.1 ARM - Raspberry PI


-  laseryet adn Ink printers enabled
-  GUI Build disabled due not required on an Headless Printer Server 


BUILD Options :

   --prefix=/usr \
   --enable-scan-build \
   --enable-network-build \
   --enable-foomatic-ppd-install \
   --enable-policykit \
   --disable-gui-build \
   --enable-new-hpcups \
   --with-cupsbackenddir=/usr/lib/cups/backend \
   --with-cupsfilterdir=/usr/lib/cups/filter \
   --enable-foomatic-drv-install \
   --enable-foomatic-ppd-install \
   --enable-foomatic-rip-hplip-install \
   --enable-hpijs-install \
   --enable-hpcups-install \
   --enable-cups-drv-install \
   --enable-cups-ppd-install \
   --with-hpppddir=%{_datadir}/cups/model/HP \
   PYTHON=%{__python}
