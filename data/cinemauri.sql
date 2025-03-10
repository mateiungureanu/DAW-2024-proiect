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
-- Data for Name: aplicatie1_cinemauri; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie1_cinemauri (id, nume_cinema, oras) VALUES (1, 'Chitcan', 'Bucuresti');
INSERT INTO django.aplicatie1_cinemauri (id, nume_cinema, oras) VALUES (2, 'Sobolan', 'Bucuresti');
INSERT INTO django.aplicatie1_cinemauri (id, nume_cinema, oras) VALUES (3, 'Soparlan', 'Bucuresti');
INSERT INTO django.aplicatie1_cinemauri (id, nume_cinema, oras) VALUES (4, 'Carcalac', 'Cluj');
INSERT INTO django.aplicatie1_cinemauri (id, nume_cinema, oras) VALUES (6, 'Harciog', 'Constanta');
INSERT INTO django.aplicatie1_cinemauri (id, nume_cinema, oras) VALUES (5, 'Popandau', 'Brasov');
INSERT INTO django.aplicatie1_cinemauri (id, nume_cinema, oras) VALUES (7, 'Mangusta', 'Timisoara');


--
-- Name: aplicatie1_cinemauri_id_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie1_cinemauri_id_seq', 7, true);


--
-- PostgreSQL database dump complete
--