CREATE TABLE paradigms (
    key STRING PRIMARY KEY CHECK (starts_with(key, 'para-')),
    description STRING NOT NULL,
);

CREATE TABLE people (
    key STRING PRIMARY KEY CHECK (starts_with(key, 'people-')),
    full_name STRING NOT NULL,
);

CREATE TABLE organizations (
    key STRING PRIMARY KEY CHECK (starts_with(key, 'org-')),
);

CREATE TABLE typings (
    key STRING PRIMARY KEY CHECK (starts_with(key, 'types-')),
);

CREATE TABLE environments (
    key STRING PRIMARY KEY CHECK (starts_with(key, 'env-')),
);

CREATE TABLE licenses (
    key STRING PRIMARY KEY CHECK (starts_with(key, 'lic-')),
);

CREATE TABLE extensions (
    key STRING PRIMARY KEY CHECK (starts_with(key, 'ext-')),
);

CREATE TABLE implementations (
    key STRING PRIMARY KEY CHECK (starts_with(key, 'impl-')),
);

CREATE TABLE languages (  -- noqa: PRS
    key STRING PRIMARY KEY CHECK (starts_with(key, 'pl-')),
);
COMMENT ON TABLE languages IS 'Programming languages';

CREATE TABLE language_paradigms (
    language STRING NOT NULL,
    paradigm STRING NOT NULL,
    PRIMARY KEY (language, paradigm),
    FOREIGN KEY (language) REFERENCES languages(key),
    FOREIGN KEY (paradigm) REFERENCES paradigms(key),
);

CREATE TABLE language_people (
    language STRING NOT NULL,
    person STRING NOT NULL,
    PRIMARY KEY (language, person),
    FOREIGN KEY (language) REFERENCES languages(key),
    FOREIGN KEY (person) REFERENCES people(key),
);

CREATE TABLE language_environments (
    language STRING NOT NULL,
    environment STRING NOT NULL,
    PRIMARY KEY (language, environment),
    FOREIGN KEY (language) REFERENCES languages(key),
    FOREIGN KEY (environment) REFERENCES environments(key),
);