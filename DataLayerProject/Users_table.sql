CREATE TABLE public."Users"
(
    user_id serial NOT NULL,
    username character varying NOT NULL,
    password character varying NOT NULL,
    PRIMARY KEY (user_id)
);

ALTER TABLE IF EXISTS public."Users"
    OWNER to pichi;

COMMENT ON TABLE public."Users"
    IS 'Users table for Data layer project';