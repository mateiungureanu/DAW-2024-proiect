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
-- Data for Name: aplicatie1_filme; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie1_filme (id, nume_film, durata, rating, regizor, anul_lansarii) VALUES (2, 'Star Wars Episode III: Revenge of the Sith', 140, 7.60, 'George Lucas', '2005-05-19');
INSERT INTO django.aplicatie1_filme (id, nume_film, durata, rating, regizor, anul_lansarii) VALUES (1, 'The Lord of the Rings: The Return of the King', 201, 9.00, 'Peter Jackson', '2003-12-17');
INSERT INTO django.aplicatie1_filme (id, nume_film, durata, rating, regizor, anul_lansarii) VALUES (3, 'The Dark Knight', 152, 9.00, 'Christopher Nolan', '2008-07-18');
INSERT INTO django.aplicatie1_filme (id, nume_film, durata, rating, regizor, anul_lansarii) VALUES (4, 'Oppenheimer', 180, 8.30, 'Christopher Nolan', '2023-07-21');
INSERT INTO django.aplicatie1_filme (id, nume_film, durata, rating, regizor, anul_lansarii) VALUES (5, 'Dune Part 2', 166, 8.60, 'Denis Villeneuve', '2024-03-01');


--
-- Name: aplicatie1_filme_id_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie1_filme_id_seq', 5, true);


--
-- PostgreSQL database dump complete
--

