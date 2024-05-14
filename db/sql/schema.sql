CREATE TABLE paradigms ( -- noqa: PRS
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

CREATE TABLE type_systems (
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

CREATE TABLE languages (
    key STRING NOT NULL CHECK (starts_with(key, 'lang-')),
    version STRING NOT NULL,
    name STRING NOT NULL,
    description STRING NOT NULL,
    PRIMARY KEY (key, version),
);
COMMENT ON TABLE languages IS 'Programming languages';

--------------------------------------------------------------------------------
-- Join tables
--------------------------------------------------------------------------------

CREATE TABLE language_paradigms (
    language STRING NOT NULL,
    version STRING NOT NULL,
    paradigm STRING NOT NULL,
    PRIMARY KEY (language, version, paradigm),
    FOREIGN KEY (language, version) REFERENCES languages(key, version),
    FOREIGN KEY (paradigm) REFERENCES paradigms(key),
);

CREATE TABLE language_people (
    language STRING NOT NULL,
    version STRING NOT NULL,
    person STRING NOT NULL,
    PRIMARY KEY (language, version, person),
    FOREIGN KEY (language, version) REFERENCES languages(key, version),
    FOREIGN KEY (person) REFERENCES people(key),
);

CREATE TABLE language_environments (
    language STRING NOT NULL,
    version STRING NOT NULL,
    environment STRING NOT NULL,
    PRIMARY KEY (language, version, environment),
    FOREIGN KEY (language, version) REFERENCES languages(key, version),
    FOREIGN KEY (environment) REFERENCES environments(key),
);