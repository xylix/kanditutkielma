# Bachelor thesis plan

## Basic information

This is my plan for writing my Computer Science bachelors thesis at University of Helsinki

- Name: Kerkko Pelttari
- Student number: <TODO: insert when turning in>
- Instructor: Yang Liu
- Supervisor: Dorota Glowacka
- Starting date: 05.09.2024
- Thesis language: English
- Schooling language: Finnish

## Related assignments:

- Essay: planned and actual: 16.09.
- 10 page thesis draft: planned: 25.10, actual: TBD
- Final thesis: planned: 30.11., actual: TBD
- Maturity test: Planned: During november, actual: TBD
- Presentation: Planned: When thesis group decides to, actual: TBD
- Extended abstract in Finnish: Planned: by 30.11.
- Verbal peer review: TBD
- Written peer review: TBD
- Work plan: v1 27.09.


## Work schedule
Due to having more coursework coming in study period 2, I'm trying to frontload the thesis effort.

- Course milestones (picked from the initial lectures):
    - 1 [x] picking a topic
    - 2 [x] work plan (27.09.2024, this document!)
    - 3 [ ] 11.10. Growing understanding. 10 page draft, have skimmed / initially picked most of needed literature.
    - 4 [ ] 25.10. Expertise and understanding the topic.
        - Have decent notes on most of the literature to be referenced
        - Figuring out relations between the different sources, and things under research.
    - 5 [ ] 15.11. Growing the draft into a thesis
    - 6 [ ] 29.11. Finalizing

## Idea for the structure of the thesis paper:
- Introduction ~1-2 pages
    - Python is a popular general purpose programming language, originally designed for <> and nowadays used for <>
    - Statically type hinting Python programs is becoming more common
        - Why?
    - The inherent contradiction in using a dynamically typed language but adding more tooling for static checking
- "Introducing the objects for analysis" Background: 2-3 pages
    - Python
    - Static vs dynamic typing, strong vs weak typing
    - Python type system and checkers
        - type system
            - how it works
        - Difference between the "actual" runtime types (that every Python program uses) and type hints
        - Checkers: mypy, pyright, others?
/* - TODO: Another chapter? */
- "Chapter analyzing the solutions" Types as a tool: 3-5 pages
    -  Why is statical typing for Python programs rising in popularity?
        - What are the perceived reasons programmers implement typing into Python projects
    - Empirical benefits from statically typing Python programs
    - Using type annotations for runtime behaviour
        - FastAPI, Pydantic
- Related work 1 page
- Conclusions: 1-2 page
    - Implications
        - where does dynamic typing still seem popular and/or appropriate
        - (?) growing proportion of building large applications with python
    - Shortfalls of Python type system
    - Are there specific kinds of projects that empirically benefit most from using types
- (Mandatory) Use of AI in the thesis
- References

##  ideas for parts not yet placed:
- quality of library types
- comprehensiveness of standard library types
- Part 4 discussion; going further beyond:
    - "Going further: runtime typing"
        - Python: Pydantic,
- shortfalls of static analysis with Python
    - Implications on the future of Python
- AI based type inference solutions for Python

