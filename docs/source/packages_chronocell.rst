.. _chronocell:

Chronocell: trajectory inference from single-cell genomic data
================================================================= 

For details, please `see the preprint <https://www.biorxiv.org/content/10.1101/2024.01.26.577510v1>`_.

Single-cell transcriptomics experiments provide gene expression snapshots of heterogeneous cell populations across cell states. These snapshots have been used to infer trajectories and dynamic information even without intensive, time-series data by ordering cells according to gene expression similarity. However, while single-cell snapshots sometimes offer valuable insights into dynamic processes, current methods for ordering cells are limited by descriptive notions of “pseudotime” that lack intrinsic physical meaning. Instead of pseudotime, we propose inference of “process time” via a principled modeling approach to formulating trajectories and inferring latent variables corresponding to timing of cells subject to a biophysical process. Our implementation of this approach, called Chronocell, provides a biophysical formulation of trajectories built on cell state transitions. The Chronocell model is identifiable, making parameter inference meaningful. Furthermore, Chronocell can interpolate between trajectory inference, when cell states lie on a continuum, and clustering, when cells cluster into discrete states. By using a variety of datasets ranging from cluster-like to continuous, we show that Chronocell enables us to assess the suitability of datasets and reveals distinct cellular distributions along process time that are consistent with biological process times. We also compare our parameter estimates of degradation rates to those derived from metabolic labeling datasets, thereby showcasing the biophysical utility of Chronocell. Nevertheless, based on performance characterization on simulations, we find that process time inference can be challenging, highlighting the importance of dataset quality and careful model assessment. 

Installation: 

::

  pip install... coming soon 


A `Github repository <https://github.com/pachterlab/FGP_2024>`_ is available with example notebooks.  


.. image:: figures/process_time.png
