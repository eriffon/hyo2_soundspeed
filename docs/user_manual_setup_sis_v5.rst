Sound Speed Manager - SIS v5 interaction
========================================

.. index:: SIS; v5
.. index:: K-Controller

SIS v5 is currently supported through the Data Distribution application installed with SIS v5.

This method covers both cases:

* Sound Speed Manager and SIS v5 installed on the same machine.
* Sound Speed Manager and SIS v5 installed on the different machines.

First, under the SIS v5 installation folder, locate and execute 'DataDist.exe'. Once started, you need the following
settings (see :numref:`data_dist_exe_fig`):

* Select the Echo Sounder.
* Add a datagram distribution.
* Write (and remember!) the IP address and the port where you want to send the datagrams: e.g., '127.0.0.1:16103'.
* Select the following datagram types: MRZ, SPO and SVP.
* Save the configuration.

.. _data_dist_exe_fig:

.. figure:: ./_static/data_dist_exe.png
    :width: 640px
    :align: center
    :alt: figure with DataDist.exe
    :figclass: align-center

    *Data Distribution Configuration* application with required settings.

Open in editing mode the Sound Speed Manager’s Setup Tab, then set the SIS listen port (that you have set in
the Data Distribution Configuration) in the Listeners sub-tab (see :numref:`ssm_sis5_p1_fig`).

.. _ssm_sis5_p1_fig:

.. figure:: ./_static/ssm_sis5_p1.png
    :width: 640px
    :align: center
    :alt: figure with SSM SIS5 settings part 1
    :figclass: align-center

    *Listeners tab* in the Sound Speed Manager’s Setup.

Then, switch to the Input sub-tab (see :numref:`ssm_sis5_p2_fig`) and select the True value for the Listen SIS v5 field.

.. _ssm_sis5_p2_fig:

.. figure:: ./_static/ssm_sis5_p2.png
    :width: 640px
    :align: center
    :alt: figure with SSM SIS5 settings part 2
    :figclass: align-center

    *Input tab* in the Sound Speed Manager’s Setup.

The previous steps are required to make Sound Speed Manager able to listen survey data from SIS v5 (through the
Data Distribution application).

In order to be able to transmit to SIS v5, you need to add a client in the Output sub-tab
(see :numref:`ssm_sis5_p3_fig`) using the following settings:

* IP: 127.0.0.1  *(if SIS v5 is on the same machine, otherwise the network IP address of the other machine)*
* port: 14002  *(always!)*
* protocol: SIS  *(always!)*

.. _ssm_sis5_p3_fig:

.. figure:: ./_static/ssm_sis5_p3.png
    :width: 640px
    :align: center
    :alt: figure with SSM SIS5 settings part 3
    :figclass: align-center

    *Output tab* in the Sound Speed Manager’s Setup.

Now **restart** Sound Speed Manager. If a SIS-controlled sonar is pinging, you should start
to see the parsed information in the status bar (see :numref:`ssm_sis5_p2_fig`).