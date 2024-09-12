# Contradictory superimposing of typing on dynamically typed programming languages


## sijoitettavia kappaleita / lauseita
## essay:

Exploration on the growing trend of statically typing Python and Javascript programs, its effects on code quality, mainteinance and developer satisfaction, and the technical differences between typing solutions for these languages.


Javascript is a dynamically typed programming language that has achieved widespread adoption due to being the default language for writing frontend code for the web. The most common runtimes for Javascript are google's v8, included in all Chromium based browsers, Mozilla foundation's SpiderMonkey used in Firefox, and OpenJS foundations node.js. Originally Javascript was interpreted, but nowadays almost all runtimes use just-in-time compilation. Even though it is popular, developer satisfaction has sometimes been a pain point for Javascript, and part of this blame has been assigned to its heavily dynamic and weakly typed nature. Javascript was originally inspired in part by the LISP tradition of programming languages even though its visible syntax somewhat resembles Java (the Java-like syntax and name was a marketing move to try and appeal to the growing popularity of Java in 1995), and it is possible to modify behaviour and prototypes at runtime. The popularity of the more dynamic style of programming with Javascript has been decreasing for a long time, and the popularity of gradual compile time type checking is one fact demonstrating this.

Python is a dynamically typed interpreted scripting language, that is used for building command-line tooling, applications, scientific computing and machine learning. It is a common first programming language due to its relatively simple syntax and accessible standard library. Many of Pythons design principles support developers getting up to speed quickly. It can be used as a glue-code language for integrating various tools, and it has significantly gained market share from PERL as a demonstration of this fact. It is somewhat infamous for its relative slowness compared to compiled languages, but it has for most of its lifecycle been at the slower end even compared to other popular interpreted languages.

According to Javascript and Python are in the top 5 used languages (1. P. Carbonnelle, PYPL PopularitY of Programming Language, 2017.). Over 99% of websites use Javascript for client side functionality. <source: https://w3techs.com/technologies/details/cp-javascript> <what about python>

Even though the adoption is widespread, it is commonly argued that these languages are lacking in programming ergonomics and support for ensuring correctness, in part due to their dynamically typed nature. <source> One consequence has been that from 2010 onward, significant development has happened in adding compile-time static typing for both Javascript and Python. We will investigate some of the most adopted of these tools, namely Typescript and PEP-484 and related tooling. Besides the popularity and some similar deficiencies, this essay focuses on typed Python and Javascript specifically because the common ways of adding optional typing have a lot of similarities (weakly enforced runtime typing, optionality, ) and state of the art tooling has begun development in the same time period (2012 for Typescript, 2014 for Python type hints). The timing for these tools growing popularity also coincides with tools like Language Servers that utilize syntactical information for helping in developer experience. Historically statical languages have had more comprehensive tooling features available, due to the fact that tooling makes use of information such as types for improved auto-complete intelligence and refactoring features.

There is a contradiction in the popularity of dynamically typed languages growing along with the proportion of adopting optional tooling to provide static types for these. There are various hypotheses for why this is. Some argue that these languages are being adopted for larger projects than they were originally used for, and larger programming projects require improved tooling <source>. The optionality of static analysis also provides a way to build quick prototypes where speed is prioritized over correctness, and later improve the applications maintainability by <taking into use more tooling>.

<how typescript works>
Vanilla Javascript is weakly and dynamically typed. Various in-built operators and functions do implicit casting of parameters, enabling user confusion when some operations may work unintuitively or in contradictory ways on a surface level. As an example, the operation `10 + "1"` returns the string "101", whereas the operation 10 - "1" returns 9. Even though there are situations where this implicit dynamic behaviour can be handy, it often leads to bugs or code smells and often various checkers are used to reduce problems. One such tool is a compile time type checker.

Typescript was chosen as the typing system of choice for Javascript due to its significantly higher popularity compared to other Javascript typing systems. According to Stack Overflow developer survey data, in 2019 68% of polled developers used and wanted to continue using Javascript, and 21% said the same about Typescript. In 2024 Javascript's popularity had fallen to 62% (perhaps to other front-end development technologies such as WASM as a compilation target gaining popularity), and Typescript had a popularity of 39%. So among surveyed developers the proportion of developers using Typescript compared to Javascript was 31% in 2019, and 63% in 2024. Other typing systems do not reach a high enough popularity to get mentioned.

Typescript is a transpiling Javascript compiler. The type information is used for type checking and compilation, and then erased, adding no runtime overhead but also making it impossible to access the additional type information at runtime.


<how python type annotations and mypy pyright works>
Python 3 features strong, dynamic duck typing by default. Variables do not have to be annotated, but the standard library features TypeErrors that are raised when an operation received values of a wrong type. (Such as when something expecting a list is given a string.)

Python has native type annotations since 2014 when PEP-484 was specified and implemented into Python 3.5. The standard library is effectively fully annotated, the annotations doing double work as documentation for input/output types and metadata for type checkers to make use of. The type annotations don't by themselves affect runtime behaviour, but the type metadata can be accessed at runtime, and libraries eixst to use this to add additional runtime type validations.

The reference implementation for validating the type hints and using correct types is Mypy by the Python foundation. There are alternative checkers, and Microsofts Pyright is popular due to it being the default that the popular editor Visual Studio Code recommends users to install when working with Python code.


sources:
    Introduction to Typescript https://link.springer.com/chapter/10.1007/978-1-4842-5352-6_10
    Pep 484 and the Python docs
    https://survey.stackoverflow.co/2019
    https://survey.stackoverflow.co/2024

# Python tyyppi essee
Type checking Python - An overview


## plan
suunnitelma:
- ^mitä näistä ollaan tulkitsemassa
- mitä tieteelliset paperit sanoo tai oletan että sanoo
- johtopäätöksiä / kasaan tuomista
- kappale kaikista näistä:
    - johdanto (mitä esseessä käsitellään, miksi), tutkimuskysymykset
    - mitä on python
        - python, sen tyyppisysteemi, type hintit, tyyppitarkistimet, näiden kehitysaikajana
    - miksi on valittu tutkielman tarkastelukohteeksi
    - vähän yleistä löpinää staattisen tyypityksen yleistymisestä dynaamisten kielten kanssa
    - havaittu ristiriita siinä että päällelätkitään staattisuutta dynaamisiin kieliin
        ^hypoteesejä tästä ilmiöstä
    - mitä tutkielmassa koitetaan selvittää


## sijoittamattomia kappaleita:
<TODO>: n. 100 sanaa jokaisesta, maininta onko tieteellistä tutkimusta, miksi keskitytään tiettyyn tai miksi näillä ei ole hirveästi väliä tutkimuksen kannalta.
<todo> from bullet list to actual pragraphs
- Pyright is developed by Microsoft, and integrated into Visual Studio Code through the Pylance extension.
- Pytype is developed by Google and <>
- PyCharm from Jetbrains, the number 1 Python specific IDE, has its own type checker. <>

TODO: termien type annotation ja type hint välille consistencyä

## Effect of Python type hints on finding problems

### Introduction
Types have been recognised to play a significant part in programming ergonomics and static analysis of source code, which motivates this research. An overview of how types work in Python, where they are used, and why will be provided as contextualization. The main research question is how much benefit does increased use of Python type hints provide. An Empirical Study of Type-Related Defects in Python Projects (2022) [1] found that in a 210 project open-source dataset 15% of real defects could have been avoided with type hints and type checking. Python 3 Types in the Wild: A Tale of Two Type Systems [4] found that from repositories that use Python type hints in the wild, only 15% type check succesfully.

### What Python is:
Python is a top-5 usage programming language. It is a high-level interpreted language whose syntax uses significant whitespace for conciseness. Significant usage domains include scientific computing, machine learning, web backend development and scripting. The conscise syntax and capability to make programs executable quickly have been significant advantages in growing market share from stricter, compiled languages such as Java, C# and C++.

Python's runtime type system is dynamical and strong. This has played into the aforementioned advantage, but it has also been seen as a pain point as scale of software built with Python grows. Various tools have grown to improve quality and scaling of Python projects. This includes linters, runtime validators, and frameworks.

Even though the runtime type system of Python is strong, the dynamic typing lessens the possible strictness at programming time. Historically the best way to test for this was to either run the program or write tests. This can be cumbersome for programmers, compared to checking for type errors by automatically running a type check.

In 2014 Python developers drafted Python Enhancement Proposal 484 - Type hints [5]. Ability to do improved static analysis, and possibility for improved refactoring, runtime type checks, and code generation were the motivation, with static analysis documented as the most important one. A prototypal type checker and the ability to add type metadata through a generic mechanism already existed, but this proposal standardized the way to annotate Python code with type data, enabling improved tooling development across the field.

### Python type checking:
As of 2024 there are four relevant options for Python type checking. Mypy by Python foundation is a common tool to run in Continuous Integration environments to do type checking across tests. It has a command line interface and plugins for various text editors.

It is common for developers to develop code with VS Code or PyCharm and then run `mypy` in a continuous integration environment, providing a sort of double checking with slightly different prioritizations affecting what sort of issues each checker complains about. It is plausible that in many projects the configuration between the two does not match 1:1, leading to situations where a programmer could commit locally type checking code that fails in CI, or another programmer could pull passing code from CI that does not pass locally. This phenomena is not common in other programming languages, where often a single type checker or the programming languages own compiler has a monopoly.

In 2020 Rak-amnouykit et al. researched specifics about the Python type hints [4]. They tried to answer "(i) How often and in what ways do developers use Python 3 types? (ii) Which type errors do developers make? (iii) How do type errors from different tools compare?". One result was that even though type hints and checking is more popular, only 15% of the 2678 codebases analyzed succesfully type checked with Mypy. They also found out that errors from Mypy and Pytype find both false positives and runtime defect related type errors.

### Adaption of type hints

Since the PEP was finalized, popularity of type hints has been steadily growing. In libraries the type hints also serve the function of documenting function inputs and outputs, and in stable public APIs they are cheap to maintain since the public facing interfaces rarely change. <source>

In 2022 Di Grazia & Pradel investigated the adoption of type hints in The Evolution of Type Annotations in Python: An Empirical Study. They found that in a sample of code repositories from Github.com, from 2017 to 2021 the amount of type hints has increased linearly. In the sample type hinting had focused on function parameter and return types, and less on variable types. 90.1% of type annotations never get updated. [2]

### Effects of type hinting
The effect of type hinting to program correctness has been studied. In An Empirical Study of Type-Related Defects in Python Projects [1] Khan et al. found that 11% of all researched defects could be detected by adding type annotations and running a type checker.

A representative random sample of 400 defects was sampled from a list of all Python project related Github issues labelled as defects between 2015-2018 (373 742 issues in total). They used Swanson's [3] classification system to classify fixes and the related defects, and 15% of corrective fixes were detected with Mypy. This was 11% of all fixes. Corrective fixes consist of failures in processing, performance or implementation, in contrast to "adaptive" (data or processing environment related mainteinance tasks) and "perfective" (processing inefficiencies, performance enhancements and maintability improvements).

Earlier work by Gao et al. [6] found that in another dynamic language, Javascript, 11-18% percent of defects was found by adding type annotations and checking. Even though the languages differ the similarity in results works to validate that it can be possible to find over 10% of defects with type checking.

### Conclusions

A significant body of research exists into the effects of Python type hints.

It seems that type hints and checking consistently improve code quality by helping developers find problems with their code. Common problems are reusing of variables and null safety. However most type-hint using codebases contain a significant amount of type errors, possibly contributing to people interpreting various type errors as "noise".

Further research into how type hinting compares to other static analysis tools could provide useful insights. It could be useful to research how to make programming or type hinting in ways that pass type checks easier. It could also be useful to compare different Python type checkers and their performance development from 2015 to 2024.


### Sources:
1. An Empirical Study of Type-Related Defects in Python Projects https://ieeexplore.ieee.org/abstract/document/9436020
2: The Evolution of Type Annotations in Python: An Empirical Study https://www.software-lab.org/publications/fse2022_type_study.pdf
3. The Dimensions of Mainteinance E. Burton Swanson http://www.mit.jyu.fi/ope/kurssit/TIES462/Materiaalit/Swanson.pdf
4. Python 3 Types in the Wild: A Tale of Two Type Systems https://dl.acm.org/doi/10.1145/3426422.3426981
5. Python Enchancement Proposal 484 https://peps.python.org/pep-0484/#rationale-and-goals
6. To Type or Not to Type: Quantifying Detectable Bugs in JavaScript https://ieeexplore.ieee.org/abstract/document/7985711
