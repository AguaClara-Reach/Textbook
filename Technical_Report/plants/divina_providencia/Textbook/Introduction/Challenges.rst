.. raw:: html

    <embed>
       <link rel="canonical" href="https://aguaclara.github.io/Textbook/Introduction/Challenges.html" />
       <script src="https://hypothes.is/embed.js" async></script>
    </embed>

.. _title_Challenges:

****************
Challenges
****************

Introduction
============

We are providing these innovation topics as a continuation of the journey begun by the AguaClara program in 2005. Our goal then and now was to develop improved and new technologies that would be resilient and accessible for the millions of small communities that don't currently have safe water on tap. We recognized the unserved gap between city and household-scale water systems where neither governments nor non governmental organizations had high performing solutions for treating contaminated water sources for municipal water supplies. The technology gap became the motivation for research funded by the National Science Foundation and the United States Environmental Protection Agency and collaborative innovation with a growing list of partner organizations who design/build/operate/train/transfer the technologies to communities. The feedback and learning by doing guides the research process so that we focus on real problems with a high potential for dramatic improvements over existing technologies.

Magnitude of the Challenge
--------------------------

A significant fraction of the global population needs Safe Water on Tap.

* Some three in ten people (2.3 billion) lack access to safe and readily available water at home (or maybe it is 5 in 10…)
* Additional 1.2 billion from population growth gives 3.5 billion need water by 2030
* 267 million people per year!
* 800,000 L/s per year of new installed capacity (assuming 3 mL/s per person)
* Water for 18 New York Cities per year! (new capacity installation rate!)
* Aging infrastructure for cities needs to be rehabilitated or replaced

Motivating Hypotheses
---------------------

Our underlying assumption is that communities need better tools to solve the water crisis. The AguaClara ecosystem provides a platform for development of new technologies and for directly linking research, design, invention, and implementation. Our connections with implementation partners provide a continuous source of feedback and areas for further technology development.

1. We can develop new and improved solutions fastest by working as a collaborative community where we share freely what we are learning.
2. The path to providing more communities with sustainable Safe Water on Tap is to discover the physics of the core drinking water treatment technologies so that we can both begin to optimize the design of those technologies and invent new technologies.
3. Innovation is accelerated by rapidly deploying the new technologies, evaluating their performance, learning from the plant operators, and then by using that feedback to guide research.

Research Topics
---------------
The scope of research needed to save our planet and improve the well-being of our neighbors extends well beyond our focus on water. The current research topics represents what we have identified as critical gaps in our knowledge that have the potential to revolution the constraints that we have assumed over the past century of drinking water and wastewater treatment. The research topics will expand as more universities join this effort to rethink, reimagine, and then reinvent how cities, towns, and villages manage water and wastewater.


Drinking Water Challenges
=========================

The potential to make a dramatic improvement in the quality of life of communities will guide our journey. Although the AguaClara program invented numerous technologies and contributed to a new understanding of the physics of drinking water treatment, there are still many unanswered questions.

* Why is reducing the turbidity to less than 0.01 NTU not currently possible for most surface water treatment plants that rely on flocculation, sedimentation and sand filtration? Or stated another way, what controls the particle removal efficiency of surface water treatment plants?
* How can we take measurements of raw water quality and use that to optimize the design of a water treatment plant? This will require creating the models that describe the physics of each unit process and that is a recurring theme of the research introduced below. We are making significant progress in making the connection between the properties of primary particles and the density of the resulting floc.
* How can we invent new and improved technologies that enable communities to reliably produce high quality drinking water without needing to rely on expensive, energy consuming, expendable proprietary components?

Entrance Tank for Multi-Train Plant
-----------------------------------

Introduction
^^^^^^^^^^^^

As AguaClara technologies are used for higher flow rates it becomes attractive to split the flocculator/clarifier processes into parallel treatment trains so that one treatment train can potentially be taken offline for maintenance or during low flows. In this case it is desirable to have a single entrance tank where flow is measured and divided equally between the treatment trains and where the coagulant can be added. To reduce the complexity of managing multiple treatment trains it is best if the coagulant dose for all treatment trains is set at a single location.

The AguaClara plant at Gracias, Lempira, Honduras is an example of a two train treatment plant with each train treating 60 L/s. It has two independent entrance tanks and chemical dosing systems. Although that plant is only a few years old there is already an effort underway to add a third treatment train for an additional 60 L/s. To simplify operation the goal is to design a new entrance tank that delivers water dosed with coagulant to each of the treatment trains.

Tasks and Goals
^^^^^^^^^^^^^^^

* Create a copy of the AIDE entrance tank workspace (`ET 6-60 lps <https://cad.onshape.com/documents/90e106377fd0bc25af081c88/w/1089ae6d00e64e7711db0ab0/e/6c7f58d6bbc9425f3cda1414>`_)
* Review both the FeatureScript code and the part studio feature list to learn how the entrance tank is designed and created in Onshape.
* For this design the bypass option that allows water to flow via pipe directly to the filter inlet channel can be eliminated at least initially.
* Increase the flow rate in the overrides to 180 L/s to see which components fail. Review the FeatureScript Notices to see which components reported errors.
* Develop a plan to address the current limits on the size and flow of the various components.
* Develop a plan to add the number of treatment trains as an input to the entrance tank FeatureScript code
* Modify the part studio to accommodate a variable number of treatment trains with an LFOM serving each treatment train.
* Evaluate methods to add the coagulant

   * one injection point for each treatment train (perhaps into each LFOM)
   * one injection point upstream from the LFOMs. This method requires careful design to ensure adequate mixing before the flow splits so that each treatment train receives the same coagulant dose. The advantage of this approach is that there is only one injection point to maintain.
* Carefully review the design to identify other changes that could be made for ease of fabrication, operation, and maintenance.



Prefabricated AguaClara Plant
-----------------------------

Introduction
^^^^^^^^^^^^

AguaClara plants are currently built in place using a combination of concrete, bricks and rebar for the civil structure and PVC pipes and polycarbonate sheets for the hydraulic components. Construction projects require approximately 1 year from site preparation to commissioning. There is a significant cost related to mobilizing the team to work on remote sites. Plants smaller than design flows of 10 L/s have dramatically increasing capital costs normalized by their design flow rate. This leads to the insight that prefabricated plants would significantly reduce the cost of an extended mobilization at a remote site.

Conventional prefabricated plants have demonstrated that they can quickly be installed and that they commonly fail quickly too. Thus our goal is to design prefabricated plants that have all of the advantages of the AguaClara built in place plants (see :ref:`heading_AguaClara_Innovations`) and the advantages of rapid deployment and mass production.

Tasks and Goals
^^^^^^^^^^^^^^^

 * Evaluate choice of materials for the water proof membrane used to line the tanks. Options include and aren't limited to printed concrete, PVC (see `Intuitech <https://www.intuitech.com/pilot-plants/>`_ ), HDPE, stainless steel, and ballistic nylon. Create a design for a rectangular tank (2 m long x 1 m wide x 2 m deep) that spaces the exoskeleton based on the strength of the membrane and selects the exoskeleton structural steel to resist the hydrostatic forces. Use this model to explore optimal material selection to minimize cost. See this `draft design of a PVC tank supported by rectangular structural steel <https://cad.onshape.com/documents/8a0779ccdbf6c45618c005a4/v/5dc77a476d5ae24c78469b3d/e/b9c01cd17bfaebce071f3cc8>`_.
 * Study the `clarifier <https://cad.onshape.com/documents/e05915c533ee7568c402981a/w/56de4202f426e6443151ca07/e/3f94eabd115787bc33ae755d?configuration=G_max%3D140.0%3BQm_max%3D20.0%3BShow_Internal_Components%3Dtrue%3BTEMP_min%3D10.0%3BcaptureVm%3D0.12%3BprintParams%3Dfalse%3Brep%3Dtrue%3BrepBayInternals%3Dfalse%3BupVm%3D1.0&renderMode=0&uiState=627688ef04309300574a09f6>`_ and identify the most challenging components to fabricate. Develop fabrication methods and assess if the optimal material combination previously selected works given the fabrication constraints.
 * Evaluate the materials based on life cycle analysis or environmental impact to ensure that we aren't missing an option that would be better for a sustainable planet.

Options and Questions to Explore
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 * Will you separate unit processes that are connected by piping onsite or share walls as is done in the built in place plants. Note that the walls separating unit processes must be able to handle full tank on one side and empty tank on the other side for plant maintenance.
 * How will the operator walk around the unit processes to monitor performance? AguaClara developed the standard of having walkways at a convenient height so the operator can bend over and closely observe flocs.
 * How will pipes pass through the walls of the tanks?
 * Is it advantageous to tie the top of the tanks together with tie-rods with the complication of making it difficult to install the hydraulic components, or is it better to use a strong beam around the top of the tank?


POST - Plant Operator Smart Tracker
-----------------------------------

Introduction: We need a method to collect and visualize water quality across AguaClara plants to document the performance and reliability of AguaClara technologies.

The POST team is working to develop a set of tools for a collection and visualization for water quality from AguaClara drinking water plants.

Tasks and Goals
^^^^^^^^^^^^^^^

Devise a simpler system using existing platforms to enable sharing of plant data. Likely platform is Google Sheets.
Develop/explore methods to

 * Validate incoming data
 * Automatically update graphs
 * Provide feedback to operators
 * Calculate summary statistics
   * coagulant consumed in a month
   * Days in compliance with Honduran NTU standard
   * Days in compliance with EPA NTU standard
   * more ideas here
 * Work with APP and plant operators to pilot system
 * Explore how to use incentives to encourage plant operators to interact and contribute

Trash Rack Design and Fabrication
---------------------------------

Create a high porosity trash rack that removes all particles larger than 3 mm.

Introduction
^^^^^^^^^^^^

The trash rack in the `entrance tank <https://cad.onshape.com/documents/90e106377fd0bc25af081c88/w/1089ae6d00e64e7711db0ab0/e/6c7f58d6bbc9425f3cda1414>`_ is a proposed new design that is only a draft and that needs to be fabricated and evaluated for feasibility. The idea is that the vertical bars could be thin stainless steel wires. To keep the gaps at 3 mm the wires will need to be under a large amount of tension (analysis required here!) and that will require some sort of tensioning device that needs to be designed. The frame could be rectangular tubing. It is very unlikely that PVC is strong enough to maintain the required tension in the wires.

Tasks and Goals
^^^^^^^^^^^^^^^

 * Devise a method to space the wires and put them in tension.
 * Calculate the amount of tension required to maintain the spacing of the wires
 * Calculate the required dimensions of the frame to maintain all of the wires in tension
 * Fabricate a prototype and explore failure modes that would allow material larger than 3 mm to pass between the wires.


Fractal Floc Model
------------------

The fractal floc model (FFM) will describe floc properties (density, bond strength, and surface properties) as a function of composition and floc diameter. The FFM will provide the missing connection between raw water quality and design and performance of treatment processes.
The FFM will build the average floc in a series of ordered steps that capture the order in which these processes occur in flocculation. The first step is adsorption of dissolved species (DS) to the coagulant nanoparticles (CNP) to form a CNP-DS aggregate. The CNP-DS aggregates then attaches to the primary particles (PP) in the suspension to form PP-CNP-DS aggregates. The PP-CNP-DS aggregates then combine to form flocs.

The primary particles could include powdered activated carbon (PAC) or biochar that is added to aid in the removal of dissolved species. In that case the dissolved species will partition between adsorption to the PAC or biochar and to the coagulant nanoparticles.

The floc properties calculated by the FFM will enable prediction of the terminal size and concentration of flocs in the Fluidized Floc Primary Filter, the head loss per pore in the Granular Media Secondary Filter, and the optimal coagulant dose. The FFM will be a core component of unit process models because the floc properties must be understood in order to model the floc behavior.

Flocculation
------------

The `AguaClara Hydraulic Flocculation Model <https://www.liebertpub.com/doi/full/10.1089/ees.2017.0332>`_ is the first flocculation model that can predict the relationship between coagulant dose, flocculator design, and settled water turbidity. That model has been `extended to include the effects of humic acid <https://www.liebertpub.com/doi/abs/10.1089/ees.2018.0405>`_ and given that the physics-based model explains both clay and humic acid it would seem reasonable to expect that other particulate and dissolved substances could be added to the model.

The flocculation model opens up many opportunities for further research. The model does not yet predict the floc size distribution. We hypothesize that the floc size distribution is set by floc aggregation that is controlled by fluid deformation that transports flocs toward collisions, by boundary layers that develop around flocs that are rotating in the deforming fluid, and by the ratio of shear forces to coagulant nanoparticle bond strength that determines the likelihood of attachment after a collision between flocs.

An enabling measurement will be particle size and count in a flocculating suspension. Particle counters are frequently used on high quality water and are not able to measure particles in the concentrated suspensions encountered in flocculators. There are at least two options for measuring the floc size distribution in the flocculation process.

Floc Size and Count App
^^^^^^^^^^^^^^^^^^^^^^^

Develop an app using Python, a camera with a lens that can see particles as small as a few :math:`\mu` meter to automatically count the size and number of flocs in turbid flocculated water. This requires an algorithm to ignore small particles that are obscured by the flocs. The AguaClara Cornell program developed an `image based system of floc sizing <https://www.liebertpub.com/doi/10.1089/ees.2015.0311>`_ that uses a 1 cm square sample cell and that uses image analysis to eliminate flocs that are blurry and hence aren't in the target analysis volume.

Tasks and Goals
"""""""""""""""

* Improve floc detection algorithm by testing a variety of algorithms and optimize the thresholding of images
* Calibrate camera used to capture images of flocs
* Begin/continue bottom up testing of app, starting with still images and progressing with flocculation experiments
* A long term goal is to use floc size data to provide coagulant level recommendations


An alternative is to send the water through a tube settler and then to a commercial particle counter.

Automated Coagulant Dosing Algorithm
-------------------------------------

Automated coagulant dosing (see :ref:`title_Coagulant_Automation`) and the ability to provide guidance to operators to optimize plant performance are potentially within our reach now that we have a flocculation model. The model predicts the concentration of small particles after flocculation. We can measure the concentration of small particles after flocculation by passing a continuous sample of flocculated water through a tube settler to remove the large flocs. The supernatant particle concentration from the tube settler can be measured either with a turbidimeter or a particle counter. Research will identify what is required to obtain the model parameters that will be used to set the next coagulant dose.

The AguaClara Pilot Plant at the Cornell University Water Filtration Plant provides an opportunity to operate a 0.5 L/s AguaClara plant, compare it with a conventional water treatment plant, and test new technologies. The first technology to test is the ability to control the coagulant dose automatically. As advances are made in floc recycle for enhance floc filter performance it may be possible to test that technology using the 3’ diameter bent pipe clarifier.

Tasks and Goals
^^^^^^^^^^^^^^^

 * Collect performance data as a function of coagulant dose using the ramp function in the Pilot Plant LabVIEW program.
 * Analyze the data to see if it can reasonably be linearized and used to set the coagulant dose.
 * Evaluate and develop methods to estimate the required parameters in real time continuously based on recent plant performance.
 * If necessary, improve the design of the tube settler used to sample the flocculated water.
 * Obtain overall performance data over a broad range of raw water condition
 * Develop a consistent method for analysis of performance data
 * Assess the stability of the automated coagulant dosing system (see :ref:`title_Coagulant_Automation`) and propose improvements to the algorithm.

Resources
^^^^^^^^^

* See :ref:`title_Coagulant_Automation`.

Automated Coagulant Dosing Mechanism
------------------------------------

Introduction
^^^^^^^^^^^^

The AguaClara Chemical Dose Controller (CDC) can easily be automated with a minimum of moving parts. A stepping motor can move the slider to a new location to change the coagulant dose and then the automation system can power down and wait for the next CHANGE in required coagulant dose to wake up and adjust. Yitzy Rosenberg built and demonstrated a low cost system that could be controlled via a smart phone (see `Hydraulic Autonomous Doser <../_static/references/Hydraulic Autonomous Doser HAnD MEng Report.pdf>`_).

The automated doser would be designed so that manual operation would still be easy and the automated doser would have much higher reliability (and no continuously moving parts) than conventional systems that rely on peristaltic pumps.

Low Cost Turbidimeter
---------------------

Online turbidimeters cost approximately $3,000 and an AguaClara plant should have sampling at the raw water, the clarified water, and the filtered water. Thus even basic instrumentation for continuous performance monitoring is a high cost item especially for small plants. One of the reasons for the high cost of turbidimeters is the requirement that they be EPA certified. This constraint may not be necessary in much of the world and there is a big need for turbidimeters in millions of small cities and towns.

Take the `design created by Chris Kelley et al. <https://www.mdpi.com/1424-8220/14/4/7142>`_ and build a prototype and then identify improvements necessary to begin using this system as an online turbidimeter.

Floc Filter
-----------

AguaClara invented the zero settled sludge clarifier and the required `geometry to maintain a stable fluidized floc suspension <https://ascelibrary.org/doi/abs/10.1061/%28ASCE%29EE.1943-7870.0000773>`_ that provides primary filtration. The addition of primary filtration in clarifiers improves their `particle removal efficiency <https://iwaponline.com/aqua/article/59/5/312/29069/Parameters-affecting-steady-state-floc-blanket>`_, eliminates the need for mechanized sludge removal, and dramatically reduces mean flows that commonly result in poor floc capture. Although it is known that the primary filtration process enhances particle removal, the physics of primary filtration have been elusive and are currently an AguaClara Cornell NSF research project. Experiments conducted starting in January of 2021 suggest that fluidized flocs have a finite capacity to capture particles. That insight paves the way for a new research project to optimize the design and operation of primary filters and answer a new series of questions.

1. Why do flocs in the floc filter have a finite capacity to capture incoming particles and flocs?
2. Could flocs that have reached their capacity be rejuvenated? This has the potential to dramatically improve the particle capture efficiency of the primary filter.
3. What is the optimal floc size distribution in the flocculator effluent to achieve the lowest concentration of primary particles exiting the clarifier?
4. How could flocs that have reached their full capacity be selectively removed from the primary filter?

Floc filters with recycled flocs could dramatically reduce settled water turbidity and make the AguaClara clarifier even better. Kevin Sarmiento has demonstrated that flocs in the floc filter capture particles by having flow go right through the floc. Then the flocs slowly become less porous as they fill up with particles and eventually the flocs become useless. There is also strong evidence that the flocs that come from the flocculator all go to the plate settlers where they settle and  grow in size as they avalanche back into the floc filter. Those newly formed flocs are very porous (have a low fractal dimension) and hence are useful for capturing particles. The challenge is to figure out how to increase the number of low fractal dimension (highly porous) flocs in the floc filter. One source of flocs is the floc hopper. Many of those flocs aren’t very porous anymore. The idea is to break those flocs by sending them through an orifice and then either return them to the flocculator or if they are still large enough to be captured by the plate settlers (unlikely), then they could be returned directly to the clarifier.

A second line of research would be to investigate an improved method of floc wasting. Our current floc wasting system removes flocs from the top of the floc filter and thus tends to remove flocs that have just returned from the plate settlers. Thus our current floc wasting system is the worst possible design. This may be why we have been unable to get good performance from the laboratory scale reactors that have a single 1” PVC pipe with a bend in it for the tube settler and a wasting port that intercepts most of the flocs returning from the plate settlers.

High fractal dimension flocs are more dense and thus settle faster and thus they might be more concentrated at the bottom of the floc filter. Thus it may be better to waste flocs from the sloped surface at the bottom of the floc filter where flocs slide down into the jet reverser. This hypothesis could be tested by comparing the performance of the glass walled clarifier with floc extraction from the bottom slope. Kevin Sarmiento has already experimented with this approach and thus begin by reviewing his `thesis, Particle Removal in Floc Blanket Clarifiers via Internal Flow Through Porous Fractal Aggregates <https://doi.org/10.7298/3zv3-ya45>`_.

Tasks and Goals
^^^^^^^^^^^^^^^

* Learn how the floc filter is formed and how flocs transition from flocculator to plate settlers to floc filter and then finally to the floc hopper :ref:`title_Clarification_Intro`.
* Finish setting up the experimental apparatus and ProCoDA for the floc breakup experiment
* Validate that we can break flocs into primary particles in high shear environments such as flow constrictions
* Begin testing recycling of flocs from the floc hopper
* Determine the best location for removal of flocs from the floc filter (top, middle or bottom of the clarifier)
* Find the rate of recycle that works for the given experimental conditions
* Compare existing performance data without floc recycle to new data with floc recycle
* Compare performance as a function of the injection location into the flocculator.


Plate Settlers
--------------

Although we don't currently see research into plate settlers as a priority, it is likely that we will circle around to research to determine the optimal design of plate settlers to maximize performance of the subsequent granular media filtration. The design of plate settlers is a function of the properties of the flocs given the raw water composition and the amendments added for treatment. AguaClara experience with highly colored, low turbidity water at Gracias, Honduras indicates that surface waters with those characteristics produce low density flocs that are difficult to remove by sedimentation. The minimum density of flocs given the raw water characteristic will be the critical design for clarifiers and will determine if amendments to increase floc density are required for efficient gravity-based separation.

Granular Media Filtration
-------------------------

The goal of this research is to develop a physics-based model of depth filtration of fractal flocs. The depth filtration model (DFM) will characterize the active filtration zone that migrates downstream as fractal flocs are intercepted at flow constrictions and as the deposition constrictions reach their minimum diameter. The proposed DFM will connect the interactions between pore geometry evolution caused by fractal floc deposition to the changing flow pattern that causes an increase in interception and an increase in fluid drag on flocs that ultimately prevents attachment when the pore reaches its minimum size. Laboratory experiments will be conducted to test hypotheses and guide the model development.

The DFM will be used to optimize the design and operation of rapid sand filters that continue to be the most common final particle removal process in drinking water treatment plants. The model will be used to create optimized designs of sand filters used in sustainable, gravity-powered, drinking water treatment facilities constructed through collaboration with AguaClara implementation partners in Honduras, Nicaragua, Colombia. Feedback to the design process will be provided from monitoring community-scale treatment plants and from informal conversations with engineers, technicians, and plant operators.

Research questions for granular media filtration:

1. Is the ratio of coagulant nanoparticle bond strength to the drag force on a primary particle a reasonable characterization of the ability of a flow constriction to capture a primary particle?
2. Is the velocity distribution at the entrance to a forming flow constriction reasonably modeled as uniform?
3. How much of a change in flow can a fully formed flow constriction withstand before the fluid forces exceed its strength and how does the constriction fail? Specifically, what size flocs do ruptured flow constrictions shed?
4. What size of flocs is optimal for producing partially formed flow constrictions that are then able to efficiently capture primary particles?

Tasks and Goals
^^^^^^^^^^^^^^^

 * Build a sand filter that allows for varying sand particles
 * Possibly set up multiple filters to test multiple factors at once
 * Run a series of experiments to measure performance (filtered water turbidity and head loss as a function of time) over a range of sand diameters. Ideally use a fairly wide range of perhaps 0.2 mm to 1 mm.


Gravity Exclusion Zones
-----------------------

Technology to completely eliminate slotted pipes in the StaRS filters.

Introduction
^^^^^^^^^^^^

The StaRS Filter is filled with alternating influent and effluent pipes. The biggest challenge with the effluent pipes is figuring out how to allow water to enter the pipe without letting sand exit the filter. StaRS filters currently use slotted pipes, but that method has multiple disadvantages including challenges sourcing the slotted pipes and clogging with sand grains.

Gravity Exclusion Zones (GEZs) are an alternative method that would eliminate the need for slotted pipes. The GEZ rely on the weight of the sand to create pockets of clean water that are big enough to not allow sand to get through. This is achieved by creating a zone with a sand-water interface that is large enough to prevent sand fluidization. The efficacy of this design needs to be tested at small scale specifically to learn what causes the GEZ to fail as the effluent flow rate is gradually increased.

Tasks and Goals
^^^^^^^^^^^^^^^

 * Study the current design of the StaRS Filter, specifically the influent and effluent pipes
 * Create a small scale model of the GEZ with accompanying sand, pipes, and water
 * Test the model at different flow rates
 * Observe quantitative and qualitative characteristics of the system
   * At what flow rate does it fail
   * When in a filtration cycle will the system be most likely to fail? Check all of the water level changes from beginning a filtration run through backwash and back to filtration. Look for times when water will flow the fastest through the outlet system.

Resources
^^^^^^^^^

 * `StaRS FInE Presentation <https://www.youtube.com/watch?v=Y5BJtLSR1uU&list=PLhsGtpY8ipdZL4lExJA8KC0zCkaxwfs8R&index=17&ab_channel=AguaClaraCornell>`_
 * `Gravity Exclusion Zone calculations <https://github.com/AguaClara/PF200/blob/master/Fall%202019/PF200_Final_Report.ipynb>`_
 * :ref:`title_Filtration_Introduction`

Dissolved Organic Matter (DOM) Removal
--------------------------------------

Introduction
^^^^^^^^^^^^

The goal of the DOM team is to develop a method to remove DOM from water. One of the challenges with DOM is that when DOM forms flocs by attaching to coagulant nanoparticles the resulting flocs have a density that is very close to the density of water and in some cases the resulting flocs are buoyant.  Dissolved Air Floatation (DAF) would be a great method to separate these flocs from water, but DAF requires an air compressor, a completely different clarifier design, and it can’t be used with a floc filter. Thus we would like to explore options for increasing the density of the resulting flocs so they can be removed in an AguaClara clarifier.

There are two very different approaches to this problem. (We should also explore other options that might result in improved removal of DOM!) One is to add clay so that the flocs have a sufficient clay concentration so they are dense enough to settle to the plate settlers. The other solution is to add Powdered Activated Carbon (PAC) that will both absorb DOM and increase the density of the flocs. In both cases PACl will need to be added to form the flocs.

Both of these methods are expected to work. The questions are which strategy produces the best quality of water and which strategy is the most economical.

Tasks and Goals
^^^^^^^^^^^^^^^

 * Use a single high concentration of humic acid (perhaps 15 mg/L as humic acid salt).
 * Determine how much coagulant is needed and how much clay is needed to form a floc filter and produce low turbidity water (note that the clarifier design will likely need to be modified to remove excess flocs from the bottom of the floc filter rather than from the top of the floc filter. - talk with the floc recycle team to learn why!). This will require a series of experiments at different clay concentrations and each clay concentration will require different coagulant dosages. Use the hydraulic flocculation model to inform the ranges of coagulant dosages that you test.
 * Develop a method to assess the concentration of the floc filter. One easy method is to add a sample tap and then measure the turbidity of that sample. If the turbidity is too high to be measured, then dilute it by a factor of 10 or more.
 * Repeat the clay experiments but use PAC instead of clay.
 * Assess which method works best and compare operating costs.

Relevant research
^^^^^^^^^^^^^^^^^

* :ref:`title_Flocculation_Model`


Disinfection
------------

After more than 100 years of chlorination it may be time to review the public health trade-off compared with alternatives that don't have the negative health impacts associated with chlorine. The water treatment industry has long assumed that chlorination is an essential barrier required to fully protect public health. An analysis of the underlying assumptions for requiring a chlorine residual reveals that the residual would only provide protection for recontamination events with a maximum carbon concentration of about 1 mg/L. Thus it is unlikely that a chlorine residual would provide protection against recontamination. A pathogen by pathogen analysis of the protection provided by chlorine vs the protection provided by the particle removal processes suggests that chlorine is most effective against organisms that have high infective doses and thus the particle removal processes may already provide sufficient protection. The challenge of taking on the emotionally charged questions associated with chlorination will require a thoughtful strategy and may not be amenable to scientific research.

RAM Pump
--------

Create a reliable and efficient ram pump for plant implementation

Introduction
^^^^^^^^^^^^

The goal is to design and develop an efficient hydraulic ram pump for implementation in AguaClara plants. The ram pump is needed to deliver filtered water from the end of the treatment process to the higher elevation chemical platform for utilization in chemical stock tanks and possibly for the plant bathroom. The conventional ram pump that spills the wasted water have been used in AguaClara plants for many years. The AguaClara design uses a closed pipe system that facilitates returning the "wasted" water to the pipe that goes to the community water storage tank. In January 2020, a prototype ram pump was tested at the AguaClara plant in Gracias, Honduras.

Tasks and Goals
^^^^^^^^^^^^^^^

 * Repair the ram pump using stronger components that will resist the cyclical high pressures
 * Calculate the spring force required to open the valve
 * Develop a method to measure the distance the valve opens
 * Develop a method to design the required spring that sets BOTH the maximum force that will be used to open the valve and the distance over which the spring force drops to zero (based on the optimal distance that the valve should be opened).
 * Develop methods to quickly and easily “tune” the spring to achieve the desired performance. Perhaps develop a spring attachment method that allows the number of spring coils to be continuously varied and yet provides a connection method that doesn’t shift as the pump operates.
 * Collect high speed data sets (perhaps 1000 Hz) to characterize the cycle time and then calculate the efficiency of the pump (compared with what can theoretically be pumped in a cycle of that time duration).
 * Write Python or Matlab code to measure the cycle time of the ram pump
 * Vary the driving head on the pump by adding a flexible hose to the waste valve and see what is required to adjust the spring to achieve efficient performance
 * Develop the equations and theory that determines the spring properties required for efficient performance

Resources
^^^^^^^^^

 * `Hydraulic Engineering Lecture on ram pumps <https://github.com/monroews/Hydraulics/raw/master/06_Hydraulic_Transients.pptx>`_
 * `Github <https://github.com/AguaClara/ram_pump>`_



Wastewater Treatment Challenges
===============================

Although AguaClara began with a focus on drinking water treatment, we have always been keenly aware that adequate wastewater treatment is absolutely essential to reduce harm to the environment and harm to downstream communities.

One of the core ideas of the AguaClara design process is that reactor geometry and hydraulic design are critical to obtain the target performance. Environmental engineers have tended to focus on the microbiology and chemistry of unit processes and have sometimes neglected the interactions between fluids, particles, and reactor geometry. We hypothesize that it will be possible to significantly improve on the conventional UASB design by inventing a anaerobic digester that accounts for the interactions between fluids, particles, and reactor geometry. Similarly, we hypothesize that it will be possible to dramatically improve the design of ultra low energy atmospheric oxygen transfer into aerobic reactors.

Wastewater treatment generally requires more land, capital, and energy than drinking water treatment and thus is out of reach for most towns and villages. The result is that the majority of human waste reaches the environment with little or no treatment. Drinking water treatment is currently beyond the reach of many towns and villages and wastewater treatment isn't even on the horizon. Thus we need innovations that are better by a factor of 10 or more. The treatment technologies must have retention times measured in minutes rather than hours or days and must also reduce moving parts and reduce energy consumption. Thus the critical questions are:

1. Why are wastewater treatment processes so slow?
2. What is the nature of the rate limiting step?
3. How could the rate be dramatically increased?

.. _heading_Anaerobic_Pulsed_Bed:

Anaerobic Pulsed Bed
--------------------

Anaerobic digestion has the advantage of not requiring aeration and the disadvantage of requiring long residence times. Presumably it is the bacteria that require a long residence time and not the water and thus these residence times must be decoupled by using sedimentation or a fixed film process.

Upflow Anaerobic Sludge Blanket digestors that don't use a recycle line have an upflow velocity that is far lower than is required to fluidize the bed of granules that form. Flow through the resulting settled bed of sludge must be highly nonuniform and the result is that much of the settled bed is likely contributing little to the treatment process.

Flow uniformity and contact with all of the solids could be achieved with a fluidized bed. The velocity required for a fluidized bed would require a very tall reactor given the assumed requirements for residence time. Presumably the residence time requirement is based on the poor flow distribution in the settled sludge. Nonetheless, for reasonable depth reactors it will be difficult to operate a once through fluidized bed.

The hydraulic solution to this problem is to use pulsed flow with a pulse having a volume equal to perhaps 1-5 cm of depth in the reactor. The pulse will completely lift the settled bed of sludge and the sludge will then fall through the water column. This lift and drop cycle is expected to have much more uniform flow of water through the sludge bed then would be achieved by a stagnant bed that would rapidly develop preferential flow paths.

Upflow anaerobic settled bed (UASB) are conventionally known as upflow anaerobic sludge blanket reactors. The word "blanket" is frequently used in the field of water and wastewater treatment to refer to a fluidized bed of suspended particles (see floc filter). Unfortunately that definition is not clearly communicated by the term "blanket" and this has led to confusion of the fundamental mechanisms at play in UASB reactors.

Fluidized bed reactors required inlet and bottom geometry configurations that prevent settled particles from accumulating anywhere on the bottom of the reactor. Many UASB reactors have flat bottoms and the inlets are not designed to ensure continuous resuspension of settled particles. Thus conventional UASB reactors are often not fluidized beds and thus don't have the mass transfer efficiencies that they could have.

UASB reactors typically require hydraulic residence times hours and have a height of 4 or more meters. The result is a maximum upflow velocity that is orders of magnitude lower than the terminal velocity of the granules and thus it is clear that UASB reactors are primarily settled beds of stagnant sludge that is doing little to aid in the treatment of the wastewater.

The flow distribution through settled sludge is very unlikely to be uniform. The flow is likely to erode a mostly vertical path the shortest distance between the inlet and the top of the settled sludge. There doesn't appear to be any mechanism that would lead to the idealized uniform flow distribution. Thus conventional UASB reactors are evidently plagued by short circuiting with actual hydraulic residence times a fraction of the design value. (Cite literature in support of this hypothesis.) This leads to short-circuiting and formation of preference flow patterns in sludge bed which in turn leads to dead zones in the sludge as well as improper treatment (`Pena, 2006 <https://doi.org/10.1016/j.watres.2005.11.021>`_)

The upflow velocity required to maintain a fully fluidized bed of the anaerobic granules is approximately (cite AguaClara UASB research by Cho, et al. who measured the terminal velocity of anaerobic granules) x mm/s. At this velocity the height of the reactor would need to be x m in order to achieve the target hydraulic residence time of y hrs. This is not a practical design for community scale reactors and thus it would be advantageous to invent an alternate system for providing more uniform flow through the solids that contain the microorganisms in a UASB reactor.

Our proposed solution to this mismatch between required upflow velocity for a fluidized bed and target hydraulic residence time is to use a pulsed flow inlet. The pulsed flow will be designed to lift the entire settled bed off of the floor of the UASB reactor so that the influent wastewater is uniformly distributed to the bottom of the reactor. We hypothesize that the settled bed will then break apart and settled into the band of fresh wastewater that is on the bottom of the reactor. With this proposed mechanism it is clear that a critical parameter is the depth of wastewater that should be injected with each pulse. It is likely that this depth of fresh wastewater should be

 * A small fraction of the depth of the UASB (perhaps less than 10% to ensure that no fresh wastewater can jet through the entire UASB in the time that the sludge settled again)
 * Large enough to provide a flow passage underneath the lifted bed without requiring flow velocities that are so high that the bed is scoured near the inlet jet. This translates to larger than a minimum ratio of fresh wastewater depth per pulse/inlet spacing.

Research is needed to characterize settled bed behavior under pulsed flow.

 * How does a settled bed form as suspended solids gradually settle for the cases of continuous and pulsed flows?
 * What is the actual hydraulic residence time distribution in the bed for the case of continuous and pulsed flows?
 * What are the failure modes for the pulsed system?
 * What is the optimal pulsed height (volume of pulse/area of reactor)?
 * How does the optimal pulsed height scale inlet spacing and bed depth? It will be difficult to conduct experiments at full scale and thus these experiments will require careful consideration of scaling effects. Full scale validation will be very helpful if we can develop a method.

All of this research will be aided by using transparent reactor walls to facilitate direct observation of the settled solids. Research on this topic is currently underway by Ruth Richardson and the AguaClara Cornell team with an EPA P3 grant.

The UASB subteam is testing a gravity-powered reactor for wastewater treatment at the Ithaca Area Wastewater Treatment Facility (IAWWTF). The big goal of this research is to develop a wastewater treatment system that uses the same principles as the AguaClara water treatment plant. These goals include

 * Minimize the volume of treatment processes because process volume directly influences cost. Traditional wastewater treatment systems have hydraulic residence times that are approximately 6 hours. This is 10 times longer than the AguaClara water treatment plant residence time and that means that wastewater treatment plants cost about 10x more than water treatment. Given that most communities still can’t afford water treatment plants this means that it is imperative to develop new wastewater treatment technologies that operate roughly 10x faster.
 * Eliminate or reduce moving parts including pumps and valves

One tipping bucket UASB has been operating and successfully treating wastewater for many months.

Tasks and Goals
^^^^^^^^^^^^^^^

 * Finish fabricating the 2nd UASB. Transfer half of the granules from the 1st UASB to the 2nd UASB and begin operation.
 * Develop a method to continuously measure methane production as a way to monitor performance. One option is to measure the methane pressure at the top of the UASB by connecting a pressure sensor to the line coming from the methane port. An increase in pressure means that the methane is filling up a larger height in the top of the UASB and thus needs to be vented. A Golander peristaltic pump could be controlled by ProCoDA to run whenever the pressure is above a target value. The ProCoDA code required for this is the on-off controller.
 * Determine if the tipping bucket makes a difference by comparing gas production rates of the two UASB reactors.
 * Test both UASB reactors for ability to treat higher flow rates. Given that the incoming wastewater is relatively dilute it should be possible to operate at a much higher flow rate before the anaerobes are unable to keep up and organic acids begin to accumulate. We hypothesize that the tipping bucket design will be able to handle much higher flow rates because it fluidizes the bed of granules and thus achieves much more uniform flow distribution. This is expected to ensure that all of the anaerobes have access to incoming BOD. Remember that the goal is to get the hydraulic residence time as low as possible and ideally much less than 1 hr.
 * Improve the tipping bucket design so that the rectangular tank walls can’t bow and allow the tipping bucket to fall. This failure mode happened once and could easily be prevented by reinforcing the tank walls at the elevation of the tipping bucket axis.
 * If the tipping bucket is better than the conventional UASB, then install the tipping bucket on the 2nd UASB.
 * Experiment with tipping volume to obtain optimal design. Try a wide range from 1 cm of bed lift to perhaps 10 cm of bed lift.
 * Identify any other design flaws or opportunities to improve the design with a focus on operation and maintenance.
 * Work with AguaClara Reach and APP to begin piloting this system in Honduras.


.. _heading_String_Digester:

Aerobic String Digester (ASD)
-----------------------------

Aerobic digestion requires transfer of oxygen to the bacteria that then oxidize the waste. The broad goal is to reduce the hydraulic residence time by having efficient transfer of nutrients from the flowing water to the microorganisms. If we rely on diffusion for the mass transport of oxygen, then the thickness of the water must be order 1 mm. The string digestor represents the obvious evolution from trickling filters to the appropriate length scale that will in turn allow the minimum reactor volume.

The strings will hang vertically and be spaced a few mm apart. The spacing is expected to be close to the typical water droplet diameter to ensure that once the water droplets attach to a string, that they follow the string the whole way to the bottom of the reactor.
Trickling filters are an old wastewater treatment technology that is much more energy efficient than the activated sludge process.

The measured hydraulic residence time for trickling filters is very short. This suggests that with proper design the ASD could be very compact. `Hinton and Stense (1991) <https://www-sciencedirect-com.proxy.library.cornell.edu/science/article/pii/0043135491901179>`_ measured the residence time per unit length to be 30 seconds/meter. Thus for a 4 meter deep trickling filter the residence time would be 120 seconds. If this is accurate, then we may be able to achieve a compact design if we can pack stainless steel cables close together (order 4 mm spacing) AND achieve uniform flow distribution. In addition, `Hinton and Stense (1991) <https://www-sciencedirect-com.proxy.library.cornell.edu/science/article/pii/0043135491901179>`_ used a hydraulic application rate of 4 m/hr (1.1 mm/s). This velocity confirms that a compact, well-designed ASD may be smaller than AguaClara clarifiers that traditionally have operated at 1 mm/s.

Modular plastic trickling filter media are typically manufactured with the `following specific surface areas <https://pubmed.ncbi.nlm.nih.gov/21657190/>`_:

- 223 :math:`m^2/m^3` as high density
- 138 :math:`m^2/m^3` as medium density
- 100 :math:`m^2/m^3` as low density

Vertical-flow media require an average hydraulic approach velocities greater than 1.8 m/h (0.5 mm/s) to maximize BOD5 removal efficiency. Shallow towers using cross-flow media have used hydraulic approach velocities in the range 0.4 to 1.1 m/h (0.1 to 0.3 mm/s) (`Daigger and Boltz, 2011 <https://pubmed.ncbi.nlm.nih.gov/21657190/>`_)

`Crine et al. (1990) <https://doi.org/10.2166/wst.1990.0149>`_ found that the wetted area-to-specific-surface-area ratio ranged from 0.2 to 0.6 with the lowest values for high-density random pack trickling filter media. This confirms that conventional trickling filters are unable to efficiently wet all biofilm surfaces and thus the trickling filters must be substantially over-designed (by a factor of 2 to 5) to accommodate this poor wetting efficiency.

If we take the hydraulic approach velocity of 0.5 mm/s and divide by the wetted area-to-specific-surface-area ratio of 0.6 we obtain 0.83 mm/s, a velocity that is comparable to the upflow velocity in an AguaClara clarifier. Thus a well designed String Digester could be quite compact.

There is extensive literature on design of trickling filters for removal of various nutrients and integration into multi-process treatment trains. Control of biofilm thickness seems to be a recurring issue and thus may be an important research area for the Aerobic String Digester.

Research Enabling Tools
=======================

ProCoDA Python Transition
-------------------------

Convert existing ProCoDA software to run in Python

Introduction
^^^^^^^^^^^^

The ProCoDA software has been serving research teams for many years. Although the software used to run our long term bench top experiments has experienced many updates and improvements it’s major flaw is that maintenance and upgrades require coding in LabVIEW.

In order to improve access to this vital piece of AguaClara Research technology this team aims to transition the entirety of the code and all of its functionality to Python so that the open source community can provide upgrades and maintenance.

ProCoDA is a very large application built from many modules that can be developed in parallel by different teams. This project has the advantage of having a working example of the code that can be explored to learn how ProCoDA is structured and how to create the many modules needed for the ProCoDA package.

Resources
 * `ProCoDA Chapter <https://monroews.github.io/EnvEngLabTextbook/ProCoDA/ProCoDA.html#>`_ in the Environmental Laboratory Textbook
 * `ProCoDA Githb Repository <https://github.com/monroews/LabVIEW/wiki/ProCoDA>`_
