Homepage for Pachter Lab Biophysics Tools
=========================================

General diagram of biophysics approach and where we fit in.

Table of tools
---------------
Below is a table of the current tools for biophysical modeling of high-throughput genomics data. The main features and input data types are listed across the columns.


+-------------------------------+------------+------------+---------------+------------------+----------+-------------------------+
| Tool                          | Resolution | Modalities | Steady State? | Technical Noise? | Language | Experimental Technology |
+===============================+============+============+===============+==================+==========+=========================+
| Monod: :ref:`packages`        | gene       | U/S RNA    | yes           | yes (3' seq)     | Python   | Need UMIs               |
+-------------------------------+------------+------------+---------------+------------------+----------+-------------------------+
| biVI: :ref:`packages`         | cell/gene  | U/S RNA    | yes           | coming soon      | Python   | Need UMIs               |
+-------------------------------+------------+------------+---------------+------------------+----------+-------------------------+
| Process Time: :ref:`packages` | gene       | U/S RNA    | no            | no               | Python   | Need UMIs               |
+-------------------------------+------------+------------+---------------+------------------+----------+-------------------------+
| Spatial: coming soon          | gene       | S RNA      | yes           | yes              | Python   | Need UMIs               |
+-------------------------------+------------+------------+---------------+------------------+----------+-------------------------+

**For more details on the available methods see** :doc:`packages`

Not sure which tool is best for your data? See :doc:`choose`.

Foundational Literature
-----------------------
You can also explore the foundational literature for biophysical modeling of transcription in :doc:`foundations`, and the lab's publications in this domain at :doc:`contributions`.


.. note::

   This project is under active development.

