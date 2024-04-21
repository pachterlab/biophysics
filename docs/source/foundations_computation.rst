.. _computation:

Computation of Molecular, Cellular, and Transcriptional Dynamics
================================================================= 
Here we list a few papaer on solving chemical master equation.

.. dropdown:: Munsky and Khammash, 2006. `The finite state projection algorithm for the solution of the chemical master equation. <https://doi.org/10.1063/1.2145882>`_

            .. grid:: 2

                .. grid-item:: 
                    This article introduced the finite state projection (FSP) method to directly solves or approximates the solution of the chemical master equation. If there are only a finite number of reachable states, the exact soluiton can be computed using matrix exponentials. When there are infinite or extremely large number of reachable states, the state space is projected onto finite space, and the authors provided an estimation of accuracy of the truncated space approximation.

                .. grid-item-card:: Fig 1 Conceptual figure for the finite state projection method

                    .. image:: ./figures/Munsky_2006.jpeg
                        :width: 300
                        :align: center
                        :alt: some text


.. dropdown:: Singh and Bokes, 2012. `Consequences of mRNA transport on stochastic variability in protein levels. <https://doi.org/10.1016/j.bpj.2012.07.015>`_

            .. grid:: 2

                .. grid-item:: 
                    This article derived the analytical solution of bursty model.
                
                    

                .. grid-item-card:: Fig 1 Schematic of the gene expression model 

                    .. image:: ./figures/Singh_2012.jpeg
                        :width: 300
                        :align: center
                        :alt: some text
            
