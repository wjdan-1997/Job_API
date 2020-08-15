--
-- PostgreSQL database dump
--

-- Dumped from database version 12.3
-- Dumped by pg_dump version 12.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Job; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Job" (
    id integer NOT NULL,
    job_title character varying NOT NULL
);


ALTER TABLE public."Job" OWNER TO postgres;

--
-- Name: Job_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Job_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Job_id_seq" OWNER TO postgres;

--
-- Name: Job_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Job_id_seq" OWNED BY public."Job".id;


--
-- Name: Person; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Person" (
    id integer NOT NULL,
    name character varying NOT NULL,
    phone integer NOT NULL,
    email character varying(120) NOT NULL,
    job_id integer NOT NULL
);


ALTER TABLE public."Person" OWNER TO postgres;

--
-- Name: Person_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Person_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Person_id_seq" OWNER TO postgres;

--
-- Name: Person_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Person_id_seq" OWNED BY public."Person".id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: Job id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Job" ALTER COLUMN id SET DEFAULT nextval('public."Job_id_seq"'::regclass);


--
-- Name: Person id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Person" ALTER COLUMN id SET DEFAULT nextval('public."Person_id_seq"'::regclass);


--
-- Data for Name: Job; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Job" (id, job_title) FROM stdin;
1	Manager
2	Supervisor
3	software_engineer
4	Programmer
\.


--
-- Data for Name: Person; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Person" (id, name, phone, email, job_id) FROM stdin;
2	Wejdan	503337232	Wejdan@outlook.sa	1
3	Ahmed	503337232	Ahmed@outlook.com	2
4	Mohammed	503337232	Mohammed@outlook.com	3
5	Afnan	503337232	Afnan@outlook.com	4
6	Fatmah	503337232	Fatmah@outlook.com	4
7	Joly	503337232	Joly@outlook.com	3
8	Nada	503337232	Nada@outlook.com	3
9	Sam	503337232	Sam@outlook.com	3
10	Aymn	503337232	Aymn@outlook.com	1
11	Mone	503337232	Mone@outlook.com	2
12	Jna	503337232	Jna@outlook.com	4
13	Dema	503337232	Dema@outlook.com	4
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
\.


--
-- Name: Job_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Job_id_seq"', 4, true);


--
-- Name: Person_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Person_id_seq"', 13, true);


--
-- Name: Job Job_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Job"
    ADD CONSTRAINT "Job_pkey" PRIMARY KEY (id);


--
-- Name: Person Person_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Person"
    ADD CONSTRAINT "Person_pkey" PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: Person Person_job_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Person"
    ADD CONSTRAINT "Person_job_id_fkey" FOREIGN KEY (job_id) REFERENCES public."Job"(id);


--
-- PostgreSQL database dump complete
--

