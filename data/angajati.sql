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
-- Data for Name: aplicatie1_angajati; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie1_angajati (id, nume, prenume, email, nr_telefon, salariu, pct_comision, data_angajarii, cinema_id, id_sef) VALUES (8, 'PersonHH', 'PersonH', NULL, 888888888, 5000, 0.10, '2021-01-11', 7, 1);
INSERT INTO django.aplicatie1_angajati (id, nume, prenume, email, nr_telefon, salariu, pct_comision, data_angajarii, cinema_id, id_sef) VALUES (1, 'PersonAA', 'PersonA', 'persona@gmail.com', 111111111, 7000, 0.70, '2017-08-19', 1, NULL);
INSERT INTO django.aplicatie1_angajati (id, nume, prenume, email, nr_telefon, salariu, pct_comision, data_angajarii, cinema_id, id_sef) VALUES (2, 'PersonBB', 'PersonB', NULL, 222222222, 5000, 0.50, '2018-05-12', 1, 1);
INSERT INTO django.aplicatie1_angajati (id, nume, prenume, email, nr_telefon, salariu, pct_comision, data_angajarii, cinema_id, id_sef) VALUES (3, 'PersonCC', 'PersonC', NULL, 333333333, 5000, 0.40, '2019-07-07', 2, 1);
INSERT INTO django.aplicatie1_angajati (id, nume, prenume, email, nr_telefon, salariu, pct_comision, data_angajarii, cinema_id, id_sef) VALUES (4, 'PersonDD', 'PersonD', NULL, 444444444, 5000, 0.30, '2019-10-14', 3, 1);
INSERT INTO django.aplicatie1_angajati (id, nume, prenume, email, nr_telefon, salariu, pct_comision, data_angajarii, cinema_id, id_sef) VALUES (5, 'PersonEE', 'PersonE', NULL, 555555555, 5000, 0.20, '2019-12-16', 4, 1);
INSERT INTO django.aplicatie1_angajati (id, nume, prenume, email, nr_telefon, salariu, pct_comision, data_angajarii, cinema_id, id_sef) VALUES (6, 'PersonFF', 'PersonF', NULL, 666666666, 5000, 0.10, '2020-07-29', 5, 1);
INSERT INTO django.aplicatie1_angajati (id, nume, prenume, email, nr_telefon, salariu, pct_comision, data_angajarii, cinema_id, id_sef) VALUES (7, 'PersonGG', 'PersonG', 'persong@gmail.com', 777777777, 5000, 0.10, '2020-08-02', 6, 1);


--
-- Name: aplicatie1_angajati_id_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie1_angajati_id_seq', 14, true);


--
-- PostgreSQL database dump complete
--

