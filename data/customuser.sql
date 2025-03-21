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
-- Data for Name: aplicatie1_customuser; Type: TABLE DATA; Schema: django; Owner: matei
--

INSERT INTO django.aplicatie1_customuser (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, telefon, adresa, data_nasterii, gen, ocupatie, cod, email_confirmat, nume, prenume, blocat) VALUES (6, 'pbkdf2_sha256$870000$BQWRhs383MzBdqdg3s0l6D$9R25DHMvzfLkUnMQ4Ht6/TnQOit34hdY1zMwhsfkDtg=', '2025-03-10 19:10:57.30224+02', true, 'matei', 'PersonA', 'PersonAA', 'persona@gmail.com', true, true, '2024-11-30 14:40:30+02', '+40111111111', 'Bucuresti', '2004-08-19', 'M', 'Student', NULL, true, 'PersonAA', 'PersonA', false);
INSERT INTO django.aplicatie1_customuser (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, telefon, adresa, data_nasterii, gen, ocupatie, cod, email_confirmat, nume, prenume, blocat) VALUES (11, 'pbkdf2_sha256$870000$LQZt8WCNe1vi6DxAsDy8dt$iGPxKyqJ0b6IWVPZbShaRVan8oHiB1p2zTw7g8pCYcM=', '2025-01-07 13:08:34.737956+02', false, 'genghischan', 'PersonC', 'PersonCC', 'personc@gmail.com', false, true, '2024-12-01 17:25:33+02', '+40333333333', 'Bragadiru', '2004-07-07', 'M', 'Student', 'BEdRW18CM1S1xS8E3hFboOjEIVBS4UVqNjKqglSxi57z0S12OG', true, 'PersonCC', 'PersonC', false);
INSERT INTO django.aplicatie1_customuser (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, telefon, adresa, data_nasterii, gen, ocupatie, cod, email_confirmat, nume, prenume, blocat) VALUES (12, 'pbkdf2_sha256$870000$QJbmKhrCkQwhg8mhXSsGJc$zggWWeIAToL4AAaVWYKe6OLo7HNgiEb8+EYOpGn0fbc=', '2025-01-07 13:49:15.818528+02', false, 'jerma985', 'PersonE', 'PersonEE', 'persone@protonmail.com', false, true, '2024-12-01 17:31:37+02', '+40555555555', 'Bucuresti', '2004-12-16', 'M', 'Libertin', 'BfUcpRXlmAlsCFFp3eamzEIgv0QIpbwKtLUcrebZhIYKnVcEvv', true, 'PersonEE', 'PersonE', false);
INSERT INTO django.aplicatie1_customuser (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, telefon, adresa, data_nasterii, gen, ocupatie, cod, email_confirmat, nume, prenume, blocat) VALUES (9, 'pbkdf2_sha256$870000$gkXADci89laObOcWzVuLp0$UbZ0rGKw7vRrMHdAUDsh8+9kQV4pMMGMin2Mgl/8aYQ=', '2025-01-07 13:55:19.952642+02', false, 'grief', 'PersonD', 'PersonDD', 'persond@gmail.com', false, true, '2024-12-01 17:10:01+02', '+40444444444', 'Bragadiru', '2004-10-14', 'M', 'Student', '10KEyXlkJj3kfx6W188SXuySvJuMma6Nvmrl0C0UFgWDzYPtLc', true, 'PersonDD', 'PersonD', false);
INSERT INTO django.aplicatie1_customuser (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, telefon, adresa, data_nasterii, gen, ocupatie, cod, email_confirmat, nume, prenume, blocat) VALUES (10, 'pbkdf2_sha256$870000$dbgf1CS9fzaS9Bwuy2R94Z$5gBzLcyAyAVU39MAzNETDUOTWZccvdVn40KR7pvRE50=', '2025-01-07 13:55:38.217157+02', false, 'viceroy', 'PersonA', 'PersonAA', 'persona@gmail.com', false, true, '2024-12-01 17:20:40+02', '+40111111111', 'Bucuresti', '2004-08-19', 'M', 'Gamer', 'J9XHfDVp3GJzUibS5LiIgESGmwZWvGZgCsDM5iwZy8ZfrkVVj1', true, 'PersonAA', 'PersonA', false);


--
-- Name: aplicatie1_customuser_id_seq; Type: SEQUENCE SET; Schema: django; Owner: matei
--

SELECT pg_catalog.setval('django.aplicatie1_customuser_id_seq', 19, true);


--
-- PostgreSQL database dump complete
--

