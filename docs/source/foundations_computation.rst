.. _computation:

Theory and Computation of Transcriptional Dynamics
================================================================= 
Here we list a few reference papers on the theory and simulation of the chemical master equation as well as its application in stochastic modeling of gene expression.

.. dropdown:: `A general method for numerically simulating the stochastic time evolution of coupled chemical reactions. <https://doi.org/10.1016/0021-9991(76)90041-3>`_ Gillespie, 1976. 

            In this article, Gillespie described the Stochastic Simulation Algorithm (Gillespie algorithm).

.. dropdown:: `The Poisson Representation. I. A New Technique for Chemical Master Equations. <https://doi.org/10.1007/BF01014349>`_ Gardiner and Chaturvedi, 1977. 

            In this article, Gardiner and Chaturvedi introduced the Poisson representation which expresses the probability distribution as a convolution of Poisson distributions. This representation transforms chemical master equations into Fokker-Planck and stochastic differential equations and leads to a simple expression of chemical equilibrium states.

.. dropdown:: `Markovian Modeling of Gene-Product Synthesis. <https://doi.org/10.1006/tpbi.1995.1027>`_ Peccoud and Ycart, 1995. 

            .. grid:: 2

                .. grid-item:: 
                    This article studied the telegraph model of transcription. They studies properties of the systems and derived an analytical steady state solution.

                .. grid-item-card:: The telegraph model

                    .. image:: ./figures/Peccoud_1995.png
                        :width: 300
                        :align: center
                        :alt: some text

.. dropdown:: `The chemical Langevin equation. <https://doi.org/10.1063/1.481811>`_ Gillespie, 2000. 

            In this article, Gillespie derived the chemical Langevin equation (CLE) from the chemical master equation (CME) based on the existence of a timescale with certain properties. In particular, the two properties are: 1) the timescale is small enough that the change in the state will be so slight and the propensity functions do not changes appreciably; 2) the timescale is large enough that the expected number of occurrences of each reaction channel will be much larger than 1.


.. dropdown:: `Approximate accelerated stochastic simulation of chemically reacting systems. <https://doi.org/10.1063/1.1378322>`_ Gillespie, 2001. 
            
            In this article, Gillespie proposed the "τ-leap" method for Gillespie algorithm. It finds a time τ that is small enough that the change in the state and propensity function are negligible. Therefore, in this time interval, the propensity function will be essentially constant and the number of times a reaction channel fires will be a Poisson random variable.

.. dropdown:: `Summing up the noise in gene networks. <https://doi.org/10.1038/nature02257>`_ Paulsson, 2004. 

            In this article, Paulsson used fluctuation-dissipation theorem to derive an equation for second order noise. The equation depends on kinetic orders of reactions and unified results from a few studies of gene expression noise.

.. dropdown:: `The finite state projection algorithm for the solution of the chemical master equation. <https://doi.org/10.1063/1.2145882>`_ Munsky and Khammash, 2006. 

            .. grid:: 2

                .. grid-item:: 
                    This article introduced the finite state projection (FSP) method to directly solves or approximates the solution of the chemical master equation. If there are only a finite number of reachable states, the exact soluiton can be computed using matrix exponentials. When there are infinite or extremely large number of reachable states, the state space is projected onto finite space, and the authors provided an estimation of accuracy of the truncated space approximation.

                .. grid-item-card:: Fig 1 Conceptual figure for the finite state projection method

                    .. image:: ./figures/Munsky_2006.jpeg
                        :width: 300
                        :align: center
                        :alt: some text

.. dropdown:: `Solving the chemical master equation for monomolecular reaction systems analytically. <https://doi.org/10.1007/s00285-006-0034-x>`_  Jahnke and Huisinga, 2007. 
            
            This article derives the exact solution formula for the chemical master equations of monomolecular reaction systems. It shows that the solutions can be expressed as a convolution of multinomial and product Poisson distributions, with time-dependent parameters evolving according to traditional reaction-rate equations.

.. dropdown:: `A stochastic model of gene regulation using the chemical master equation. <https://doi.org/10.1007/978-0-8176-4558-8_7>`_ Booth et. al., 2007. 
            
            This chapter describes a hybrid deterministic/stochastic simulation for chemical master equation in combination with chemical rate equations, which is applied to study genetic regulatory networks in prokaryotes: states of the gene represent the binding and unbinding of protein complexes to DNA are modeled using the master equation, while protein and substrate concentrations are represented by continuum variables modeled by differential equations.


.. dropdown:: `Analytical distributions for stochastic gene expression. <www.pnas.org/cgi/doi/10.1073/pnas.0803850105>`_ Shahrezaei and Swain, 2008. 

            .. grid:: 2

                .. grid-item:: 
                    This article used time-scale difference of mRNA and protein decay to derive an approximation of protein distribution under the two-stage (constitutive) and three-stage (telegraph) model.
                

                .. grid-item-card:: Fig 3 Predictions and simulations for a three-stage model of gene expression. 

                    .. image:: ./figures/Swain_2008.png
                        :width: 300
                        :align: center
                        :alt: some text
            


.. dropdown:: `Consequences of mRNA transport on stochastic variability in protein levels. <https://doi.org/10.1016/j.bpj.2012.07.015>`_ Singh and Bokes, 2012. 

            .. grid:: 2

                .. grid-item:: 
                    This article derived the analytical solution of bursty model via probability generating function methods. They studied the effects of pre-mRNA export on mRNA and protein levels, and concluded that export step can reduce variability at mRNA level but not protein level.
                

                .. grid-item-card:: Fig 1 Schematic of the gene expression model 

                    .. image:: ./figures/Singh_2012.jpeg
                        :width: 300
                        :align: center
                        :alt: some text
            

.. dropdown:: `Steady-state fluctuations of a genetic feedback loop: An exact solution. <https://doi.org/10.1063/1.4736721>`_ Grima et al., 2012. 

            .. grid:: 2

                .. grid-item:: 
                    This article derived the exact steady-state solution of the chemical master equation for a gene regulatory feedback loop
                
                .. grid-item-card:: The model for a gene regulatory feedback loop
            
                                .. image:: ./figures/Grima_2012.png
                                    :width: 300
                                    :align: center
                                    :alt: some text
                        
.. dropdown:: `Steady-state fluctuations of a genetic feedback loop: An exact solution. <https://doi.org/10.1063/1.4736721>`_ Grima et al., 2012. 

            .. grid:: 2

                .. grid-item:: 
                    This article derived the exact steady-state solution of the chemical master equation for a gene regulatory feedback loop
                
                .. grid-item-card:: The model for a gene regulatory feedback loop
            
                                .. image:: ./figures/Grima_2012.png
                                    :width: 300
                                    :align: center
                                    :alt: some text
                        
.. dropdown:: `Phenotypic switching in gene regulatory networks. <https://doi.org/10.1073/pnas.140004911>`_ Thomas et al., 2014. 

            .. grid:: 2
            
                .. grid-item:: 
                    This article extended linear noise approximation (LNA) to conditional LNA. 
                
                .. grid-item-card:: The model for a gene regulatory feedback loop
            
                                .. image:: ./figures/Thomas_2014.png
                                    :width: 300
                                    :align: center
                                    :alt: some text
