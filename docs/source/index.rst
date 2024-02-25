Homepage for Pachter Lab Biophysics Tools
=========================================

General diagram of biophysics approach and where we fit in.

Below is a table of the current tools for biophysical modeling of high-throughput genomics data, alongside the major features and data types each method handles.

To see more details about the available methods in each package, refer to :doc:`packages.

+-------------------------------+------------+------------+---------------+------------------+----------+-------------------------+
| Tool                          | Resolution | Modalities | Steady State? | Technical Noise? | Language | Experimental Technology |
+===============================+============+============+===============+==================+==========+=========================+
| Monod: :ref:`packages`        | gene       | U/S RNA    | yes           | yes (3' seq)     | Python   | Need UMIs               |
+-------------------------------+------------+------------+---------------+------------------+----------+-------------------------+
| biVI: :ref:`packages`         | cell/gene  | U/S RNA    | yes           | coming soon      | Python   | Need UMIs               |
+-------------------------------+------------+------------+---------------+------------------+----------+-------------------------+
| Process Time: :ref:`packages` | gene       | U/S RNA    | no            | no               | Python   | Need UMIs               |
+-------------------------------+------------+------------+---------------+------------------+----------+-------------------------+
| Spatial: :ref:`packages`      | gene       | S RNA      | yes           | yes              | Python   | Need UMIs               |
+-------------------------------+------------+------------+---------------+------------------+----------+-------------------------+


Keeping :doc:`packages` section here as an example page for now, and this
call to a subsection, :ref:`installation`.

.. note::

   This project is under active development.

Contents
--------

.. toctree::

   packages
   foundations
   contributions
   choose
