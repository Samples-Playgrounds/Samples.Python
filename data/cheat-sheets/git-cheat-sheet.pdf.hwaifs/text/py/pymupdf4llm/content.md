# **Git Cheat Sheet**

## **01 Git configuration**



1










## **04 Storing your work**




## **02 Starting a project**






## **05 Git branching model**




## **03 Day-to-day work**









**Commit** a state of the code base

**Branch** a reference to a commit; can have a **tracked upstream**

**Tag** a reference (standard) or an object (annotated)

**HEAD** a place where your **working directory** is now


2


## **06 Inspect history**


## **09 Synchronizing repositories**








## **07 Tagging commits**








## **08 Reverting changes**


## **10 Git installation**

For GNU/Linux distributions, Git should be available in the standard system repository. For
example, in Debian/Ubuntu please type inthe terminal:


sudo apt-get install git


If you need to install Git from source, you can get it from **[git-scm.com/downloads](https://git-scm.com/downloads)** .

An excellent Git course can be found in the great Pro Git book by Scott Chacon and Ben Straub.
The book is available online for free at **[git-scm.com/book.](https://git-scm.com/book/en/v2)**

## **11 Ignoring files**

```
cat  <<EOF > .gitignore

/logs/*

!logs/.gitkeep

/tmp

*.swp

EOF

```

To ignore files, create a .gitignore file in your repository with a line for each pattern. File ignoring will
work for the current and sub directories where .gitignore file is placed. In this example, all files are
ignored in the logs directory (excluding the .gitkeep file), whole tmp directory and all files *.swp.








