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
-- Data for Name: aplicatie1_sali; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie1_sali (id, cinema_id) VALUES (9, 5);
INSERT INTO django.aplicatie1_sali (id, cinema_id) VALUES (11, 6);
INSERT INTO django.aplicatie1_sali (id, cinema_id) VALUES (12, 6);
INSERT INTO django.aplicatie1_sali (id, cinema_id) VALUES (13, 7);
INSERT INTO django.aplicatie1_sali (id, cinema_id) VALUES (14, 7);
INSERT INTO django.aplicatie1_sali (id, cinema_id) VALUES (1, 1);
INSERT INTO django.aplicatie1_sali (id, cinema_id) VALUES (2, 1);
INSERT INTO django.aplicatie1_sali (id, cinema_id) VALUES (3, 2);
INSERT INTO django.aplicatie1_sali (id, cinema_id) VALUES (4, 2);
INSERT INTO django.aplicatie1_sali (id, cinema_id) VALUES (5, 3);
INSERT INTO django.aplicatie1_sali (id, cinema_id) VALUES (6, 3);
INSERT INTO django.aplicatie1_sali (id, cinema_id) VALUES (7, 4);
INSERT INTO django.aplicatie1_sali (id, cinema_id) VALUES (8, 4);
INSERT INTO django.aplicatie1_sali (id, cinema_id) VALUES (10, 5);


--
-- Name: aplicatie1_sali_id_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie1_sali_id_seq', 15, true);


--
-- PostgreSQL database dump complete
--

