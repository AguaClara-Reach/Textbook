# Textbook [![Documentation](https://github.com/AguaClara-Reach/Textbook/actions/workflows/build-docs.yml/badge.svg)](https://aguaclara-reach.github.io/Textbook/)

Please enjoy [the AguaClara textbook](https://aguaclara-reach.github.io/Textbook/)!  
If you are interested in helping out by writing, begin by reading [this page](https://github.com/AguaClara-Reach/Textbook/wiki/Contributing-by-writing)!  
If you are interested in helping out by editing existing sections, begin by reading [this page](https://github.com/AguaClara-Reach/Textbook/wiki/Contributing-by-editing)!

# Textbook Structure
This is the first version attempted of an AguaClara textbook. The current proposed structure is as follows:

Each chapter will cover a unit process, like "Flow Control and Measurement" or "Clarification."

Each chapter will have the following three sections:
- Introduction
- Design
- Theory and Future Work

Each chapter may also have up to three appendices:
- Appendix A: Derivations
- Appendix B: Examples


## Introduction
The introduction contains two components:
- Introduces and explains concepts relevant to the physics and design of the unit process
- Covers briefly the design of conventional water treatment plants and how they solve the problems associated with the unit process.  

## Design
Contains the details of an AguaClara design for the unit process. Goes over logic and explains thoroughly why design decisions are made.

## Theory and Future Work
Contains working theories in the AguaClara lab and future research projects to better understand the physics of water treatment and improve plant design.

## Publishing
Every push to `master` automatically builds the textbook and publishes it with GitHub Pages. Pull requests run the same HTML build as a check before merging. A deployment can also be started manually from the **Documentation** workflow in the repository's **Actions** tab.

## Appendix A: Derivations
Many of the equations that show up in the `Introduction` and `Design` sections have lengthy derivations that have been done by AguaClara in the past. The step-by-step derivations of these equations will be found in this section. Equations that require derivations will be noted as such in the text and linked to their derivations.


## Appendix B: Examples
This section will contain example problems. A big portion of these example problems will be design challenges that were used in previous years, before this textbook was made available.
