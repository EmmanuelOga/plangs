-- paradigms
insert into paradigms (key, description)
values
('para-oop', 'Object-Oriented'),
('para-imp', 'Imperative'),
('para-func', 'Functional'),
('para-struct', 'Structured'),
('para-refl', 'Reflective');

-- type_systems
insert into type_systems (key)
values
('types-duck'),
('types-dynamic'),
('types-strong'),
('types-optional');

-- environments
insert into environments (key)
values
('env-linux'),
('env-windows'),
('env-macos'),
('env-ios'),
('env-android'),
('env-wasm'),
('env-rpi');
