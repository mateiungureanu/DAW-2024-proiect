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
-- Data for Name: aplicatie1_promotii; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie1_promotii (id, nume, data_creare, data_expirare, subiect, mesaj, reducere_procentuala, suma_minima_comanda) VALUES (9, 'promotie1', '2024-12-01 20:22:25.903578+02', '2024-12-09 01:21:00+02', 'promotie 1 subiect', 'promotie 1 mesaj', 10.00, 500.00);
INSERT INTO django.aplicatie1_promotii (id, nume, data_creare, data_expirare, subiect, mesaj, reducere_procentuala, suma_minima_comanda) VALUES (10, 'promotie1', '2024-12-01 20:24:31.424252+02', '2024-12-09 01:21:00+02', 'promotie 1 subiect', 'promotie 1 mesaj', 10.00, 500.00);
INSERT INTO django.aplicatie1_promotii (id, nume, data_creare, data_expirare, subiect, mesaj, reducere_procentuala, suma_minima_comanda) VALUES (11, 'promotie1', '2024-12-01 20:33:03.315225+02', '2024-12-09 01:21:00+02', 'promotie 1 subiect', 'promotie 1 mesaj', 10.00, 500.00);
INSERT INTO django.aplicatie1_promotii (id, nume, data_creare, data_expirare, subiect, mesaj, reducere_procentuala, suma_minima_comanda) VALUES (12, 'promotie1', '2024-12-01 20:39:44.961791+02', '2024-12-09 01:21:00+02', 'promotie 1 subiect', 'promotie 1 mesaj', 10.00, 500.00);
INSERT INTO django.aplicatie1_promotii (id, nume, data_creare, data_expirare, subiect, mesaj, reducere_procentuala, suma_minima_comanda) VALUES (13, 'promotie 2', '2024-12-01 20:44:31.937321+02', '2024-12-19 22:44:00+02', 'promotie 2 subiect', 'promotie 2 mesaj', 10.00, 10.00);
INSERT INTO django.aplicatie1_promotii (id, nume, data_creare, data_expirare, subiect, mesaj, reducere_procentuala, suma_minima_comanda) VALUES (14, 'promotie 2', '2024-12-01 20:45:53.358199+02', '2024-12-19 22:44:00+02', 'promotie 2 subiect', 'promotie 2 mesaj', 10.00, 10.00);


--
-- Name: aplicatie1_promotii_id_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie1_promotii_id_seq', 14, true);


--
-- PostgreSQL database dump complete
--

