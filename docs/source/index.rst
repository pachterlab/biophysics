Pachter Lab Biophysics Home
=========================================

.. raw:: html

   <p align="center">
     <img src="https://github.com/pachterlab/biophysics/raw/main/docs/source/figures/monod_v2.png" align="center" width=600 alt="Diagram"/>
   </p>

=========================================

**Our Motivation**


*As biological data becomes increasingly complex and multimodal, we need tools which can interpret the relationships between these high-dimensional, noisy measurements and illuminate the intertwined components of DNA and RNA regulation. In the Pachter Lab, we harness stochastic, biophysical models to represent these high-throughput, genomics data. With our tools, we aim to explicitly model the noise in the data, to capture and reveal important biological variation as well as technical effects of the sequencing pipeline. By treating the underlying biophysical processes which generate our molecular measurements, we can uncover how the processes of the central dogma define cellular diversity, differentiation, and perturbation.*

=========================================

Table of tools
---------------
Below is a table of the Pachter Lab's current tools for biophysical modeling of high-throughput genomics data. The main features and input data types are listed across the columns.
All methods require data with UMIs (molecular count data).


+-------------------------------+--------------------+------------+------------+---------------+------------------+----------+
| Tool                          | Task               | Resolution | Modalities | Steady State? | Technical Noise? | Language |
+===============================+====================+============+============+===============+==================+==========+
| :ref:`Monod<monod>`           |Parameter Inference | gene       | U/S RNA    | yes           | yes (3' seq)     | Python   |
+-------------------------------+--------------------+------------+------------+---------------+------------------+----------+
| :ref:`biVI<bivi>`             |Parameter Inference | cell/gene  | U/S RNA    | yes           | coming soon      | Python   |
+-------------------------------+--------------------+------------+------------+---------------+------------------+----------+
| :ref:`meK-Means<mekmeans>`    |Clustering          | gene       | U/S RNA    | yes           | yes (3' seq)     | Python   |
+-------------------------------+--------------------+------------+------------+---------------+------------------+----------+
| :ref:`Chronocell<chronocell>` |Trajectory Inference| gene       | U/S RNA    | no            | no               | Python   |
+-------------------------------+--------------------+------------+------------+---------------+------------------+----------+
| Spatial: coming soon          |Parameter Inference | gene       | S RNA      | yes           | yes              | Python   |
+-------------------------------+--------------------+------------+------------+---------------+------------------+----------+

**For more details on the available methods see** :doc:`packages`.

Not sure which tool is best for your data? See :doc:`choose`.

Foundational Literature
-----------------------

Explore the foundational literature for biophysical modeling of transcription in :doc:`foundations`, and the lab's publications at :doc:`contributions`.

.. raw:: html

   <p align="right">
         <br>
        <em> 
         Figure created by Kayla Jackson
         </em>
    </p>

.. toctree::
   :hidden:


   packages
   foundations
   contributions
   choose



.. note::

   This project is under active development.

