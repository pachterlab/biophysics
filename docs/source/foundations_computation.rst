.. _computation:

Computation of Molecular, Cellular, and Transcriptional Dynamics
================================================================= 
Here we list a few papaer on solving chemical master equation.

.. dropdown:: Peccoud and Ycart, 1995. `Markovian Modeling of Gene-Product Synthesis. <https://doi.org/10.1006/tpbi.1995.1027>`_

            .. grid:: 2

                .. grid-item:: 
                    This article studied the telegraph model of transcription. They studies properties of the systems and derived an analytical solution.

                .. grid-item-card:: The telegraph model

                    .. image:: ./figures/Peccound_1995.png
                        :width: 300
                        :align: center
                        :alt: some text

.. dropdown:: Munsky and Khammash, 2006. `The finite state projection algorithm for the solution of the chemical master equation. <https://doi.org/10.1063/1.2145882>`_

            .. grid:: 2

                .. grid-item:: 
                    This article introduced the finite state projection (FSP) method to directly solves or approximates the solution of the chemical master equation. If there are only a finite number of reachable states, the exact soluiton can be computed using matrix exponentials. When there are infinite or extremely large number of reachable states, the state space is projected onto finite space, and the authors provided an estimation of accuracy of the truncated space approximation.

                .. grid-item-card:: Fig 1 Conceptual figure for the finite state projection method

                    .. image:: ./figures/Munsky_2006.jpeg
                        :width: 300
                        :align: center
                        :alt: some text

.. dropdown:: Jahnke and Huisinga, 2007. `Solving the chemical master equation for monomolecular reaction systems analytically.<https://doi.org/10.1007/s00285-006-0034-x>`_

            .. grid:: 2

                .. grid-item:: 
                    This article derives the exact solution formula for the chemical master equations of monomolecular reaction systems. It shows that the solutions can be expressed as a convolution of multinomial and product Poisson distributions, with time-dependent parameters evolving according to traditional reaction-rate equations.

.. dropdown:: Shahrezaei and Swain, 2008. `Analytical distributions for stochastic gene expression. <www.pnas.org/cgi/doi/10.1073/pnas.0803850105>`_

            .. grid:: 2

                .. grid-item:: 
                    This article used time-scale difference of mRNA and protein decay to derive an approximation of protein distribution under the two-stage (constitutive) and three-stage (telegraph) model.
                

                .. grid-item-card:: Fig 3 Predictions and simulations for a three-stage model of gene expression. 

                    .. image:: ./figures/Swain_2008.png
                        :width: 300
                        :align: center
                        :alt: some text
            


.. dropdown:: Singh and Bokes, 2012. `Consequences of mRNA transport on stochastic variability in protein levels. <https://doi.org/10.1016/j.bpj.2012.07.015>`_

            .. grid:: 2

                .. grid-item:: 
                    This article derived the analytical solution of bursty model via probability generating function methods. They studied the effects of pre-mRNA export on mRNA and protein levels, and concluded that export step can reduce variability at mRNA level but not protein level.
                

                .. grid-item-card:: Fig 1 Schematic of the gene expression model 

                    .. image:: ./figures/Singh_2012.jpeg
                        :width: 300
                        :align: center
                        :alt: some text
            
