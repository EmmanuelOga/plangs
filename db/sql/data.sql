insert into paradigms (key, description) -- noqa: PRS
values
('para-oop', 'Object-Oriented'),
('para-imp', 'Imperative'),
('para-func', 'Functional'),
('para-struct', 'Structured'),
('para-refl', 'Reflective');

insert into typings (key)
values
('types-duck'),
('types-dynamic'),
('types-strong'),
('types-optional');

insert into environments (key)
values
('env-linux'),
('env-windows'),
('env-macos'),
('env-ios'),
('env-android'),
('env-wasm'),
('env-rpi');

--------------------------------------------------------------------------------
-- PYTHON
--------------------------------------------------------------------------------

insert into people (key, full_name)
values
('people-guido', 'Guido van Rossum');

insert into languages (key)
values
('pl-python');

insert into language_paradigms (language, paradigm)
values
('pl-python', 'para-oop'),
('pl-python', 'para-imp'),
('pl-python', 'para-func');
