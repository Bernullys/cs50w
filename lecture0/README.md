Lecture 0. HTML and CSS

Some notes:

- elements in HTML have attributes, and attributes have properties:
    <h1 style="color: blue; text-align: center;">Title</h1>
    style is an attribute. Color and text-align are properties.

- Specificity in css:
    - inline.
    - id.
    - class.
    - type.

- Ways to specify which element would like to style:
    - a, b  Multiple element selector.
    - a b   Descendant Selector.
    - a > b Child selector.
    - a + b Adjacent sibling selector.
    - [a=b] Attribute selector. (Watch lecture file).
    - a:b   Pseudoclass selector.
    - a::b  Pseudoelement selector.

- Responsives design:
    - Viewport.
    - Media queries.
    - Flexbox.
    - Grid.
    - Library Bootstrap.
        - Go to Bootstrap an use the link of the style. Then use the classes that link bring into my elements.
    - Sass. file_name.scss. Is a different language, is an extantion of css, it has to be compiled like this: sass file_name.scss:file_name.css every time is modify. Or run this command: --watch file_name.scss:file_name.css. Sass can perform inheritance. (Watch lecture file).