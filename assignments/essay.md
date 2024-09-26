## Effect of Python type hints on code quality

### Introduction
Types have been recognised to play a significant part in programming ergonomics and static analysis of source code, which motivates this research. An overview of how types work in Python, where they are used, and why will be provided as contextualization. This essay explores the benefits from Python type hints in preventing programming errors and increasing code quality.

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

Since 2014 popularity of type hints has been steadily growing. In libraries the type hints also serve the function of documenting function inputs and outputs, and in stable public APIs they are cheap to maintain since the public facing interfaces rarely change.

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

