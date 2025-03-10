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
-- Data for Name: aplicatie1_bilete; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (1, 5, 3, 1, 2, 1);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (2, 5, 4, 1, 2, 1);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (3, 5, 5, 1, 2, 1);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (4, 5, 6, 1, 2, 1);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (5, 5, 7, 1, 2, 1);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (6, 5, 8, 1, 2, 1);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (7, 6, 5, 2, 2, 2);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (8, 6, 6, 2, 2, 2);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (9, 4, 4, 3, 5, 3);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (10, 4, 5, 3, 5, 3);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (11, 6, 5, 4, 5, 4);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (12, 7, 4, 5, 5, 6);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (13, 7, 5, 5, 5, 6);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (14, 7, 6, 5, 5, 6);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (15, 6, 5, 6, 6, 7);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (16, 6, 6, 6, 6, 7);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (17, 3, 5, 7, 3, 8);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (18, 5, 5, 8, 8, 9);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (19, 5, 6, 8, 8, 9);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (20, 4, 5, 9, 3, 10);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (21, 4, 6, 9, 3, 10);
INSERT INTO django.aplicatie1_bilete (id, rand, coloana, achizitie_id, angajat_id, difuzare_id) VALUES (22, 5, 5, 10, 2, 11);


--
-- Name: aplicatie1_bilete_id_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie1_bilete_id_seq', 22, true);


--
-- PostgreSQL database dump complete
--

