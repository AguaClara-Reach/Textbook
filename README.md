# Textbook [![Documentation](https://github.com/AguaClara-Reach/Textbook/actions/workflows/build-docs.yml/badge.svg)](https://aguaclara-reach.github.io/Textbook/)

Please enjoy [the AguaClara textbook](https://aguaclara-reach.github.io/Textbook/)!  
If you are interested in helping out by writing, begin by reading [this page](https://github.com/AguaClara-Reach/Textbook/wiki/Contributing-by-writing)!  
If you are interested in helping out by editing existing sections, begin by reading [this page](https://github.com/AguaClara-Reach/Textbook/wiki/Contributing-by-editing)!

## Publishing
Every push to `master` automatically builds the textbook and publishes it with GitHub Pages. Pull requests run the same HTML build as a check before merging. A deployment can also be started manually from the **Documentation** workflow in the repository's **Actions** tab.

# Running locally
We use [act](https://github.com/nektos/act) to run the workflow locally. After installing act, run `act --container-architecture linux/amd64` in the root directory to see a list of workflows that can be run locally. 

