# Thesis plan

- idea ACM luokittelusta: CCS -> Software and its engineering -> Software notations and tools -> General programming languages -> Language features -> ??
- my personal learning goals:
    - How rigid is the type system of Python, what guarantees does it provide?
    - Describing Pythons type system and type hint system on a technical level
    - How popular are typing solutions for Python
        - The evolution of type annotations in python: an empirical study
            - Our results show that (i) type annotations are getting more popular, and once added, often remain unchanged in the projects for a long time, (ii) projects follow three evolution patterns for type annotation usage -- regular annotation, type sprints, and occasional uses -- and that the used pattern correlates with the number of contributors, (iii) more type annotations help find more type errors (0.704 correlation), but nevertheless, many commits (78.3%) are committed despite having such errors. Our findings show that better developer training and automated techniques for adding type annotations are needed, as most code still remains unannotated, and they call for a better integration of gradual type checking into the development process.

    - Mitä empiriistä hyötyä näistä tyypitysratkaisuista on, mitä subjektiivisia hyötyjä koodarit claimaa / millä talking pointeilla näitä pitchataan
        - empiirisistä hyödyistä:
            - Python type hint in Competitive Programming
                - Sample size 5, aika epäselvää onko hyötyä, tosi isoa vaihtelua experimenttien / testihenkilöiden välillä

Title ideas:
    - Python type hints as programming ergonomic and correctness aid
    - Type checking Python - How, why and where?:

## The structure of the thesis paper:
- Introduction
    - Python is a popular general purpose programming language, originally designed for <> and nowadays used for <>
    - Statically type hinting Python programs is becoming more common
        - Why?
    - The inherent contradiction in using a dynamically typed language but adding more tooling for static checking
- Chapter: introducing the objects for analysis:
    - Python
    - Static vs dynamic typing, strong vs weak typing
    - Python type system and checkers
        - type system
            - how it works
        - Difference between the "actual" runtime types (that every Python program uses) and type hints
        - Checkers: mypy, pyright, others?
- Another chapter?
- Chapter: analyzing the solutions:
    -  Why is statical typing for Python programs rising in popularity?
        - What are the perceived reasons programmers implement typing into Python projects
    - Empirical benefits from statically typing Python programs
- Conclusions:
    - Implications
        - where does dynamic typing still seem popular and/or appropriate
        - (?) growing proportion of building large applications with python
    - Shortfalls of Python type system
    - Are there specific kinds of projects that empirically benefit most from using types

- ideas for parts not yet placed:
    - quality of library types
    - comprehensiveness of standard library types
    - Part 4 discussion; going further beyond:
        - "Going further: runtime typing"
            - Python: Pydantic,
    - shortfalls of static analysis with Python
        - Implications on the future of Python
- Tekoälyn käyttö tutkielmassa:
