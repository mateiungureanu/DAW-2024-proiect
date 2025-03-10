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
-- Data for Name: aplicatie1_difuzari; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie1_difuzari (id, data_ora, film_id, sala_id) VALUES (1, '2018-10-28 19:30:00+02', 1, 1);
INSERT INTO django.aplicatie1_difuzari (id, data_ora, film_id, sala_id) VALUES (2, '2018-11-30 22:30:00+02', 2, 1);
INSERT INTO django.aplicatie1_difuzari (id, data_ora, film_id, sala_id) VALUES (3, '2019-07-17 19:30:00+03', 1, 3);
INSERT INTO django.aplicatie1_difuzari (id, data_ora, film_id, sala_id) VALUES (4, '2019-09-03 21:30:00+03', 2, 4);
INSERT INTO django.aplicatie1_difuzari (id, data_ora, film_id, sala_id) VALUES (5, '2019-12-15 22:30:00+02', 3, 2);
INSERT INTO django.aplicatie1_difuzari (id, data_ora, film_id, sala_id) VALUES (6, '2020-08-27 20:45:00+03', 1, 5);
INSERT INTO django.aplicatie1_difuzari (id, data_ora, film_id, sala_id) VALUES (7, '2020-11-30 22:30:00+02', 3, 6);
INSERT INTO django.aplicatie1_difuzari (id, data_ora, film_id, sala_id) VALUES (8, '2023-07-23 19:15:00+03', 4, 2);
INSERT INTO django.aplicatie1_difuzari (id, data_ora, film_id, sala_id) VALUES (9, '2023-08-01 20:30:00+03', 4, 7);
INSERT INTO django.aplicatie1_difuzari (id, data_ora, film_id, sala_id) VALUES (10, '2024-03-01 21:30:00+02', 5, 10);
INSERT INTO django.aplicatie1_difuzari (id, data_ora, film_id, sala_id) VALUES (11, '2024-03-14 00:30:00+02', 5, 4);


--
-- Name: aplicatie1_difuzari_id_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie1_difuzari_id_seq', 11, true);


--
-- PostgreSQL database dump complete
--

