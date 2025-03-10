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
-- Data for Name: aplicatie1_achizitii; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie1_achizitii (id, email, nr_telefon) VALUES (1, 'persona@gmail.com', 111111111);
INSERT INTO django.aplicatie1_achizitii (id, email, nr_telefon) VALUES (2, 'persona@gmail.com', 111111111);
INSERT INTO django.aplicatie1_achizitii (id, email, nr_telefon) VALUES (3, 'persona@gmail.com', 111111111);
INSERT INTO django.aplicatie1_achizitii (id, email, nr_telefon) VALUES (4, 'persong@gmail.com', 777777777);
INSERT INTO django.aplicatie1_achizitii (id, email, nr_telefon) VALUES (5, NULL, 555555555);
INSERT INTO django.aplicatie1_achizitii (id, email, nr_telefon) VALUES (6, NULL, 666666666);
INSERT INTO django.aplicatie1_achizitii (id, email, nr_telefon) VALUES (7, NULL, 444444444);
INSERT INTO django.aplicatie1_achizitii (id, email, nr_telefon) VALUES (8, NULL, 888888888);
INSERT INTO django.aplicatie1_achizitii (id, email, nr_telefon) VALUES (9, NULL, 333333333);
INSERT INTO django.aplicatie1_achizitii (id, email, nr_telefon) VALUES (10, NULL, 222222222);


--
-- Name: aplicatie1_achizitii_id_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie1_achizitii_id_seq', 10, true);


--
-- PostgreSQL database dump complete
--

