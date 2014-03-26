OpenSuSE-hplip
==============

hplip - "HP Linux Imaging and Printing"<br>
Orign source from hplip-3.14.3.run downloaded from http://hplipopensource.com/hplip-web/install/install/index.html

We had the need to get Our HP 6500 Desktop Printer alive on Our RPI Print server with Samba and CUPS.<br>
Thus re created simply an RPM build  for that based on Opensuse 13.1 ARM - Raspberry PI<br>

 OSS currently not provide  This on Arm .<br>
 How to setup an HP Printer on OSS see here : https://en.opensuse.org/SDB:How_to_set-up_a_HP_printer


-  laseryet backend for cups enabled
-  hp Ink backend for cups enabled
-  hp scanners backend for cups enabled
-  hp fax backend for cups enabled
-  GUI Build disabled due not required on an Headless Printer Server 


  SPEC & Build Project  Info are here .<br>
  The Build for Raspberry PI RPM & SRPM created for Opensuse 13.1 RPI arm<br>
  are stored at Our Drop Box URL https://www.dropbox.com/sh/ofpzj8u3j2v43zq/mqoFqLLzQB<br>



BUILD Options :

   --prefix=/usr \<br>
   --enable-scan-build \<br>
   --enable-network-build \<br>
   --enable-foomatic-ppd-install \<br>
   --enable-policykit \<br>
   --disable-gui-build \<br>
   --enable-new-hpcups \<br>
   --with-cupsbackenddir=/usr/lib/cups/backend \<br>
   --with-cupsfilterdir=/usr/lib/cups/filter \<br>
   --enable-foomatic-drv-install \<br>
   --enable-foomatic-ppd-install \<br>
   --enable-foomatic-rip-hplip-install \<br>
   --enable-hpijs-install \<br>
   --enable-hpcups-install \<br>
   --enable-cups-drv-install \<br>
   --enable-cups-ppd-install \<br>
   --with-hpppddir=%{_datadir}/cups/model/HP \<br>
   PYTHON=%{__python}<br>
   
   
   The RPM / SRPM simply provide  all nesseary Driver  materials for Most HP Printers .
   <br>
