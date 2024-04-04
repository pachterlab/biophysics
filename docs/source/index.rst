Homepage for Pachter Lab Biophysics Tools
=========================================

General diagram of biophysics approach and where we fit in.

Table of tools
---------------
Below is a table of the current tools for biophysical modeling of high-throughput genomics data. The main features and input data types are listed across the columns.
All methods require data with UMIs (molecular count data).


+-------------------------------+--------------------+------------+------------+---------------+------------------+----------+
| Tool                          | Task               | Resolution | Modalities | Steady State? | Technical Noise? | Language |
+===============================+====================+============+============+===============+==================+==========+
| Monod: :ref:`packages`        |Parameter Inference | gene       | U/S RNA    | yes           | yes (3' seq)     | Python   |
+-------------------------------+--------------------+------------+------------+---------------+------------------+----------+
| biVI: :ref:`packages`         |Parameter Inference | cell/gene  | U/S RNA    | yes           | coming soon      | Python   |
+-------------------------------+--------------------+------------+------------+---------------+------------------+----------+
| meK-Means: :ref:`packages`    |Clustering          | gene       | U/S RNA    | yes           | yes (3' seq)     | Python   |
+-------------------------------+--------------------+------------+------------+---------------+------------------+----------+
| Chronocell:   :ref:`packages` |Trajectory Inference| gene       | U/S RNA    | no            | no               | Python   |
+-------------------------------+--------------------+------------+------------+---------------+------------------+----------+
| Spatial: coming soon          |Parameter Inference | gene       | S RNA      | yes           | yes              | Python   |
+-------------------------------+--------------------+------------+------------+---------------+------------------+----------+

**For more details on the available methods see** :doc:`packages`

Not sure which tool is best for your data? See :doc:`choose`.

Foundational Literature
-----------------------
You can also explore the foundational literature for biophysical modeling of transcription in :doc:`foundations`, and the lab's publications at :doc:`contributions`.


.. toctree::



.. note::

   This project is under active development.

