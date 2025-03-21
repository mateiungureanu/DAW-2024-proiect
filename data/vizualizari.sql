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
-- Data for Name: aplicatie1_vizualizari; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie1_vizualizari (id, data_vizualizare, produs_id, utilizator_id) VALUES (3, '2024-12-01 18:42:08.002118+02', 7, 12);
INSERT INTO django.aplicatie1_vizualizari (id, data_vizualizare, produs_id, utilizator_id) VALUES (4, '2024-12-01 18:42:14.301335+02', 1, 12);
INSERT INTO django.aplicatie1_vizualizari (id, data_vizualizare, produs_id, utilizator_id) VALUES (5, '2024-12-01 18:44:42.886864+02', 15, 12);
INSERT INTO django.aplicatie1_vizualizari (id, data_vizualizare, produs_id, utilizator_id) VALUES (13, '2024-12-01 20:18:12.874749+02', 1, 10);
INSERT INTO django.aplicatie1_vizualizari (id, data_vizualizare, produs_id, utilizator_id) VALUES (14, '2024-12-01 20:18:18.044074+02', 9, 10);
INSERT INTO django.aplicatie1_vizualizari (id, data_vizualizare, produs_id, utilizator_id) VALUES (15, '2024-12-01 20:18:22.814256+02', 14, 10);
INSERT INTO django.aplicatie1_vizualizari (id, data_vizualizare, produs_id, utilizator_id) VALUES (16, '2024-12-01 20:19:20.623374+02', 16, 10);
INSERT INTO django.aplicatie1_vizualizari (id, data_vizualizare, produs_id, utilizator_id) VALUES (17, '2024-12-01 20:19:29.192585+02', 12, 10);
INSERT INTO django.aplicatie1_vizualizari (id, data_vizualizare, produs_id, utilizator_id) VALUES (18, '2024-12-01 20:20:03.668967+02', 9, 6);
INSERT INTO django.aplicatie1_vizualizari (id, data_vizualizare, produs_id, utilizator_id) VALUES (19, '2024-12-01 20:20:08.927554+02', 10, 6);
INSERT INTO django.aplicatie1_vizualizari (id, data_vizualizare, produs_id, utilizator_id) VALUES (20, '2024-12-01 20:20:30.349678+02', 5, 6);


--
-- Name: aplicatie1_vizualizari_id_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie1_vizualizari_id_seq', 20, true);


--
-- PostgreSQL database dump complete
--

