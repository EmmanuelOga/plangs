-- insert-lang
insert into languages (key, version, name, description)
values
($key, $version, $name, $desc); -- noqa: PRS

-- insert-people
insert into people (key, full_name)
values
($key, $full_name);
