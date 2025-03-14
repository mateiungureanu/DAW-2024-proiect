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
-- Data for Name: aplicatie1_produse; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie1_produse (id, nume, categorie, pret, descriere, stoc) VALUES (11, 'Chiloti', 'Haine', 20.00, '', 5);
INSERT INTO django.aplicatie1_produse (id, nume, categorie, pret, descriere, stoc) VALUES (13, 'Tricou', 'Haine', 60.00, '', 0);
INSERT INTO django.aplicatie1_produse (id, nume, categorie, pret, descriere, stoc) VALUES (16, 'Ciorapi', 'Haine', 80.00, '', 3);
INSERT INTO django.aplicatie1_produse (id, nume, categorie, pret, descriere, stoc) VALUES (4, 'Pantaloni', 'Haine', 200.00, '', 4);
INSERT INTO django.aplicatie1_produse (id, nume, categorie, pret, descriere, stoc) VALUES (1, 'Televizor', 'Electronice', 1500.00, '', 4);
INSERT INTO django.aplicatie1_produse (id, nume, categorie, pret, descriere, stoc) VALUES (3, 'Camasa', 'Haine', 100.00, '', 4);
INSERT INTO django.aplicatie1_produse (id, nume, categorie, pret, descriere, stoc) VALUES (10, 'Monitor', 'Electronice', 1000.00, '', 4);
INSERT INTO django.aplicatie1_produse (id, nume, categorie, pret, descriere, stoc) VALUES (15, 'Hanorac', 'Haine', 200.00, '', 3);
INSERT INTO django.aplicatie1_produse (id, nume, categorie, pret, descriere, stoc) VALUES (9, 'Mouse', 'Electronice', 300.00, '', 4);
INSERT INTO django.aplicatie1_produse (id, nume, categorie, pret, descriere, stoc) VALUES (8, 'Casti', 'Electronice', 400.00, '', 4);
INSERT INTO django.aplicatie1_produse (id, nume, categorie, pret, descriere, stoc) VALUES (14, 'Geaca', 'Haine', 500.00, '', 4);
INSERT INTO django.aplicatie1_produse (id, nume, categorie, pret, descriere, stoc) VALUES (2, 'Laptop', 'Electronice', 3500.00, '', 3);
INSERT INTO django.aplicatie1_produse (id, nume, categorie, pret, descriere, stoc) VALUES (12, 'Sosete', 'Haine', 10.00, '', 0);
INSERT INTO django.aplicatie1_produse (id, nume, categorie, pret, descriere, stoc) VALUES (7, 'Telefon', 'Electronice', 3000.00, '', 4);
INSERT INTO django.aplicatie1_produse (id, nume, categorie, pret, descriere, stoc) VALUES (6, 'XboxOne', 'Electronice', 2000.00, '', 4);
INSERT INTO django.aplicatie1_produse (id, nume, categorie, pret, descriere, stoc) VALUES (5, 'PS5', 'Electronice', 2500.00, '', 4);


--
-- Name: aplicatie1_produse_id_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie1_produse_id_seq', 16, true);


--
-- PostgreSQL database dump complete
--

