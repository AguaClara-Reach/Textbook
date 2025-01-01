# Textbook [![Documentation](https://github.com/AguaClara/Textbook/workflows/Documentation/badge.svg)](https://aguaclara.github.io/Textbook/)

Please enjoy [the AguaClara textbook](https://aguaclara.github.io/Textbook/)!  
If you are interested in helping out by writing, begin by reading [this page](https://github.com/AguaClara/Textbook/wiki/Contributing-by-writing)!  
If you are interested in helping out by editing existing sections, begin by reading [this page](https://github.com/AguaClara/Textbook/wiki/Contributing-by-editing)!

## Publishing
To publish, first ensure all of your changes have been merged into master by following the Pull Request best practices [here](https://github.com/AguaClara/Textbook/wiki/Contributing-by-writing). Then follow these steps:

1. `git checkout master`
2. `git pull`
3. `git tag <tagname>`
   1. To get `<tagname>`, check the latest release and increment by 1, following semantic versioning. For Example, if the current version were `v0.0.76` and there were only small edits the next would be `v0.0.77`. If there were more significant changes it would be `v0.1.0`, and for extremely large changes (maybe a whole new chapter?), `v1.0.0`.
4. `git push origin <tagname>`

Pushing a tag will kick off the automated release workflow which builds the PDF and HTML documentation.

# Running locally
We use [act](https://github.com/nektos/act) to run the workflow locally. After installing act, run `act --container-architecture linux/amd64` in the root directory to see a list of workflows that can be run locally. 

