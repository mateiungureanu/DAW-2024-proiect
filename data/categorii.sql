--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie1_categorii; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie1_categorii (id, nume) VALUES (1, 'Electronice');
INSERT INTO django.aplicatie1_categorii (id, nume) VALUES (2, 'Haine');


--
-- Name: aplicatie1_categorii_id_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie1_categorii_id_seq', 2, true);


--
-- PostgreSQL database dump complete
--

